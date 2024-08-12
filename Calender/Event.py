from dateutil import parser
import json
from datetime import datetime

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class Event:
    def __init__(self, json = None):
        self.changed = False
        self.delete = False
        self.label = None

        self.event = {
        'summary': "",
        'location': '',
        'description': "",
        'start': {
            'dateTime': "",
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': "",
            'timeZone': 'America/Los_Angeles',
        },
        'recurrence': [
        ],
        'attendees': [
        ],
        "colorId": "",
        'reminders': {
            'useDefault': False,
            'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
            ],
        },
        }

        if (json != None):
            self.event['summary'] = json['summary']
            self.CalenderID = json['id']

            if ('location' in json):
                self.event['location'] = json['location']

            if ('description' in json):
                if (json['description'] == None):
                    self.event['description'] = self.CalenderID
                else:
                    self.event['description'] = json['description']
            else:
                self.event['description'] = self.CalenderID

            self.event['start']['dateTime'] = json['start']['dateTime']
            self.startTime = parser.parse(str(json['start']['dateTime']))

            self.event['end']['dateTime'] = json['end']['dateTime']
            self.endTime = parser.parse(str(json['end']['dateTime']))

            self.LastModifyed = parser.parse(str(json['updated']))

            if ('colorId' in json):
                self.event['colorId'] = json['colorId']

    #Getters
    def getCalenderID(self):
        return str(self.CalenderID)

    def getName(self):
        return str(self.event['summary'])

    def getLocation(self):
        return self.event['location']

    def getDescription(self): ##correct get description to getlabel
        return self.label

    def getColorID(self):
        return self.event['colorId']

    def getStartDate(self):
        return self.endTime

    def getEndDate(self):
        return self.endTime

    def getEditStatus(self):
        return self.changed
    
    def getDeleteStatus(self):
        return self.delete

    def getEvent(self):
        return self.event

    def getLastModifyed(self):
        return self.LastModifyed

    def getID(self):
        return self.event['description']

    def printEventJson(self):
        print(self.event)

    #Setters
    def toggleEditStatus(self):
        self.changed = not self.changed

    def toggleDeleteStatus(self):
        self.delete = not self.delete

    def setName(self,Name):
        self.changed = True
        self.event['summary'] = Name

    def setLocation(self,Location):
        self.changed = True
        self.event['location'] = Location

    def setLabel(self,Label):
        self.changed = True
        self.label = Label 
        self.event['colorId'] = Label.getCalenderColor()

    def setID(self,id):
        self.event['description'] = id

    def setDates(self,StartTime,EndTime):
        self.changed = True
        if (StartTime > EndTime):
            raise Exception("StartTime cannot be bigger then EndTime")
        else:
            self.changed = True
            self.endTime = EndTime
            self.startTime = StartTime

            self.event['start']['dateTime'] = StartTime.isoformat()
            self.event['end']['dateTime'] = EndTime.isoformat()




    
"""{
        'summary': "",
        'location': '',
        'description': "",
        'start': {
            'dateTime': "",
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': "",
            'timeZone': 'America/Los_Angeles',
        },
        'recurrence': [
        ],
        'attendees': [
        ],
        "colorId": "",
        'reminders': {
            'useDefault': False,
            'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
            ],
        },
        }"""