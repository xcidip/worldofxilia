from prettytable import PrettyTable
import items

def get_number_in_range(min_value, max_value):
  while True:
    try:
      user_input = input(f"Enter a number between {min_value} and {max_value}: ")
      number = int(user_input)
      if min_value <= number <= max_value:
        return number
      else:
        print(f"Please enter a number between {min_value} and {max_value}.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def pressAnyKeyToContinue():
    input("Press any key to continue...")




class Inventory:
    def __init__(self):
        self.slots = []

    def add(self, item: object):
        self.slots.append(item)
        print(f"{item.name} has been added to inventory")

    def remove(self, item:object):
        if item in self.slots:
            self.slots.remove(item)
            print(f"{item.name} has been removed from inventory")
            return
        print(f"\"{item.name}\" hasnt been found in the inventory")

    def removeByName(self, name):
        i = 0
        for item in self.slots:
            if item.name == name:
                del self.slots[i]
                print(f"{name} has been removed from inventory")
                return
            i = i + 1
        print(f"\"{name}\" hasnt been found in the inventory")
    
    def print(self):
        table = PrettyTable()
        table.field_names = ["Item name", "Price", "Rarity"]
        for item in self.slots:
            table.add_row([item.name, item.price, item.rarity])
        print(table)


        
class Gear:
    def __init__(self):
        self.dictionary = {'Head': None, 'Chest': None, 'Legs': None, 'Weapon': None}

    def equip(self, inventory, item):
        if self.dictionary[item.type] is not None:
            inventory.add(self.dictionary[item.type])
        self.dictionary[item.type] = item
        print(f"{item.name} has been equipped")


    def print(self):
        table = PrettyTable()
        table.field_names = ["Armor slot", "Name","Rarity", "Def", "Att", "HP", "MinDmg", "MaxDmg", "Speed"]
        for key, value in self.dictionary.items():
            if value is None:
                table.add_row([key, "", "","","", "", "", "", ""])
            else:
                if isinstance(value, Weapon):
                    table.add_row([key, value.name, value.rarity, value.defense, value.attack_bonus, value.hp_bonus, value.min_dmg, value.max_dmg, value.speed])
                else:
                    table.add_row([key, value.name, value.rarity, value.defense, value.attack_bonus, value.hp_bonus, "", "", ""])
                
        print(table)


class Player:
    def __init__(self):
        self.name = ""
        self.inventory = Inventory()
        self.gear = Gear()
        self.hp = 100
        self.defense = 0
        self.min_damage = 1
        self.max_damage = 1
        self.speed = 1
    

    def load_stats(self): # defense, attack_bonus, hp_bonus, min_dmg, max_dmg, speed
        self.hp = 100
        self.min_damage = 1
        self.max_damage = 1
        self.defense = 0
        self.speed = 0
        for key, value in self.gear.dictionary.items():
            if value is not None:
                self.defense += value.defense
                self.min_damage += value.attack_bonus
                self.max_damage += value.attack_bonus

                self.hp += value.hp_bonus
                
                if isinstance(value, Weapon):
                    self.min_damage += value.min_dmg -1
                    self.max_damage += value.max_dmg -1
                    self.speed += value.speed

    def print_stats(self):
        table = PrettyTable()
        table.field_names = ["Player","HP","Defense", "Damage", "Speed"]
        table.add_row([self.name,self.hp, self.defense, f"{self.min_damage}-{self.max_damage}", self.speed])
        print(table)

    def Interact(self):
        while True:
            self.load_stats()

            print("---Stats---")
            self.print_stats()
            print("---Gear---")
            self.gear.print()
            print("---Inventory---")
            self.inventory.print()
            
            print("Actions: (1)Use/Equip (2)Inspect (3)Destroy (4)Exit")
            action = get_number_in_range(1, 4)
            if action == 4:
                return # exit Inventory
            
            if len(self.inventory.slots) > 0:
                print("---Which Item do you want to interact with?---")
                itemnum = get_number_in_range(1, len(self.inventory.slots))
                item = self.inventory.slots[itemnum -1]
                
                if action == 1: # todo (armor only for now)
                    if isinstance(item, Armor):
                        self.gear.equip(self.inventory, item)
                        self.inventory.remove(item)
                
                if action == 2: # print out attributes
                    item.inspect()
                    pressAnyKeyToContinue()

                if action == 3: # Remove item from inventory
                    self.inventory.remove(item)
                    pressAnyKeyToContinue()

            
            print("Inventory empty!")


player = Player()
player.name = input("Whats your characters name: ")


sword = Weapon("Broadsword", 20, "common", "Weapon",0,0,1,1,5,2)
headpiece = Armor("Bronze medhelm", 20, "common", "Head", 2, 10, 0)
headpiece2 = Armor("Iron medhelm", 20, "common", "Head", 2, 10, 0)
chestpiece = Armor("Adamant platebody", 40, "rare", "Chest", 20, 30, 5)


player.inventory.add(sword)
player.inventory.add(headpiece)
player.inventory.add(headpiece2)
player.inventory.add(chestpiece)

player.Interact()

