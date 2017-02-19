class plugboard:
    def __init__(self):
        self._plug_board_dict = { 'A' : 'Z', 'B' : 'P', 'C' : 'M',
                                 'D' : 'S', 'E' : 'Y', 'F' : 'U',
                                 'G' : 'N', 'H' : 'V', 'I' : 'Q',
                                 'J' : 'X', 'K' : 'T', 'L' : 'R',
                                 'M' : 'C', 'N' : 'G', 'O' : 'W', 
                                 'P' : 'B', 'Q' : 'I', 'R' : 'L',
                                 'S' : 'D', 'T' : 'K', 'U' : 'F', 
                                 'V' : 'H', 'W' : 'O', 'X' : 'J',
                                 'Y' : 'E', 'Z' : 'A'}
        
    def plugboard_conversion(self, letter):
        return self._plug_board_dict[letter]
    
    def plugboard_conversion_inv(self, letter):
        for key in self._plug_board_dict:
            if self._plug_board_dict[key] == letter:
                return key