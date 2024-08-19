import items
import characters
import quests
import utility
from fighting import start_fight
from npc import NpcList


# Setup (player, item/enemy lists)
item_list = items.Items()
enemy_list = characters.Enemies()

quest_log = quests.QuestLog(item_list, enemy_list)
player = characters.Player(quest_log,"Player1",100,0,1,1)
#player.account_status = utility.ask_and_get_number_in_range("Choose your account status: (1)Normal (2)Ironman (3)Ultraman (4)Crazyman",1,4)




#player.interact()

#player.quest_log.print()

npc_list = NpcList()

npc1 = npc_list.lookup("Norwyn")

#npc1.talk(player)

enemy1 = enemy_list.lookup("Sheep")

start_fight("number_game",player, enemy1)

