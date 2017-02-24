import unittest
from hypothesis import given, strategies
from enigma import Enigma
import sys

class TestEnigma(unittest.TestCase):

    @given(letter=strategies.sampled_from(['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
                                           'O','P','Q','R','S','T','U','V','W','X','Y','Z']),
           rotor_list = strategies.lists(strategies.integers(min_value=1, max_value=8), min_size=3, max_size=3),
           reflector = strategies.sampled_from(['B', 'C']),
           key = strategies.text( alphabet = ['A','B','C','D','E','F','G',
                                              'H','I','J','K','L','M','N',
                                              'O','P','Q','R','S','T','U',
                                              'V','W','X','Y','Z'], min_size=3, max_size=3))
    def testAlphabet(self, letter, rotor_list, reflector, key):
        machine = Enigma(rotor_list=rotor_list, user_reflector=reflector)
        machine.set_key(key)
        machine.type_phrase(letter)

if __name__ == "__main__":
    unittest.main()
