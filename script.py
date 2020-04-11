from food import Food
from drink import Drink

food1 = Food('Pasta', 5, 450)
food2 = Food('Pizza', 6, 400)
food3 = Food('Burger', 3, 350)

foods = [food1, food2, food3]

drink1 = Drink('Cappuccino', 3, 210)
drink2 = Drink('Mango Milkshake', 4, 350)
drink3 = Drink('Hard Rock Coffee', 4, 290)

drinks = [drink1, drink2, drink3]

print('Food')
index = 0
for food in foods:
    print(str(index) + '. ' + food.info())
    index += 1

print('Drinks')
index = 0
for drink in drinks:
    print(str(index) + '. ' + drink.info())
    index += 1

print('--------------------')

food_order = int(input('Enter food item number: '))
selected_food = foods[food_order]

drink_order = int(input('Enter drink item number: '))
selected_drink = drinks[drink_order]

# Take input from the console and assign it to the count variable
count = int(input('How many meals would you like to purchase? (10% off for 5 or more): '))

# Call the get_total_price method from selected_food and from selected_drink
result=selected_food.get_total_price(count)+selected_drink.get_total_price (count)

# Output 'Your total is $____'
print('Your total is $' +str(result))
