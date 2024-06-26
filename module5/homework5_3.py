class Building:
    def __init__(self):
        self.numberOfFloors = int
        self.buildingType = str

    def __eq__(self):
        print(self.numberOfFloors == self.buildingType)

a = Building()
a.__eq__()