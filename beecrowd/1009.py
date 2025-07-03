# QUE:
# Make a program that reads a seller's name, his/her fixed salary and the sale's total made by himself/herself in the month (in money). Considering that this seller receives 15% over all products sold, write the final salary (total) of this seller at the end of the month , with two decimal places.
# - Don’t forget to print the line's end after the result, otherwise you will receive “Presentation Error”.
# - Don’t forget the blank spaces.
# Input
# The input file contains a text (employee's first name), and two double precision values, that are the seller's salary and the total value sold by him/her.

seller_name = input()
salary = float(input())
total_sold = float(input())

sold_percent_amount = (total_sold * 15) / 100
total_salary = sold_percent_amount + salary

print(f"TOTAL = R$ {total_salary:.2f}")
