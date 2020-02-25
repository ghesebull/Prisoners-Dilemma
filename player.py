import random

class Player:

    def __init__(self, ai):
        self.ai = ai
        self.points = []
        self.moves = []

    def makeMove(self):
        if self.ai:
            self.moves.append(random.randint(0, 1))
        else:
            result = input('Would you like to Cooperate (c) or Defect (d)? ').lower()
            while(len(result) == 0 or (result[0] != 'c' and result[0] != 'd')):
                print("ERROR: Invalid Input")
                result = input('Would you like to Cooperate (c) or Defect (d)? ').lower()
            move = 0
            if result == 'd':
                move = 1
            self.moves.append(move)

    def addPoint(self, other):
        if self.moves[-1] == 0:
            if other.moves[-1] == 0:
                self.points.append(1)
            else:
                self.points.append(0)
        else:
            if other.moves[-1] == 0:
                self.points.append(3)
            else:
                self.points.append(2)
