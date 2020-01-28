#Below is the naming of variables required in the car calculations.
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
#Below are the car calculations allowing us to see how many cars are avaiable for the day.
#The calculations use the varables defined above.
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#The below are strings so that the interpretor prints out the calculations above. Without them the
#sums would be completed, but no results would be avaiable. 
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

#When Zed originally wrote the above program he had an error on line 8. The error relates to
#the naming of a varaible. It's stating an name is not defined. Most likely he misspelt the variable.

#Study drills:
#1: The space_in_a_car varable was a float number (I changed it). It made no difference to the code.
#
