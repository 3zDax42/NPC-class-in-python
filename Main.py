import random
random.randrange(0, 5)
class NPC:
    def __init__(self, name, dialogue, quest, position):
        self.name = name
        self.dialogue = dialogue
        self.quest = quest
        self.quest_acepted = False
        self.position = position
    def talk(self):
        print("Hello, my name is", self.name, ". ", self.dialogue)
    def give_quest(self):
        print(self.quest)
        self.quest_acepted = True
    def move(self):
        if self.quest_acepted == True:
            self.position = "Northwestern Coast"
        else:
            print("I'm not ready to move yet")
        
moving_npc = NPC("Jenifer", "I'm planning to move to the next town over soon, but I would like have a gaurd first.", "Could you gaurd me as I move to the next town over?", "West Coast")
