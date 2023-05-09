from coffee_data import MENU, resources

def process_coins():
  print("Please insert coins.")
  total = int(input("How many quarters?: ")) * 0.25
  total += int(input("How many dimes?: ")) * 0.10
  total += int(input("How many nickles?: ")) * 0.05
  total += int(input("How many pennies?: ")) * 0.01
  return total


def check_price(flavor, money):
  coffee = MENU[flavor]
  cost = coffee['cost']
  if money < cost:
    print("Sorry that's not enough money. Money refunded.")

def coffee_machine():
  coffee_left = resources['coffee']
  water_left = resources['water']
  milk_left = resources['milk']
  profit = 0

  is_on = True

  while is_on:
    flavor = input("  What would you like? (espresso/latte/cappuccino): ").lower()
    if flavor == 'off':
      is_on = False
    elif flavor == 'report':
      print(f"Coffee: ${coffee_left}")
      print(f"Water: ${water_left}")
      print(f"Milk: ${milk_left}")
      print(f"Money: ${profit}")
    else:
      coffee = MENU[flavor]
      coffee_ingredients = coffee['ingredients']

      ingredient_coffee = coffee_ingredients['coffee']
      ingredient_water = coffee_ingredients['water']
      ingredient_milk = 0
      if flavor != 'espresso':
        ingredient_milk = coffee_ingredients['milk']

      if (coffee_left - ingredient_coffee) < 0:
        print(" Sorry there is not enough coffee")
      elif (water_left -ingredient_water) < 0:
        print(" Sorry there is not enough water")
      elif (milk_left - ingredient_milk) < 0:
        print(" Sorry there is not enough milk")
      else:
        coffee_left -= ingredient_coffee
        water_left -= ingredient_water
        milk_left -= ingredient_milk
        
        cost = coffee['cost']
        payment = process_coins()
        profit += payment
        check_price(flavor, payment)

        change = round(payment - cost, 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {flavor} ☕️. Enjoy!")

coffee_machine()