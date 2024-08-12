from dateutil import parser
import json
from datetime import datetime

class Event:
    def __init__(self, Title, StartDate, EndDate, ModifyedDate, EventID, LabelColor = None, Status = None):
        self.title = Title

        if (LabelColor != None):
            self.ColorMapping(LabelColor)
        else:
            self.strLabelColor = LabelColor

        self.strStatus = Status
        self.eventId = EventID

        self.startDate = parser.parse(str(StartDate))
        self.endDate = parser.parse(str(EndDate))
        self.dateModifyed = parser.parse(str(ModifyedDate))

    def getName(self):
        return self.title
    
    def getID(self):
        return self.eventId

    def getStartDate(self):
        return self.startDate

    def getEndDate(self):
        return self.endDate

    def getLastModifyed(self):
        return self.dateModifyed

    def getStrLabel(self):
        return self.strLabelColor
    
    def getStrStatus(self):
        return self.strStatus

    def getStrSelf(self):
        return ("Name: " + str(self.title) + " startDate: " + str(self.startDate) + " endDate: " + str(self.endDate) + " label: " + str(self.strLabelColor) + " status: " + str(self.strStatus) + " ID: " + str(self.eventId))

    def cardParodySync(self,card):
        self.title = card.getName()
        self.startDate = card.getStartDate()
        self.dueDate = card.getDueDate()
        self.strLabelColor = self.ColorMapping(card.getLabel()[1]) #The returned label is an array. 0: is the name and 1: is the color
        self.strStatus = card.getStatus()

    def ColorMapping(self,cardColor):
        colorMap = {
            'green':2,
            'yellow': 4,
            'orange': 5,
            'red': 11,
            'purple': 3,
            'blue' : 1,
        }

        if (len(cardColor) > 10):
            return cardColor
        else:
            return colorMap[str(cardColor)]

    def jsonReturn(self):
        event = {
        'summary': self.getName(),
        'location': '',
        'description': self.getStrStatus(),
        'start': {
            'dateTime': self.startDate.isoformat(),
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': self.endDate.isoformat(),
            'timeZone': 'America/Los_Angeles',
        },
        'recurrence': [
        ],
        'attendees': [
        ],
        "colorId": str(self.strLabelColor),
        'reminders': {
            'useDefault': False,
            'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
            ],
        },
        }

        return event
