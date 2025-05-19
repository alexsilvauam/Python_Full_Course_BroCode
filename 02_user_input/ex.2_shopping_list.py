item = input("Enter the item you want to buy: ")
price = float(input("Enter the price of the item "))
quantity = int(input("Enter the quantity of the item "))

total = price * quantity

print(f"You have bought {quantity} of {item} for a total of {total} U$")
