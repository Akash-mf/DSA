#You are writing a program that iterates over the following nested dictionary to determine
#if the dishes need to be served cold or hot. Can you complete the program so that it outputs the following?

#Sushi is best served cold.
#Paella is best served hot.
#Samosa is best served hot.
#Gazpacho is best served cold.

my_menu = {
    'sushi': {
        'price': 19.25,
        'best_served': 'cold'
    },
    'paella': {
        'price': 15,
        'best_served': 'hot'
    },
    'samosa': {
        'price': 14,
        'best_served': 'hot'
    },
    'gazpacho': {
        'price': 8,
        'best_served': 'cold'
    }
}

# Iterate through the menu items and print how they are best served
for dish, values in my_menu.items():
    print(f"{dish.title()} is best served {values['best_served']}.")
