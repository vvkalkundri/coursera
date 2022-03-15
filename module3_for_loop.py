def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return True
  # Recursive case: keep dividing number by base.
  return is_power_of( 8/2, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False




# def factorial(n):
#     result = 1
#     for x in range(1,n):
#         result = result * x
#     return result
#
#
# # print(factorial(10))
# for n in range(1,10):
#     print(n, factorial(n+1))
