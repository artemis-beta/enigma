import random

class rotor:
    def __init__(self):

        self.alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                      'H', 'I', 'J', 'K', 'L', 'M', 'N',
                      'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                      'V', 'W', 'X', 'Y', 'Z']
        
        self.notch = self.alpha[random.randint(0,25)]

        self.input = self.alpha[random.randint(0,25)]

        self.wiring = {}

        for i in range(len(self.alpha)):
            n = i
            allocated = []
            while n==i or n in allocated:
                n = random.randint(0, len(self.alpha)-1)
            allocated.append(n)
            self.wiring[i] = n

    def rotate_rotor(self, other=None):
        pos = self.alpha.index(self.input)
        if pos == 25:
            pos = 0
        else:
            pos += 1
        if other:
            other.rotate_rotor()

        self.input = self.alpha[pos]

    def rotate_inner_ring(self):
        for wire in self.wiring:
            if self.wiring[wire] == 26:
                self.wiring[wire+1] = 0
            elif wire == 26:
                x = self.wiring[wire]
                self.wiring[0] = x+1
            else:
                x = self.wiring[wire]
                self.wiring[wire+1] = x+1

    def get_output_terminal(self, letter):
        i = self.alpha.index(letter)
        return self.wiring[i]
    
    def get_input_terminal(self, letter):
        i = self.alpha.index(letter)
        for key in self.wiring:
            if key == i:
                return key

    def get_rotor_conversion(self, letter):
        i = self.alpha.index(letter)
        return self.alpha[self.wiring[i]]

    def get_rotor_conversion_inv(self, letter):
        i = self.alpha.index(letter)
        for key in self.wiring:
            if key == i:
                return self.alpha[key]