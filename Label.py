class Label:
    def __init__(self, json):
        self.label = json

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

    def returnJson(self):
        return self.label

    def getID(self):
        return self.label["id"]

    def getName(self):
        return self.label["name"]

    def getTrelloColor(self):
        return self.label["color"]

    def getCalenderColor(self):
        return self.ColorKey[self.label["color"]]