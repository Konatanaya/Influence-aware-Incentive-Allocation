from threading import Thread


class Approach:
    def __init__(self, budget, time):
        self.per_budget = budget
        self.budget = 0.0
        self.time = time
        self.status = []
        self.status.append(0.0)

    def check_action(self, action):
        if action == 0:
            return 1
        else:
            return 0

    def output(self, i):
        print(i)

    def print_thread(self):
        for i in range(30):
            t1 = Thread(target=self.output(i * 1), name="t1")
            t2 = Thread(target=self.output(i * 10), name="t2")

            t1.start()
            t2.start()


if __name__ == "__main__":
    app = Approach(1, 1)
    app.print_thread()
