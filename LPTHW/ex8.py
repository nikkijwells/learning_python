# A variable declairing a string with curly braces in it. These allow us to replce them with text later in the code
# by calling the format() function.
formatter = "{} {} {} {}"

# A print statement using the variable above to insert intergers into the formatter variable.
print(formatter.format(1, 2, 3, 4))
# A print statement using the variable above to insert strings into the formatter variable.
print(formatter.format("one", "two", "three", "four"))
# A print statement using the variable above to insert booleans into the formatter variable.
print(formatter.format(True, False, True, False))
# A print statement using the variable above to insert the formatter decleration into the formatter variable.
print(formatter.format(formatter, formatter, formatter, formatter))
# A print statement using the variable above to insert Zed's poem into the formatter variable.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
