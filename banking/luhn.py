import random


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


test = luhn_algo()
print(test)
print(luhn_check(test))

