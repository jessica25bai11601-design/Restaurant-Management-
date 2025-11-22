Menu={
    'Pizza':100,
    'Pasta':120,
    'Coffee':90,
    'Shake':90,
    'Waffle':150,
    'Cheese cake':160
}

print("Welcome to Cafe Restaurant")
print("Here's our menu:")
for item, price in Menu.items():
    print(f"{item}: Rs{price}")

order_total = 0
order_list = {}

while True:
    item_action = input("\nEnter item name (to order), 'remove' (to remove an item), 'change' (to modify quantity), or 'done' (to finish): ").strip().title()

    if item_action == 'Done':
        break

    elif item_action == 'Remove':
        if not order_list:
            print("Your order is currently empty. Nothing to remove.")
            continue

        print("\nCurrent Order:")
        for item, qty in order_list.items():
            print(f"{item}: {qty}")

        item_to_remove = input("Enter the name of the item to remove: ").strip().title()
        if item_to_remove in order_list:
            try:
                current_qty = order_list[item_to_remove]
                quantity_to_remove = int(input(f"How many '{item_to_remove}' do you want to remove (current: {current_qty})? "))
                if not (0 < quantity_to_remove <= current_qty):
                    print(f"Invalid quantity. Please enter a number between 1 and {current_qty}.")
                    continue

                removed_price = Menu[item_to_remove] * quantity_to_remove
                order_total -= removed_price
                order_list[item_to_remove] -= quantity_to_remove

                if order_list[item_to_remove] == 0:
                    del order_list[item_to_remove]

                print(f"{quantity_to_remove} x {item_to_remove} has been removed from your order.")
                print(f"Current total: Rs{order_total}")
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        else:
            print(f"'{item_to_remove}' is not in your current order.")

    elif item_action == 'Change':
        if not order_list:
            print("Your order is currently empty. Nothing to change.")
            continue

        print("\nCurrent Order:")
        for item, qty in order_list.items():
            print(f"{item}: {qty}")

        item_to_change = input("Enter the name of the item to change quantity: ").strip().title()
        if item_to_change in order_list:
            try:
                current_qty = order_list[item_to_change]
                new_quantity = int(input(f"Enter the new quantity for '{item_to_change}' (current: {current_qty}): "))
                if new_quantity <= 0:
                    print("New quantity must be a positive number. If you want to remove an item, use 'remove'.")
                    continue

                price_difference = (new_quantity - current_qty) * Menu[item_to_change]
                order_total += price_difference
                order_list[item_to_change] = new_quantity

                print(f"Quantity of {item_to_change} changed to {new_quantity}.")
                print(f"Current total: Rs{order_total}")
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        else:
            print(f"'{item_to_change}' is not in your current order.")

    elif item_action in Menu:
        try:
            quantity = int(input(f"How many '{item_action}' would you like? "))
            if quantity <= 0:
                print("Quantity must be a positive number. Please try again.")
                continue

            item_price = Menu[item_action] * quantity
            order_total += item_price
            order_list[item_action] = order_list.get(item_action, 0) + quantity
            print(f"{quantity} x {item_action} has been added to your order.")
            print(f"Current total: Rs{order_total}")
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    else:
        print(f"Sorry, '{item_action}' is not in our menu yet! Please choose from {list(Menu.keys())}.")

print("\n--- Your Order Summary ---")
if order_list:
    for item, qty in order_list.items():
        print(f"{item}: {qty} x Rs{Menu[item]} = Rs{qty * Menu[item]}")
    print(f"Total amount to pay: Rs{order_total}")
else:
    print("No items were ordered. Goodbye!")
