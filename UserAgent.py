
from DataProcessing import FileIO

class Action:
    def __init__(self, id, preference, benefit):
        self.id = id
        self.preference = preference
        self.benefit = benefit

class UserAgent:
    def __init__(self, id):
        self.id = id
        self.preference = []
        self.action = 0
        self.inNeighbors = {}
        self.outNeighbors = {}

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)



if __name__ == '__main__':
    a = set()
    u1 = UserAgent(1)
    u2 = UserAgent(1)
    a.add(u1)
    a.add(u2)
    if u1 not in a:
        print("!")
    print(a)