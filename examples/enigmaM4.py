import enigma

enigma_m4 = enigma.Enigma(debug="DEBUG", enigma_type="M4", rotor_list=[1, 3, 5, 8])
version = enigma_m4.version

if enigma_m4.is_beta:
    version += " (BETA)"

intro = """
===========================================

  WELCOME TO THE PYTHON ENIGMA M4 ENCODER
                  {}
          
           Kristian Zarebski

===========================================
Type 'q' or 'quit' to exit.
              
""".format(
    version
)

inp = ""

print(intro)
while inp not in ["quit", "q"]:
    enigma_m4 = enigma.Enigma(debug="DEBUG", enigma_type="M4", rotor_list=[1, 3, 5, 8])
    enigma_m4.set_key("LEAR")
    inp = input("INPUT: ")
    if inp not in ["quit", "q"]:
        print("OUTPUT: {}".format(enigma_m4.type_phrase(inp)))
