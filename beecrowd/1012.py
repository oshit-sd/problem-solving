# QUE 
# Make a program that reads three floating point values: A, B and C. Then, calculate and show:
# a) the area of the rectangled triangle that has base A and height C.
# b) the area of the radius's circle C. (pi = 3.14159)
# c) the area of the trapezium which has A and B by base, and C by height.
# d) the area of ​​the square that has side B.
# e) the area of the rectangle that has sides A and B.
# Input
# The input file contains three double values with one digit after the decimal point.

A = float(input())
B = float(input())
C = float(input())

pi = 3.14159

triangle = (A * C) / 2
circle = pi * (C ** 2)
trapezium = ((A + B) / 2) * C
square = B ** 2
rectangle = A * B

print(f"TRIANGULO: {triangle:.3f}")
print(f"CIRCULO: {circle:.3f}")
print(f"TRAPEZIO: {trapezium:.3f}")
print(f"QUADRADO: {square:.3f}")
print(f"RETANGULO: {rectangle:.3f}")