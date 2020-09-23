input_string = "the quick brown fox jumps over the lazy dog"
vowels = frozenset("aeiou")

string_set = set(input_string)
consonants = string_set.difference(vowels)
print(sorted(consonants))