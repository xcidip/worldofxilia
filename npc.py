from typing import Callable, Optional

import utility


class DialogNode:
    def __init__(self, text: str, script_responses: list[[str, Callable]] = None, dialog_responses: list[[str, 'DialogNode']] = None):
        self.text = text
        self.script_responses = script_responses or []
        self.dialog_responses = dialog_responses or []

class Npc:
    def __init__(self,name, dialog_node: DialogNode):
        self.dialog = dialog_node
        self.name = name

    def talk(self, player):
        while True:
            dialog = self.dialog
            while True:
                print(f"{self.name}: {dialog.text}")

                options = []
                for i, (text, _) in enumerate(dialog.script_responses + dialog.dialog_responses):
                    options.append(f"({i + 1}) {text}")

                if not options: # End if no dialogue is available
                    break

                print(*options, sep='\n') # Print every option with simple command

                choice = int(input("Choose an option: ")) - 1
                if 0 <= choice < len(dialog.script_responses):
                    dialog.script_responses[choice][1](player)
                    break
                elif 0 <= choice < len(dialog.script_responses) + len(dialog.dialog_responses):
                    dialog = dialog.dialog_responses[choice - len(dialog.script_responses)][1]
                else:
                    print("Invalid choice")

            if utility.ask_and_get_number_in_range("\nTalk again? (1)No (2) Yes",1,2) == 1: break


class NpcList:
    def __init__(self):
        self.list: list[Npc] = [
            Npc("Norwyn", DialogNode(
                text="Hey there, I am Norwyn and I will guide you through the basics of how to survive here!",
                dialog_responses=[
                        ("Tell me about this place.", DialogNode(text="Well, this place is just an ordinary island with few things going on. You can learn skills to start your journey on the planet xperia and learn basic things like killing enemies and crafting your first weapon and armor")),
                        ("What am I doing here?", DialogNode(text="Looks like you just spawned in, well welcome to the planet xperia it is an RPG world filled with creatures, quests and most of all grind. jk"))],
                script_responses=[
                    ("Lets start!", lambda player: player.quest_log.start_quest("Sheep killer")),
                    ("Goodbye!", lambda player: print("Not so quickly dude!")),
                ],
                ),
            )
        ]

    def lookup(self, name):
        for npc in self.list:
            if npc.name == name:
                return npc