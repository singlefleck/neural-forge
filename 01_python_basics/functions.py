
def calculate_savings(original_price, new_price):
    savings = original_price - new_price
    print(f"Original price: ₹{original_price}")
    return savings



result = calculate_savings(12000, 9500)

print(f"You save ₹{result}")

def check_price(price):
    if price < 0:
        return "Error: Price cannot be negative"  # Returns here if true
    
    if price > 10000:
        return "Luxury Tier"  # Returns here if the first one was false
    
    return "Standard Tier"  # Returns here if both above are false

print(check_price(result))  # Luxury Tier