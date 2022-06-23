#I have created simpler functions based on what an ATM can do to make the testing easier for me as I am not confident with the topic
import unittest
import calc
# Example 1. Testing subtraction with assertEqual

def money_out(a, b):
  return(a - b)

class TestMoneyOut(unittest.TestCase):
    def test_money_out(self):
        self.assertEqual(money_out(10, 5), 5)  #This would return a OK test
        self.assertEqual(money_out(10, 5), 4) #This would return a FAILED test

# Example 2. Testing a deposit (addition) with assertEqual

def money_in(a, b):
    return(a + b)

class TestMoneyIn(unittest.TestCase):
    def test_money_in(self):
        self.assertEqual(money_in(10, 5), 15)  #This would return a OK test
        self.assertEqual(money_in(10, 5), 14) #This would return a FAILED test
# Example 3. Testing to make sure the withdrawal is always smaller than the client's balance with assertRaises

def impossible_withdrawal(money_taken, balance):
     if money_taken > balance:
         raise ValueError("You do not have enough money in your account")

class Testwithdrawals(unittest.TestCase):
    def test_impossible_withdrawal(self):
        self.assertRaises(ValueError, impossible_withdrawal, 99, 100) #This would return a FAILED test as 99 is smaller than 100
        self.assertRaises(ValueError, impossible_withdrawal, 115, 100) #This would return an OK test as 115 is NOT smaller than 100

#  Example 4. Making sure users enter a correct pin and testing it with assertIs

def correct_pin(user_attempt, user_pin):
  if user_attempt == user_pin:
    return("Correct pin number. Pick an option")
  else:
    return("Incorrect pin. Try again")

class TestCorrectPin(unittest.TestCase):
  def test_correct_pin(self):
    self.assertIs(15, 14) # This returns a FAILED test because 15 is not 14
    self.assertIs(15, 15)  # This returns an OK test because 15 is 15

if __name__ == '__main__':
  unittest.main()
