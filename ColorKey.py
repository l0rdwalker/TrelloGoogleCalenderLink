class Calender:
    def __init__(self):
        self.ColorKey = {
            "purple": 1,
            "green": 2,
            "black": 3,
            "yellow": 4,
            "orange": 5,
            "red": 6,
            "blue": 7,
            "black": 8,

            1:"purple",
            2:"green",
            3:"black",
            4:"yellow",
            5:"orange",
            6:"red",
            7:"blue",
            8:"black",
        }

    def getColor(self,index):
        if index in self.ColorKey:
            return self.ColorKey[index]
        else:
            raise Exception("Unknown color key code combo ")