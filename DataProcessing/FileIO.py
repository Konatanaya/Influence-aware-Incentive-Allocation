from Agents import UserAgent
import random, datetime


class FileIO:
    def __init__(self, name):
        self.userList = {}
        self.num = 2
        self.add_net = '../data/' + name + '_network.txt'
        self.add_user = '../data/' + name + '_user.txt'
        self.net = '../data/'+ name + '.txt'

    def import_data(self):
        try:
            file = open(self.net, 'r')
            for line in file:
                arr = line.strip('\n').split()
                u1 = UserAgent.UserAgent(int(arr[0]))
                u2 = UserAgent.UserAgent(int(arr[1]))
                if u1 not in self.userList:
                    u1.init_preference(self.num)
                    self.userList[u1] = u1
                else:
                    u1 = self.userList[u1]
                if u2 not in self.userList:
                    u2.init_preference(self.num)
                    self.userList[u2] = u2
                else:
                    u2 = self.userList[u2]
                influence = random.random() * u1.remaining_influence
                u1.remaining_influence -= influence
                u1.in_neighbors[u2] = influence
                u2.out_neighbors[u1] = influence
        finally:
            if file:
                file.close()
        self.export_data()

    def export_data(self):
        l = list(self.userList.values())
        # l.sort(key=lambda x: int(x.id), reverse=False)
        try:
            file = open(self.add_user, 'w')
            file1 = open(self.add_net, 'w')
            for user in l:
                line = str(user.id) + " "
                for pre in user.preference:
                    line += str(pre) + " "
                file.write(line + "\n")
                for key in user.in_neighbors:
                    line = str(user.id) + " " + str(key.id) + " " + str(user.in_neighbors.get(key))
                    file1.write(line + "\n")
        finally:
            if file:
                file.close()
            if file1:
                file1.close()

    def import_user_data(self):
        try:
            file = open(self.add_user, 'r')
            for line in file:
                arr = line.strip('\n').split()
                ID = arr[0]
                arr.pop(0)
                user = UserAgent.UserAgent(int(ID))
                user.assign_preference(list(map(lambda x: float(x), arr)))
                self.userList[user] = user
            file.close()
            file = open(self.add_net, 'r')
            for line in file:
                arr = line.strip('\n').split()
                u1 = UserAgent.UserAgent(int(arr[0]))
                u2 = UserAgent.UserAgent(int(arr[1]))
                influence = float(arr[2])
                u1 = self.userList[u1]
                u2 = self.userList[u2]
                u1.in_neighbors[u2] = influence
                u2.out_neighbors[u1] = influence
        finally:
            if file:
                file.close()

    def print_list(self):
        l = list(self.userList.values())
        l.sort(key=lambda x: int(x.id), reverse=False)
        for user in l:
            print(str(user.id) + ": " + str(len(user.out_neighbors)))


if __name__ == "__main__":
    start = datetime.datetime.now()
    io = FileIO()
    # io.import_data()
    io.import_user_data()
    io.print_list()
    end = datetime.datetime.now()
    print("time: " + str((end - start).seconds) + "s")
