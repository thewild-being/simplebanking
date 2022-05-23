import random
import main

counter = 1
control_input = ""
exit_loop = 0
switch = True
account_number = ""
pin = 0
add_income = 0
transfer_balance = ""


# _________________________________________________________________________________
# class generated data bank account

class CreditCard:
    def __init__(self, Pin, accountNumber):
        self.accountNumber = accountNumber
        self.Pin = Pin

    def Pin(self):
        return self

    def accountNumber(self):
        return self


# _________________________________________________________________________________
# Luhn Algo » da chiamare dentro gli obj che controllano se il card numb sia corretto o meno


def luhn_algo():
    luhn_switch = True

    # usa uno switch per un while loop per iterare un codice valido
    while luhn_switch:
        account_number = ("400000" + str(random.randrange(1000000000, 9999999999, 1)))
        account_number1 = list(account_number)
        check_sum = account_number1.pop()
        processed_index = []

        for index, digit in enumerate(account_number1):  # gli index partono da 1 su jetbrain, non zero
            if index % 2 == 0:
                double_digit = int(digit) * 2

                if double_digit > 9:
                    double_digit -= 9

                processed_index.append(double_digit)  # prova a sostituire e non appendere
            else:
                processed_index.append(int(digit))  # worst case, metti un massimo di index alla lista

        tot = int(check_sum) + (sum(processed_index))
        if int(tot) % 10 == 0:
            luhn_switch = False
            return account_number


def luhn_check(transfer_numb):
    account_number1 = list(transfer_numb)
    check_sum = account_number1.pop()
    processed_index = []

    for index, digit in enumerate(account_number1):  # gli index partono da 1 su jetbrain, non zero
        if index % 2 == 0:
            double_digit = int(digit) * 2

            if double_digit > 9:
                double_digit -= 9

            processed_index.append(double_digit)  # prova a sostituire e non appendere
        else:
            processed_index.append(int(digit))  # worst case, metti un massimo di index alla lista

    tot = int(check_sum) + (sum(processed_index))
    if int(tot) % 10 == 0:
        return bool(True)


# _________________________________________________________________________________
# engine
while control_input != exit_loop:
    connection = main.connect()
    main.create_table(connection)
    commit = connection.commit()

    if not switch:
        control_input = \
            int(input("\n1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n>"))
    if switch:
        control_input = int(input("\n1. Create an account\n2. Log into account\n0. Exit\n>"))

    if control_input == 0:
        print("Bye!")
        break

    if control_input == 1 and switch:
        Card = CreditCard(Pin=(random.randrange(1000, 9999, 1)),
                          accountNumber=(luhn_algo()))
        main.add_cards(connection, Card.accountNumber, Card.Pin)
        # commit()

        if switch:
            print("Your card number:")
            print(Card.accountNumber)
            print("Your card PIN:")
            print(Card.Pin)

        # _______________BALANCE
    if control_input == 1 and not switch:
        print("Balance:" + str(add_income))

    if control_input == 2:
        Card_in = CreditCard(Pin=None, accountNumber=None)
        if switch:
            print("Enter your card number:")
            Card_in.accountNumber = str(input("> "))
            print("Enter your PIN:")
            Card_in.Pin = int(input("> "))
            if Card.accountNumber == Card_in.accountNumber and Card.Pin == Card_in.Pin:
                switch = not switch
                print("You have successfully logged in!")
            else:
                print("Wrong card number or PIN!")

        # _______________ADD INCOME » devi salvare le nuove info
        elif not switch:
            add_income = int(input("Enter income:\n>"))
            main.add_balance(connection, add_income)
            if add_income:
                print("Income was added!")

    # ⚠️PER VEDERE NEL DB IN OGNI STEP
    """if control_input == 8:
        cards = main.see_db(connection)
        for card in cards:
            print(card)"""

    """if control_input == 9:
        main.delete_card(connection)
        print("db empty")"""
    # _______________
    """if (switch == False) and control_input == 9:
        cards = main.see_db(connection)
        for card in cards:
            print(card)"""

    # _______________TRANSFER
    if (switch == False) and control_input == 3:
        transfer_switch = True
        transfer_numb = (input("Transfer\nEnter card number:\n>"))
        cards = main.check_cards(connection, transfer_numb)

        # _______________BALANCE CHECK
        if cards and luhn_check(transfer_numb):
            transfer_balance = int(input("Enter how much money you want to transfer:\n>"))

            if int(transfer_balance) > int(add_income):
                print("Not enough money!")
            elif int(transfer_balance) <= int(add_income):
                add_income = add_income - transfer_balance
                main.add_balance(connection, add_income)
                print("Success!")

        if not cards and (transfer_switch == False):
            print("Such a card does not exist.")
        if luhn_check == False or not cards:
            print("Probably you made a mistake in the card number.\nPlease try again!")
            transfer_switch = False

    if (switch == False) and control_input == 4:
        main.delete_card(connection)
        del(Card_in.accountNumber, Card.accountNumber)
        switch = True
        print("The account has been closed!")
