class robot:

    def __init__(self, name, age, character):
        self.name = name
        self.age = age
        self.character = character
    
    def introduction(self):
        print("I am {}, a robot.".format(self.name))
        print("I was made {} years ago.".format(self.age))
        print("These are my personality traits: {}.".format(self.character))

robot1 = robot("Alpha 331B", 3, ['playful', 'empathetic', 'curious'])
robot2 = robot("Synthesica 4", 6, ['intelligent', 'humble', 'independent'])

robot1.introduction()
print()
robot2.introduction()
