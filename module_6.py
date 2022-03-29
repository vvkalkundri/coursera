import glob

# file_names = ['rfk_entity_category_paths.json.gz', 'product_records_complete.json.gz']
# file_name = glob.glob('*_category_*')[0]
# print(file_name)
#
# wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
# new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
# wardrobe.update(new_items)


class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return self.name

# Create a new instance with a name of your choice
some_person = Person("Superb")
# Call the greeting method
print(some_person.greeting())
#
# # define a basic city class
# class City:
# 	name = ""
# 	country = ""
# 	elevation = 0
# 	population = 0
#
# # create a new instance of the City class and
# # define each attribute
# city1 = City()
# city1.name = "Cusco"
# city1.country = "Peru"
# city1.elevation = 3399
# city1.population = 358052
#
# # create a new instance of the City class and
# # define each attribute
# city2 = City()
# city2.name = "Sofia"
# city2.country = "Bulgaria"
# city2.elevation = 2290
# city2.population = 1241675
#
# # create a new instance of the City class and
# # define each attribute
# city3 = City()
# city3.name = "Seoul"
# city3.country = "South Korea"
# city3.elevation = 38
# city3.population = 9733509
#
# def max_elevation_city(min_population):
# 	# Initialize the variable that will hold
# # the information of the city with
# # the highest elevation
# 	return_city = City()
# 	highest_elevation = 0
#
# 	# Evaluate the 1st instance to meet the requirements:
# 	# does city #1 have at least min_population and
# 	# is its elevation the highest evaluated so far?
# 	if city1.population > min_population and city1.elevation > highest_elevation :
# 		highest_elevation = city1.elevation
# 		return_city.name , return_city.country = city1.name , city1.country
# 	# Evaluate the 2nd instance to meet the requirements:
# 	# does city #2 have at least min_population and
# 	# is its elevation the highest evaluated so far?
# 	if city2.population > min_population and city2.elevation > highest_elevation :
# 		highest_elevation = city1.elevation
# 		return_city.name , return_city.country = city2.name , city2.country
# 	# Evaluate the 3rd instance to meet the requirements:
# 	# does city #3 have at least min_population and
# 	# is its elevation the highest evaluated so far?
# 	if city3.population > min_population and city3.elevation > highest_elevation :
# 		highest_elevation = city1.elevation
# 		return_city.name , return_city.country = city3.name , city3.country
#
# 	#Format the return string
# 	if return_city.name:
# 		return return_city.name + ", "+ return_city.country
# 	else:
# 		return ""
#
# print(max_elevation_city(100000)) # Should print "Cusco, Peru"
# print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
# print(max_elevation_city(10000000)) # Should print ""
#


# def add_prices(basket):
# 	# Initialize the variable that will be used for the calculation
# 	total = 0
# 	# Iterate through the dictionary items
# 	for name,price in basket.items():
# 		# Add each price to the total calculation
# 		# Hint: how do you access the values of
# 		# dictionary items?
# 		total += price
# 	# Limit the return value to 2 decimal places
# 	return round(total, 2)
#
# groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
# 	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

# print(add_prices(groceries)) # Should print 28.44



# def groups_per_user(group_dictionary):
# 	user_groups = {}
# 	# Go through group_dictionary
# 	for role,users in group_dictionary.items():
# 		# Now go through the users in the group
# 		for user in users :
# 			if user not in user_groups:
# 				user_groups[user] = []
# 			user_groups[user].append(role)
# 			# Now add the group to the the list of
# # groups for this user, creating the entry
# # in the dictionary if necessary
#
# 	return(user_groups)

# print(groups_per_user({"local": ["admin", "userA"],
# 		"public":  ["admin", "userB"],
# 		"administrator": ["admin"] }))

#
# def email_list(domains):
#     emails = []
#     for email, users in domains.items():
#         for user in users:
#             emails.append(user + '@' + email)
#     return (emails)
#
#
# print(email_list(
#     {"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"],
#      "hotmail.com": ["bruce.wayne"]}))

# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# # Generate newfilenames as a list containing the new filenames
# # using as many lines of code as your chosen method requires.
# newfilenames = [ filename.replace('.hpp','.h') if ".hpp" in filename else filename for filename in filenames ]
#
# print(newfilenames)
# # Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
#
#
# def pig_latin(text):
#     say = ""
#     # Separate the text into words
#     words = text.split()
#     for word in words:
#         # Create the pig latin word and add it to the list
#         say += word[1:] + word[0] +'ay' + ' '
#         # Turn the list back into a phrase
#     return say
#
#
# print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"


# def octal_to_string(octal):
#     result = ""
#     value_letters = [(4, "r"), (2, "w"), (1, "x")]
#     # Iterate over each of the digits in octal
#     for digit in [int(n) for n in str(octal)]:
#         # Check for each of the permissions values
#         for value, letter in value_letters:
#             if digit >= value:
#                 result += letter
#                 digit -= value
#             else:
#                 result += '-'
#     return result


# print(octal_to_string(755))  # Should be rwxr-xr-x
# print(octal_to_string(644))  # Should be rw-r--r--
# print(octal_to_string(750))  # Should be rwxr-x---
# print(octal_to_string(600))  # Should be rw-------

#
# def guest_list(guests):
#     for element in guests:
#         name, age, profession = element
#         print("{} is {} years old and works as {}".format(name,age,profession))
#
# guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

# Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""
