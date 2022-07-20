###############################################################################
#                                                                             #
#                               Enigma Class                                  #
#                                                                             #
#   Main Enigma object class and methods representing M3/M4 variants of the   #
#   Enigma machine for simulating encoding/decoding.                          #
#                                                                             #
#   @authors :   K. Zarebski, N. Farley                                       #
#   @date    :   last modified 2021-08-14                                     #
#                                                                             #
###############################################################################
from collections import OrderedDict
from typing import List

from enigma import rotor
from enigma import plugboard
from enigma import reflector
import logging
import string
import random


class Enigma:
    """
    Enigma class consisting of rotor, reflector, plugboard subclasses
    and simulating either an M3 or M4 variant of the famous WWII cipher
    encoding/decoding machine.
    """

    def __init__(
        self,
        rotor_list: List[int] = None,
        user_reflector: str = None,
        debug: str = "ERROR",
        enigma_type: str = "M3",
    ) -> None:
        """
        Enigma Machine Class based on the Enigma Model 3 ciphering machine.

        Arguments
        ---------
           rotor_list:     [i,k,k]   Any three non-identical numbers
                                     1-8 for rotor choice

           user_reflector:   'B'     Reflector type to be used 'B' or 'C'

           enigma_type: 'M4'         Enigma type 'M3' or 'M4'

           debug:          'DEBUG'   Set debug level, default is 'ERROR'

        """
        self.version = "v1.2.2"
        self.is_beta = False
        self.type = enigma_type.upper()

        # Initialise all rotor types as objects within member dictionary
        self._rotor_types = {
            1: rotor.Rotor1(),
            2: rotor.Rotor2(),
            3: rotor.Rotor3(),
            4: rotor.Rotor4(),
            5: rotor.Rotor5(),
            6: rotor.Rotor6(),
            7: rotor.Rotor7(),
            8: rotor.Rotor8(),
        }

        # Initialise all reflectors as objects within member dictionary
        self._reflector_types = {
            "B": reflector.ReflectorB(),
            "C": reflector.ReflectorC(),
        }

        # Chosen rotor set stored as an ordered dictionary
        self.rotors = OrderedDict()

        # Setup logger for errors, warnings and info output
        self.logger = logging.getLogger(__name__)

        self.logger.setLevel(debug)
        logging.basicConfig()

        if self.type == "M3":
            if not rotor_list:
                rotor_list = [5, 3, 1]

            if len(rotor_list) != 3:
                raise IndexError("Invalid Rotor List Argument for Enigma M3")

            self.rotors["left"] = self._rotor_types[rotor_list[0]]
            self.rotors["middle"] = self._rotor_types[rotor_list[1]]
            self.rotors["right"] = self._rotor_types[rotor_list[2]]

        elif self.type == "M4":
            if not rotor_list:
                rotor_list = [5, 3, 1, 2]

            if len(rotor_list) != 4:
                raise IndexError("Invalid Rotor List Argument for Enigma M4")

            self.rotors["left"] = self._rotor_types[rotor_list[0]]
            self.rotors["middle left"] = self._rotor_types[rotor_list[1]]
            self.rotors["middle right"] = self._rotor_types[rotor_list[2]]
            self.rotors["right"] = self._rotor_types[rotor_list[3]]

        else:
            raise TypeError(f"Unrecognised Enigma type '{self.type}'")

        # After setting rotors, get a tuple of the dict keys for index tricks.
        self._rotor_dict_keys = tuple(self.rotors.keys())

        # Setup the reflector choice
        user_reflector = user_reflector or "B"
        self.reflector = self._reflector_types[user_reflector]

        # Setup plugboard
        self.plugboard = plugboard.Plugboard()

    def _move_rotor(self, name: str, amount: int) -> None:
        """
        Perform a rotor rotation of a fixed amount.

        Arguments
        ---------
        name   (string)     Name of rotor

        amount (int)        Amount of intervals to rotate by

        """
        for j in range(amount):
            self.logger.debug("[%s] Rotating rotor %s by %s", j, name, amount)
            self.rotors[name].rotate_rotor()

    def ringstellung(self, name: str, amount: int) -> None:
        """
        Rotate internal rotor wiring by a fixed amount.

        Arguments
        ---------
        name   (string)     Name of rotor

        amount (int)        Amount of intervals to rotate by

        """
        letter = "A"

        for j in range(amount):
            self.logger.debug(
                "Ringstellung[%s]: Conversion for rotor %s was %s to %s",
                j,
                name,
                letter,
                self.rotors[name].get_rotor_conversion(letter),
            )

            self.rotors[name].rotate_inner_ring()

            self.logger.debug(
                "Ringstellung[%s]: Conversion for rotor %s now %s to %s",
                j,
                name,
                letter,
                self.rotors[name].get_rotor_conversion(letter),
            )

    def _set_rotor(self, name: str, letter: str) -> None:
        """
        Set the given rotor to position corresponding to letter.

        Arguments
        ---------
        name    (string)    name of rotor to modify

        letter  (string)    letter to set rotor position too

        """
        self.logger.debug("Setting rotor %s to %s", name, letter)

        while self.rotors[name].face != letter:
            self._move_rotor(name, 1)

    def _get_rotor_conv(self, name: str, letter: str) -> str:
        """
        Encode a given letter using the rotor at the given position.

        Arguments
        ---------
        name    (string)    label of given rotor, e.g. 'right'

        letter  (string)    letter to encode

        Returns
        -------
        the cipher for the given letter as a string

        """
        self.logger.debug(
            "Rotor %s conversion: %s to %s",
            name,
            letter,
            self.rotors[name].get_rotor_conversion(letter),
        )

        return self.rotors[name].get_rotor_conversion(letter)

    def _get_rotor_conv_inv(self, name: str, letter: str) -> str:
        """
        Decode a given cipher letter using the rotor at the given position.

        Arguments
        ---------
        name    (string)    label of given rotor, e.g. 'right'

        letter  (string)    letter to decode

        Returns
        -------
        the cipher for the given letter as a string

        """
        self.logger.debug(
            "Rotor %s conversion: %s to %s",
            name,
            letter,
            self.rotors[name].get_rotor_conversion_inv(letter),
        )

        return self.rotors[name].get_rotor_conversion_inv(letter)

    def _get_inter_rotor_conv(self, name1: str, name2: str, letter: str) -> str:
        """
        Find encoding of a given letter when passed between two rotors.

        Arguments
        ---------
        name1   (string)    label of first rotor, e.g. 'right'

        name2   (string)    label of second rotor, e.g. 'middle'

        letter  (string)    letter to encode

        Returns
        -------

        the cipher for the given letter as a string

        """
        # Get the rotor terminal of the first rotor for the given letter
        terminal = self.rotors[name1].alpha.index(letter)

        # Find the terminal of the current displayed letter of the first rotor
        zero_point_1 = self.rotors[name1].alpha.index(self.rotors[name1].face)

        # Find the terminal of the current displayed letter of the second rotor
        zero_point_2 = self.rotors[name2].alpha.index(self.rotors[name2].face)

        # Offset between the two letter positions of the two rotors
        interval = zero_point_2 - zero_point_1

        i = list(range(26))
        # Find the subsequent letter from the second rotor given the index on
        # the first taking into account the maximum index of 25
        if interval > 0:
            n = i[(terminal + interval) % len(i)]
        else:
            n = i[(26 + terminal + interval) % len(i)]

        self.logger.debug(
            "Rotor %s rotor to %s rotor conversion: %s to %s",
            name1,
            name2,
            letter,
            self.rotors[name2].alpha[n],
        )

        if not self.rotors[name2].alpha[n]:
            raise AssertionError(
                f"Inter-rotor conversion from {name1} -> {name2} failed for letter {letter}"
            )

        return self.rotors[name2].alpha[n]

    def _get_inter_rotor_conv_inv(self, name1: str, name2: str, letter: str) -> str:
        """
        Find inverse conversion between rotors (same as forward conversion).

        Arguments
        ---------
        name1   (string)    first rotor label, e.g. 'middle'

        name2   (string)    second rotor label, e.g. 'right'

        """
        return self._get_inter_rotor_conv(name1, name2, letter)

    def type_letter(self, letter: str) -> str:
        """
        Pass letter through the enigma machine system and find cipher

        Arguments
        ---------

        letter  (string)    letter to encode

        Returns
        -------
        the cipher for the given letter as a string

        """
        # Convert input to upper case before passing through machine
        letter = letter.upper()

        self.logger.debug("-----------------------")

        # Pass letter through the plugboard and get cipher
        cipher = self.plugboard.plugboard_conversion(letter)

        self.logger.debug("Plugboard conversion: %s to %s", letter, cipher)

        # Move the rightmost rotor by 1
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
            adj_rotor_key_index = self._rotor_dict_keys.index(rotor_key) - 1
            # At this point we should be ready for reflection
            if adj_rotor_key_index < 0:
                break
            adj_rotor_key = self._rotor_dict_keys[adj_rotor_key_index]
            cipher = self._get_inter_rotor_conv(rotor_key, adj_rotor_key, cipher)
        else:
            raise ValueError("Failed to create cipher")

        cipher = self._get_reflector_conv(cipher)

        # Start making the cipher
        for rotor_key in self._rotor_dict_keys:
            # Get the rotor conversion for given key
            cipher = self._get_rotor_conv_inv(rotor_key, cipher)
            try:
                # Get the inter rotor conv_inversion for the key and the key-1
                adj_rotor_key_index = self._rotor_dict_keys.index(rotor_key) + 1
                adj_rotor_key = self._rotor_dict_keys[adj_rotor_key_index]
                cipher = self._get_inter_rotor_conv_inv(
                    rotor_key, adj_rotor_key, cipher
                )
            except IndexError:
                # At this point we should be ready for reflection
                break
        else:
            raise ValueError("Failed to create cipher")

        # Pass cipher back through plugboard
        cipher_out = self.plugboard.plugboard_conversion_inv(cipher)

        self.logger.debug("Plugboard conversion: %s to %s", cipher, cipher_out)
        self.logger.debug("-----------------------")

        return cipher_out

    def _get_reflector_conv(self, phrase: str) -> str:
        """
        Find cipher when given phrase/letter is passed through the reflector.

        Arguments
        ---------
        phrase  (string)    phrase to encode via the reflector

        Returns
        -------
        the cipher of for the given phrase as a string

        """
        out = self.reflector.reflector_conversion(phrase)
        self.logger.debug("Reflector conversion: %s to %s", phrase, out)
        return out

    def type_phrase(self, phrase: str) -> str:
        """
        Encode phrase using this enigma machine instance.

        Arguments
        ---------
        phrase  (string)    phrase to encode

        Returns
        -------
        the encoded phrase as a string of group letters

        """
        # Remove spaces from the phrase string
        phrase = phrase.replace(" ", "")

        # Determine how many extra characters are required in order to assemble
        # cipher into the expected groups of 5 letters
        remainder = 5 - len(phrase) % 5 if len(phrase) % 5 != 0 else 0

        # Generate as many random letters and append to the input phrase
        for _ in range(remainder):
            phrase += random.choice(string.ascii_letters.upper())

        out_str = "".join(self.type_letter(letter) for letter in list(phrase))

        # Format the output to be groups five letters in size
        out_str = " ".join(out_str[i : i + 5] for i in range(0, len(out_str), 5))

        return out_str

    def set_key(self, key: str) -> None:
        """
        Set the cipher key by positioning the machine rotors.

        Arguments
        ---------
        key (string)    cipher key, which should be the same length as the
                        number of rotors for the given machine variant

        """
        if len(self.rotors) != len(key):
            raise ValueError("Key length must match no. of rotors.")
        if not key.isalpha():
            raise ValueError("Key can only contain alphabetic characters!")

        key = key.upper()

        # Position the rotors of the machine to match the input key
        for rotor_dict_key, letter in zip(self._rotor_dict_keys, key):
            self._set_rotor(rotor_dict_key, letter)

    def rewire_plugboard(self, letter_1: str, letter_2: str) -> None:
        """
        Rewire the plugboard connecting two letters both forward and backward.

        Arguments
        ---------
        letter_1    (char)      First letter to connect with wire.
        letter_2    (char)      Second letter to connect with wire.

        """
        if not isinstance(letter_1, str) and isinstance(letter_2, str):
            raise ValueError(
                "Invalid Characters for Plugboard Rewiring '%s' and '%s'",
                letter_1,
                letter_2,
            )

        if letter_1 != letter_2:
            raise AssertionError("Letters for Plugboard Rewiring must be Unique")

        self.plugboard.rewire(letter_1, letter_2)
