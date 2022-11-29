# ENIGMA
![python3.8](https://github.com/artemis-beta/enigma/workflows/python3.8/badge.svg) ![python3.9](https://github.com/artemis-beta/enigma/workflows/python3.9/badge.svg) ![python3.10](https://github.com/artemis-beta/enigma/workflows/python3.10/badge.svg) ![python3.11](https://github.com/artemis-beta/enigma/workflows/python3.11/badge.svg)

[![CodeFactor](https://www.codefactor.io/repository/github/artemis-beta/enigma/badge)](https://www.codefactor.io/repository/github/artemis-beta/enigma)![GitHub](https://img.shields.io/github/license/artemis-beta/enigma) [![codecov](https://codecov.io/gh/artemis-beta/enigma/branch/master/graph/badge.svg?token=9D087TSZEA)](https://codecov.io/gh/artemis-beta/enigma) 

This is a small application written in python which simulates both the M3 and M4, 3 and 4 rotor variants of the Enigma machine which was utilised by German forces during WWII to encode information.

Included are two example scripts which can be found in the `examples` folder, these demonstrate the two variants.

For the C++ version of this application visit [here](https://github.com/artemis-beta/enigma-cpp).

## Installation

To install simply run:
```bash
pip install .
```
within the repository directory.

## Executable
After installing the module the command `enigma` is available within the terminal and can be used to launch a demonstration application.

## Custom Machine
To create a new instance of Enigma the default can be used which is an M3 instance with pre-selected rotor arrangement and reflector choice, or all settings can be chosen by the user. Note as with the machine itself, one of the 8 numbered rotor types may only be selected once:
```python
my_rotor_list = [1,4,6,3]     # 3 or 4 of 1,2,3,4,5,6,7,8
my_reflector  = 'B'           # 'B' or 'C'
machine_type  = 'M4'          # 'M3' or 'M4' (should match rotor list)
debug_level   = 'ERROR'       # 'ERROR', 'INFO', 'DEBUG' (see python 'logging' module documentation)

enigma = enigma.Enigma( rotor_list     = my_rotor_list ,
                        user_reflector = my_reflector  ,
                        enigma_type    = machine_type  ,
                        debug          = debug_level)

enigma.ringstellung('right', 2)  # Perform an internal wire rotation on the right rotor of 2 steps 
                                 # for M3 rotors are ['left', 'middle', 'right']
                                 # for M4 rotors are ['left', 'middle left', 'middle right', 'right']

enigma.set_key('NERO')
enigma.type_phrase('NOBODYEXPECTSTHESPANISHINQUISITION')
```
