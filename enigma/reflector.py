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

class reflector_B(reflector):
    def __init__(self):
        super().__init__()
        self._reflector_dict = { 'A' : 'Y', 'B' : 'R', 'C' : 'U',
                                 'D' : 'H', 'E' : 'Q', 'F' : 'S',
                                 'G' : 'L', 'H' : 'D', 'K' : 'N',
                                 'L' : 'G', 'M' : 'O', 'N' : 'K',
                                 'O' : 'M', 'P' : 'I', 'Q' : 'E',
                                 'R' : 'B', 'S' : 'F', 'T' : 'Z',
                                 'U' : 'C', 'V' : 'W', 'W' : 'V',
                                 'X' : 'J', 'Y' : 'A', 'Z' : 'T',
				                 'I' : 'P', 'J' : 'X'}

class reflector_C(reflector):
    def __init__(self):
        super().__init__()
        self._reflector_dict = { 'A' : 'F', 'B' : 'V', 'C' : 'P',
                                 'D' : 'J', 'E' : 'I', 'F' : 'A',
                                 'G' : 'O', 'H' : 'Y', 'K' : 'R',
                                 'L' : 'Z', 'M' : 'X', 'N' : 'W',
                                 'O' : 'G', 'P' : 'C', 'Q' : 'T',
                                 'R' : 'K', 'S' : 'U', 'T' : 'Q',
                                 'U' : 'S', 'V' : 'B', 'W' : 'N',
                                 'X' : 'M', 'Y' : 'H', 'Z' : 'L',
				                 'I' : 'E', 'J' : 'D'}
