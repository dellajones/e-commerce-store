import time
user_name = []
pass_word = []
shipping_address = []
billing_address = []
card_number = []

def main():
    print("Hello! Welcome to _____ Emporium where we sell all kinds of instruments")
    print("Please! Choose 1 of the following options based on what you would like to do.")
    print("1. Login to Account")
    print("2. Create Account")
    print("Any other Number: Close application")
    user_choice = input("Please enter 1, 2, or any number: ")
    if user_choice == '1':
        login_function()
    elif user_choice == '2':
        account_create_function()
    else:
        print("The program will now shutdown. Thank you for your continued patronage and have a nice day")
        time.sleep(5)
        quit()

def login_function():
    for x in range(50):
        print("")
    user_name = input("Please enter your username: ")
    pass_word = input("Please enter your password: ")
    #COMPARE TO WHAT IS IN DATABASE HERE. Maybe a while loop here to continuously check it to make sure that it matches idk
    #if statement checking if database check returns true
    if True:
	#for more user friendlyness: probable should print: logging in now
        print("You are being logged in to your account!")
        time.sleep(5)
        main_menu_function()
    if False:
        print("Your username and password did not match our database. Please re-enter them.")
        login_function()
              
        

def account_create_function():
    for x in range(50):
        print("")
    print("I did made it here")
    user_name = input("Please choose a username: ")
    #ADD USERNAME TO DATABASE HERE
    #Do we need to add rules to the user and password
    #or check to see if information already exists??
    pass_word = input("Please enter a password: ")
    #Somehow need to make sure it is at least 8 characters here
    email_new = input("Please enter an email address: ")
    #ADD EMAIL TO DATABASE
    billing_address_new = input("Please enter your billing address: ")
    #ADD BILLING TO DATABASE
    check_for_address = input("Are your shipping and billing addresses the same? Please type 1 for Yes and 2 for No: ")
    while True:
        if check_for_address == '1':
            #ADD BILLING ADDRESS INTO SHIPPING ON DATABASE
            print("I have added the shipping address information from your billing address.")
            break
        elif check_for_address == '2':
            shipping_address = input("Please enter your shipping address: ")
            #ADD SHIPPING TO DATABASE
            break
        else:
            print("Your input was invalid. Please enter 1 or 2!")
            check_for_address = input("Are your shipping and billing addresses the same? Please type 1 for Yes and 2 for No: ")        
    debit_card_number = input("Please enter a FAKE 16 digit debit card number: ")
    #ADD CARD TO DATABASE
    main()
    
def main_menu_function():
    for x in range(50):
        print("")
    print("Thank you for logging in and your continued patronage is appreciated.")
    print("There are several options you can do now. You like to shop for items, view your cart, edit personal info, or logout(Closing the application)")
    print("1. Shop for Instruments")
    print("2. View Cart")
    print("3. Edit Personal Information")
    print("Any other number: Logoff")
    menu_choice = input("Please enter one of the numbers above: ")
    if menu_choice == '1':
        shopping_function()
    elif menu_choice == '2':
        view_cart_function()
    elif menu_choice == '3':
        personal_info_function()
    else:
        quit()

def shopping_function():
    #ACCESS DATABASE HERE OR SOMETHIN IDK
    for x in range(50):
        print("")
    print("Welcome to our online shop!")
    print("We will now provide a categorized list of items you can purchase")
    #PRINT INFO OUT ABOUT THE ITEMS
    #FIGURE OUT HOW TO LET PEOPLE CHOOSE ONE
    user_choice = input("If you would like to shop for items, please press 1: ")
    while user_choice == '1':
        shop_choice = input("Please choose an item from the above list: ")
        #BASED ON WHAT NUMBER THEY TYPE ADD THAT ITEM TO CART
        user_choice = input("If you would like to purchase another item, please press 1: ")
        if user_choice is not '1':
            print("You will now be returned to the main menu!")
            time.sleep(5)
            break
            
    

def view_cart_function():
    #cart stuff here
    for x in range(50):
        print("")
    print("Welcome to the cart menu!")
    print("Here you can access your cart, checkout, and many other things.")
    print("1. Display Items in cart.")
    print("2. Remove Item from cart.")
    print("3. View Previous orders.")
    print("4. Checkout!")
    print("Any other Number. Return to Main menu")
    user_choice = input("If you would like to access one of these options please press 1: ")
    while user_choice == '1':
        user_menu_choice = input("Which option would you like to choose? Please press 1, or any number listed above: ")
        if user_menu_choice == '1':
            display_cart_function()
        elif user_menu_choice == '2':
            remove_item_function()
        elif user_menu_choice == '3':
            view_orders_function()
        elif user_menu_choice == '4':
            checkout_function()
        else:
            print("You will now be returned to the main menu.")
            time.sleep(5)
            break
        user_menu_choice = input("Would you like to choose another option? If so, please press 1: ")
    main_menu_function()

    #CHECKOUT IN HERE
    #DISPLAY ALL ITEMS IN CART
    #REMOVE ITEMS FROM CART
    #RETURN TO MAIN MENU
    #VIEW PREVIOUS ORDERS
    
def display_cart_function():
    for x in range(50):
        print("")
    print("I have made a list of the current items in your cart.")
    #print out the items in the cart. Maybe include their prices, names, other useful info. taken from database i think
    user_choice = input("Please press 1 when you would like to return to the main menu!")
    while True:
        if user_choice == '1':
            print("You will now be returned to the main menu!")
            time.sleep(5)
            break
        else:
            print("You did not press 1. Please press 1 to return to the main menu.")
            print("")
            user_choice = input("Please press 1 when you would like to return to the main menu!")
    main_menu_function()
    
    
def remove_item_function():
    for x in range(50):
        print("")
    print("Here is a list of your current items.")
    i = 1
    #this number needs to be defined as cart number something#
    while i < 50:
    	print("Item #", i)
    	i+1
    user_choice = input("If you would like to choose an item to remove, please press 1: ")
    while user_choice == '1':
        remove_item = input("Please enter the number of the item you wish to remove. If you do not want to remove any more items please press a number not labled in your cart: ")
        if remove_item <= 50:
            print("The item has been removed!")
        else:
            print("We will assume that you do not want to remove any more items from your cart and we will now send you back to the main menu.")
            time.sleep(5)
            break
        user_if_change = input("If you would like to remove another item, please press 1: ")
    print("Your items have been successfully removed from your cart. We will now send you back to the main menu!")
    time.sleep(5)
    main_menu_function()
    

def view_orders_function():
    print("previous orders here")
    for x in range(50):
        print("")
    print("Here is a list of your previous orders!")
    #DISPLAY PREVIOUS ORDERS. IF there are multiple, write an if statement
    print("You will now be sent back to the main menu! Thank you for your continued patronage!")
    time.sleep(5)
    main_menu_function()

def cart_checkout_function():
    print("I have made a list of the current items in your cart.")
    print("")
    #i = 1
    #For i < Total cart # of items
    #print each cart item

def checkout_function():
    print("checkout menu things")
    for x in range(50):
        print("")
    print("Welcome to the checkout page!")
    cart_checkout_function()
    #PULL ADDRESSES FROM DATABASE STORE IN VARIABLES
    #Display addresses
    user_choice = input("Is this shipping and billing information correct? Please press 1 if it is: ")
    if user_choice != '1':
        print("We are very sorry to hear that we had your information stored incorrectly. Could you please tell us which address is wrong?")
        while True:
            user_second_choice = input("Please type 1 if your shipping address is wrong and 2 if your billing address is wrong. If it is correct please type any other number: ")
            if user_second_choice == '1':
                #update shipping address in database
                shipping_address = input("Please enter your shipping address so we can properly store it in our database: ")
            elif user_second_choice == '2':
                #update billing address in database
                billing_address = input("Please enter your billing address so that we can properly store it in our database: ")
            else:
                print("Assuming that you didn't press 1 or 2, we will use the current information stored as your current address.")
                break
            user_second_choice = input("Please type 1 if your shipping address is wrong or 2 if your billing address is wrong. If it is correct, please type any number: ")
    #display card number
    user_card_number = input("Is this card number correct? Press 1 if it is: ")
    if user_card_number != '1':
        print("We are very sorry to hear that we had your information stored incorrectly. Could you please tell us the correct card number?")
        while True:
            user_card = input("Please type 1 to change your card number associated with your account: ")
            if user_card == '1':
                #update card number in database
                card_number = input("Please enter your correct card number that you would like associated with your account: ")
                break
            else:
                print("We will assume that your card information is now correct. Thank you for giving us this information!")
                break
    print("Here is your order! Please confirm that it is correct!")
    #print order details here. Make sure to display price total
    user_third_choice = input("Please press 1 to confirm that your order is correct: ")
    if user_third_choice != 1:
        print("We will now reroute you to the main menu. From there you can go to the shopping area or open up the cart area so that you can remove items")
        time.sleep(5)
        main_menu_function()
    print("Your order has been placed! Thank you for your patronage, and we will now reroute you to the main menu!")
    time.sleep(5)
    main_menu_function()


def personal_info_function():
    #editing personal info stuff
    for x in range(50):
        print("")
    print("Time to update your personal information.")
    print("Please! Choose 1 of the following options based on what information you would like to update.")
    print("1. Username")
    print("2. Password")
    print("3. Email")
    print("4. Billing Address")
    print("5. Shipping Address")
    print("6. Payment Info")
    print("Any other Number: Back to the Main Menu")
    user_if_change = input("If you would like to change something please press 1. If you do not want anything changed press any number besides 1: ")
    while user_if_change == '1':
        user_choice = input("Please enter 1, 2, or any number above: ")
        if user_choice == '1':
            username_new = input("Please enter a new username: ")
            #UPDATE USERNAME TO DATABASE HERE
        elif user_choice == '2':
            password_new = input("Please enter a new password: ")
            #UPDATE PASSWORD TO DATABASE HERE
        elif user_choice == '3':
            email = input("Please enter a new email: ")
            #UPDATE EMAIL TO DATABASE HERE
        elif user_choice == '4':
            billing_address = input("Please enter a new billing address: ")
            #UPDATE BILLING TO DATABASE HERE
        elif user_choice == '5':
            shipping_address = input("Please enter a new shipping address: ")
            #UPDATE SHIPPING TO DATABASE HERE
        elif user_choice == '6':
            debit_card_number = input("Please enter new payment information: ")
            #UPDATE PAYMENT TO DATABASE HERE
        else:
            print("You will now be transferred back to the Main Menu!")
            time.sleep(5)
            break
        user_if_change = input("If you would like to change something else, please press 1: ")
    main_menu_function()

if __name__ == "__main__":
    main()
