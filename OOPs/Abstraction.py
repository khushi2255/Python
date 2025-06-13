class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True  # unnecessary details hide.
        self.acc = True  # hide
        print("Car Started..")  # print


car1 = Car()
car1.start()
