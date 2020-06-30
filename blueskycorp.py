# BlueSkyCorp.py
# Programmer: Nick Tuttle
# Created: 6/20/20
# Updated: 6/23/20

from Classes.customer import Customer, CustomerRewards
import webbrowser
import os
import pickle
# import requests


# VARIABLES
run = True
customerExists = False
customer = None


# load_customer_profile
# Loads customer profile data from binary
def load_customer_profile(customer_id=None):
    global customer, customerExists
    # Would use HTTP for actual app
    # customer = requests.get(myCustomerDataURL/customer_id)
    # Fake flow with file load
    if os.path.getsize('customer.txt') > 0:
        with open('customer.txt', 'rb') as profile:
            customer = pickle.load(profile)
        customerExists = True
        print("Has Customer", customerExists)
    else:
        print("No Customer", customerExists)


# save_customer_profile
# Saves customer profile data to binary
def save_customer_profile():
    global customer
    # Would use HTTP for actual app
    # customer = requests.post(myCustomerDataURL, data = customer)
    with open('customer.txt', 'wb') as profile:
        pickle.dump(customer, profile)


def value_customer():
    global customer
    rewards1 = CustomerRewards(True, 50, 100)
    customer = Customer("Bob", "Customer", "abc@123.net",
                        "789-445-2112", rewards1)


def emailCustomer():
    global customer
    webbrowser.open(
        f'mailto:{customer.email}?subject=This is my subject&body=And how about some body', new=1)


def run_selection(selection):
    print(selection)


# main_menu
# Main menu for Blue Sky Corp POS
def main_menu():
    print("   (1) Sell Items")
    print("   (2) Customer Profile")
    print()
    print("   (X) Exit")
    print()


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


def main():
    global run
    run_splash()
    while run:
        main_menu()
        run_selection(input("Selection: "))


main()
