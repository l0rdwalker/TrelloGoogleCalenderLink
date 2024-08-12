from datetime import datetime
from Calender.Calender import Calender
from Calender.Event import Event
from Trello.TrelloBoard import TrelloBoard
from Labels import Labels

class SyncAPI:
    def __init__(self):
        self.LabelLst = Labels("", "","")
        self.Calender = Calender()
        self.TrelloBoard = TrelloBoard("", "","")
        
        self.TrelloBoard.GetCards()
        self.Calender.getEvents()

        self.LabelLst.retreiveLabels()

        TrelloCards = self.TrelloBoard.returnCards() 
        CalenderEvents = self.Calender.returnEvents() 

        for card in TrelloCards:
            fndLabel = self.LabelLst.getLabel(TrelloCards[card].getLabel())
            if (fndLabel != None):
                TrelloCards[card].setLabel(fndLabel)

        for event in CalenderEvents:
            fndLabel = self.LabelLst.getLabel(CalenderEvents[event].getColorID())
            if (fndLabel != None):
                CalenderEvents[event].setLabel(fndLabel)

    def card2event(self):
        TrelloCards = self.TrelloBoard.returnCards() 
        CalenderEvents = self.Calender.returnEvents() 

        for eventName in CalenderEvents:
            if (eventName in TrelloCards):
                TrelloCards[eventName].togglePaired()

                if (CalenderEvents[eventName].getLastModifyed() > TrelloCards[eventName].getLastModifyed()):
                    self.TrelloBoard.updateCard(CalenderEvents[eventName])
                elif ((CalenderEvents[eventName].getLastModifyed() < TrelloCards[eventName].getLastModifyed())): 
                    self.Calender.updateEvent(TrelloCards[eventName])
                    
            else:
                self.Calender.deleteEvent(eventName)

        for card in TrelloCards:
            if ((TrelloCards[card].getPaired() == False) & (TrelloCards[card].canEvent())):
                self.Calender.createEvent(TrelloCards[card])

Crossover = SyncAPI()
Crossover.card2event()

