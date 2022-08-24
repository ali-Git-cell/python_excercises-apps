menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}

def calculate_subtotal(order):      
    print('Calculating bill subtotal...')
    sub_total = 0
    for i in order:
        sub_total += i["price"]
    sub_total = round(sub_total, 2)
    return sub_total

    raise NotImplementedError()

def calculate_tax(subtotal):
    print('Calculating tax from subtotal...')
    tax = round((subtotal * 0.15), 2)
    return tax

    raise NotImplementedError()

def summarize_order(order):
    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)
    total = round((tax + subtotal),2)
    names = []
    for n in order:
        names.append(n["name"])
    return names,total
    
    print_order(order)

    raise NotImplementedError()

# This function will print out the items in an order
def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order

# This function  will display the menu
def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

# This function will create an order by prompting the user to select menu items
def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order

# function calls for testing the app
def main():
    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))

    tax = calculate_tax(subtotal)
    print("Tax for the order is: " + str(tax))

    items, subtotal = summarize_order(order)

if __name__ == "__main__":
    main()
