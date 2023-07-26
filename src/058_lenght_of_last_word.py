def length_of_last_word(s: str) -> int:
  s = s.strip().split(' ')
  return len(s[-1])

print(length_of_last_word('Hello World'))
print(length_of_last_word('   fly me   to   the moon  '))

