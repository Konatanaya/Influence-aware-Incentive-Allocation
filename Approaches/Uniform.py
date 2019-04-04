from Approach import Approach


class Uniform(Approach):
    def __init__(self, budget, time, userList):
        Approach.__init__(self, budget, time)
        self.userList = userList

    def simulate(self):
        for t in range(1, self.time + 1):
            s = 0
            self.budget = self.per_budget
            reward = self.per_budget / len(self.userList)
            for user in self.userList:
                if self.budget > 0.0:
                    user.reward = reward
                user.take_action()
                if user.action == 0:
                    self.budget -= user.reward
                user.reward = 0.0
                s += self.check_action(user.action)
            self.status.append(s / len(self.userList))
