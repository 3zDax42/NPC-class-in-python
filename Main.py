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
        randnum = (random.randrange(0, 3))
        if randnum == 0:
            print("Hello, my name is", self.name, ".", self.dialogue)
        elif randnum == 1:
            print("Curently We're in the", self.position, "town.")
        elif randnum == 2:
            print("The roads between towns have been dangerous lately...")
    def give_quest(self):
        print(self.quest)
        self.quest_acepted = True
    def move(self):
        if self.quest_acepted == True:
            self.position = "Northwestern Coast"
            print("Thanks for escorting me to the Northwestern Coast town")
        else:
            print("I'm not ready to move yet")
        
traveling_npc = NPC("Jenifer", "I'm planning to move to the next town over soon, but I would like have a gaurd first.", "Could you gaurd me as I move to the next town over?", "West Coast")
traveling_npc.talk()
traveling_npc.talk()
traveling_npc.talk()
traveling_npc.move()
traveling_npc.give_quest()
traveling_npc.move()
