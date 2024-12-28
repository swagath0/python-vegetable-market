print(' ' * 30, '-' * 38)
print(' ' * 30, '*' * 10, 'VEGETABLE MARKET', '*' * 10)
print(' ' * 30, '-' * 38)


veg = ['tomato', 'brinjal', 'onion', 'potato']
quantity = [25, 30, 35, 30]
org_price = [30, 20, 15, 30]
selling_price = [35, 25, 20, 40]


customers = []  
customer_purchases = []  

while True:
    ch = input('Are you owner or customer: ')

    if ch == 'owner':
        print(' ' * 30, '-' * 38)
        print(' ' * 30, '*' * 10, 'LOGIN PAGE', '*' * 10)
        print(' ' * 30, '-' * 38)

        while True:
            owner_name = input('Login Id: ')
            password = input('Password: ')
            if owner_name == 'swagath' and password == '123456':
                print(' ' * 30, '-' * 58)
                print(' ' * 30, '*' * 10, 'Welcome', owner_name, '*' * 10)
                print(' ' * 30, '-' * 58)
                break
            else:
                print('Please enter correct login credentials.')

        while True:
            chh = input('Do you want to 1.add 2.remove 3.modify 4.display 5.c_display 6.itemized bill and revenue  7.exit? : ')
            if chh == '1':
                item = input('Enter the vegetable name to add: ')
                qty = float(input('Enter the quantity you want to add: '))
                price_1 = float(input('Enter the original price: '))
                price = float(input('Enter the selling price: '))
                veg.append(item)
                quantity.append(qty)
                org_price.append(price_1)
                selling_price.append(price)
                print('item', ' ' * 5, 'quantity', '  ' * 1, 'org_price', ' ' * 1, 'selling_price')
                for i, j, k, q in zip(veg, quantity, org_price, selling_price):
                    print(f"{i:<15} {j:<10}  {k:<5}  {q:<15}")
                print(item, ' has been added to your inventory.')
                print('*' * 85)

            elif chh == '2':
                vegetable = input('What do you want to remove?: ')
                if vegetable in veg:
                    idx = veg.index(vegetable)
                    veg.pop(idx)
                    quantity.pop(idx)
                    org_price.pop(idx)
                    selling_price.pop(idx)
                    print(vegetable, ' is removed from your inventory.')
                else:
                    print('Sorry', vegetable, 'is not in the inventory.')

            elif chh == '3':
                vegetable = input('Which vegetable do you want to modify?: ')
                if vegetable in veg:
                    idx = veg.index(vegetable)
                    while True:
                        i = input('What do you want to modify 1.quantity/2.org_price/3.selling_price/4.exit: ')
                        if i == '1':
                            new_qty = float(input('Enter new quantity: '))
                            quantity[idx] = new_qty
                        elif i == '2':
                            new_price = float(input('Enter the original price: '))
                            org_price[idx] = new_price
                        elif i == '3':
                            new_price = float(input('Enter new selling price: '))
                            selling_price[idx] = new_price
                        elif i == '4':
                            print(vegetable, ' has been updated.')
                            break
                        else:
                            print('Invalid option.')
                else:
                    print('Sorry', vegetable, 'is not in the inventory.')

            elif chh == '4':
                print('Current Inventory:')
                print('item', ' ' * 5, 'quantity', '  ' * 1, 'org_price', ' ' * 1, 'selling_price')
                for i, j, k, q in zip(veg, quantity, org_price, selling_price):
                    print(f"{i:<15} {j:<10}  {k:<5}  {q:<15}")

            elif chh == '5':
                print('Customer Purchases:')
                for customer in customers:
                    print(f"Name: {customer['name']}, Phone: {customer['phone']}")
                    print('item', ' ' * 5, 'quantity', '  ' * 1, 'price')
                    for item, qty, price in zip(customer['items'], customer['quantities'], customer['prices']):
                        print(f"{item:<15} {qty:<10}  {price:<5}")
                    print('-' * 40)

            elif chh == '6':
                print('Itemized Revenue and Profit:')
                total_revenue = 0
                total_cost = 0

                print(f"{'Item':<15} {'Quantity Sold':<15} {'Original Price':<15} {'Selling Price':<15} {'Revenue':<15} {'Profit':<15}")

                for i in range(len(veg)):
                    sold_qty = sum(customer['quantities'][j] for customer in customers for j in range(len(customer['items'])) if customer['items'][j] == veg[i])
                    revenue = sold_qty * selling_price[i]
                    cost = sold_qty * org_price[i]
                    profit = revenue - cost

                    total_revenue += revenue
                    total_cost += cost

                    if sold_qty > 0:
                        print(f"{veg[i]:<15} {sold_qty:<15} {org_price[i]:<15} {selling_price[i]:<15} {revenue:<15} {profit:<15}")

                total_profit = total_revenue - total_cost
                print('-' * 90)
                print(f"{'Total Revenue:':<40} {total_revenue:<50}")
                print(f"{'Total Cost:':<40} {total_cost:<50}")
                print(f"{'Total Profit:':<40} {total_profit:<50}")
                print('-' * 90)

            elif chh == '7':
                print('Exiting owner mode.')
                break
            else:
                print('Invalid option. Please try again.')

    elif ch == 'customer':
        customer = {
            'name': '',
            'phone': '',
            'items': [],
            'quantities': [],
            'prices': []
        }
        
        while True:
            cust_name = input('Enter your name: ')
            if not cust_name.isalpha():
                print('Please enter a valid name.')
                continue
            ph_no = input('Enter your phone number: ')
            if len(ph_no) != 10 or not ph_no.isdigit():
                print('Please enter a valid 10-digit phone number.')
                continue
            customer['name'] = cust_name
            customer['phone'] = ph_no
            customers.append(customer)  # Add customer to the list
            break
        
        while True:
            chh = input('Do you want to 1.add 2.remove 3.modify 4.display 5.bill? 6.exit: ')

            if chh == '1':
                item = input('Enter the vegetable name to add: ')
                if item in veg:
                    qty = float(input('Enter the quantity you want to add: '))
                    if qty > 0:
                        idx = veg.index(item)
                        if qty <= quantity[idx]:  # Check available stock
                            if item in customer['items']:  # Check if item already exists in customer's purchases
                                item_idx = customer['items'].index(item)
                                customer['quantities'][item_idx] += qty
                                customer['prices'][item_idx] = customer['quantities'][item_idx] * selling_price[idx]
                            else:
                                quantity[idx] -= qty  # Update inventory
                                amount = qty * selling_price[idx]
                                customer['items'].append(item)
                                customer['quantities'].append(qty)
                                customer['prices'].append(amount)
                            print(f"{qty} of {item} has been added to your purchases.")
                        else:
                            print('Sorry, we don\'t have enough', item)
                    else:
                        print("Invalid quantity.")
                else:
                    print('Item is not available.')

            elif chh == '2':
                vegetable = input('What do you want to remove from your purchases?: ')
                if vegetable in customer['items']:
                    idx = customer['items'].index(vegetable)
                    qty = customer['quantities'][idx]
                    customer['items'].pop(idx)
                    customer['quantities'].pop(idx)
                    customer['prices'].pop(idx)
                    quantity[veg.index(vegetable)] += qty  # Update inventory
                    print(vegetable, ' has been removed from your purchases.')
                else:
                    print('Sorry', vegetable, 'is not in your purchases.')

            elif chh == '3':
                vegetable = input('Which vegetable do you want to modify?: ')
                if vegetable in customer['items']:
                    idx = customer['items'].index(vegetable)
                    new_qty = float(input('Enter new quantity: '))
                    if new_qty > 0:
                        old_qty = customer['quantities'][idx]
                        amount = new_qty * selling_price[veg.index(vegetable)]
                        customer['quantities'][idx] = new_qty
                        customer['prices'][idx] = amount
                        quantity[veg.index(vegetable)] += old_qty - new_qty  # Adjust inventory
                        print(vegetable, ' has been updated.')
                    else:
                        print("Invalid quantity.")
                else:
                    print('Sorry', vegetable, 'is not in your purchases.')

            elif chh == '4':
                print('Your Purchases:')
                print('item', ' ' * 5, 'quantity', '  ' * 1, 'price')
                for i, J, K in zip(customer['items'], customer['quantities'], customer['prices']):
                    print(f"{i:<15} {J:<10}  {K:<5}")

            elif chh == '5':
                print('Your Bill:')
                print('items', ' ' * 5, 'quantities', '  ' * 1, 'prices')
                for i, J, K in zip(customer['items'], customer['quantities'], customer['prices']):
                    print(f"{i:<15} {J:<10}  {K:<5}")
                total = sum(customer['prices'])
                print('Please pay', total, 'rupees')
                print(' ' * 30, '*' * 10, 'THANK YOU FOR SHOPPING! PLEASE VISIT AGAIN', '*' * 10)
                break
            elif chh == '6':
                print('Exiting.')
                break

    else:
        print('Invalid input. Please enter "owner" or "customer".')
