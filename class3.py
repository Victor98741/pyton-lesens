class Fraction:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        
    def __str__(self):
        return f'{self.numer} / {self.denom}'
    
    def __add__(self, other):
        result1 = self.numer * other.denom + self.denom * other.numer
        result2 = self. denom * other.denom
        return Fraction(result1, result2)
    
    def __sub__ (self, other):
        result1 = self.numer * other.denom - self.denom * other.numer
        result2 = self. denom * other.denom
        return Fraction(result1, result2)
    
    def convert (self):
        result = self.numer / self.denom
        return result
oneHalf = Fraction(1, 2)
twoThirds = Fraction(2, 3)

print(oneHalf.convert()) 


