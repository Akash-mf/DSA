#Correcting bugs in a dictionary
#You have been given a program that is supposed to iterate over the dishes of a menu,
# printing the name and its value. Correct the mistake in the for loop. Correct the mistake in the print() function.

my_menu = {
  'lasagna': 14.75,
  'moussaka': 21.15,
  'sushi': 16.05,
  'paella': 21,
  'samosas': 14
}

# Correct the mistake
for key, value in my_menu.items():
  # Correct the mistake
  print(f"The price of the {key} is {value}.")