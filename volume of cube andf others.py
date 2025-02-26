#matthew Robinson
#2025-02-25

import math
Pi=math.pi

A = float(input("Area: "))
R = float(input("Radius: "))
H = float(input("Height: "))


one=(A**3)
two=(4/3*Pi*R**2)
three=(1/3*Pi*R**2*H)
four=(Pi*R**2*H)

I=input('''Type "Cube" or "Sphere" or "Cone" or "Cylinder" ''')

if I == "Cube":
 print(one)
if I == "Sphere":
 print (two)
if I == "Cone":
 print (three)
if I == "Cylinder":
 print(four)
