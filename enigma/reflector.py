class reflector:
    def __init__(self):
       	self._reflector_dict = None
 
    def reflector_conversion(self, letter):
        try:
            if self._reflector_dict[letter]:
                return self._reflector_dict[letter]
        except:
            print("ERROR: Could not find '{}' in Reflector Dictionary".format(letter))
            raise SystemExit

class reflector_B(reflector):
    def __init__(self):
        super().__init__()
        self.name  = 'B'
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
        self.name  = 'C'
        self._reflector_dict = { 'A' : 'F', 'B' : 'V', 'C' : 'P',
                                 'D' : 'J', 'E' : 'I', 'F' : 'A',
                                 'G' : 'O', 'H' : 'Y', 'K' : 'R',
                                 'L' : 'Z', 'M' : 'X', 'N' : 'W',
                                 'O' : 'G', 'P' : 'C', 'Q' : 'T',
                                 'R' : 'K', 'S' : 'U', 'T' : 'Q',
                                 'U' : 'S', 'V' : 'B', 'W' : 'N',
                                 'X' : 'M', 'Y' : 'H', 'Z' : 'L',
				                 'I' : 'E', 'J' : 'D'}
