name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it excatly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

#calcualtion to convert inches to centimeters for height
centimeters = height * 2.54
#calculation to convert lbs to kg
kg = weight / 2.205
print(f"{name}'s height in cm is {centimeters} and his weight in kgs is {kg}.")
 
