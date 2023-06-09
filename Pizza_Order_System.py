import csv
import datetime

with open("menu.txt", "w") as menu:
    menu.write("* Please Choose a Pizza Base:\n 1: Classic Pizza\n 2: Margherita Pizza\n 3: Turkish Pizza\n 4: Regular Pizza\n\n* and sauce of your choice:\n 11: Olive\n 12: Mushroom\n 13: Goat Cheese\n 14: Meat\n 15: Onion\n 16: Corn\n\n* Thank you!\"\n")

with open("menu.txt", "r") as menu:
    print(menu.read())

##/////////////////////////////////////////////////////////////////////////////

class Pizza:  
  def __init__(self):
    self.cost=0
    self.description="UPizza"

  def get_description(self):
    return self.description

  def get_cost(self):
    return self.cost


class Classic(Pizza):
  def __init__(self):
    self.description = "Classic Pizza "
    self.cost = 120
  
  def get_description(self):
    return super().get_description()
  def get_cost(self):
    return super().get_cost()


class Margherita(Pizza):
    def __init__(self):
        self.description = "Margherita Pizza "
        self.cost = 110

    def get_cost(self):
        return super().get_cost()
    def get_description(self):
        return super().get_description()


class Turkish(Pizza):
    def __init__(self):
        self.description = "Turkish Pizza "
        self.cost = 125

    def get_cost(self):
        return super().get_cost()
    def get_description(self):
        return super().get_description()


class Regular(Pizza):
    def __init__(self):
        self.description = "Regular Pizza "
        self.cost = 105

    def get_cost(self):
        return super().get_cost()
    def get_description(self):
        return super().get_description()

##/////////////////////////////////////////////////////////////////////////////
class Decorator(Pizza):
    def __init__(self, component):
        self.component = component
        
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        
        return self.component.get_description() + ' ' + Pizza.get_description(self)


class OliveSauce(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Olive"
        self.cost = 6


class MushroomSauce(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Mushroom"
        self.cost = 6


class GoatCheeseSauce(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Goat Cheese"
        self.cost = 8


class MeatSauce(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Meat"
        self.cost = 10


class OnionSauce(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Onion"
        self.cost = 6


class CornSauce(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Corn"
        self.cost = 6

##/////////////////////////////////////////////////////////////////////////////
        
while True:
    pizza_choice = input("Please Choose a Pizza Base (1 to 4): ")

    if pizza_choice == "1":
        pizza = Classic()
        break
    elif pizza_choice == "2":
        pizza = Margherita()
        break
    elif pizza_choice == "3":
        pizza = Turkish()
        break
    elif pizza_choice == "4":
        pizza = Regular()
        break
    else:
        print("Invalid choice. Please try again.")

sos_list = []

while True:
    sos_choice = input("Please Choose a Pizza Sauce (11 to 16): ")

    if sos_choice == "11":
        sos = OliveSauce(pizza)
        sos_list.append(11)
        break
    elif sos_choice == "12":
        sos = MushroomSauce(pizza)
        sos_list.append(12)
        break
    elif sos_choice == "13":
        sos = GoatCheeseSauce(pizza)
        sos_list.append(13)
        break
    elif sos_choice == "14":
        sos = MeatSauce(pizza)
        sos_list.append(14)
        break
    elif sos_choice == "15":
        sos = OnionSauce(pizza)
        sos_list.append(15)
        break
    elif sos_choice == "16":
        sos = CornSauce(pizza)
        sos_list.append(16)
        break
    else:
        print("Invalid choice. Please try again.")

sos_cost = 0
sos_description = ""

for element in sos_list:
    if element == 11:
        sos_cost += OliveSauce(pizza).cost
        sos_description += " " + OliveSauce(pizza).description
    elif element == 12:
        sos_cost += MushroomSauce(pizza).cost
        sos_description += " " + MushroomSauce(pizza).description
    elif element == 13:
        sos_cost += GoatCheeseSauce(pizza).cost
        sos_description += " " + GoatCheeseSauce(pizza).description
    elif element == 14:
        sos_cost += MeatSauce(pizza).cost
        sos_description += " " + MeatSauce(pizza).description
    elif element == 15:
        sos_cost += OnionSauce(pizza).cost
        sos_description += " " + OnionSauce(pizza).description
    elif element == 16:
        sos_cost += CornSauce(pizza).cost
        sos_description += " " + CornSauce(pizza).description
        
##/////////////////////////////////////////////////////////////////////////////

total_cost = pizza.get_cost() + sos_cost
description = pizza.get_description() + "and" + sos_description

print("Selected Pizza: {}".format(pizza.__class__.__name__))
print("Selected Sauce: {}".format(sos_description))
print("Total cost: {} ₺".format(total_cost))
print("Order description:  {} " .format(description))

if input("Confirm your order? (Yes/No)\n").lower() == "yes":
    name = input("Name: ")
    tc_no = input("Identity Number: ")
    card_number = input("Card Number: ")
    card_pin = input("Card Password: ")
    order = {
        "Username": name,
        "TC": tc_no,
        "Card Number": card_number,
        "Order Description": description,
        "Order Time": datetime.datetime.now(),
        "Card Pin": card_pin
    }
    with open('Orders_Database.csv', mode='a', newline='') as file:
        fieldnames = ['Username', 'TC', 'Card Number', 'Order Description', 'Order Time', 'Card Pin']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(order)
    print("Order placed successfully!")

