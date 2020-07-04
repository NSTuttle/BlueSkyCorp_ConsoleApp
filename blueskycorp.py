# BlueSkyCorp.py
# Programmer: Nick Tuttle
# Created: 6/20/20
# Updated: 7/3/20

from Classes.customer import Customer, CustomerRewards
from Classes.email import Email
from helpers import *
import webbrowser
import re
import os
import pickle
import templates
# import requests


# VARIABLES
run = True
customerExists = False
customer = None
submenu = None


# Items for sale
items = (
    {
        "name": "Ballons",
        "price": 2,
    },
    {
        "name": "Kite",
        "price": 10,
    },
    {
        "name": "Bird",
        "price": 20,
    },
    {
        "name": "Hot Air Ballon",
        "price": 50,
    },
    {
        "name": "Airplane",
        "price": 60,
    },
    {
        "name": "Thunderstorm Generator",
        "price": 100000,
    }
)


# load_customer_profile
# Loads customer profile data from binary
def load_customer_profile(customer_id=None):
    global customer, customerExists
    # Would use HTTP for actual app
    # customer = requests.get(myCustomerDataURL/customer_id)
    # Alt flow with file load
    if os.path.isfile('customer.txt') and os.path.getsize('customer.txt') > 0:
        with open('customer.txt', 'rb') as profile:
            customer = pickle.load(profile)
        customerExists = True
    else:
        print("No Customer", customerExists)
        value_customer()
        save_customer_profile()


# save_customer_profile
# Saves customer profile data to binary
def save_customer_profile():
    global customer
    # Would use HTTP for actual app
    # customer = requests.post(myCustomerDataURL, data = customer)
    with open('customer.txt', 'wb') as profile:
        pickle.dump(customer, profile)


# Values a basic Customer
def value_customer():
    global customer
    rewards1 = CustomerRewards(False, 0, 0)
    customer = Customer("Bob", "Customer", "abc@123.net", rewards1)
    save_customer_profile()


# emailCustomer
# Builds Purchse email to customer
# Allows for appended text
# Displays String email
# Asks for send w/ default email client
def emailCustomer(transaction=None):
    global customer
    global templates
    email = build_template("Purchase", customer)
    if transaction != None:
        email.appendToString(transaction)
    else:
        if len(customer.getTransactions()) > 0:
            email.appendToString(customer.getTransactions()[-1])
    add_note = input("Add note to email? (Y/N) ")
    if eval_user_yes(add_note):
        email.appendToString(input("Note: "))
    # Present Tempalte Menu
    # User selects, new email instance created and passed to Email function.
    print()
    print(email.ToString())
    print()
    send = input("Send Email? (Y/N) ")
    if eval_user_yes(send):
        print("Email opening in default client...")
        webbrowser.open(
            f'mailto:{email.toEmail}?subject={email.subject}&body={email.body}', new=1)


# Injects name into template
def build_template(template, customer):
    subject = re.sub("\[name\]", customer.get_fullname(),
                     templates.email_templates[template]["subject"])
    body = re.sub("\[name\]", customer.get_fullname(),
                  templates.email_templates[template]["body"])
    return Email(customer.email, '', subject, body)


# run_selection
# Runs menu selections
def run_selection(selection, menu=None):
    if selection.lower() == "x" or selection.lower() == "exit":
        exit()
        return
    if menu == "cp":
        if test_int(selection) and int(selection) == 1:
            if len(customer.getTransactions()) > 0:
                print("\n", *customer.getTransactions(), sep="\n\n")
            else:
                print("\nNo Transactions")
        elif test_int(selection) and int(selection) == 2:
            if len(customer.getTransactions()) > 0:
                emailCustomer()
    else:
        if test_int(selection) and int(selection) == 1:
            sell_items()
        elif test_int(selection) and int(selection) == 2:
            customer_profile()


# exit
# exits out of submenu or run to False
def exit():
    global run
    global submenu
    save_customer_profile()
    if submenu != None:
        submenu = None
    else:
        run = False


# MENUS

# main_menu
# Main menu for Blue Sky Corp POS
def main_menu():
    print("   (1) Sell Items")
    print("   (2) Customer Profile")
    print()
    print("   (X) Exit")
    print()


# customer_menu
# customer_menu details customer + communications
def customer_menu():
    global customer
    print()
    print("CUSTOMER MENU")
    print("   (1) Sale History")
    if len(customer.getTransactions()) > 0:
        print("   (2) Email Last Purchase")
    print()
    print("   (X) Exit")
    print()


# sales_menu
# sales_menu allows for the sale of the items
def sales_menu():
    global items
    print()
    print("SALES MENU: Choose item and qty, t to total")
    for index, item in enumerate(items, start=1):
        print(
            f'({index}) {item["name"]} ${item["price"]}')
    print()
    print("   (T) Total")
    print("   (X) Exit")
    print()


# run_splash title
def run_splash():
    print()
    print("______ _            _____ _          ")
    print("| ___ \ |          /  ___| |         ")
    print("| |_/ / |_   _  ___\ `--.| | ___   _ ")
    print("| ___ \ | | | |/ _ \`--. \ |/ / | | |")
    print("| |_/ / | |_| |  __/\__/ /   <| |_| |")
    print("\____/|_|\__,_|\___\____/|_|\_\\__, |")
    print("                                __/ |")
    print("                               |___/ ")


# main runs the program, loads customer
def main():
    global run
    run_splash()
    load_customer_profile()
    while run:
        main_menu()
        run_selection(input("Selection: "))


# OPTION FUNCTIONS
# sell_items
# Displays sale menu, allows selection of items and quantity.
# Sums Items, checks for discount
# Updates customer/rewards with trnsaction data
def sell_items():
    global submenu
    global items
    global customer
    submenu = "s"
    while submenu == "s":
        sales_menu()
        adding_items = True
        total = 0
        item_total = 0
        transaction = f"************ Sale - {get_datetime()} ************\n"
        # Add Items
        while adding_items == True:
            itemSelect = input("Item Number: ")
            if itemSelect.lower() == "t" or itemSelect.lower() == "total":
                adding_items = False
            else:
                try:
                    cost = int(items[int(itemSelect)-1]["price"])
                    qty = input("Qty: ")
                    total += cost * int(qty)
                    item_total += int(qty)
                    transaction = transaction + \
                        f'{items[int(itemSelect)-1]["name"]}: {qty} @ ${int(items[int(itemSelect)-1]["price"])}\n'
                except IndexError:
                    print("Invalid Entry, try again")
        if total <= 0:
            return
        print()
        print(f'Total: ${total}')
        # If Customer has Discount
        if getattr(customer, "rewards").hasDiscount:
            getattr(customer, "rewards").useDiscount()
            totalWithDiscount = round(getattr(
                customer, "rewards").totalMinusDiscount(total))
            totalDiscount = round(
                getattr(customer, "rewards").totalDiscount(total))
            print(f'With Discount: ${totalWithDiscount}')
            print(f'Saved: ${totalDiscount}')
            getattr(customer, "rewards").incrementCycleDollars(
                totalWithDiscount)
            getattr(customer, "rewards").incrementTotalDollars(
                totalWithDiscount)
            transaction = transaction + \
                f'\nDiscount Used\nSaved: ${totalDiscount}\nTransaction Total: ${totalWithDiscount}'
        # No Discount
        else:
            getattr(customer, "rewards").incrementCycleDollars(total)
            getattr(customer, "rewards").incrementTotalDollars(total)
            transaction = transaction + \
                f'\nTransaction Total: ${total}'
        # Earned Discount?
        if int(getattr(customer, "rewards").getCycleDollars()) >= 200:
            getattr(customer, "rewards").resetCycle()
            transaction = transaction + "\nDISCOUNT EARNED"
        print(f'Total Items Sold: {item_total}')
        save_customer_profile()
        receipt = input("Email Receipt? (Y/N)")
        if eval_user_yes(receipt):
            emailCustomer(transaction)
        customer.addTransaction(transaction)
        submenu = None


# customer_profile
# customer_profile displays customer menu/details, allows for transaction history
def customer_profile():
    global submenu
    global customer
    submenu = "cp"
    print(
        f'\n{customer.get_fullname()}\nTotal Transactions: {customer.transactionCount()}\nLifetime Spending: ${getattr(customer, "rewards").getTotalDollars()}')
    while submenu == "cp":
        customer_menu()
        run_selection(input("Selection: "), "cp")


# RUN MAIN
main()
