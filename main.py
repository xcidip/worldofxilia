import items
import characters
import quests
import utility
from npc import NpcList


# Setup (player, item/enemy lists)
item_list = items.Items()
enemy_list = characters.Enemies()

quest_log = quests.QuestLog(item_list, enemy_list)
player = characters.Player(quest_log)
player.name = input("Whats your characters name: ")
player.account_status = utility.ask_and_get_number_in_range("Choose your account status: (1)Normal (2)Ironman (3)Ultraman (4)Crazyman",1,4)




#player.interact()

#player.quest_log.print()

npc_list = NpcList()

npc1 = npc_list.lookup("Norwyn")

npc1.talk(player)



