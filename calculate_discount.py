def calculate_discount(price, discount_percent):
    """
    Calculates and returns the final price after applying a discount.
    The discount is applied only if discount_percent is 20% or higher.
    Otherwise, returns the original price.
    
    :param price: float — original price of the item
    :param discount_percent: float — discount percentage to consider
    :return: float — final price after discount (if applied)
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

def get_valid_float(prompt):
    """
    Prompts the user for input until a valid non-negative float is entered.
    
    :param prompt: str — message to display to the user
    :return: float — valid user-input value
    """
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def main():
    print("=== Discount Calculator ===")
    
    # Get validated user inputs
    price = get_valid_float("Enter the original price of the item: ")
    discount_percent = get_valid_float("Enter the discount percentage: ")

    # Compute the final price using the calculate_discount function
    final_price = calculate_discount(price, discount_percent)

    # Display results
    if discount_percent >= 20:
        print(f"\nDiscount applied ({discount_percent:.2f}%):")
        print(f"Original price: ${price:.2f}")
        print(f"Final price after discount: ${final_price:.2f}")
    else:
        print("\nNo discount applied (must be 20% or more).")
        print(f"Original price remains: ${price:.2f}")

if __name__ == "__main__":
    main()
