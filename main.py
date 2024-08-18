from prettytable import PrettyTable

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


class Item:
    def __init__(self, name, price, rarity ):
        self.name = name
        self.price = price
        self.rarity = rarity
    def inspect(self):
        raise NotImplementedError("Subclasses must implement inspect()")

class Weapon(Item):
    def __init__(self, name, price, rarity, min_dmg, max_dmg, speed):
        super().__init__(name,price, rarity)
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.speed = speed
    def inspect(self):
        print(f"Name: {self.name}")
        print(f"Damage range: {self.min_dmg}-{self.max_dmg}")
        print(f"Speed: {self.speed}")
        print(f"Rarity: {self.rarity}")
        print(f"Price: {self.price}")


class Armor(Item): # Types: Head, Chest, Legs
    def __init__(self, name, price, rarity, type, defense, hp_bonus, attack_bonus):
        super().__init__(name,price, rarity)
        self.type = type
        self.defense = defense
        self.hp_bonus = hp_bonus
        self.attack_bonus = attack_bonus
    def inspect(self):
        print(f"Name: {self.name}")
        print(f"Attack bonus: {self.attack_bonus}")
        print(f"Health bonus: {self.hp_bonus}")
        print(f"Defense bonus: {self.defense}")
        print(f"Rarity: {self.rarity}")
        print(f"Price: {self.price}")

class Potion(Item): # Healing, enemy damaging
    def __init__(self, name, price, rarity, effect_type, value):
        super().__init__(name, price, rarity)
        self.effect_type = effect_type
        self.value = value
    def inspect(self):
        print(f"Name: {self.name}")
        print(f"Effect type: {self.effect_type}")
        print(f"Effect value: {self.value}")
        print(f"Rarity: {self.rarity}")
        print(f"Price: {self.price}")



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

    def Interact(self,gear):
        while True:
            print("---Gear---")
            gear.print()
            print("---Inventory---")
            self.print()
            
            print("Actions: (1)Use/Equip (2)Inspect (3)Destroy (4)Exit")
            action = get_number_in_range(1, 4)
            if action == 4:
                return # exit Inventory
            
            if len(self.slots) > 0:
                print("---Which Item do you want to interact with?---")
                itemnum = get_number_in_range(1, len(self.slots))
                item = self.slots[itemnum -1]
                
                if action == 1: # todo (armor only for now)
                    if isinstance(item, Armor):
                        gear.equip(self, item)
                        self.remove(item)
                
                if action == 2: # print out attributes
                    item.inspect()
                    pressAnyKeyToContinue()

                if action == 3: # Remove item from inventory
                    self.remove(item)
                    pressAnyKeyToContinue()

            
            print("Inventory empty!")

        



class Gear:
    def __init__(self):
        self.dictionary = {'Head': None, 'Chest': None, 'Legs': None}

    def equip(self, inventory, armor):
        if self.dictionary[armor.type] is not None:
            inventory.add(self.dictionary["Head"])
        self.dictionary[armor.type] = armor
        print(f"{armor.name} has been equipped")


    def print(self):
        table = PrettyTable()
        table.field_names = ["Armor slot", "Name", "Def", "Att", "HP"]
        for key, value in self.dictionary.items():
            if value is None:
                table.add_row([key, "", "", "", ""])
            else:
                table.add_row([key, value.name, value.defense, value.attack_bonus, value.hp_bonus])
        print(table)


        


sword = Weapon("Broadsword", 20, "common", 1,5,2)
inventory = Inventory()
gear = Gear()

headpiece = Armor("Bronze medhelm", 20, "common", "Head", 2, 10, 0)
headpiece2 = Armor("Iron medhelm", 20, "common", "Head", 2, 10, 0)
chestpiece = Armor("Adamant platebody", 40, "rare", "Chest", 20, 30, 5)

inventory.add(sword)
inventory.add(sword)

gear.equip(inventory, headpiece)

gear.equip(inventory, headpiece2)
gear.equip(inventory, chestpiece)

inventory.Interact(gear)

