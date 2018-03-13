import enigma

enigma_m3 = enigma.Enigma(debug='DEBUG')
version = enigma_m3.version

if enigma_m3.isBeta:
   version += ' (BETA)'

intro='''
===========================================

  WELCOME TO THE PYTHON ENIGMA 3 ENCODER
                  {}
          
           Kristian Zarebski

===========================================
Type 'q' or 'quit' to exit.
              
'''.format(version)

def apply_rsg(rsg, eg):
        if eg_type == 'M3':
            for i, name in zip(rsg, ['left', 'middle', 'right']):
                eg.ringstellung(name, i)
        else:
            for i, name in zip(rsg, ['left', 'middle left', 'middle right', 'right']):
                eg.ringstellung(name, i)

inp = ''

print(intro)
choice = ''
rotors = [2,3,4]
key  = 'YES'
while choice not in ['y','Y','n','N']:
   choice = input('Set key? [y/N] ')
if choice.upper() == 'Y':
    key = input('Enter 3/4 character key: ')
    assert len(key) == 3 or len(key) == 4, "Only Enigma M3 and Enigma M4 supported"
choice=''
while choice not in ['y','Y','n','N']:
    choice = input('Set Rotors? [y/N] ')
if choice.upper() == 'Y':
    rot = input('Set Number Combination (Unique numbers 1-8): ')
    rotors = [ int(a) for a in rot ]
    assert len(rotors) == len(key), "Rotor Quantity Does not Match Key Length"
choice=''

eg_type = 'M3' if len(rotors) == 3 else 'M4'

enigma_ = enigma.Enigma(rotor_list=rotors, enigma_type=eg_type, debug='DEBUG')

rsg = [0 for i in range(len(rotors)-1)]

while choice not in ['y','Y','n','N']:
    choice = input('Ringstellung? [y/N] ')
    if choice.upper() == 'Y':
        rot = input('Set Number of Internal Wiring Rotation Increments for Each Rotor: ')
        rsg = [ int(a) for a in rot ]
        apply_rsg(rsg, enigma_)

while inp not in ['quit', 'q', 'exit']:
    inp = input("INPUT: ")
    if inp not in ['quit', 'q', 'exit']:
        if inp == "reset":
            enigma_ = enigma.Enigma(rotor_list=rotors, enigma_type=eg_type, debug='DEBUG')
            enigma_.set_key(key)
            apply_rsg(rsg, enigma_)
        print("OUTPUT: {}".format(enigma_m3.type_phrase(inp)))
