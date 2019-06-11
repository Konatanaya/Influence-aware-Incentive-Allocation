from Approach import Approach
from DataProcessing.FileIO import FileIO
from UserAgent import UserAgent
import Plot.plot as plot
import random, datetime, math
import numpy as np
from threading import Thread
from multiprocessing import Pool
import os, time, random


class IPE(Approach):
    def __init__(self, budget, time, userList):
        Approach.__init__(self, budget, time)
        self.beta = 0.1
        self.userList = userList
        self.active_users = {}
        self.pre_active_users = {}
        self.status_last_time = 0.0
        self.matrix = self.init_matrix()

    def init_matrix(self):
        return np.zeros((len(self.userList), len(self.userList)))

    def simulate(self):
        for t in range(1, self.time + 1):
            print("round " + str(t), end=":")
            start = time.time()
            s = 0
            # p = Pool(1)
            self.budget = self.budget + self.per_budget
            for user in self.userList:
                if self.budget > 0.0:
                    self.calculate_reward(user)
                user.take_action()
                if user.action == 0:
                    self.budget -= user.reward
                    if self.budget < 0.0:
                        self.budget = 0.0
                    if t != 0:
                        # p.map(self.estimate_influence, (user, t))
                        # thr = Thread(target=self.estimate_influence, args=(user, t))
                        self.estimate_influence(user, t)
                        # thr.start()
                        # if user.id == len(self.userList) - 1:
                        # thr.join()
                        1

                    self.active_users[user] = user.action
                self.update_probability(user)
                user.reward = 0.0
                s += self.check_action(user.action)
            # p.close()
            # p.join()
            self.calculate_influence()
            self.pre_active_users = self.active_users
            self.active_users = {}
            self.status_last_time = s / len(self.userList)
            self.status.append(self.status_last_time)
            end = time.time()
            print(str(end - start) + "s")

    def calculate_influence(self):
        list = {}
        a = []
        sum = self.matrix.sum(axis=1)
        for user in self.userList:
            s = sum[user.id]
            user.idegree = s / len(self.userList)
            user.total = user.idegree + user.probability
            list[user] = user.total
        a = sorted(list.items(), key=lambda x: x[1], reverse=True)
        for x in a:
            list[x[0]] = x[0]
        self.userList = list

    def estimate_influence(self, user, time):
        for u in self.userList:
            x = self.matrix[u.id, user.id]
            if u.action_list[time - 1] == user.action:
                x = x + (math.exp(x - 1) - self.beta) * self.beta
            else:
                x = x - (math.exp(-x) - self.beta) * self.beta
            if x > 1.0:
                x = 1.0
            elif x < 0.0:
                x = 0.0
            self.matrix[u.id, user.id] = x
        # for u in self.pre_active_users:
        #     if u not in user.est_in_neighbors:
        #         user.est_in_neighbors[u] = 0.0
        #         u.est_out_neighbors[user] = 0.0
        # for u in user.est_in_neighbors:
        #     x = u.est_out_neighbors[user]
        #     if u.action_list[time - 1] == user.action:
        #         x = x + (math.exp(x - 1) - self.beta) * self.beta
        #     else:
        #         x = x - (math.exp(-x) - self.beta) * self.beta
        #     # print(x)
        #     if x > 1.0:
        #         x = 1.0
        #     elif x < 0.0:
        #         x = 0.0
        #     u.est_out_neighbors[user] = x
        #     user.est_in_neighbors[u] = x

    def update_probability(self, user):
        if user.action == 0:
            user.probability = user.probability / (user.probability + user.omega * (1 - user.probability))
        else:
            user.probability *= 0.8

    def calculate_reward(self, user):
        a = user.utility_difference ** self.status_last_time
        b = user.idegree ** self.status_last_time
        reward = (1 - user.probability) * (a + b)

        # print(str(a)+" "+str(b)+" "+str(reward))
        if reward > self.budget:
            reward = self.budget
        user.reward = reward
        # print(str(user.id)+":"+str(user.reward)+":"+str(user.utility_difference)+":"+str(self.status_last_time))
        # print(str(user.id)+":"+str(user.reward))


if __name__ == "__main__":
    io = FileIO('fb')
    io.import_user_data()
    userlist = io.userList
    start = datetime.datetime.now()
    ipe = IPE(10000, 10, userlist)
    print(ipe.matrix)
    b = np.arange(12).reshape(3, 4)
    print(b)
    c = b.sum(axis=1)
    print(c[0])
    # ipe.simulate()
    end = datetime.datetime.now()
    print("time: " + str((end - start).seconds) + "s")
    print(len(ipe.status))
    # plot.draw_plot(ipe.status)
