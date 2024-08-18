class Item:
    def __init__(self, name, price, rarity ):
        self.name = name
        self.price = price
        self.rarity = rarity
    def inspect(self):
        raise NotImplementedError("Subclasses must implement inspect()")


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

class Weapon(Armor):
    def __init__(self, name, price, rarity, type, defense, hp_bonus, attack_bonus, min_dmg, max_dmg):
        super().__init__(name,price, rarity, type, defense, hp_bonus, attack_bonus)
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
    def inspect(self):
        print(f"Name: {self.name}")
        print(f"Damage range: {self.min_dmg}-{self.max_dmg}")
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


class Items:
    def __init__(self):
        self.itemlist = [[Item("Fish",5, "common")],
                    [Weapon("Broadsword",10,"common","Weapon",0,0,0,2,4)]]
        

    def lookup(self, name):
        for row in self.itemlist:
            for element in row:
                if element.name is name:
                    return element
        
        print(f"{name} is not found in the item list")