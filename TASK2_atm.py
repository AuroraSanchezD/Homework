import sys
import unittest
attempt = 0
client = {
    'balance': 100,
    'pin': 1234
}

while attempt < 3:
    pin_input = input("Enter your 4 digit pin")
    attempt += 1
    if int(pin_input) == client['pin']:
        print("Thank you")
        break
    elif attempt < 3:
        print("Your pin is incorrect, try again")
    else:
        print("Three incorrect attempts. Your card is locked. Contact a member of staff to get help")
        sys.exit(1)


def withdrawing_money():
    money_out = int(input("How much money do you want to withdraw?"))
    try:
        if money_out < client['balance']:
            client['balance'] = client['balance'] - money_out
            print(f"£{money_out} withdrawn from your account.")
        else:
            raise Exception("You don't have enough money to complete this transaction.")
    except Exception as e:
        print(e)
        sys.exit(1)
    finally:
        print(f"Your current balance is £{client['balance']}.")


def total_balance():
    print(f"Your total balance is £{client['balance']}")


next_step = int(input("If you want to withdraw money, press 1. If you want to see your balance, press 2"))
if next_step == 1:
    withdrawing_money()
elif next_step == 2:
    total_balance()
