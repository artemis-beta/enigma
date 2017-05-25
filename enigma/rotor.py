import random

class rotor:
    def __init__(self):

        self.alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                      'H', 'I', 'J', 'K', 'L', 'M', 'N',
                      'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                      'V', 'W', 'X', 'Y', 'Z']
        
        self.notches = [self.alpha[random.randint(0,25)]]

        self.face = self.alpha[random.randint(0,25)]

        self.name = 'rotor_temp'

        self.wiring = {}

        for i in range(len(self.alpha)):
            n = i
            allocated = []
            while n==i or n in allocated:
                n = random.randint(0, len(self.alpha)-1)
            allocated.append(n)
            self.wiring[i] = n

    def rotate_rotor(self, other=None):
        pos = self.alpha.index(self.face)
        if pos == 25:
            pos = 0
        else:
            pos += 1
        if other:
            other.rotate_rotor()

        self.face = self.alpha[pos]

    def rotate_inner_ring(self):
        x = self.wiring[0]
        for wire in self.wiring:
            if wire == 26:
                self.wiring[wire] = x
            else:
                y = self.wiring[wire+1]
                self.wiring[wire] = y

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
        print(self.alpha[self.wiring[i]])
        try:
            assert self.alpha[self.wiring[i]] is not None, "ERROR: Wiring element '{}' returned 'None'"
            return self.alpha[self.wiring[i]]
        except:
            raise SystemExit

    def get_rotor_conversion_inv(self, letter):
        i = self.alpha.index(letter)
        for key in self.wiring:
            if self.wiring[key] == i:
                print(self.alpha[key])
                try:
                    assert self.alpha[key] is not None, "ERROR: Wiring element '{}' returned 'None'"
                    return self.alpha[key]
                except:  
                    raise SystemExit

        ## Let's Be Safe and Check That All Rotors Function Correctly
        print("ERROR: Could not find key which returns alphabet index {} in wiring dictionary for rotor '{}':".format(self.alpha.index(letter), self.name))
        print(list(self.wiring.values()))
        seen = set()
        for x in list(self.wiring.values()):
            if list(self.wiring.values()).count(x) >= 2:
               seen.add(x)
        if len(seen) != 0:
           print("Duplicates found: ")
           print(seen)
        else:
           print("Have you missed out a value in the wiring definition range 0-25?")
        raise SystemExit

class rotor_1(rotor):
    def __init__(self):
        super().__init__()
        self.name   = 'I'
        self.wiring = {0 : 4, 1 : 10, 2 : 12,
                    3 : 5, 4 : 11, 5 : 6,
                    6 : 3, 7 : 16, 8 : 21,
                    9 : 25, 10 : 13, 11 : 19,
                    12 : 14, 13 : 22, 14 : 24,
                    15 : 7, 16 : 23, 17 : 20,
                    18 : 18, 19 : 15, 20 : 0,
                    21 : 8, 22 : 1, 23 : 17,
                    24 : 2, 25 : 9}
        
        self.notches = ['R']
        self.face = 'A'


class rotor_2(rotor):
    def __init__(self):
        super().__init__()
        self.name   = 'II'
        self.wiring = {0 : 0, 1 : 9, 2 : 3,
                    3 : 10, 4 : 18, 5 : 8,
                    6 : 17, 7 : 20, 8 : 23,
                    9 : 1, 10 : 11, 11 : 7,
                    12 : 22, 13 : 19, 14 : 12,
                    15 : 2, 16 : 16, 17 : 6,
                    18 : 25, 19 : 13, 20 : 15,
                    21 : 24, 22 : 5, 23 : 21,
                    24 : 14, 25 : 4}
        
        self.notches = ['F']
        self.face = 'A'

class rotor_3(rotor):
    def __init__(self):
        super().__init__()
        self.name   = 'III'
        self.wiring = {0 : 1, 1 : 3, 2 : 5,
                    3 : 7, 4 : 9, 5 : 11,
                    6 : 2, 7 : 15, 8 : 17,
                    9 : 19, 10 : 23, 11 : 21,
                    12 : 25, 13 : 13, 14 : 24,
                    15 : 4, 16 : 8, 17 : 22,
                    18 : 6, 19 : 0, 20 : 10,
                    21 : 12, 22 : 20, 23 : 18,
                    24 : 16, 25 : 14}
        
        self.notches = ['W']
        self.face = 'A'

class rotor_4(rotor):
    def __init__(self):
        super().__init__()
        self.name   = 'IV'
        self.wiring = {0 : 4, 1 : 18, 2 : 14,
                    3 : 21, 4 : 15, 5 : 25,
                    6 : 9, 7 : 0, 8 : 24,
                    9 : 16, 10 : 20, 11 : 8,
                    12 : 17, 13 : 7, 14 : 23,
                    15 : 11, 16 : 13, 17 : 5,
                    18 : 19, 19 : 6, 20 : 10,
                    21 : 3, 22 : 2, 23 : 12,
                    24 : 22, 25 : 1}
        
        self.notches = ['K']
        self.face = 'A'

class rotor_5(rotor):
    def __init__(self):
        super().__init__()
        self.name   = 'V'
        self.wiring = {0 : 21, 1 : 25, 2 : 1,
                    3 : 17, 4 : 6, 5 : 8,
                    6 : 19, 7 : 24, 8 : 20,
                    9 : 15, 10 : 18, 11 : 3,
                    12 : 13, 13 : 7, 14 : 11,
                    15 : 23, 16 : 0, 17 : 22,
                    18 : 12, 19 : 9, 20 : 16,
                    21 : 14, 22 : 5, 23 : 4,
                    24 : 2, 25 : 10}
        
        self.notches = ['A']
        self.face = 'A'

class rotor_6(rotor):
    def __init__(self):
        super().__init__()
        self.name   = 'VI'
        self.wiring = {0 : 9, 1 : 15, 2 : 6,
                    3 : 21, 4 : 14, 5 : 20,
                    6 : 12, 7 : 5, 8 : 24,
                    9 : 16, 10 : 1, 11 : 4,
                    12 : 13, 13 : 7, 14 : 25,
                    15 : 17, 16 : 3, 17 : 10,
                    18 : 0, 19 : 18, 20 : 23,
                    21 : 11, 22 : 8, 23 : 2,
                    24 : 19, 25 : 22}
        
        self.notches = ['A', 'N']
        self.face = 'A'

class rotor_7(rotor):
    def __init__(self):
        super().__init__()
        self.name   = 'VII'
        self.wiring = {0 : 13, 1 : 25, 2 : 9,
                    3 : 7, 4 : 6, 5 : 17,
                    6 : 2, 7 : 23, 8 : 12,
                    9 : 24, 10 : 18, 11 : 22,
                    12 : 1, 13 : 14, 14 : 20,
                    15 : 5, 16 : 0, 17 : 8,
                    18 : 21, 19 : 11, 20 : 15,
                    21 : 4, 22 : 10, 23 : 16,
                    24 : 3, 25 : 19}
        
        self.notches = ['A', 'N']
        self.face = 'A'

class rotor_8(rotor):
    def __init__(self):
        super().__init__()
        self.name   = 'VIII'
        self.wiring = {0 : 5, 1 : 10, 2 : 16,
                    3 : 7, 4 : 19, 5 : 11,
                    6 : 23, 7 : 14, 8 : 2,
                    9 : 1, 10 : 9, 11 : 18,
                    12 : 15, 13 : 3, 14 : 25,
                    15 : 17, 16 : 0, 17 : 12,
                    18 : 4, 19 : 22, 20 : 13,
                    21 : 8, 22 : 20, 23 : 24,
                    24 : 6, 25 : 21}
        
        self.notches = ['A', 'N']
        self.face = 'A'
