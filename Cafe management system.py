#cafe management 2 - With Multiple Menus
import time

# Define separate menu dictionaries for different cuisines
maincourse_menu = {
    "Farmhouse Pizza": 350.00,
    "Cheeseburst Pzza ": 250.00,
    "Tandoori Paneer Pizza": 300.00,
    "French Fries": 80.00,
    "Peri-Peri Fries": 100.00,
    "Veggie Burger": 150.00,
    "Burger": 70.00,
    "Red Sauce Pasta": 109.00,
    "White Sauce Pasta": 119.00,
    "Garlic Bread": 90.00,
    "Paneer Tikka": 150.00,
    "Cheese maggie": 100.00,
    "Vegetable magggie": 75.00,
}

beverages_menu = {
    "Coffe": 50.00,
    "Cappuccino": 70.00,
    "Ginger Tea": 30.00,
    "Orea Shake": 120.00,
    "Kit-Kat Shake": 100.00,
    "Milkshake": 109.00,
}

cakes_menue = {
    "Choco Lava Cake": 109.00,
    "Red Velvet Cake": 150.00,
    "Black Forest Cake": 130.00,
    "Vanilla Cake": 140.00,
    "Fruit Cake": 160.00,
    "Cheesecake": 180.00,
}

# Mapping of choices to the actual menu data
menu_options = {
    '1': ('Main Course', maincourse_menu),
    '2': ('Beverages', beverages_menu),
    '3': ('Cakes', cakes_menue),
}

# --- FUNCTIONS ---

def display_menu(menu_name, menu):
    """Prints the selected menu in a neat, aligned format."""
    print("\n" + "="*40)
    print(f" 🍽️  WELCOME TO THE COPICO CAFE - {menu_name.upper()} MENU  🍽️ ")
    print("="*40)
    print(f"{'Item Name':<30} | {'Price':>6}")
    print("-" * 40)
    
    for item, price in menu.items():
        # The :<30 aligns text to the left, :>6 aligns price to the right
        print(f"{item:<30} | ₹{price:>5}")
    print("-" * 40)

def take_order(menu):
    """Interacts with the customer to build their order list."""
    order = {}
    total_bill = 0.0
    
    print("\nI'm ready to take your order!")

    while True:
        user_input = input("What would you like to order? (Type 'done' to finish): ").strip()
        
        # Handle casing so 'taco', 'TACO', and 'Taco' all work
        item_name = user_input.title() 

        if item_name == 'Done':
            break

        if item_name in menu:
            while True:
                try:
                    qty_input = input(f"How many {item_name} would you like? ")
                    quantity = int(qty_input)
                    
                    if quantity > 0:
                        break
                    else:
                        print("Please enter a number greater than zero.")
                except ValueError:
                    print("Oops, that doesn't look like a valid number. Try again.")

            # update the order dictionary
            order[item_name] = order.get(item_name, 0) + quantity
            
            # Add to running total
            item_price = menu[item_name]
            total_bill += item_price * quantity
            
            print(f"Got it! Added {quantity} x {item_name} to your order.")
            
        else:
            print(f"Sorry, we don't have '{item_name}' on this menu today.")

    return order, total_bill

def print_receipt(order, total_bill, menu):
    """Prints the final receipt with a thank you note."""
    print("\nProcessing your receipt...")
    time.sleep(1) # Adds a small pause to feel more realistic
    
    print("\n" + "*"*40)
    print("         YOUR RECEIPT         ")
    print("*"*40)
    
    for item, quantity in order.items():
        # Ensure we don't crash if an item somehow doesn't exist in the menu (safety check)
        price_per_item = menu.get(item, 0.0) 
        item_total = price_per_item * quantity
        # Changed $ to ₹ to match the rest of your code's currency symbol
        print(f"{item:<25} x{quantity:<3} ₹{item_total:>8}")
        
    print("-" * 40)
    print(f"TOTAL AMOUNT DUE:           ₹{total_bill:>8}")
    print("*"*40)
    print("Thank you for visiting! 🙏")

def cuisine_selection():
    """Allows the user to select which menu they want to use."""
    while True:
        print("\n--- CUISINE SELECTION ---")
        print("1. Main Course Menu")
        print("2. Beverages Menu")
        print("3. Cakes Menu")
        print("4. Back to Main Menu")

        choice = input("\nPlease choose a cuisine (1-4): ")

        if choice in menu_options:
            menu_name, selected_menu = menu_options[choice]
            return menu_name, selected_menu
        elif choice == '4':
            return None, None # Signal to go back to the main menu
        else:
            print("Invalid selection. Please choose 1, 2, 3, or 4.")

def main():
    """The main loop that keeps the cafe system running."""
    while True:
        print("\n--- MAIN CAFE SYSTEM ---")
        print("1. Select Cuisine & Order")
        print("2. Close Shop (Exit)")

        main_choice = input("\nPlease choose an option (1-2): ")

        if main_choice == '1':
            menu_name, selected_menu = cuisine_selection()
            
            if selected_menu: # If a valid cuisine was chosen
                while True:
                    print(f"\n--- {menu_name.upper()} MENU ACTIONS ---")
                    print("1. Show Menu")
                    print("2. Place New Order")
                    print("3. Change Cuisine / Back to Main")

                    action_choice = input("\nPlease choose an action(1-3): ")

                    if action_choice == '1':
                        display_menu(menu_name, selected_menu)
                        
                    elif action_choice == '2':
                        # Display the menu first so they know what to order
                        display_menu(menu_name, selected_menu) 
                        current_order, current_bill = take_order(selected_menu)
                        
                        if current_order:
                            print_receipt(current_order, current_bill, selected_menu)
                        else:
                            print("\nOrder cancelled. Hope to see you again soon!")
                            
                    elif action_choice == '3':
                        break # Break out of the menu actions loop to go back to cuisine selection/main menu
                        
                    else:
                        print("Invalid action choice. Please try 1, 2, or 3.")

        elif main_choice == '2':
            print("\nClosing up shop. Have a wonderful day! 👋")
            break
        else:
            print("I didn't understand that choice. Please try 1 or 2.")

if __name__ == "__main__":
    main()