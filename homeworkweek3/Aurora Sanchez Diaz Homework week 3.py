# TASK 1
# Question 1

# rain = input("Is it raining?")
# if rain == ("y"):
#     print("You need an umbrella")
# elif rain == ("n"):
#     print("You don't need an umbrella")

# Question 2. Fixing incorrect code.
"""
Changes. I made the 20 + 5 in boat_cost a string to be able to compare it with my_money. Also, changed the comparison
operator in my_money < boat_cost to my money > boat_cost. Lastly, I closed the parenthesis at the end of the print() in
the else.
"""

# my_money = input('How much money do you have?')
# boat_cost = "20 + 5"
# if my_money > boat_cost:
# 	print('You can afford the boat hire')
# else:
# 	print('You cannot afford the board hire')

# Question 3. Centuries and decades in library
# year = input("When was the book written?")
# decade = {
#     "0": "first decade",
#     "1": "tens",
#     "2": "twenties",
#     "3": "thirties",
#     "4": "forties",
#     "5": "fifties",
#     "6": "sixties",
#     "7": "seventies",
#     "8": "eighties",
#     "9": "nineties"
# }
# if year == "1800":
#     print("Eighteenth Century")
# elif year.startswith("18") or year.endswith("1900"):
#     print("Nineteenth Century,", decade[year[2:3]])
# elif year.startswith("19") and int(year) <= 1950:
#     print("Twentieth Century,", decade[year[2:3]])
# else:
#     print("Out of Range")

# TASK 2

# Question 1. Fixing shopping list
# shopping_list = [
# 	"oranges",
# 	"cat food",
# 	"sponge cake",
# 	"long-grain rice",
# 	"cheese board",
# ]
# print(shopping_list[0])
# The mistake here was that the index was incorrect. The fist item in a list will be index [0], not [1]

# Question 2. I'm setting up my own market stall to sell chocolates. I need a basic till

# chocolates = {
#
#     'white': 1.50,
#
#     'milk': 1.20,
#
#     'dark': 1.80,
#
#     'vegan': 2.00,
# }
# choice = input('Choose your chocolate out of the following options: white, milk, dark and vegan')
# cost = "Your total will be £"
# if choice == 'white':
#     print(cost, chocolates.get('white'))
# elif choice == 'milk':
#     print(cost, chocolates.get('milk'))
# elif choice == 'dark':
#     print(cost, chocolates.get('dark'))
# elif choice == 'vegan':
#     print(cost, chocolates.get('vegan'))
# else:
#     print("Unfortunately, we do not stock this item. Try again")

# Question 3. Lottery simulator.
# import random
# import operator
# given_numbers = [1,2,3,4,5,6,7]
# random_list = []
# for given_number in given_numbers:
#     random_list.append(random.randint(1, 10))
# print(random_list)
# total_count = 0
# for s in given_numbers:
#     total_count += operator.countOf(random_list, s)
# print(total_count)
#
# if total_count == 3:
#     print('You have won £20')
# elif total_count == 4:
#     print('You have won £40')
# elif total_count == 5:
#     print('You have won £100')
# elif total_count == 6:
#     print('You have won £10000')
# elif total_count == 7:
#     print('You have won £1000000')
# else:
#     print('Best of luck next time ;)')
# TASK 3. Reading and writing files

# Question 1. What is PIP and its advantages.
# PIP is the official package-management system in Python used to install and manage software packages
# Benefits: PIP extends Python's functionalities because it allows us to install new packages.
# NumPy is an example of a package you can install thanks to PIP. Numpy can be used to generate random numbers or perform
# advanced operations with arrays. We have also covered talked about the DateTime package.

# Question 2 .This program should save my data to a file, but it doesn't work when I run it.
# What is the problem and how do I fix it?

# The problem was the 'r' in the second line. 'R' means we can only read the file but not modify it.
# The solution is to change that 'r' for 'w' (allows to write in said file), or 'w+' (reading AND writing)
# Once we have done this, a txt file named will be created in the folder. It will contain the message "I like..."
# poem = 'I like Python and I am not very good at poems'
# with open('poem.txt', 'w+') as poem_file:
#     poem_file.write(poem)

# Question 3.
# with open("song.txt", "w+") as f:
#     f.write('You could never know what it´s like\nYour blood like winter freezes just like ice\nAnd theres a cold lonely light that shines from you\nYou´ll wind up like the wreck you hide behind that mask you use\n\nAnd did you think this fool could never win?\nWell look at me, I´m coming back again\nI got a taste of love in a simple way\nAnd if you need to know while I´m still standing, you just fade away\n\nDon´t you know I´m still standing better than I ever did\nLooking like a true survivor, feeling like a little kid\nI´m still standing after all this time\nPicking up the pieces of my life without you on my mind\n\nI´m still standing (Yeah, yeah, yeah)\nI´m still standing (Yeah, yeah, yeah)')

# Question 4. Find strings with 'still'

# file_read = open('song.txt', "r")
# lines = file_read.readlines()
# new_list = []
# index = 0
# for line in lines:
#     if 'still' in line:
#         new_list.insert(index, line)
#         index += 1
# if len(new_list) > 0:
#     lineLen = len(new_list)
#     print("\nLines with \"" + 'still' + "\"")
# for i in range(lineLen):
#     print(end=new_list[i])

# TASK 4. Pokemon API
# import requests
# id_list = [1, 2, 3, 4, 5, 6]
# all_pokemon = []
# for identifier in id_list:
#     response = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(identifier))
#     current_pokemon = []
#     if response.status_code == 200:
#         data = response.json()
#         current_pokemon.append(data['name'])
#         current_pokemon_moves = []
#         for moves in data['moves']:
#             current_pokemon_moves.append(moves['move']['name'])
#         current_pokemon.append(current_pokemon_moves)
#     all_pokemon.append(current_pokemon)
#
# with open('pokemon.txt','w+') as text_file:
#     for entry in all_pokemon:
#         pokemon = entry[0]
#         text_file.write(pokemon +"\n")
#         for move in entry[1]:
#             text_file.write("--" + move + "\n")
