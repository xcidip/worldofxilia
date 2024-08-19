from pickle import TUPLE

import utility
import items
from prettytable import PrettyTable

class Inventory:
    def __init__(self, inventory_spaces):
        self.slots = []
        self.inventory_spaces = inventory_spaces

    def add(self, item_list: list | items.Item):
        if isinstance(item_list, list):
            if self.how_many_spaces_left() > len(item_list):
                for single_item in item_list:
                    self.slots.append(single_item)
                    print(f"{single_item.name} has been added to inventory")
                    return
            print("Not enough space in inventory!")

        if self.how_many_spaces_left() > 0:
            self.slots.append(item_list)
            print(f"{item_list.name} has been added to inventory")
        print("Not enough space in inventory!")
        return

    def how_many_spaces_left(self):
        return self.inventory_spaces - len(self.slots)

    def remove(self, item_list:object):
        if isinstance(item_list, list):
            for i in item_list:
                if i not in self.slots:
                    print(f"\"{item_list.name}\" hasnt been found in the inventory")
                self.slots.remove(i)
                print(f"{i.name} has been removed from inventory")
            return

        if item_list in self.slots:
            self.slots.remove(item_list)
            print(f"{item_list.name} has been removed from inventory")
            return
        print(f"\"{item_list.name}\" hasnt been found in the inventory")

    def remove_by_name(self, name):
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

    def multiple_item_check(self, num_of_wanted_items, what_item):
        num_of_items = 0
        for item in self.slots:
            if item is what_item:
                num_of_items += 1
            if num_of_items == num_of_wanted_items:
                return True
            
        print(f"Not enough {what_item}")
        return False


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
        table.field_names = ["Armor slot", "Name","Rarity", "Def", "Att", "HP", "MinDmg", "MaxDmg"]
        for key, value in self.dictionary.items():
            if value is None:
                table.add_row([key, "", "","","", "", "", ""])
            else:
                if isinstance(value, items.Weapon):
                    table.add_row([key, value.name, value.rarity, value.defense, value.attack_bonus, value.hp_bonus, value.min_dmg, value.max_dmg])
                elif isinstance(value, items.Armor):
                    table.add_row([key, value.name, value.rarity, value.defense, value.attack_bonus, value.hp_bonus, "", ""])
                else:
                    raise "Something weird is in your gear that shouldn't be there"

        print(table)


class Character:
    def __init__(self, name, hp, defense, min_damage, max_damage):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.min_damage = min_damage
        self.max_damage = max_damage
    
    def take_damage(self, amount):
        self.hp -= amount
        self.is_dead()

    def is_dead(self):
        if self.hp > 0:
            return False
        print(f"{self.name} died")
        return True
        
class Enemy(Character):
    def __init__(self, name, hp, defense, min_damage, max_damage):
        super().__init__(name, hp, defense, min_damage, max_damage)

class Enemies:
    def __init__(self):
        self.list = [[Enemy("Sheep",20,1,1,2)]]
        

    def lookup(self, name):
        for row in self.list:
            for element in row:
                if element.name is name:
                    return element
        
        print(f"{name} is not found in the enemy list")


class Player:
    def __init__(self, quest_log):
        self.defense = None
        self.max_damage = None
        self.min_damage = None
        self.hp = None
        self.name = None

        self.inventory_spaces = 28
        self.account_status = "Normal" # Normal / Ironman / Hardcore Ironman / Ultimate Ironman

        self.inventory = Inventory(self.inventory_spaces)
        self.gear = Gear()
        self.load_stats()
        self.quest_log = quest_log
        self.kill_stats: list[[int, Enemy]] = [()]
        self.death_counter = 0

    def load_stats(self): # defense, attack_bonus, hp_bonus, min_dmg, max_dmg
        self.hp = 100
        self.min_damage = 1
        self.max_damage = 1
        self.defense = 0
        for key, value in self.gear.dictionary.items():
            if value is not None:
                self.defense += value.defense
                self.min_damage += value.attack_bonus
                self.max_damage += value.attack_bonus

                self.hp += value.hp_bonus
                
                if isinstance(value, items.Weapon):
                    self.min_damage += value.min_dmg -1
                    self.max_damage += value.max_dmg -1

    def print_stats(self):
        table = PrettyTable()
        table.field_names = ["Player","HP","Defense", "Damage"]
        table.add_row([self.name,self.hp, self.defense, f"{self.min_damage}-{self.max_damage}"])
        print(table)

    def interact(self):
        while True:
            self.load_stats()

            print("---Stats---")
            self.print_stats()
            print("---Gear---")
            self.gear.print()
            print("---Inventory---")
            self.inventory.print()

            action = utility.ask_and_get_number_in_range("Actions: (1)Use/Equip (2)Inspect (3)Destroy (4)Exit",1, 4)
            if action == 4:
                return # exit Inventory
            
            if len(self.inventory.slots) > 0:
                itemnum = utility.ask_and_get_number_in_range("---Which Item do you want to interact with?---",1, len(self.inventory.slots))
                item = self.inventory.slots[itemnum -1]
                
                if action == 1: # todo (armor only for now)
                    if isinstance(item, items.Armor):
                        self.gear.equip(self.inventory, item)
                        self.inventory.remove(item)
                
                if action == 2: # print out attributes
                    item.inspect()
                    utility.press_any_key_to_continue()

                if action == 3: # Remove item from inventory
                    self.inventory.remove(item)
                    utility.press_any_key_to_continue()

            
            print("Inventory empty!")