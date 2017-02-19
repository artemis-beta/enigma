class reflector:
    def __init__(self):
        self._reflector_dict = { 'A' : 'P', 'B' : 'Z', 'C' : 'H',
                                 'D' : 'S', 'E' : 'Y', 'F' : 'U',
                                 'G' : 'N', 'H' : 'M', 'K' : 'B',
                                 'L' : 'F', 'M' : 'D', 'N' : 'K',
                                 'O' : 'J', 'P' : 'L', 'Q' : 'C',
                                 'R' : 'T', 'S' : 'W', 'T' : 'X',
                                 'U' : 'A', 'V' : 'E', 'W' : 'I',
                                 'X' : 'R', 'Y' : 'O', 'Z' : 'G',
				 'I' : 'Q', 'J' : 'V'}
        
    def reflector_conversion(self, letter):
        return self._reflector_dict[letter]
