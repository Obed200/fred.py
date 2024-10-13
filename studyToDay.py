
print("____________________________________________")
def sum_of_multiples(limit):
  

  sum = 0
  for i in range(limit):
    if i % 3 == 0 or i % 5 == 0:
      sum += i
  return sum

# Example usage:
limit = 20
result = sum_of_multiples(limit)
print(f"The sum of multiples of 3 and 5 less than {limit} is: {result}")
print("____________________________________________")

def count_upper_lower(input_string):
    upper_count = 0
    lower_count = 0
    
    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    print("Number of Uppercase letters:", upper_count)
    print("Number of Lowercase letters:", lower_count)

# Example usage:
sample_string = "Python"
count_upper_lower(sample_string)
print("____________________________________________")
def sum_multiples_3_5(limit):
    result = 0

    for num in range(limit + 1):
        if num % 3 == 0 or num % 5 == 0:
            result += num

    return result

# Example usage:
limit = 20
result = sum_multiples_3_5(limit)
print("Sum of multiples of 3 and 5 up to", limit, "is:", result)
print("____________________________________________")
def sum_list_numbers(input_list):
    return sum(input_list)

# Example usage:
sample_list = [8, 2, 3, 0, 7]
result = sum_list_numbers(sample_list)
print("Sum of numbers in the list:", result)
print("____________________________________________")
def replace_vowels_with_star(input_string):
    vowels = "aeiouAEIOU"
    result_string = ""

    for char in input_string:
        if char in vowels:
            result_string += '*'
        else:
            result_string += char

    return result_string

# Example usage:
input_str = input("enter a string:")
output_str = replace_vowels_with_star(input_str)
print("Original String:", input_str)
print("String with Vowels Replaced:", output_str)