###############################################################################
#                                                                             #
#                               Plugboard Class                               #
#                                                                             #
#   Class to represent the plugboard component of the Enigma machine whereby  #
#   a manual conversion between two letters is set by plugging a wire between #
#   two terminals.                                                            #
#                                                                             #
#   @authors :   K. Zarebski                                                  #
#   @date    :   last modified 2020-01-12                                     #
#                                                                             #
###############################################################################


class Plugboard:
    """
    Class representing the Enigma plugboard component for manual letter
    encoding by connecting two letters via a dictionary
    """

    def __init__(self) -> None:
        """Initialise a plugboard instance as a Python dictionary."""

        # Initialise member Python dictionary for encoding characters
        self._plug_board_dict = {
            "A": "Z",
            "B": "P",
            "C": "M",
            "D": "S",
            "E": "Y",
            "F": "U",
            "G": "N",
            "H": "V",
            "I": "Q",
            "J": "X",
            "K": "T",
            "L": "R",
            "M": "C",
            "N": "G",
            "O": "W",
            "P": "B",
            "Q": "I",
            "R": "L",
            "S": "D",
            "T": "K",
            "U": "F",
            "V": "H",
            "W": "O",
            "X": "J",
            "Y": "E",
            "Z": "A",
        }

    def plugboard_conversion(self, letter: str) -> str:
        """
        Encode a given letter using the plugboard dictionary.

        Arguments
        ---------
        letter  (string)    letter to encode

        Returns
        -------
        output encoded letter as string

        """
        return self._plug_board_dict[letter]

    def plugboard_conversion_inv(self, letter: str) -> str:
        """
        Perform reverse encoding on the given letter.

        Arguments
        ---------
        letter  (string)    letter to encode

        Returns
        -------
        output reverse encoded letter as string

        """
        for key in self._plug_board_dict:
            if self._plug_board_dict[key] == letter:
                return key

        raise KeyError(f"Could not find conversion for '{letter}'")

    def rewire(self, letter_1: str, letter_2: str) -> None:
        """
        Rewire two letters both forward and backward.
        e.g. A->K and K->A. Automatically updates to avoid duplicates.

        Arguments
        ---------
        letter_1    (char)      First letter to connect with wire.
        letter_2    (char)      Second letter to connect with wire.

        """
        # Find existing conversions for given letters
        init_1 = self.plugboard_conversion(letter_1)
        init_2 = self.plugboard_conversion_inv(letter_2)

        # Perform swap based on chosen letters
        self._plug_board_dict[letter_1] = letter_2
        self._plug_board_dict[letter_2] = letter_1
        self._plug_board_dict[init_2] = init_1
        self._plug_board_dict[init_1] = init_2
