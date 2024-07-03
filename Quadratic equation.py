# EQUATION
import math
a = int(input('enter value a : '))
b = int(input('enter value b : '))
c = int(input('enter value c : '))
root1 = -b + (math.sqrt(b**2 - 4 * a * c)) / 2* a
root2 = -b - (math.sqrt(b**2 - 4 * a * c)) / 2* a
print('r1 =' ,root1 ,'r2 =', root2)
