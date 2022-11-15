from polynomial import Polynomial

pol1 = Polynomial([5,2,0, 1])
pol2 = Polynomial([0,1,1])
print(pol1)
print(pol2)
'''
pol3 = pol1.__add__(pol2)
pol4 = pol1.__sub__(pol2)
print(pol4)
print(pol1.__eq__(pol1))
'''

print(pol1.__mul__(pol2))