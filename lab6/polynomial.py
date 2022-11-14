import math
class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def deg(self):
        return len(self.coefficients) - 1

    def __str__(self):
        wynik = ''
        j = len(self.coefficients)
        while j > 1:
            wynik += str(self.coefficients[j-1]) + ' * x^' + str(j-1) + ' + '
            j -= 1
        wynik += str(self.coefficients[0])
        return wynik

    def __neg__(self):
        nowe = self.coefficients
        for i in range(0,len(nowe)):
            nowe[i] *= -1
        return Polynomial(nowe)


    def __mul__(self, other):
        W1 = self.coefficients[::-1]
        W2 = other.coefficients[::-1]
        W3 = []

        for i in range(0, len(W1) + len(W2) - 1):
            W3.append(0)

        for i in range(0, len(W1)):
            for j in range(0, len(W2)):
                W3[i + j] = W3[i + j] + W1[i] * W2[j]

        return Polynomial(W3)

    def __call__(self, x):
        i = len(self.coefficients)
        wynik = 0
        while i > 0:
            wynik += math.pow(x,i-1) * self.coefficients[i-1]
            i -= 1
        return wynik



