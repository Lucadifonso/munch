'''
Munch App MVP
v0.1
The purpose of Munch is to prodice a dinner menu from favourite dishes,
and produce a shopping list of ingredients if required.
'''

# ----- IMPORTS ------
from random import choice

# A. ----- FUNCTION ------
# A.1 Choose dishes


def ChooseDishes(days):
    while len(MyMenu) < int(days): #3. Repeat until we have required number of dishes in MyMenu
                                    # I HAD TO MAD 'DAYS' INTO 'int(days) BECAUSE I CANNOT COMPARE INT with STR
        ChosenDish = choice(FoodWeLike) #1. Choose random dish from FoodWeLike
        if ChosenDish not in MyMenu: #2. Check dish not been chosen. If not add to MyMenu
            MyMenu.append(ChosenDish)

    print("Done! Here is your menu...")
    print()
    for dish in MyMenu:
        print(dish)
    print()
    print("Out of all these meals, my favourite dish has to be " + choice(MyMenu))

    
# A.2 Shopping list function

def BuildShoppingList():
    MyShoppingList = [] #local in scope so has to be printed inside the function and cannot be print out of it
    if "Pizza" in MyMenu:
        MyShoppingList.append(Pizza)
    if "Pasta" in MyMenu:
        MyShoppingList.append(Pasta)
    if "Potatoes" in MyMenu:
        MyShoppingList.append(Potatoes)
    if "Avocado Toast" in MyMenu:
        MyShoppingList.append(AvocadoToast)
    if "Fish and Chips" in MyMenu:
        MyShoppingList.append(FishAndChips)
    if "Wrap" in MyMenu:
        MyShoppingList.append(Wrap)
    if "Arrosticini" in MyMenu:
        MyShoppingList.append(Arrosticini)
    print ()
    print ("Those are all the ingredients you will need")
    print ()
    for dish in MyShoppingList:
        for ingredient in dish:
            print (ingredient)
    print("Voila! Bon apetit...")
    

# B. ------ Lists ------

FoodWeLike = ["Pizza", "Pasta", "Potatoes", "Avocado Toast", "Fish and Chips", "Wrap", "Arrosticini"]

Pizza = ["Pizza base" , "Tomato Sauce","Cheese","Pepperoni","Chillis"]
Pasta = ["Pasta", "Olive Oil", "Parmesan"]
Potatoes = ["Potatoes","Salami","Melted Cheese"]
AvocadoToast = ["Avocado","Toast","Salt","Pepper"]
FishAndChips = ["Cod","Fries","Frying Oil"]
Wrap = ["Tacos","Guacamole","Fajitas"]
Arrosticini = ["Lamb","Salt"]

MyMenu = []


# 1. How many days to plan for?

print("Hello! I am Munch and I will help you plan your dinner menu")

answer = input("How many days would you like me to plan? ")

print("Ok, I am going to plan ", answer, "dinner(s) from your favourite meals list.")


# 2. Choose dishes

ChooseDishes(answer)


# 3. Build shopping list

answer = input("Would you like a shopping list for these dishes? Enter 'y' or 'n'")

if answer == "y":
    print()
    BuildShoppingList()

else:
   print("You got it! Bye for now!")
