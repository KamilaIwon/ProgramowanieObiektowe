from polynomial import Polynomial

pierwszy = Polynomial([5, 4, 3, 0, 1])
print(pierwszy.deg())
# print(pierwszy.__neg__())
pol1 = Polynomial([3, 1, 1])
pol2 = Polynomial([5,2])
print(pol1.__mul__(pol2))
print(pol1)
print(pierwszy)
print(pierwszy.coefficients)
print(pierwszy.__call__(2))
pol3 = Polynomial([5,10,15])
print(pol3.__call__(3))

print(pierwszy)