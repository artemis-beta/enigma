###############################################################################
#                                                                             #
#                          Enigma Application Script                          #
#                                                                             #
#   Script to run an instance of Enigma with the user providing arguments     #
#   via a CLI like interface. This provides a quick demo of the module's      #
#   capability.                                                               #
#                                                                             #
#   @authors :   K. Zarebski                                                  #
#   @date    :   last modified 2021-08-14                                     #
#                                                                             #
###############################################################################
import enigma
from typing import List


class EnigmaApp:
    """
    Terminal demonstration application for the Enigma machine Python module.
    Consists of a set of prompts to the user allowing them to setup a machine
    and then enter phrases to be encoded.
    """

    def __init__(self) -> None:
        """Initialise a new instance of the Enigma Terminal Application"""
        _enigma_m3_intro = enigma.Enigma(debug="DEBUG")
        _version = _enigma_m3_intro.version
        self._key: str = ""
        self._rotors: List[int] = []

        if _enigma_m3_intro.is_beta:
            _version += " (BETA)"

        _intro = """
        ===========================================

           WELCOME TO THE PYTHON ENIGMA ENCODER
                        {}

                   Kristian Zarebski

        ===========================================
        Type 'q' or 'quit' to exit.

        """.format(
            _version
        )

        print(_intro)

    def ringstellung_option(self) -> List[int]:
        """Give prompt asking if user wants to apply Ringstellung."""
        _choice = ""
        _ringstellung_offsets = None

        while _choice.upper() not in ["Y", "N"]:
            _choice = input("Ringstellung? [y/N] ")
            if _choice.upper() in ["Q", "QUIT"]:
                exit(0)

        if _choice == "N":
            return [0] * (len(self._rotors) - 1)

        while not _ringstellung_offsets:
            try:
                _rsg_input = input(f"Set Number of Internal Wiring Rotation Increments for Each of the {len(self._key)} Rotors: ")


                _ringstellung_offsets = [
                    int(i) for i in list(_rsg_input.replace(" ", "").strip())
                ]

                if len(_ringstellung_offsets) != len(
                    self._key
                ):
                    raise AssertionError("Invalid number of offsets")

            except (AssertionError, ValueError):
                _ringstellung_offsets = None

        return _ringstellung_offsets

    def key_set_option(self):
        """Give prompt asking if the user wishes to set a machine key."""
        _choice = ""
        _key = None

        while _choice.upper() not in ["Y", "N"]:
            _choice = input("Set key? [y/N] ")
            if _choice.upper() in ["Q", "QUIT"]:
                exit(0)

        if _choice.upper() == "N":
            return "YES"

        while not _key:
            try:
                _key = input("Enter 3/4 character key: ")
                if len(_key) not in {3, 4}:
                    raise AssertionError("Only Enigma M3 and Enigma M4 supported")

                if not _key.isalpha():
                    raise AssertionError(f"Key '{_key}' must be formed of characters only")

            except AssertionError:
                _key = None

        return _key

    def rotor_set_option(self) -> List[int]:
        """Give prompt asking if user wants to set rotors for the machine."""
        _choice = ""
        _rotors = None

        while _choice.upper() not in ["Y", "N"]:
            _choice = input("Set Rotors? [y/N] ")
            if _choice.upper() in ["Q", "QUIT"]:
                exit(0)

        if _choice.upper() == "N":
            return [2, 3, 4]

        while not _rotors:
            try:
                _rotor_input = input(f"Set Number Combination ({len(self._key)} Unique space separated numbers 1-8): ")


                _rotors = [int(i) for i in list(_rotor_input.replace(" ", "").strip())]

                if len(_rotors) != len(self._key):
                    raise AssertionError("Invalid number of rotor inputs")

            except (AssertionError, ValueError):
                _rotors = None

        return _rotors

    def fetch_phrases(self, machine: enigma.Enigma, ringstellung: List[int]) -> None:
        """Request user inputs for phrases to encode."""
        self.apply_rsg(ringstellung, machine)

        _input_phrase = ""
        while _input_phrase not in ["quit", "q", "exit"]:
            _input_phrase = input("INPUT: ")
            if _input_phrase not in ["quit", "q", "exit"]:
                if _input_phrase == "reset":
                    enigma_ = enigma.Enigma(
                        rotor_list=self._rotors,
                        enigma_type=self._enigma_type,
                        debug="DEBUG",
                    )
                    enigma_.set_key(self._key)
                    self.apply_rsg(ringstellung, machine)
                print(f"OUTPUT: {machine.type_phrase(_input_phrase)}")

    def run(self) -> None:
        """Run terminal application"""
        self._enigma_type = "M3" if len(self._key) == 3 else "M4"

        _enigma = enigma.Enigma(
            rotor_list=self._rotors, enigma_type=self._enigma_type, debug="DEBUG"
        )

        self._key = self.key_set_option()

        self._rotors = self.rotor_set_option()

        _ringstellung = self.ringstellung_option()

        self.fetch_phrases(_enigma, _ringstellung)

    def apply_rsg(self, ringstellung: List[int], machine: enigma.Enigma) -> None:
        """Apply the ringstellung offsets to an Enigma instance."""
        for terminal, name in zip(ringstellung, machine.rotors.keys()):
            machine.ringstellung(name, terminal)


def main():
    """Main method for command line executable"""
    EnigmaApp().run()
