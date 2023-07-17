import math

def isPalindrome(num):
  num_convert_to_string = str(num)
  num_reverse = num_convert_to_string[::-1]
  for i in range(0, math.ceil(len(num_reverse)/2)):
    if num_reverse[i] != num_convert_to_string[i]:
      return False
  return True

print(isPalindrome(10101))
