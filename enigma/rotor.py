###############################################################################
#                                                                             #
#                                 Rotor Class                                 #
#                                                                             #
#   Class to represent the plugboard component of the Enigma machine whereby  #
#   a manual conversion between two letters is set by plugging a wire between #
#   two terminals.                                                            #
#                                                                             #
#   @authors :   K. Zarebski                                                  #
#   @date    :   last modified 2021-08-14                                     #
#                                                                             #
###############################################################################

import random
import string


class Rotor:
    """
    Base Rotor class for an Enigma rotor which consists of 26 positions
    representing all letters of the alphabet connecting in a unique scheme.
    """

    def __init__(self) -> None:
        """Initialise an instance of the Rotor class."""
        self.alpha = string.ascii_uppercase

        # Randomly assign a letter at which movement of the neighbouring
        # rotor is triggered
        self.notches = [self.alpha[random.randint(0, 25)]]

        # Randomly assign the starting letter position of the rotor
        self.face = self.alpha[random.randint(0, 25)]

        self.name = "Rotortemp"

        # Randomly allocated a wiring scheme to the rotor by linking two
        # letters together as an entry in the wiring scheme dictionary
        self.wiring = {}

        for i in range(len(self.alpha)):
            n = i
            allocated = []
            while n == i or n in allocated:
                n = random.randint(0, len(self.alpha) - 1)
            allocated.append(n)
            self.wiring[i] = n

    def set_notch(self, letter: str) -> None:
        """
        Set the notch location of the rotor to a given letter.

        Arguments
        ---------
        letter  (string)    letter to set as notch position

        """
        if letter.upper() not in self.alpha:
            raise AssertionError("Invalid Rotor Symbol")
        self.notches = [letter.upper()]

    def rotate_rotor(self, other=None) -> None:
        """
        Rotate this rotor (and other if specified) by one step.

        Optional Arguments
        ------------------
        other   (string)    other rotor to also rotate

        """
        # Get the position of the current face letter as an index
        pos = self.alpha.index(self.face)

        # Handle the 26 index limit by returning to 0 when the limit
        # is exceeded
        if pos == 25:
            pos = 0
        else:
            pos += 1

        # If another rotor is specified perform the same action on that
        # rotor also
        if other:
            try:
                other.rotate_rotor()
            except AttributeError as e:
                raise ValueError("Failed to rotate 'other' rotor, is it of type Rotor?") from e

        self.face = self.alpha[pos]

    def rotate_inner_ring(self) -> None:
        """'Ringstellung' movement of rotating internal wiring one interval."""

        x = self.wiring[0]
        for wire in self.wiring:
            if wire == 25:
                self.wiring[wire] = x
            else:
                y = self.wiring[wire + 1]
                self.wiring[wire] = y

    def get_output_terminal(self, letter: str) -> int:
        """
        Get the terminal index for a given letter.

        Arguments
        ---------
        letter  (string)    letter to obtain output terminal index for

        Returns
        -------
        integer index of the output terminal for the given letter

        """
        i = self.alpha.index(letter)
        return self.wiring[i]

    def get_input_terminal(self, letter: str) -> int:
        """
        Get the terminal index for a given letter.

        Arguments
        ---------
        letter  (string)    letter to obtain input terminal index for

        Returns
        -------
        integer index of the input terminal for the given letter

        """
        i = self.alpha.index(letter)

        for key in self.wiring:
            if key == i:
                return key

        raise ValueError(f"Failed to find input terminal for letter '{letter}'")

    def get_rotor_conversion(self, letter: str) -> str:
        """
        Get conversion of letter within the rotor.

        Arguments
        ---------
        letter  (string)    letter to encode

        Returns
        -------
        encoded letter as string

        """
        i = self.alpha.index(letter)
        try:
            self.alpha[self.wiring[i]]
            return self.alpha[self.wiring[i]]
        except KeyError as e:
            raise ValueError(f"Failed to find conversion for letter '{letter}'") from e

    def get_rotor_conversion_inv(self, letter: str) -> str:
        """
        Get inverse conversion of letter within the rotor.

        Arguments
        ---------
        letter  (string)    letter to encode

        Returns
        -------
        encoded letter as string

        """
        i = self.alpha.index(letter)
        for key in self.wiring:
            if self.wiring[key] == i:
                try:
                    return self.alpha[key]
                except KeyError as e:
                    raise ValueError(f"Failed to find inverse conversion for letter '{letter}' using rotor wire scheme.") from e

        # Let's Be Safe and Check That All Rotors Function Correctly
        print(f"ERROR: Could not find key which returns alphabet index {self.alpha.index(letter)} in wiring dictionary for rotor '{self.name}':")

        print(list(self.wiring.values()))
        if seen := {x for x in list(self.wiring.values()) if list(self.wiring.values()).count(x) >= 2}:
            print("Duplicates found: ")
            print(seen)
        else:
            print("Have you missed out a value in the wiring " "definition range 0-25?")
        raise SystemExit


class Rotor1(Rotor):
    """Enigma Rotor Type I"""

    def __init__(self):
        super().__init__()
        self.name = "I"
        self.wiring = {
            0: 4,
            1: 10,
            2: 12,
            3: 5,
            4: 11,
            5: 6,
            6: 3,
            7: 16,
            8: 21,
            9: 25,
            10: 13,
            11: 19,
            12: 14,
            13: 22,
            14: 24,
            15: 7,
            16: 23,
            17: 20,
            18: 18,
            19: 15,
            20: 0,
            21: 8,
            22: 1,
            23: 17,
            24: 2,
            25: 9,
        }

        self.notches = ["R"]
        self.face = "A"


class Rotor2(Rotor):
    """Enigma Rotor Type II"""

    def __init__(self) -> None:
        """
        Initialise a Type 2 Enigma rotor.

        Definitions for Type 2 Rotor conversions are obtained from:
        https://www.codesandciphers.org.uk/enigma/rotorspec.htm

        """
        super().__init__()
        self.name = "II"
        self.wiring = {
            0: 0,
            1: 9,
            2: 3,
            3: 10,
            4: 18,
            5: 8,
            6: 17,
            7: 20,
            8: 23,
            9: 1,
            10: 11,
            11: 7,
            12: 22,
            13: 19,
            14: 12,
            15: 2,
            16: 16,
            17: 6,
            18: 25,
            19: 13,
            20: 15,
            21: 24,
            22: 5,
            23: 21,
            24: 14,
            25: 4,
        }

        self.notches = ["F"]
        self.face = "A"


class Rotor3(Rotor):
    """Enigma Rotor Type III"""

    def __init__(self) -> None:
        """
        Initialise a Type 3 Enigma rotor.

        Definitions for Type 3 Rotor conversions are obtained from:
        https://www.codesandciphers.org.uk/enigma/rotorspec.htm

        """
        super().__init__()
        self.name = "III"
        self.wiring = {
            0: 1,
            1: 3,
            2: 5,
            3: 7,
            4: 9,
            5: 11,
            6: 2,
            7: 15,
            8: 17,
            9: 19,
            10: 23,
            11: 21,
            12: 25,
            13: 13,
            14: 24,
            15: 4,
            16: 8,
            17: 22,
            18: 6,
            19: 0,
            20: 10,
            21: 12,
            22: 20,
            23: 18,
            24: 16,
            25: 14,
        }

        self.notches = ["W"]
        self.face = "A"


class Rotor4(Rotor):
    """Enigma Rotor Type IV"""

    def __init__(self) -> None:
        """
        Initialise a Type 4 Enigma rotor.

        Definitions for Type 4 Rotor conversions are obtained from:
        https://www.codesandciphers.org.uk/enigma/rotorspec.htm

        """
        super().__init__()
        self.name = "IV"
        self.wiring = {
            0: 4,
            1: 18,
            2: 14,
            3: 21,
            4: 15,
            5: 25,
            6: 9,
            7: 0,
            8: 24,
            9: 16,
            10: 20,
            11: 8,
            12: 17,
            13: 7,
            14: 23,
            15: 11,
            16: 13,
            17: 5,
            18: 19,
            19: 6,
            20: 10,
            21: 3,
            22: 2,
            23: 12,
            24: 22,
            25: 1,
        }

        self.notches = ["K"]
        self.face = "A"


class Rotor5(Rotor):
    """Enigma Rotor Type V"""

    def __init__(self) -> None:
        """
        Initialise a Type 5 Enigma rotor.

        Definitions for Type 5 Rotor conversions are obtained from:
        https://www.codesandciphers.org.uk/enigma/rotorspec.htm

        """
        super().__init__()
        self.name = "V"
        self.wiring = {
            0: 21,
            1: 25,
            2: 1,
            3: 17,
            4: 6,
            5: 8,
            6: 19,
            7: 24,
            8: 20,
            9: 15,
            10: 18,
            11: 3,
            12: 13,
            13: 7,
            14: 11,
            15: 23,
            16: 0,
            17: 22,
            18: 12,
            19: 9,
            20: 16,
            21: 14,
            22: 5,
            23: 4,
            24: 2,
            25: 10,
        }

        self.notches = ["A"]
        self.face = "A"


class Rotor6(Rotor):
    """Enigma Rotor Type VI"""

    def __init__(self) -> None:
        """
        Initialise a Type 6 Enigma rotor.

        Definitions for Type 6 Rotor conversions are obtained from:
        https://www.codesandciphers.org.uk/enigma/rotorspec.htm

        """
        super().__init__()
        self.name = "VI"
        self.wiring = {
            0: 9,
            1: 15,
            2: 6,
            3: 21,
            4: 14,
            5: 20,
            6: 12,
            7: 5,
            8: 24,
            9: 16,
            10: 1,
            11: 4,
            12: 13,
            13: 7,
            14: 25,
            15: 17,
            16: 3,
            17: 10,
            18: 0,
            19: 18,
            20: 23,
            21: 11,
            22: 8,
            23: 2,
            24: 19,
            25: 22,
        }

        self.notches = ["A", "N"]
        self.face = "A"


class Rotor7(Rotor):
    """Enigma Rotor Type VII"""

    def __init__(self) -> None:
        """
        Initialise a Type 7 Enigma rotor.

        Definitions for Type 7 Rotor conversions are obtained from:
        https://www.codesandciphers.org.uk/enigma/rotorspec.htm

        """
        super().__init__()
        self.name = "VII"
        self.wiring = {
            0: 13,
            1: 25,
            2: 9,
            3: 7,
            4: 6,
            5: 17,
            6: 2,
            7: 23,
            8: 12,
            9: 24,
            10: 18,
            11: 22,
            12: 1,
            13: 14,
            14: 20,
            15: 5,
            16: 0,
            17: 8,
            18: 21,
            19: 11,
            20: 15,
            21: 4,
            22: 10,
            23: 16,
            24: 3,
            25: 19,
        }

        self.notches = ["A", "N"]
        self.face = "A"


class Rotor8(Rotor):
    def __init__(self) -> None:
        """
        Initialise a Type 8 Enigma rotor.

        Definitions for Type 8 Rotor conversions are obtained from:
        https://www.codesandciphers.org.uk/enigma/rotorspec.htm

        """
        super().__init__()
        self.name = "VIII"
        self.wiring = {
            0: 5,
            1: 10,
            2: 16,
            3: 7,
            4: 19,
            5: 11,
            6: 23,
            7: 14,
            8: 2,
            9: 1,
            10: 9,
            11: 18,
            12: 15,
            13: 3,
            14: 25,
            15: 17,
            16: 0,
            17: 12,
            18: 4,
            19: 22,
            20: 13,
            21: 8,
            22: 20,
            23: 24,
            24: 6,
            25: 21,
        }

        self.notches = ["A", "N"]
        self.face = "A"
