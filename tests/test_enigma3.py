import unittest
from hypothesis import given, strategies, settings, example, assume
from enigma import Enigma
import logging

import string

logger = logging.getLogger('ENIGMATEST')
logging.basicConfig()
logger.setLevel('DEBUG')


class TestEnigma(unittest.TestCase):

    @given(
        phrase=strategies.text(
            alphabet=string.ascii_uppercase,
            min_size=1,
            max_size=10),
        rotor_list=strategies.lists(
            strategies.integers(min_value=1, max_value=8),
            min_size=3,
            max_size=4),
        reflector=strategies.sampled_from(['B', 'C']),
        key=strategies.text(
            alphabet=string.ascii_uppercase,
            min_size=3,
            max_size=4)
    )
    @settings(max_examples=100, min_satisfying_examples=10, timeout=10)
    @example(phrase="FORK", rotor_list=[1, 2, 3], reflector='B', key='ABC')
    def testEnigma(self, phrase, rotor_list, reflector, key):
        assume(len(key) == len(rotor_list))

        def make_machine():
            if len(rotor_list) == 3:
                enigma_type = 'M3'
            elif len(rotor_list) == 4:
                enigma_type = 'M4'

            machine = Enigma(
                rotor_list=rotor_list,
                user_reflector=reflector,
                enigma_type=enigma_type,
                debug='DEBUG'
            )
            machine.set_key(key)
            return machine

        machine = make_machine()
        logger.debug("Encrypting %s", phrase)
        result = machine.type_phrase(phrase)

        logger.debug("Finding Original")
        machine = make_machine()
        orig = machine.type_phrase(result)
        logger.debug(
            "Key '%s'\n -> Running Enigma: Phrase Conversion     %s  ----->  %s  ------> %s", key, phrase, result, orig)
        logger.debug("Machine type: %s" % machine.type)
        assert phrase == orig, "ERROR: Reverse Encryption Does Not Match Original Phrase"

    @given(
        key=strategies.text(alphabet=string.ascii_uppercase, max_size=10),
        rotor_list=strategies.lists(
            strategies.integers(min_value=1, max_value=8),
            min_size=3,
            max_size=4),
    )
    def testEngimaKeyCheck(self, key, rotor_list):
        assume(len(key) != len(rotor_list))

        if len(rotor_list) == 3:
            enigma_type = 'M3'
        elif len(rotor_list) == 4:
            enigma_type = 'M4'

        machine = Enigma(
            rotor_list=rotor_list,
            enigma_type=enigma_type,
            debug='DEBUG'
        )
        with self.assertRaises(ValueError):
            machine.set_key(key)


if __name__ == "__main__":
    unittest.main()
