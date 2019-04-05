from Approaches import IPE, Uniform, DGIA
from DataProcessing.FileIO import FileIO
import Plot.plot as plot
import datetime

userlist = {}
list = []


def init_userlist():
    for user in userlist:
        user.reset()


if __name__ == "__main__":
    budget = 200
    time = 150
    name = 'wiki'
    io = FileIO(name)
    # io.import_data()
    io.import_user_data()
    userlist = io.userList
    start = datetime.datetime.now()
    dgia = DGIA.DGIA(budget, time, userlist)
    dgia.simulate()
    list.append(dgia.status)

    # init_userlist()
    # ipe = IPE.IPE(budget, time, userlist)
    # ipe.simulate()
    # list.append(ipe.status)

    init_userlist()
    uni = Uniform.Uniform(budget, time, userlist)
    uni.simulate()
    list.append(uni.status)
    #
    init_userlist()
    uni = Uniform.Uniform(0, time, userlist)
    uni.simulate()
    list.append(uni.status)
    #
    # init_userlist()
    # uni = Uniform.Uniform(budget * 2, time, userlist)
    # uni.simulate()
    # list.append(uni.status)
    #
    # init_userlist()
    # uni = Uniform.Uniform(budget * 3, time, userlist)
    # uni.simulate()
    # list.append(uni.status)

    end = datetime.datetime.now()
    print("time: " + str((end - start).seconds) + "s")

    # list.append(ipe.status)

    print(len(list))
    plot.draw_plot(list, time)
