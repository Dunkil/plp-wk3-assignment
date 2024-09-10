def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (price * discount_percent) / 100
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Greet the user
print("Welcome to the Discount Calculator!")

# Prompt the user for input
try:
    original_price = float(input("Please enter the original price of the item (e.g., 100.00): $"))
    discount_percent = float(input("Please enter the discount percentage (e.g., 25): "))
    
    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percent)
    
    # Provide a friendly message with the result
    if discount_percent >= 20:
        print(f"Great news! Your discount of {discount_percent}% has been applied.")
    else:
        print("Unfortunately, the discount was less than 20%, so no discount was applied.")
    
    print(f"The final price of the item is: ${final_price:.2f}")

except ValueError:
    print("Oops! It seems you entered something that isn't a number. Please try again.")
