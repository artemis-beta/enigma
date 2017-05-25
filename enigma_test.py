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
while inp not in ['quit', 'q']:
    enigma_m3 = enigma.Enigma(debug='DEBUG')
    enigma_m3.set_key('ARE')
    inp = input("INPUT: ")
    if inp not in ['quit', 'q']:
        print("OUTPUT: {}".format(enigma_m3.type_phrase(inp)))
