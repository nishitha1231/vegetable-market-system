# Vegetable Market Management System
import datetime

# Admin credentials
admin_name = 'Nishitha'
admin_password = 'Nishitha@123'

# Market data
vegetable = ["potato", "mirchi", "tomato", "onion", "carrots", "radish"]
quantity = [30, 50, 25, 30, 10, 15]
price = [20, 10, 30, 35, 15, 20]
MRP=[40,20,40,50,30,35]
sel_price = [30, 15, 35, 40, 20, 25]
sold_vegetables = []
sold_quantity = []
user_details = []

total_revenue = 0
total_cost = 0

print("*" * 20, "WELCOME TO VEGETABLE MARKET", "*" * 20)

while True:
    print("\nSelect Role:")
    print("A. OWNER")
    print("B. USER")
    print("C. EXIT")
    ch = input("Choose your option: ").upper()

    if ch == "A":
        print("\nWelcome to OWNER section")
        for attempt in range(3):
            name = input("Enter owner name: ")
            pwd = input("Enter owner password: ")
            if name == admin_name and pwd == admin_password:
                print("\nWelcome OWNER")
                break
            else:
                print("Invalid credentials")
        else:
            print("Too many failed attempts.")
            continue

        while True:
            print("\na. Add Item\nb. Remove Item\nc. Update Item\nd. View User Details\ne. View Report\nf. Total Revenue\ng. Exit")
            owner_choice = input("Enter your choice: ").lower()

            if owner_choice == 'a':
                while True:
                    veg = input("Enter vegetable to add: ")
                    if veg in vegetable:
                        print(veg, "is already available.")
                    else:
                        q = int(input("Enter quantity: "))
                        mrp=int(input("Enetr market price:"))
                        c = int(input("Enter cost price: "))
                        s = int(input("Enter selling price: "))
                        vegetable.append(veg)
                        quantity.append(q)
                        price.append(c)
                        sel_price.append(s)
                        MRP.append(mrp)
                        print(veg, "added successfully!")
                    if input("Add more? (yes/no): ") == "no":
                        break

            elif owner_choice == 'b':
                while True:
                    veg = input("Enter vegetable to remove (or 'exit'): ")
                    if veg == "exit":
                        break
                    if veg in vegetable:
                        idx = vegetable.index(veg)
                        for item in [vegetable, quantity, price, sel_price,MRP]:
                            item.pop(idx)
                        print(veg,"removed.")
                    else:
                        print("Vegetable not found.")

            elif owner_choice == 'c':
                veg = input("Enter vegetable to update: ")
                if veg in vegetable:
                    idx = vegetable.index(veg)
                    quantity[idx] += int(input("Enter additional quantity: "))
                    sel_price[idx] = int(input("Enter new selling price: "))
                    MRP[idx]=int(input("Enter new market price:"))
                    print("Updated successfully.")
                else:
                    print(veg,"Not found.")

            elif owner_choice == 'd':
                print("\nUSER DETAILS")
                if user_details:
                    for user in user_details:
                        print("Name:", user["name"])
                        print("Mobile:", user["mobile"])
                        print("Items:")
                        
                        for veg, qty in user["items"]:
                            print(f" - {veg}: {qty} kg")
                        print("-" * 30)
                else:
                    print("No user records found.")

            elif owner_choice == 'e':
                print(f"{'Name':<15}{'Available':<10}{'Cost':<10}{'Selling':<10}")
                print("-" * 50)
                for v, q, c, s in zip(vegetable, quantity, price, sel_price):
                    print(f"{v:<15}{q:<10}{c:<10}{s:<10}")

            elif owner_choice == 'f':
                print("\nTotal Revenue Report")
                print("-" * 60)
                print(f"{'Vegetable':<15}{'Sold Qty':<10}{'Revenue':<10}{'Profit':<10}")
                print("-" * 60)
                total_revenue = 0
                total_cost = 0
                for v, q in zip(sold_vegetables, sold_quantity):
                    if v in vegetable:
                        idx = vegetable.index(v)
                        revenue = sel_price[idx] * q
                        cost = price[idx] * q
                        profit = revenue - cost
                        total_revenue += revenue
                        total_cost += cost
                        print(f"{v:<15}{q:<10}{revenue:<10}{profit:<10}")
                print("-" * 60)
                print("Total Revenue:", total_revenue)
                print("Total Cost:", total_cost)
                print("Total Profit:", total_revenue - total_cost)

            elif owner_choice == 'g':
                break

            else:
                print("Invalid option.")

    elif ch == "B":
        cart_veg = []
        cart_quantity = []
        print("\nAvailable Vegetables")
        print(f"{'Name':<15}{'Qty':<10}{'Price':<10}")
        print("-" * 35)
        for v, q, s in zip(vegetable, quantity, sel_price):
            print(f"{v:<15}{q:<10}{s:<10}")

        while True:
            print("\na. Add\nb. Remove\nc. update \nd.veiw\ne. billing \nf.exit")
            uc = input("Enter your choice: ").lower()

            if uc == 'a':
                veg = input("Enter vegetable name: ")
                if veg in vegetable:
                    idx = vegetable.index(veg)
                    qua = int(input("Enter quantity (kg): "))
                    if qua <= quantity[idx]:
                        cart_veg.append(veg)
                        cart_quantity.append(qua)
                        quantity[idx] -= qua
                        sold_vegetables.append(veg)
                        sold_quantity.append(qua)
                        print(veg, "added to cart.")
                        #add_more=(input('do you want to add another vegetable(yes/no):').strip())
                        #if (add_more)!='yes':
                              #break
                        
                        
                    else:
                        print("Insufficient quantity.")
                else:
                    print("Not available.")
                #add_more=(input('do you want to add another vegetable(yes/no):').strip())
                #if (add_more)!='yes':
                              #break

            elif uc == 'b':
                veg = input("Enter vegetable to remove from cart: ")
                if veg in cart_veg:
                    idx = cart_veg.index(veg)
                    cart_veg.pop(idx)
                    cart_quantity.pop(idx)
                    print(f"{veg} removed from cart.")
                else:
                    print("Item not in cart.")
            elif uc=='c':
                veg = input("Enter vegetable to modify in cart: ")
                
                if veg in cart_veg:
                    new_qty = int(input("Enter new quantity (kg): "))
                    cidx = cart_veg.index(veg)
                    veg_idx = vegetable.index(veg)
                    current_qty = cart_quantity[cidx]

                    if new_qty > current_qty:
                        diff = new_qty - current_qty
                        if diff <= quantity[veg_idx]:
                            cart_quantity[cidx] = new_qty
                            quantity[veg_idx] -= diff
                            print("Quantity increased.")
                        else:
                            print("Not enough stock.")
                    elif new_qty < current_qty:
                        diff = current_qty - new_qty
                        cart_quantity[cidx] = new_qty
                        quantity[veg_idx] += diff
                        print("Quantity decreased.")
                    else:
                        print("Same quantity entered. No changes made.")
                else:
                    print("Vegetable not in cart.")

            elif uc == 'd':
                print("\nYour Cart")
                for v, q in zip(cart_veg, cart_quantity):
                    print(f"{v}: {q} kg")

            elif uc == 'e':
                if not cart_veg:
                    print("Cart is empty.")
                    continue

                name = input("Enter your name: ")
                while True:
                    mobile = input("Enter 10-digit mobile number: ")
                    if mobile.isalpha():
                        print("invalid number because it contains alphabets")
                    if ((mobile[0]) not in  '6789'):
                        print("invalid number:")
                    if len(mobile) == 10 and mobile.isdigit() and ((mobile[0]) in '6789'):
                        break

                user_details.append({"name": name, "mobile": mobile, "items": list(zip(cart_veg, cart_quantity))})

                now = datetime.datetime.now()
                inv_id = f"TVG-INV{now.strftime('%H%M%S')}"

                print("\n" + "=" * 50)
                print("NISHITHA VEGETABLES INVOICE")
                print("Shop No. 1 , Kphb, jntu")
                print("Hyderabad, Telangana, India")
                print("Phone: 8885940634")
                print("Email: nishithathatiparthi8@gmail.com")
                print("=" * 50)
                print("Invoice No:", inv_id)
                print("Date:", now.strftime("%d/%m/%Y %I:%M:%S %p"))
                print("Name:", name)
                print("Mobile No:", mobile)
                print("=" * 50)

                print(f"{'S.No.':<10}{'Item':<15}{'Qty':<10}{'MRP':<10}{'Rate':<10}{'Amount':<10}")
                print("-" * 50)
                total = 0
                #dis_amt=0
                for i, (v, q), in enumerate(zip(cart_veg, cart_quantity), 1):
                    idx = vegetable.index(v)
                    rate = sel_price[idx]
                    aft_dis_amt = rate * q
                    mrp=MRP[idx]
                    act_amt=mrp*q
                    total += aft_dis_amt
                    red_amt=(mrp*q)-(rate*q)
                    print(f"{i:<10}{v:<15}{q:<10}{mrp:<10}{rate:<10}{act_amt:<10}")
                    #print("RED_AMOUNT:>40:","   ""₹",red_amt)
                print("-" * 100)
                print("before discount:",act_amt)
                print("RED_AMOUNT:","   ""₹",red_amt)
                
                print("TOTAL:","    "" ₹",total)
                pay_ch=input("Payment Method : UPI/cash:")
                if pay_ch=='UPI':
                    print("please use the scanner and pay")
                else:
                    print("ok, cash is accepted.")
                print("we will share you bill to your mobile number sir/madam")
                print("Thank you for shopping with us!")
                print("=" * 50)

                cart_veg.clear()
                cart_quantity.clear()

            elif uc == 'f':
                break

            else:
                print("Invalid option.")

    elif ch == "C":
        print("Thank you. Visit Again!")
        break

    else:
        print("Invalid option.")

