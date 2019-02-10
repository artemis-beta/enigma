import unittest
import enigma
from hypothesis import strategies, given, settings
import logging

logger = logging.getLogger('ROTORTEST')
logging.basicConfig()
logger.setLevel('DEBUG')

import string

class RotorTest(unittest.TestCase):

    @settings(max_examples=100)
    @given(letter = strategies.text( alphabet=string.ascii_uppercase, min_size=1, max_size=1),
           key    = strategies.text( alphabet = string.ascii_uppercase, min_size=3, max_size=3),
           reflector = strategies.text(alphabet=['B','C'], min_size=1, max_size=1))
    def test_reflector_conv(self, letter, reflector, key):
        machine = enigma.Enigma(user_reflector=reflector)
        machine.set_key(key)
        out = machine._get_reflector_conv(letter)
        back = machine._get_reflector_conv(out)
        logger.debug("Key '%s' - Running Reflector Setting: %s        %s  ----->  %s  ------> %s", key, reflector, letter, out, back)
        assert back == letter, "Cipher->Decipher Failed to Return Initial Letter"

    @settings(max_examples=100)
    @given(letter = strategies.text( alphabet=string.ascii_uppercase, min_size=1, max_size=1),
           key    = strategies.text( alphabet = string.ascii_uppercase, min_size=3, max_size=3),
           rotor_list = strategies.lists(strategies.integers(min_value=1, max_value=8), min_size=3, max_size=3))
    def test_inter_rotor_conv(self, letter, rotor_list, key):
        machine = enigma.Enigma(rotor_list=rotor_list, user_reflector='B')
        machine.set_key(key)
        out = machine._get_inter_rotor_conv('left', 'middle', letter)
        back = machine._get_inter_rotor_conv_inv('middle','left', out)
        logger.debug("Key '%s' - Running InterRotor Setting: %s        %s  ----->  %s  ------> %s", key, rotor_list, letter, out, back)
        assert back == letter, "Cipher->Decipher Failed to Return Initial Letter"

    @settings(max_examples=100)
    @given(letter = strategies.text( alphabet=string.ascii_uppercase, min_size=1, max_size=1),
           key    = strategies.text( alphabet = string.ascii_uppercase, min_size=3, max_size=3),
           rotor = strategies.integers(min_value=1, max_value=8),
           position = strategies.sampled_from(['left', 'middle', 'right']))
    def test_rotor_conv(self, letter, rotor, position, key):
        rotor_list = []
        if position == 'left':
           rotor_list.append(rotor)
           rotor_list.append(4)
           rotor_list.append(3)
        elif position == 'middle':
           rotor_list.append(4)
           rotor_list.append(rotor)
           rotor_list.append(3)
        else:
           rotor_list.append(4)
           rotor_list.append(3)
           rotor_list.append(rotor)
                
        machine = enigma.Enigma(rotor_list=rotor_list, user_reflector='B')
        machine.set_key(key)
        out = machine._get_rotor_conv('left', letter)
        back = machine._get_rotor_conv_inv('left', out)
        logger.debug("Key '%s' - Running Rotor Setting: %s        %s  ----->  %s  ------> %s", key, rotor_list, letter, out, back)
        assert back == letter, "Cipher->Decipher Failed to Return Initial Letter"

if __name__=="__main__":
    unittest.main()
