inventory = []

def add_product():
    print("\n--- Add New Product ---")
    name = input("Product name: ")

    # .isalpha() make sure they are only letters
    # .replace(" ", "") It allows names with spaces like "Papa Criolla"
    if name.replace(" ", "").isalpha():
        try:
            price = float(input("Price: "))
            amount = int(input("amount: "))
            
            # If everything is okay, we create the dictionary and save it.
            product = {"name": name, "price": price, "amount": amount}
            inventory.append(product)
            print(f"¡{name} successfully added!")
            
        except ValueError:
            print("Error: The price and quantity must be numbers..")
    else:
        # If the name contains numbers or symbols, skip here
        print("Error:The product name can only contain letters.")

def show_inventory():
    print("\n--- Current inventory ---")
    if not inventory:
        print("El inventario está vacío.")
    else:
        for p in inventory:
            print(f"Product: {p['Name']} | Price: {p['Price']} | Amount: {p['Amount']}")

def calculate_statistics():
    print("\n--- Statistics ---")
    if not inventory:
        print("There is no data to calculate.")
        return

    total_value = 0
    total_units = 0
    for p in inventory:
        total_value += (p['price'] * p['amount'])
        total_units += p['amount']
    
    print(f"Registered products: {len(inventory)}")
    print(f"Total units: {total_units}")
    print(f"Total inventory value: ${total_value}")
    print("Error: Enter valid numbers for price and quantity.")