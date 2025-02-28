#matthew Robinson
#2025-02-25

#Imports Pi for my codes
import math
Pi=math.pi

#Allows for the storage of the mesurments as floats
A = float(input("Area: "))
R = float(input("Radius: "))
H = float(input("Height: "))

#Equations for the differnt shapes and alocates a number for each shape
one=(A**3)
two=(4/3*Pi*R**2)
three=(1/3*Pi*R**2*H)
four=(Pi*R**2*H)

# give instructions and makes I an variable
I=input('''Type "Cube" or "Sphere" or "Cone" or "Cylinder" ''')

#depending on what I is equal to will print out the anwser to the equation
if I == "Cube":
 print(one)
if I == "Sphere":
 print (two)
if I == "Cone":
 print (three)
if I == "Cylinder":
 print(four)
