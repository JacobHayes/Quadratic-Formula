#Jacob Hayes
#Quadratic Formula
#A = Leading Coefficient, B = Secondary Coefficient, C = Constant

import math

print "\t\t\t\t  Jacob Hayes"

print "\n\t\t\t     *Quadratic Formula*"
print "\n\t\t\t        *Ax^2+Bx+C=0*\n"

A = float(raw_input("Enter the Leading Coefficient: "))
B = float(raw_input("Enter the X Coefficient: "))
C = float(raw_input("Enter the Constant: "))

Discriminant = (B * B) - (4 * A * C)
Denominator = 2 * A

print "\nDiscriminant: (", B, "*", B, ") - ( 4.0 *", A, "*", C, ")" 
print "Discriminant: (", B * B, ") - (", 4 * A * C, ")"
print "The Discriminant is", Discriminant

raw_input("\nPress enter to continue.")

if Discriminant >= 0:
    Quadratic_X = (-B + (math.sqrt(Discriminant)) / Denominator)
    Quadratic_X2 = (-B - (math.sqrt(Discriminant)) / Denominator)

    print "\nX =", Quadratic_X, "and", Quadratic_X2, "."

    raw_input("\nPress enter to continue.")

    print "           _________"
    print -B, "+/- \/", Discriminant
    print "___________________________"
    print "\t", Denominator
    print "\nReduce if possible."

elif Discriminant < 0:
    print "           _____"
    print -B, "+/- \/", (Discriminant * -1), "i"
    print "___________________________"
    print "\t", Denominator

raw_input("\nPress Enter to Exit")
