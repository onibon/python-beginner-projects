import random

meals = [
    "Rice and chicken",
    "Spaghetti and sauce",
    "Pounded yam and egusi",
    "Beans and plantain",
    "Fried rice",
    "Noodles and egg",
    "Amala and ewedu"
]

print("Welcome to What to Eat!")
mood = input("How are you feeling today? (press Enter to skip): ").lower()

if mood:
    print("Here’s a meal you might enjoy based on your mood:")
    print(random.choice(meals))
else:
    print("Can’t decide? Here's a random suggestion:")
    print(random.choice(meals))
