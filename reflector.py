class reflector:
    def __init__(self):
        self._reflector_dict = { 'A' : 'P', 'B' : 'Z', 'C' : 'H',
                                 'D' : 'S', 'E' : 'Y', 'F' : 'U',
                                 'G' : 'N', 'H' : 'J', 'K' : 'B',
                                 'L' : 'F', 'M' : 'D', 'N' : 'K',
                                 'O' : 'H', 'P' : 'L', 'Q' : 'C',
                                 'R' : 'T', 'S' : 'W', 'T' : 'P',
                                 'U' : 'A', 'V' : 'E', 'W' : 'I',
                                 'X' : 'R', 'Y' : 'O', 'Z' : 'G'}
        
    def reflector_conversion(self, letter):
        return self._reflector_dict[letter]