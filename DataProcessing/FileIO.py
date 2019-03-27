from Agents import UserAgent
import random


class FileIO:
    def __init__(self):
        self.userList = set()
        self.importdata()

    def importdata(self):
        try:
            file = open('../data/Wiki-Vote.txt', 'r')
            for line in file:
                arr = line.strip('\n').split()
                u1 = UserAgent.UserAgent(arr[0])
                u2 = UserAgent.UserAgent(arr[1])
                if u1 not in self.userList:
                    self.userList.add(u1)
                else:
                    u1 = list(self.userList)[list(self.userList).index(u1)]
                if u2 not in self.userList:
                    self.userList.add(u2)
                else:
                    u2 = list(self.userList)[list(self.userList).index(u2)]
                influence = random.random() * u1.remainingInf
                u1.remainingInf -= influence
                u1.inNeighbors[u2] = influence
                u2.outNeighbors[u1] = influence
        finally:
            if file:
                file.close()

    def printList(self):
        l = list(self.userList)
        l.sort(key=lambda x: int(x.id), reverse=False)
        self.userList = set(l)
        for user in l:
            print(user.id + ": " + str(len(user.outNeighbors)))


if __name__ == "__main__":
    io = FileIO()
    io.printList()
