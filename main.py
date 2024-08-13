print("Welcome to the GC Fruit Market!")

# Ask for user's name and store it
name = input("What is your name?\n> ")

# Initialize variables to track purchases
apple_count = 0
grape_count = 0
orange_count = 0
total_cost = 0

# Dictionary to store fruit prices
fruit_prices = {
    "1": {"name": "Apple", "price": 2},
    "2": {"name": "Grape", "price": 1},
    "3": {"name": "Orange", "price": 3}
}

# Loop to keep asking the user for more fruit
while True:
    # Display fruit options
    print(f"\nWelcome {name}. Which fruit would you like to buy?")
    for key, fruit in fruit_prices.items():
        print(f"{key}. {fruit['name']} ${fruit['price']}")

    # Ask user to choose a fruit
    choice = input("> ")

    # Check if the user input is valid
    if choice in fruit_prices:
        fruit_name = fruit_prices[choice]["name"]
        fruit_price = fruit_prices[choice]["price"]

        # Update the corresponding fruit count and total cost
        if fruit_name == "Apple":
            apple_count += 1
        elif fruit_name == "Grape":
            grape_count += 1
        elif fruit_name == "Orange":
            orange_count += 1

        total_cost += fruit_price
        print(f"You bought 1 {fruit_name} at ${fruit_price}")
    else:
        print("Invalid choice. Please select a valid option.")

    # Ask if the user wants to buy more fruit
    more_fruit = input("Would you like to buy another piece of fruit? y/n\n> ")
    if more_fruit.lower() != "y":
        break

# Calculate subtotal and tax
subtotal = total_cost
tax = subtotal * 0.05
total = subtotal + tax

# Print the receipt
print(f"\nOrder for {name}")
print(f"{apple_count} apple(s) at $2 apiece")
print(f"{grape_count} grape(s) at $1 apiece")
print(f"{orange_count} orange(s) at $3 apiece")
print(f"Sub Total: ${subtotal}")
print(f"5% Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
