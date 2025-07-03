# QUE: 
# In this problem, the task is to read a code of a product 1, the number of units of product 1, the price for one unit of product 1, the code of a product 2, the number of units of product 2 and the price for one unit of product 2. After this, calculate and show the amount to be paid.
# Input
# The input file contains two lines of data. In each line there will be 3 values: two integers and a floating value with 2 digits after the decimal point

prices = []

for _ in range(2):
    line = input()
    product_code, p_unit, p_price = line.split()
    
    prices.append(int(p_unit) * float(p_price))

paid_amount = sum(prices)
print(f"VALOR A PAGAR: R$ {paid_amount:.2f}")