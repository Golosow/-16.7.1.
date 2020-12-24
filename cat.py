

class Cat:
    def __init__(self, имя, пол, возраст):
        self.name = имя
        self.gender = пол
        self.age = возраст
    def getName(self):
        return self.name
    def getGender(self):
        return self.gender
    def getAge(self):
        return self.age
    def getData(self):
        return self.name, self.gender, self.age
