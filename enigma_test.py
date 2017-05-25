import enigma

enigma_m3 = enigma.Enigma()

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

    inp = input("INPUT: ")
    if inp not in ['quit', 'q']:
        print("OUTPUT: {}".format(enigma_m3.type_phrase(inp)))
