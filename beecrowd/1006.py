# QUE: 
# Read three values (variables A, B and C), which are the three student's grades. Then, calculate the average, considering that grade A has weight 2, grade B has weight 3 and the grade C has weight 5. Consider that each grade can go from 0 to 10.0, always with one decimal place.

A = float(input())
B = float(input())
C = float(input())

D = A * 2
E = B * 3
F = C * 5

result = (D+E+F) / (2+3+5)

print(f"MEDIA = {result:.1f}")