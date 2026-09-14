price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print(f"{quantity} items at {price:.2f} each = {total:.2f}")