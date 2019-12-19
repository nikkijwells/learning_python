def is_isogram(string):
    string = string.lower()
    return len(set(string)) == len(string)

print(is_isogram("Dermatoglyphics"))
print(is_isogram("aba"))
print(is_isogram("moOse"))
