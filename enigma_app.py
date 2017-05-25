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

inp = ''

print(intro)
choice = ''
rotors = [2,3,4]
key  = 'YES'
while choice not in ['y','Y','n','N']:
   choice = input('Set 3 letter key? [y/N] ')
if choice.upper() == 'Y':
    key = input('Enter 3 letter key: ')

choice=''
while choice not in ['y','Y','n','N']:
    choice = input('Set Rotors? [y/N] ')
if choice.upper() == 'Y':
    rot = input('Set Number Combination (Unique numbers 1-8): ')
    rotors = [ int(a) for a in rot ]

while inp not in ['quit', 'q']:
    enigma_m3 = enigma.Enigma(rotor_list=rotors)
    enigma_m3.set_key(key)
    inp = input("INPUT: ")
    if inp not in ['quit', 'q']:
        print("OUTPUT: {}".format(enigma_m3.type_phrase(inp)))
