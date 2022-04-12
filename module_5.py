# The is_palindrome function checks if a string is a palindrome. A palindrome is a string that can be equally read from left to right or right to left, omitting blank spaces, and ignoring capitalization. Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even". Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.
# def is_palindrome(input_string):
# 	# We'll create two strings, to compare them
# 	input_string = input_string.replace('\t','').replace(' ','').lower()
# 	reverse_string = input_string[::-1]
# 	return input_string ==reverse_string
#
# print(is_palindrome("Never  		Odd or Even")) # Should be True
# print(is_palindrome("abc")) # Should be False
# print(is_palindrome("kayak")) # Should be True


# def combine_lists(list1, list2):
#     list2.extend(list1[::-1])
#     print(list2)
#
#
# # Generate a new list containing the elements of list2
# # Followed by the elements of list1 in reverse order
#
#
# Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
# Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
#
# print(combine_lists(Jamies_list, Drews_list))

# def highlight_word(sentence, word):
# 	return(sentence.replace(word,word.upper()))
#
# print(highlight_word("Have a nice day", "nice"))
# print(highlight_word("Shhh, don't be so loud!", "loud"))
# print(highlight_word("Automating with Python is fun", "fun"))


def format_address(address_string):
    # Declare variables
    # Separate the address string into parts
    # Traverse through the address parts
    details = ''
    house_number = ''
    final_address = address_string.split()
    house_number =final_address[0]
    address = ' '.join(final_address[1:])
    print("house number {} on street named {}".format(final_address,details))
    # Determine if the address part is the
    # house number or part of the street name
    # Does anything else need to be done
    # before returning the result?

    # Return the formatted string
    return "house number {} on street named {}".format(house_number,address)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"



print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"


# problem 2
# Using the format method, fill in the gaps in the convert_distance
# function so that it returns the phrase "X miles equals Y km",
# with Y having only 1 decimal place. For example, convert_distance(12) should return "12 miles equals 19.2 km".

# def convert_distance(miles):
# 	km = miles * 1.6
# 	result = "{} miles equals {:.1f} km".format(miles,km)
# 	return result
#
# print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
# print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
# print(convert_distance(11)) # Should be: 11 miles equals 17.6 km


# problem 3
# If we have a string variable named Weather = "Rainfall", which of the following will print the substring or all characters before the "f"?


# problem 4
# def nametag(first_name, last_name):
# 	return("{} {}.".format(first_name,last_name[0]))
#
# print(nametag("Jane", "Smith"))
# # Should display "Jane S."
# print(nametag("Francesco", "Rinaldi"))
# # Should display "Francesco R."
# print(nametag("Jean-Luc", "Grand-Pierre"))
# # Should display "Jean-Luc G."


# # problem 5
# def replace_ending(sentence, old, new):
#     # Check if the old string is at the end of the sentence
#     if old in sentence.split(" ")[-1]:
#         # Using i as the slicing index, combine the part
#         # of the sentence up to the matched string at the
#         # end with the new string
#         index = sentence.rfind(old)
#         i = sentence[:index]
#         new_sentence = i + new
#         return new_sentence
#     # Return the original sentence if there is no match
#     return sentence
#
#
# print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# # Should display "It's raining cats and dogs"
# print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# # Should display "She sells seashells by the seashore"
# print(replace_ending("The weather is nice in May", "may", "april"))
# # Should display "The weather is nice in May"
# print(replace_ending("The weather is nice in May", "May", "April"))
# # Should display "The weather is nice in April"

# def combine_guests(guests1, guests2):
#   # Combine both dictionaries into one, with each key listed
#   # only once, and the value from guests1 taking precedence
#   for name,number_of_people in guests2.items():
#       if name in guests1:
#           guests2[name] = guests1[name]
#   print(guests2)

#
# Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
# Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}
#
# print(combine_guests(Rorys_guests, Taylors_guests))



# def car_listing(car_prices):
#   result = ""
#   for name,price in car_prices.items():
#     result += "{} costs {} dollars".format(name,price) + "\n"
#   return result
#
# print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))




# def count_letters(text):
#   result = {}
#   text = text.lower()
#   # Go through each letter in the text
#   for letter in text:
#     if not letter.isalpha():
#         continue
#     # Check if the letter needs to be counted or not
#     if letter not in result:
#         result[letter] = 1
#     else:
#         result[letter] += 1
#     # Add or increment the value in the dictionary
#   return result

# print(count_letters("AaBbCc"))
# # Should be {'a': 2, 'b': 2, 'c': 2}
#
# print(count_letters("Math is fun! 2+2=4"))
# # Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}
#
# print(count_letters("This is a sentence."))
# # Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
