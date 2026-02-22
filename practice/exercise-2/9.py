''' Write a program that takes as input the cost price and selling price of an item, prints whether
the sale resulted in a profit or a loss, and prints the amount. '''
cost_price = float(input("Enter the cost price of the item: "))
selling_price = float(input("Enter the selling price of the item: "))
if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"The sale resulted in a profit of: {profit}")
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print(f"The sale resulted in a loss of: {loss}")
else:
    print("The sale resulted in neither profit nor loss.")