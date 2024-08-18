import items
import characters
from prettytable import PrettyTable

# FETCH item quest, KILL number of enemies quest, TALK to someone quest
class Quest:
    def __init__(self, name, reward, quest_giver_npc, hint):
        self.name = name
        self.reward = reward
        self.quest_giver_npc = quest_giver_npc
        self.state = "Hidden" # Hidden / Started / Completed
        self.hint = hint
    
    def start_quest(self):
        self.state = "Started"    
    
    def complete_quest(self, inventory): # Give reward to player
        self.state = "Completed"
        inventory.add(self.reward)
    
    def check_if_tasks_met(self, inventory):
        raise("Checking quest completion not implemented")

class FetchQuest(Quest):
    def __init__(self, name, reward, quest_giver_npc, items_to_fetch: list[(int, items.Item)], hint):
        super().__init__(name, reward, quest_giver_npc, hint)
        self.items_to_fetch = items_to_fetch
    
    def check_if_tasks_met(self, inventory):
        everything_done = True
        for item in self.items_to_fetch:
            if inventory.multiple_item_check(item[0], item[1]) is not True:
                everything_done = False
        if everything_done:
            return True
        print(f"You dont have the required items in the inventory for {self.name}")
        return False
    
class KillQuest(Quest):
    def __init__(self, name, reward, quest_giver_npc, enemies_to_kill: list[(int, characters.Enemy)], hint):
        super().__init__(name, reward, quest_giver_npc, hint)
        self.enemies_to_kill = enemies_to_kill
        self.enemies_killed = []
        for t in self.enemies_to_kill:
            new_tuple = (0,) + t[1:]
            self.enemies_killed.append(new_tuple)

    def check_if_tasks_met(self):
        everything_done = True
        index = 0
        for enemy in len(self.enemies_to_kill):
            if (self.enemies_killed[index] < self.enemies_to_kill[index]):
                everything_done = False   
        if everything_done:
            return True
        print(f"You havent killed enough enemies required for the completion of {self.name}")
        return False
    
class TalkQuest(Quest):
    def __init__(self, name, reward, quest_giver_npc, npcs_to_talk_to: list[(bool, characters.Npc)], hint):
        super().__init__(name, reward, quest_giver_npc, hint)
        self.npcs_to_talk_to = npcs_to_talk_to
    
    def check_if_tasks_met(self):
        everything_done = True
        for tuple in self.npcs_to_talk_to:
            if tuple[0] == False:
                everything_done = False
        if everything_done:
            return True
        print(f"You havent talked to all the NPCs from {self.name}")
        return False

class QuestLog:
    def __init__(self, item_list, enemy_list):
        self.quest_log = [KillQuest("Sheep killer", [item_list.lookup("Fish"), item_list.lookup("Fish")],"Swen", [(5, enemy_list.lookup("Sheep"))],"Go to the sheeps and kill them")]

    def print(self):
        table = PrettyTable()
        table.field_names = ["Quest name", "From", "Bring items", "Kill enemies", "Talk to"]
        for quest in self.quest_log:
            if quest.state == "Started":
                bring = ""
                kill = ""
                talk = ""

                if isinstance(quest, FetchQuest):
                    for each_item in quest.items_to_fetch:
                        bring += f"{each_item[0]}x {each_item[1]} "
                if isinstance(quest, KillQuest):
                    for index in range(len(quest.enemies_to_kill)):
                        kill += f"{quest.enemies_killed[index][0]}/{quest.enemies_to_kill[index][0]} {quest.enemies_to_kill[index][1].name}"
                if isinstance(quest, TalkQuest):
                    for each_npc in quest.npcs_to_talk_to:
                        talk += f"{each_npc[1]} ({each_npc[0]}) "

                table.add_row([quest.name, quest.quest_giver_npc, bring, kill, talk])
        print(table)