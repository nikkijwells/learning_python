#a variable delaring the number of people types there are.
types_of_people = 10
#a string to use the data from the variable above. Stored in a variable for later use.
x = f"There are {types_of_people} types of people"

#a varibale with the word binary in it.
binary = "binary"
#a variable with the word don't in it.
do_not = "don't"
#a string to use the data from the variables above. Stored in a variable for later use.
y = f"Those who know {binary} and those who {do_not}." #a string (or two) inside a string

#a statement to print the x variable defined on line 4.
print(x)
#a statement to print the y variable defined on line 11.
print(y)

#another pritn statement to print the variable x. This time with some added text.
print(f"I said: {x}.") #a string inside a string.
#another pritn statement to print the variable y. This time with some added text.
print(f"I also said: '{y}'") #a string inside a string.

#a boolean. To keep me on my toes.
hilarious = False
#a string with some curly brackets for later formatting.
joke_evaluation = "Isn't that joke so funny?! {}"
#a print statement using the boolena and string with formating directly above.
print(joke_evaluation.format(hilarious))

# a variable, w, containing a string.
w = "This is the left side of..."
# a varibale, e, containing further string text
e = "a string with a right side."

# a print statement using the two variables above and concatcenating them together.
print(w + e)

# There are three strings inside of strings in this exercise. The first posibility on line 4 is actually an integer inside of a string.
# The second potential is the print statement on line 28. This is a string with a boolean, not another string.
