###############################################################################
#                                                                             #
#                               Reflector Class                               #
#                                                                             #
#   Class to represent the reflector component of an Enigma machine, the      #
#   input letter is translated to another letter in a pattern unique to the   #
#   reflector type before being sent back through the machine as an output.   #
#                                                                             #
#   @authors :   K. Zarebski                                                  #
#   @date    :   last modified 2020-01-12                                     #
#                                                                             #
###############################################################################

from typing import Dict


class Reflector:
    """
    Base class for construction of a reflector which sends forward encoded
    cipher back through enigma machine after translation.
    """

    def __init__(self) -> None:
        """Initialise an instance of the reflector class."""
        self._reflector_dict: Dict[str, str] = {}

    def reflector_conversion(self, letter: str) -> str:
        """
        Pass the given letter through the reflector and obtain cipher.

        Arguments
        ---------
        letter  (string)    input letter to encode

        Returns
        -------
        encoded letter as string

        """
        try:
            return self._reflector_dict[letter]
        except KeyError as e:
            raise KeyError(f"Could not find '{letter}' in Reflector Dictionary") from e


class ReflectorB(Reflector):
    """Enigma Reflector Type B"""

    def __init__(self) -> None:
        """
        Initialise a Type B Enigma Reflector.

        Definitions for Reflector B conversions are obtained from:
        https://www.codesandciphers.org.uk/enigma/rotorspec.htm

        """
        super().__init__()

        self.name = "B"

        self._reflector_dict = {
            "A": "Y",
            "B": "R",
            "C": "U",
            "D": "H",
            "E": "Q",
            "F": "S",
            "G": "L",
            "H": "D",
            "K": "N",
            "L": "G",
            "M": "O",
            "N": "K",
            "O": "M",
            "P": "I",
            "Q": "E",
            "R": "B",
            "S": "F",
            "T": "Z",
            "U": "C",
            "V": "W",
            "W": "V",
            "X": "J",
            "Y": "A",
            "Z": "T",
            "I": "P",
            "J": "X",
        }


class ReflectorC(Reflector):
    """Enigma Reflector Type C"""

    def __init__(self) -> None:
        """
        Initialise a Type C Enigma Reflector.

        Definitions for Reflector C conversions are obtained from:
        https://www.codesandciphers.org.uk/enigma/rotorspec.htm

        """
        super().__init__()

        self.name = "C"

        self._reflector_dict = {
            "A": "F",
            "B": "V",
            "C": "P",
            "D": "J",
            "E": "I",
            "F": "A",
            "G": "O",
            "H": "Y",
            "K": "R",
            "L": "Z",
            "M": "X",
            "N": "W",
            "O": "G",
            "P": "C",
            "Q": "T",
            "R": "K",
            "S": "U",
            "T": "Q",
            "U": "S",
            "V": "B",
            "W": "N",
            "X": "M",
            "Y": "H",
            "Z": "L",
            "I": "E",
            "J": "D",
        }
