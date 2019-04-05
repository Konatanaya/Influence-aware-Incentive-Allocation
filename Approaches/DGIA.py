from IPE import IPE
import random, datetime, math, time

class DGIA(IPE):
    def __init__(self, budget, time, userList):
        IPE.__init__(self, budget, time, userList)

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
                    self.active_users[user] = user.action
                self.update_probability(user)
                user.reward = 0.0
                s += self.check_action(user.action)
            # p.close()
            # p.join()
            self.status_last_time = s / len(self.userList)
            self.status.append(self.status_last_time)
            end = time.time()
            print(str(end - start) + "s")
