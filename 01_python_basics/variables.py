
hotel_name = "Grand Palace"
original_price = 12000
new_price = 9500

savings = original_price - new_price

print(f"Hotel: {hotel_name}")
print(f"Original price: ₹{original_price}")
print(f"New price: ₹{new_price}")
print("%d" % savings)


if new_price < original_price:
    print("Cheaper booking found!")
else:
    print("No savings available.")




