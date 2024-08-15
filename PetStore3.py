# Name: Matthew Reynolds # Date: 03/17/2024
# Class: Comp 163 #Section:002

# Description:Make a pet store



# List of pets
pets = ["Canine", "Feline", "Reptile"]
inventory = {}


def petstore_setup():
    for pet_type in pets:
        inventory[pet_type] = {}
        num_types = int(input(f"How many {pet_type} would you like to enter: "))
        for i in range(num_types):
            pet_name = input(f"What is the type of {pet_type}: ")
            pet_cost = float(input(f"What is the price per {pet_name}: "))
            inventory[pet_type][pet_name] = pet_cost


def display_pets():
    print("We offer the following pets")
    for pet_type, pet_types_dict in inventory.items():
        print(f"{pet_type} :")
        for pet_name, pet_cost in pet_types_dict.items():
            print(f"\t{pet_name} at a cost of ${pet_cost:,.2f}.")


def POS():
    print("Sale Pet Menu:")
    print("Select a category of pet:")
    for index, pet_type in enumerate(pets):  # So it iterates over the List
        print(f"{index + 1}) {pet_type}")
    category_choice = int(input("Enter your choice: ")) - 1
    category = pets[category_choice]

    print(f"Select a type of {category}:")
    for index, (pet_name, pet_cost) in enumerate(inventory[category].items()):
        print(f"{index + 1}. {pet_name} at a cost of ${pet_cost:,.2f}")
    pet_choice = int(input("Enter your choice: ")) - 1
    selected_pet = list(inventory[category].keys())[pet_choice]

    quantity = int(input(f"Enter the quantity of {selected_pet} to sell: "))
    total_cost = inventory[category][selected_pet] * quantity
    print(f"Total cost for {quantity} {selected_pet}: ${total_cost:,.2f}")
    return {"pet_category": category, "pet_type": selected_pet, "price_per_pet": inventory[category][selected_pet], "quantity": quantity}

# Calculates the Total Due
def CalculateTax(petitems):
    state_tax_rate = 0.07
    federal_tax_rate = 0.10
    total_due = sum(item["price_per_pet"] * item["quantity"] for item in petitems)
    state_tax_total = total_due * state_tax_rate
    federal_tax_total = total_due * federal_tax_rate

    return {"state_tax_total": state_tax_total, "federal_tax_total": federal_tax_total, "total_due": total_due + state_tax_total + federal_tax_total}

# Displays the Receipt
def displayReceipt(pet_items):
    print("Aggie Pet Store Bill of Sale")
    print("_" * 50)
    total = 0
    for i, item in enumerate(pet_items, 1):
        category = item["pet_category"]
        pet_type = item["pet_type"]
        price = item["price_per_pet"]
        quantity = item["quantity"]
        subtotal = price * quantity
        total += subtotal
        print(f"{i}. {category:<8} {pet_type:<7} ${price:<5,.2f} {quantity:<3} ${subtotal:.2f}")

    state_tax_rate = 0.07
    federal_tax_rate = 0.10

    state_tax_total = total * state_tax_rate
    federal_tax_total = total * federal_tax_rate
    total_due = total + state_tax_total + federal_tax_total

    print(f'            State Tax          $0.07')
    print(f'            Federal Tax        $0.10')
    print(f'            Total Due          ${total_due:.2f}')

    print("_" * 50)

def setupStore():
     petstore_setup()
# Message for when PetStore is Closed
def closePetStore():
    print("Thank you for using the Aggie PetStore POS")
    print("Aggie Pride!")

def petstore_menu():
    petitems = []
    while True:
        print("A) Setup Store")
        print("B) Display Pets")
        print("C) Sale Pet")
        print("D) Total Sale")
        print("E) Exit")

        PetStore3 = input("Menu selection: ").upper()

        if PetStore3 == 'A':
            setupStore()
        elif PetStore3 == 'B':
            display_pets()
        elif PetStore3 == 'C':
            petitems.append(POS())  # Appending to existing line items
        elif PetStore3 == 'D':
            if petitems:
                taxes = CalculateTax(petitems)
                displayReceipt(petitems)
        elif PetStore3 == 'E':
            closePetStore()
            break

# Message for when PetStore is Opened
print("Welcome to the Aggie Pet Store")
petstore_menu()
