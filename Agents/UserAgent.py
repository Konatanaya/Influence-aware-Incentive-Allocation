from DataProcessing import FileIO
import random, math, numpy as np
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
        self.action = 1
        self.action_list = []
        self.action_list.append(self.action)
        self.est_out_neighbors = {}
        self.est_in_neighbors = {}

        self.probability = 0.5
        self.omega = 0.0
        self.utility_difference = 0.0
        self.idegree = 0.0
        self.total = self.idegree + self.probability

    def reset(self):
        self.reward = 0.0
        self.action_list = []
        self.action = 1
        self.action_list.append(self.action)
        self.est_out_neighbors = {}
        self.est_in_neighbors = {}

        self.probability = 0.5
        self.idegree = 0.0
        self.total = self.idegree + self.probability

    def assign_preference(self, arr):
        self.preference = arr
        self.omega = arr[0] / sum(self.preference)
        self.utility_difference = self.preference[np.argmax(self.preference)] - self.preference[0]

    def init_preference(self, num):
        for i in range(num):
            self.preference.append(random.random())
        if random.random() < 0.7:
            self.preference[0] = 0.0

    def take_action(self):
        self.action = np.argmax(self.update_preference())
        self.action_list.append(self.action)

    def update_preference(self):
        new_preference = [0.0] * (len(self.preference))
        influence = self.calculate_influence()
        for i in range(len(self.preference)):
            new_preference[i] = self.preference[i] + influence[i]
        new_preference[0] += self.reward
        return new_preference

    def calculate_influence(self):
        influence = [0.0] * (len(self.preference))
        for user in self.in_neighbors:
            index = user.action_list[len(self.action_list) - 1]
            influence[index] += self.in_neighbors[user]
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
