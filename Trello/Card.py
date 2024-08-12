from dateutil import parser
import datetime
import requests
import json

class Card:
    def __init__(self, jsonData):
        self.card = jsonData

        self.paired = False
        self.eventable = True
        self.dateModifyed = parser.parse(str(self.card["dateLastActivity"]))
        self.label = jsonData["labels"][0]['id']

        StartDate = self.card["start"]
        DueDate = self.card["due"]

        if (StartDate == None):
            if (DueDate != None):
                self.startDate = parser.parse(str(DueDate))
                self.dueDate = self.startDate + datetime.timedelta(minutes=30)
            else:
                self.startDate = None
                self.dueDate = None
                self.eventable = False
        else:
            self.startDate = parser.parse(str(StartDate))
            if (DueDate != None):
                self.dueDate = parser.parse(str(DueDate))
            else:
                self.dueDate = self.startDate + datetime.timedelta(minutes=30)

    ###Service Functions###
    def canEvent(self):
        return (self.eventable)

    def togglePaired(self):
        self.paired = not self.paired

    def getPaired(self):
        return self.paired
    #######################
    
    ########Getters########
    def getName(self):
        return self.card["name"]

    def getID(self):
        return self.card["id"]

    def getStartDate(self): 
        return self.startDate

    def getDueDate(self):
        return self.dueDate

    def getLastModifyed(self):
        return parser.parse(str(self.card["dateLastActivity"]))

    def getLabel(self):
        return self.label

    def getCard(self):
        self.card["start"] = self.startDate
        self.card["due"] = self.dueDate
        
        return self.card
    #######################

    ########Setter########
    def setName(self,NewName):
        self.card["name"] = NewName

    def setDates(self,StartTime,EndTime):
        if (StartTime > EndTime):
            raise Exception("StartTime cannot be bigger then EndTime")
        else:
            self.dueDate = EndTime
            self.startDate = StartTime

            self.card["start"] = StartTime.isoformat()
            self.card["due"] = EndTime.isoformat()

    def setLabel(self, label):
        self.label = label
    ######################

    def print(self):
        return ("Name: " + str(self.name) + " dueDate: " + str(self.dueDate) + " label: " + str(self.label))

    def eventParodySync(self,event):
        self.name = event.getName()
        self.startDate = event.getStartDate()
        self.dueDate = event.getEndDate()
        