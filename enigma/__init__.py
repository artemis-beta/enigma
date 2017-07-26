from collections import OrderedDict

from . import rotor
from . import plugboard
from . import reflector
import logging

class Enigma:
    def __init__(self, rotor_list=None, user_reflector=None, debug='ERROR', enigma_type='M3'):
        '''Enigma Machine Class based on the Enigma Model 3 ciphering machine
          
           rotor_list:     [i,k,k]   Any three non-identical numbers 1-8 for rotor choice

           user_reflector:   'B'     Reflector type to be used 'B' or 'C'

           enigma_type: 'M4'         Enigma type 'M3' or 'M4' 
        
           debug:          'DEBUG'   Set debug level, default is 'ERROR'
      
        '''

        self.version = 'v1.1.2'
        self.isBeta = False
        self.type = enigma_type.upper()

        self._rotor_types = {1 : rotor.rotor_1(),
                             2 : rotor.rotor_2(),
                             3 : rotor.rotor_3(),
                             4 : rotor.rotor_4(),
                             5 : rotor.rotor_5(),
                             6 : rotor.rotor_6(),
                             7 : rotor.rotor_7(),
                             8 : rotor.rotor_8()}
        self._reflector_types = {'B' : reflector.reflector_B(),
                                 'C' : reflector.reflector_C()}

        self.rotors = OrderedDict()

        if self.type == 'M3':
            if rotor_list is None:
                rotor_list = [5, 3, 1]
            assert len(rotor_list) == 3, "ERROR: Invalid Rotor List Argument for Enigma M3"
            self.rotors['left'] = self._rotor_types[rotor_list[0]]
            self.rotors['middle'] = self._rotor_types[rotor_list[1]]
            self.rotors['right'] = self._rotor_types[rotor_list[2]]

        elif self.type == 'M4':
            assert len(rotor_list) == 4, "ERROR: Invalid Rotor List Argument for Enigma M4"
            self.rotors['left'] = self._rotor_types[rotor_list[0]]
            self.rotors['middle left'] = self._rotor_types[rotor_list[1]]
            self.rotors['middle right'] = self._rotor_types[rotor_list[2]]
            self.rotors['right'] = self._rotor_types[rotor_list[3]]

        else:
            # TODO put proper exception here
            assert False, "Please specify M3 or M4"

        # After setting rotors, get a tuple of the dict keys for index tricks.
        self._rotor_dict_keys = tuple(self.rotors.keys())

        if user_reflector:
            self.reflector = self._reflector_types[user_reflector]
        else:
            self.reflector = self._reflector_types['B']
        
        self.plugboard = plugboard.plugboard()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(debug)
        logging.basicConfig()

    def _move_rotor(self, name, amount):
        for j in range(amount):
            self.logger.debug("Rotating rotor %s by %s", name, amount)
            self.rotors[name].rotate_rotor()

    def rewire_rotor(self, name, amount):
        for j in range(amount):
            self.logger.debug("Rotating rotor %s wires by %s", name, amount)
            self.rotors[name].rotate_inner_ring()
    
    def _set_rotor(self, name, letter):
        self.logger.debug("Setting rotor %s to %s", name, letter)
        while self.rotors[name].face != letter:
            self._move_rotor(name, 1)
    
    def _get_rotor_conv(self, name, letter):
        self.logger.debug("Rotor %s conversion: %s to %s", name, letter, self.rotors[name].get_rotor_conversion(letter))
        return self.rotors[name].get_rotor_conversion(letter)

    def _get_rotor_conv_inv(self, name, letter):
        self.logger.debug("Rotor %s conversion: %s to %s", name, letter, self.rotors[name].get_rotor_conversion_inv(letter))
        return self.rotors[name].get_rotor_conversion_inv(letter)
    
    def _get_inter_rotor_conv(self, name1, name2, letter):
        terminal = self.rotors[name1].alpha.index(letter)
        zero_point_1 = self.rotors[name1].alpha.index(self.rotors[name1].face)
        zero_point_2 = self.rotors[name2].alpha.index(self.rotors[name2].face)
        interval = zero_point_2-zero_point_1
        if zero_point_2 > zero_point_1:
            i = [i for i in range(26)]
            n = i[(terminal+interval) % len(i)]
        else:
            i = [i for i in range(26)]
            n = i[(26+terminal+interval) % len(i)]
        self.logger.debug("Rotor %s rotor to %s rotor conversion: %s to %s", name1, name2, letter, self.rotors[name2].alpha[n])
        assert self.rotors[name2].alpha[n] is not None
        return self.rotors[name2].alpha[n]

    def _get_inter_rotor_conv_inv(self, name1, name2, letter):
        terminal = self.rotors[name1].alpha.index(letter)
        zero_point_1 = self.rotors[name1].alpha.index(self.rotors[name1].face)
        zero_point_2 = self.rotors[name2].alpha.index(self.rotors[name2].face)
        interval = zero_point_2-zero_point_1
        if zero_point_2 > zero_point_1:
            i = [i for i in range(26)]
            n = i[(terminal+interval) % len(i)]
        else:
            i = [i for i in range(26)]
            n = i[(26+terminal+interval) % len(i)]
        self.logger.debug("Rotor %s rotor to %s rotor conversion: %s to %s", name1, name2, letter, self.rotors[name2].alpha[n])
        assert self.rotors[name2].alpha[n] is not None
        return self.rotors[name2].alpha[n]

    def type_letter(self, letter):
        letter = letter.upper()
        self.logger.debug("-----------------------")
        cipher = self.plugboard.plugboard_conversion(letter)
        self.logger.debug("Plugboard conversion: %s to %s", letter, cipher)
        # Move the rightmost rotor
        self._move_rotor(self._rotor_dict_keys[-1], 1)

        # TODO not sure what to call this action...
        for i, j in zip(
                reversed(self._rotor_dict_keys[1:]),
                reversed(self._rotor_dict_keys[:-1]),
        ):
            if self.rotors[i].face in self.rotors[i].notches:
                self._move_rotor(j, 1)

        # Start making the cipher
        for rotor_key in reversed(self._rotor_dict_keys):
            # Get the rotor conversion for given key
            cipher = self._get_rotor_conv(rotor_key, cipher)
            # Get the inter rotor conversion for the key and the key-1
            adjacent_rotor_key_index = self._rotor_dict_keys.index(rotor_key)-1
            # At this point we should be ready for reflection
            if adjacent_rotor_key_index < 0:
                break
            adjacent_rotor_key = self._rotor_dict_keys[adjacent_rotor_key_index]
            cipher = self._get_inter_rotor_conv(
                rotor_key,
                adjacent_rotor_key,
                cipher
            )
        else:
            assert False, "Shouldn't get here!"

        cipher = self._get_reflector_conv(cipher)

        # Start making the cipher
        for rotor_key in self._rotor_dict_keys:
            # Get the rotor conversion for given key
            cipher = self._get_rotor_conv_inv(rotor_key, cipher)
            try:
                # Get the inter rotor conv_inversion for the key and the key-1
                adjacent_rotor_key_index = self._rotor_dict_keys.index(rotor_key)+1
                adjacent_rotor_key = self._rotor_dict_keys[adjacent_rotor_key_index]
                cipher = self._get_inter_rotor_conv_inv(
                    rotor_key,
                    adjacent_rotor_key,
                    cipher
                )
            except IndexError:
                # At this point we should be ready for reflection
                break
        else:
            assert False, "Shouldn't get here!"

        cipher_out = self.plugboard.plugboard_conversion_inv(cipher)
        self.logger.debug("Plugboard conversion: %s to %s", cipher, cipher_out)
        self.logger.debug("-----------------------")

        return cipher_out

    def _get_reflector_conv(self, phrase):
        out = self.reflector.reflector_conversion(phrase)
        self.logger.debug("Reflector conversion: %s to %s", phrase, out)
        return out

    def type_phrase(self, phrase):
        phrase = phrase.replace(' ','')
        out_str = ''
        for letter in list(phrase):
            out_str += self.type_letter(letter)
            remainder = len(out_str) % 3
        #     fill = ''
        #     import string, random
        #     for i in range(remainder):
        #       fill += random.choice(string.ascii_letters.upper())
        # out_str = ' '.join(out_str[i:i+3] for i in range(0, len(out_str),3)) + fill
        return out_str

    def set_key(self, key):
        if len(self.rotors) != len(key):
            raise ValueError("Key length must match no. of rotors.")
        if not key.isalpha():
            raise ValueError("Key can only contain alphabetic characters!")

        key = key.upper()
        for rotor_dict_key, letter in zip(self._rotor_dict_keys, key):
            self._set_rotor(rotor_dict_key, letter)
