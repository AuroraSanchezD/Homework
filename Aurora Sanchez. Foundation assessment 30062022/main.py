# QUESTION 3. Palindrome function

def reversingString(inputString):
    return inputString[::-1]
def isPalindrome(inputString):
    comparing_string = reversingString(inputString)
    if (inputString == comparing_string):
        return True
    else:
        return False
word = input("Your word: ")
check = isPalindrome(word)
if check == 1:
     print("Your word is a palindrome")
else:
     print("Your word is not a palindrome")

# QUESTION 4. Tests for the Palindrome function. I am using assertEqual, assertNotEqual and assertIsNot
import unittest
class Testmyfunction(unittest.TestCase):
    def test_reversingString(self):
        self.assertEqual(("hannah"), "hann")
        self.assertEqual(("hannah"), "hannah")

class Testmyfunction(unittest.TestCase):
    def test_reversingString(self):
        self.assert(("hannah"), "hann")
        self.assertNotEqual(("hannah"), "hannah")

class TestPalindromes(unittest.TestCase):
    def test_isPalindrome(self):
        self.assertIsNot(("hannah"), "hannah")
        self.assertIsNot(("maria"), "hannah")
if __name__ == '__main__':
    unittest.main()

# QUESTION 9

# Asking the user to input their numbers
raw_array = input('Enter elements of the list you want to create separated by space')

# Splitting the string input into a list
array = raw_array.split()

# Converting each item to integer
for i in range(len(array)):
    array[i] = int(array[i])

target_sum = int(input("Write your target sum:"))


def find_target(arr, targ):
    results = []
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == targ:
                results.append((arr[i], arr[j]))
    return results


result = find_target(array, target_sum)
print(result)