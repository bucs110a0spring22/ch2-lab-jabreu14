import random

#Part A
weeks = 16
classes = 5
tuition = 6000
classes_per_week = 3
print(classes_per_week, type(classes_per_week))
cost_per_week = ((tuition / classes) / weeks)
print(cost_per_week, type(cost_per_week))
print("Cost per week:", cost_per_week)
cost_per_class = ((cost_per_week)/(classes_per_week))
print(cost_per_class, type(cost_per_class))
print("Hello, your cost per class is:", cost_per_class, "dollars")

#Part B
my_list = [2, "Computer", 3.7, "Pizza", "Bagel"]
random_selection = random.choice(my_list)
print(random_selection)