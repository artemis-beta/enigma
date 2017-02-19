from . import rotor
from . import plugboard
from . import reflector
import logging

class Enigma:
    def __init__(self, debug='ERROR'):
        self.rotors = { 'right' : rotor.rotor() ,
                        'middle' : rotor.rotor(),
                        'left' : rotor.rotor()}
        
        self.plugboard = plugboard.plugboard()
        self.reflector = reflector.reflector()
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
    
    def set_rotor(self, name, letter):
        self.logger.debug("Setting rotor %s to %s", name, letter)
        while self.rotors[name].input != letter:
            self._move_rotor(name, 1)
    
    def _get_rotor_conv(self, name, letter):
        self.logger.debug("Rotor %s conversion: %s to %s", name, letter, self.rotors[name].get_rotor_conversion(letter))
        return self.rotors[name].get_rotor_conversion(letter)

    def _get_rotor_conv_inv(self, name, letter):
        self.logger.debug("Rotor %s conversion: %s to %s", name, letter, self.rotors[name].get_rotor_conversion(letter))
        return self.rotors[name].get_rotor_conversion_inv(letter)
    
    def _get_inter_rotor_conv(self, name1, name2, letter):
        terminal = self.rotors[name1].get_output_terminal(letter)
        zero_point = self.rotors[name2].alpha.index(self.rotors[name2].input)
        if zero_point + terminal > 24:
            n = zero_point + terminal - 25
        else:
            n = zero_point + terminal
        self.logger.debug("Rotor %s rotor to %s rotor conversion: %s to %s", name1, name2, letter, self.rotors[name2].alpha[n])
        return self.rotors[name2].alpha[n]

    def _get_inter_rotor_conv_inv(self, name1, name2, letter):
        terminal = self.rotors[name1].get_input_terminal(letter)
        zero_point = self.rotors[name2].alpha.index(self.rotors[name2].input)
        if zero_point + terminal > 24:
            n = zero_point + terminal - 25
        else:
            n = zero_point + terminal
        self.logger.debug("Rotor %s rotor to %s rotor conversion: %s to %s", name1, name2, letter, self.rotors[name2].alpha[n])
        return self.rotors[name2].alpha[n]

    def type_letter(self, letter):
        self.logger.debug("-----------------------")
        cipher = self.plugboard.plugboard_conversion(letter)
        self.logger.debug("Plugboard conversion: %s to %s", letter, cipher)
        self._move_rotor('right', 1)
        if self.rotors['right'].notch == self.rotors['right'].input:
            self._move_rotor('middle', 1)
        if self.rotors['middle'].notch == self.rotors['middle'].input:
            self._move_rotor('middle', 1)
            self._move_rotor('left', 1)
        cipher = self._get_rotor_conv('right', cipher)
        cipher = self._get_inter_rotor_conv('right', 'middle', cipher)
        cipher = self._get_rotor_conv('middle', cipher)
        cipher = self._get_inter_rotor_conv('middle', 'left', cipher)
        cipher = self._get_rotor_conv('left', cipher)
        cipher = self.reflector.reflector_conversion(cipher)
        cipher = self._get_rotor_conv_inv('left', cipher)
        cipher = self._get_inter_rotor_conv_inv('left', 'middle', cipher)
        cipher = self._get_rotor_conv('middle', cipher)
        cipher = self._get_inter_rotor_conv_inv('middle', 'right', cipher)
        cipher = self._get_rotor_conv('right', cipher)
        cipher_out = self.plugboard.plugboard_conversion_inv(cipher)
        self.logger.debug("Plugboard conversion: %s to %s", cipher, cipher_out)
        self.logger.debug("-----------------------")

        return cipher_out
    
    def type_phrase(self, phrase):
        out_str = ''
        print(list(phrase))
        for letter in list(phrase):
            out_str += self.type_letter(letter)
        return out_str