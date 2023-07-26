import math

def is_perfect_square(num: int) -> bool:
  value = int(str(math.sqrt(num)).split('.')[0])
  return True if value * value == num else False

print(is_perfect_square(9))
print(is_perfect_square(8))
print(is_perfect_square(16))
print(is_perfect_square(25))
print(is_perfect_square(144))
print(is_perfect_square(50))
