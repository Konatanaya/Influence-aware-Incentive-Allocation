import matplotlib.pyplot as plt
import numpy as np

GAUP = []
GIAC = []
budget = 80


def draw_plot(array, time):
    mark = ['-o', '-s', '-v', '-D', '-^', '-s']
    name = ['DBP-UCB', 'DGIA-IPE', 'DGIA', 'ϵ-first', 'Uniform']
    size = 18
    x = np.linspace(0, time, time+1)
    plt.figure(figsize=(10, 8))
    for index in range(len(array)):
        y = array[index]
        plt.plot(x, y, mark[index], label=name[index], ms=10)
    # plt.axis([0,150,0,1])
    plt.xticks(np.linspace(0, 100, 5), fontsize=size)
    plt.yticks(np.linspace(0, 1.0, 6), fontsize=size)
    plt.legend(loc='lower right', fontsize=size - 4)
    plt.xlabel("Time steps", fontsize=size)
    plt.ylabel("GAUP", fontsize=size)
    # plt.suptitle("Budget per time step = " + str(budget), fontsize=size)
    plt.show()

    # plt.figure(figsize=(10, 8))
    # for index in range(len(GAUP)):
    #     y = GIAC[index]
    #     plt.plot(x, y, mark[index], label=name[index], ms=10)
    # # plt.axis([0,150,0,1])
    # plt.xticks(np.linspace(0, 150, 6), fontsize=size)
    # plt.yticks(np.linspace(0, 0.5, 6), fontsize=size)
    # plt.legend(loc='upper right', fontsize=size - 4)
    # plt.xlabel("Time steps", fontsize=size)
    # plt.ylabel("GIAC", fontsize=size)
    # # plt.suptitle("Budget per time step = " + str(budget), fontsize=size)
    # plt.show()


def importData():
    num = 80
    name = ['DBPUCB', 'DGIA', 'DGIA_NI', 'EMAB', 'uniform']
    for s in name:
        g1 = []
        count = 0
        with open('data/large_' + s + '_' + str(num) + '.txt', 'r') as f:
            for i in f.read().splitlines():
                if count % 10 == 0:
                    g1.append(float(i))
                count += 1
            GAUP.append(g1)

        g2 = []
        count = 0
        with open('data/large_' + s + '_ROI_' + str(num) + '.txt', 'r') as f:
            for i in f.read().splitlines():
                if count % 10 == 0:
                    g2.append(float(i))
                count += 1
            GIAC.append(g2)


if __name__ == '__main__':
    #importData()
    #drawPlot()
    print(1)
