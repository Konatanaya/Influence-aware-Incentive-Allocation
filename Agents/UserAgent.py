from DataProcessing import FileIO
import random, math, numpy
import matplotlib


class UserAgent:
    def __init__(self, ID):
        self.id = ID
        self.preference = []
        self.action = 0
        self.in_neighbors = {}
        self.out_neighbors = {}
        self.remaining_influence = 1.0
        self.reward = 0.0

    def init_preference(self, num):
        for i in range(num):
            self.preference.append(random.random())

    def take_action(self):
        self.action = numpy.argmax(self.updatePreference())

    def update_preference(self):
        new_preference = [0.0] * (len(self.preference))
        influence = self.calculate_influence()
        for i in range(len(self.preference)):
            new_preference[i] = self.preference[i] + influence[i]
        new_preference[0] += self.reward
        return new_preference

    def calculate_influence(self):
        influence = [0.0] * (len(self.preference))
        for key in self.inNeighbors:
            influence[key.action] += self.inNeighbors.get(key)
        return influence

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)


if __name__ == '__main__':

    s1 = {"a": 1, "b": 2}
    print(s1.values())
    for i in s1.values():
        print(i)
