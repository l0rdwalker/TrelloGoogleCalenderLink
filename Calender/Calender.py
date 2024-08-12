import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import os.path
from Calender.Event import Event

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#'https://www.googleapis.com/auth/calendar.readonly'
SCOPES = ['https://www.googleapis.com/auth/calendar']

class Calender:
    def __init__(self):
        creds = None

        if os.path.exists('Calender/token.json'):
            creds = Credentials.from_authorized_user_file("Calender/token.json", SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("Calender/Creds.json", SCOPES)
                creds = flow.run_local_server(port=0)

            with open('Calender/token.json', 'w') as token:
                token.write(creds.to_json())

        self.creds = creds
        self.Events = {} 
        self.calenderID = "primary"

    def getEvents(self):
        try:
            self.service = build('calendar', 'v3', credentials=self.creds)
            events_result = self.service.events().list(calendarId=self.calenderID, singleEvents=True, orderBy='startTime').execute()
            events = events_result.get('items', [])

            for eventJson in events:
                newEvent = Event(eventJson)
                self.Events[str(newEvent.getID())] = newEvent

        except HttpError as error:
            print('An error occurred: %s' % error)

    def deleteEvent(self,cardName):
        print(f"Deleting event {cardName}")
        event = self.Events[cardName]
        self.service.events().delete(calendarId='primary', eventId=event.getCalenderID()).execute()

    def updateEvent(self,card):
        event = self.Events[card.getID()]
        event.setName(card.getName())
        event.setDates(card.getStartDate(),card.getDueDate())
        event.setLabel(card.getLabel())

        self.service.events().update(calendarId='primary', eventId=event.getCalenderID(), body=event.getEvent()).execute()

        print(f"Update Event {card.getName()}")

    def createEvent(self,card):
        newEvent = Event()

        newEvent.setName(card.getName())
        newEvent.setDates(card.getStartDate(),card.getDueDate())
        newEvent.setLabel(card.getLabel())
        newEvent.setID(card.getID())

        self.Events[newEvent.getID()] = newEvent

        self.service.events().insert(calendarId='primary', body=newEvent.getEvent()).execute()
        print(f"Create event {card.getName()}")

    def returnEvents(self):
        return self.Events


#newEvent.setLabel(self.Labels.getLabel(newEvent.getColorID()))