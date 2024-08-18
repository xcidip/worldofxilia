import items
import characters
import quests

item_list = items.Items()
enemy_list = characters.Enemies()

quest_log = quests.QuestLog(item_list, enemy_list)

player = characters.Player(item_list,quest_log)
player.name = input("Whats your characters name: ")


sword = items.Weapon("Broadsword", 20, "common", "Weapon",0,0,1,1,5)
headpiece = items.Armor("Bronze medhelm", 20, "common", "Head", 2, 10, 0)
headpiece2 = items.Armor("Iron medhelm", 20, "common", "Head", 2, 10, 0)
chestpiece = items.Armor("Adamant platebody", 40, "rare", "Chest", 20, 30, 5)



player.inventory.add(sword)
player.inventory.add(headpiece)
player.inventory.add(headpiece2)
player.inventory.add(chestpiece)

player.Interact()

player.quest_log.print()
