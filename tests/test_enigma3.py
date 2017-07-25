import unittest
from hypothesis import given, strategies, settings, example
from enigma import Enigma
import sys
import logging
 
logger = logging.getLogger('ENIGMATEST')
logging.basicConfig()
logger.setLevel('DEBUG')

import string

alph = string.ascii_uppercase
class TestEnigma(unittest.TestCase):


    @given(indices = strategies.lists(strategies.integers(min_value=1, max_value=8), min_size=3, max_size=3),
           rotor_list = strategies.lists(strategies.integers(min_value=1, max_value=8), min_size=3, max_size=3),
           reflector = strategies.sampled_from(['B', 'C']),
           key = strategies.text( alphabet = alph, min_size=3, max_size=3))
    @settings(max_examples=100, min_satisfying_examples=10, timeout=10)
    @example(indices=[1, 2, 3], rotor_list=[1, 2, 3], reflector='B', key='ABC')
    def testEnigma(self, indices, rotor_list, reflector, key):
        machine = Enigma(rotor_list=rotor_list, user_reflector=reflector,debug='DEBUG')
        machine.set_key(key)
        phrase = ''
        for i in indices: 
          phrase += alph[i]
        logger.debug("Encrypting %s", phrase)
        result = machine.type_phrase(phrase)
        logger.debug("Finding Original")
        machine = Enigma(rotor_list=rotor_list, user_reflector=reflector,debug='DEBUG')
        machine.set_key(key) 
        orig   = machine.type_phrase(result) 
        logger.debug("Key '%s' - Running Enigma: Phrase Conversion     %s  ----->  %s  ------> %s", key, phrase, result, orig)
        assert  phrase == orig, "ERROR: Reverse Encryption Does Not Match Original Phrase"

if __name__ == "__main__":
    unittest.main()
