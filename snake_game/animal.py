class Animal:
    def __init__(self):
        self.num_eyes = 2
        self.tail = 20

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):
    
    def __init__(self):
        #super().__init__()
        self.test = "hello"
    # def breathe(selfs):
    #     super().breathe()
    #     print("doing this underwater")
    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()

