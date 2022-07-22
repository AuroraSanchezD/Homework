"""

TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of item?..
3. You will need to write some examples of how your code works.

"""


class CashRegister:

    def __init__(self, discount=0):

        self.total_items = dict()  # we are going to be using a dictionary. Keys will be items, values will be prices
        self.total_price = 0
        self.discount = discount

    def add_discount(self, new_discount):  # this method allows the discount to be updated. Example: adding new coupon
        self.discount = new_discount  # this updates the previous discount

    def add_item(self, item, price):
        self.total_items[item] = price  # the [item] is updating the new key.
        # This is updating the total_items and total_price tally

    def remove_item(self, item):
        self.total_items.pop(item)  # pop() gets rid of the last element in the dictionary

    def apply_discount(self):  # This discount will be applied to the total price of the purchase, not individual items
        """
        Example:
        new price = 50 - (50 / 10) = 45. This logic is captured on line 44

        :return:
        """
        try:
            price = self.total_price - (self.total_price / self.discount)  # if discount = 0, we go to the next line
        except ZeroDivisionError:
            print("No discount available")
        else:
            self.total_price = price

    def get_total(self):
        if self.total_items:
            # 1. calculate new price
            self.total_price = sum(
                self.total_items.values())  # the values() method returns the values in a dict as list

            # 2. apply discount
            self.apply_discount()
        else:
            print("No items in the basket")

    def show_items(self):  # we are going to create a message that looks like a receipt
        msg = """
        ====================
        Items purchased
        ---------------
        {}
        
        Total: {}
        
        Thank you!
        ====================
        """
        width = 20  # this is the number of == characters in my receipt
        records = []  # we do not know the number of products we will have in our receipt

        for k, v in self.total_items.items():  # items() method returns the list with all dictionary keys with values
            txt = len(k)  # this makes the length as long as the key
            digits = len(str(v))  # this line stringifies the values and then tells their length.
            # Tells me how many dots between text and digit
            characters = width - txt - digits
            r = "{}{}{}".format(k, '.' * characters, v)
            records.append(r)

        all_records = '        \n'.join(records)  # we are joining all items and putting them in a new line
        final_msg = msg.format(all_records, self.total_price)
        print(final_msg)

    def reset_register(self):  # this resets everything so that the next customer starts blank
        self.total_price = 0
        self.total_items.clear()  # this leaves the dictionary blank
        self.discount = 0

register = CashRegister(discount=5)
register.add_item('apples', 2.45)
"""

TASK 2

Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 

"""


class Student:

    def __init__(self, name, age, _id):
        self.name = name
        self.age = age
        self.id = _id
        self.subjects = dict()

    def add_subjects(self, list_of_subjects):
        for subject in list_of_subjects:
            self.subjects[subject] = None


class CFGStudent(Student):  # This class inherits the properties in the Student class

    def __init__(self, stream, *args, **kwargs):  # the parameter stream tells us if the student does data, software...
        # *args and **kwargs are substituting the name, age and _id parameters in the original Student class
        super().__init__(*args, **kwargs)  # this initialises the CFGStudent subclass
        self.specialisation = stream

    def add_subject(self, subject):
        self.subjects[subject] = None  # I add None because I do not know what the subject is going to be

    def remove_subject(self, subject):
        self.subjects.pop(subject)  # again, the pop() method gets rid of a subject

    def view_all_subjects(self):
        return list(self.subjects.keys())  # we are using the keys method to get all the keys in the dict.
        # Then, the dict is converted into a list

    def update_grade(self, subject, grade):
        self.subjects[subject] = grade

    def get_overall_mark(self):
        current = dict({(k, v) for k, v in self.subjects.items() if v is not None})
        """
        The code in line 143 is a list comprehension that
        gets rid of values of subjects whose grades might not be available yet to be able to later create an overall 
        mark that does not take into consideration empty values
        """
        return sum(current.values()) / len(current.values())  # this line calculates the average grade
