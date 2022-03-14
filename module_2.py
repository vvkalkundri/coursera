import math
def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to
# keep just the fractional part of the quotient
	if denominator == 0:
		return 0
	remainder = numerator%denominator
	quotient = round(numerator / denominator,3)
	if remainder == 0:
		return remainder
	else:
		return (quotient % 1)
# print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0


# Longest word
#
# def longest_word(word1, word2, word3):
#     if len(word1) >= len(word2) and len(word1) >= len(word3):
#         word = word1
#     elif len(word2) >= len(word1) and len(word2) >= len(word3):
#         word = word2
#     else:
#         word = word3
#     return (word)
#
#
# print(longest_word("chair", "couch", "table"))
# print(longest_word("bed", "bath", "beyond"))
# print(longest_word("laptop", "notebook", "desktop"))

# Color translator

# def color_translator(color):
# 	if color == "red":
# 		hex_color = "#ff0000"
# 	elif color == "green":
# 		hex_color = "#00ff00"
# 	elif color =="blue":
# 		hex_color = "#0000ff"
# 	else:
# 		hex_color = "unknown"
# 	return hex_color
#
# print(color_translator("blue")) # Should be #0000ff
# print(color_translator("yellow")) # Should be unknown
# print(color_translator("red")) # Should be #ff0000
# print(color_translator("black")) # Should be unknown
# print(color_translator("green")) # Should be #00ff00
# print(color_translator("")) # Should be unknown
