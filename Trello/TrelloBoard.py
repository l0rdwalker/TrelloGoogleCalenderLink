import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import requests
import json
from Trello.Card import Card

class TrelloBoard:
    def __init__(self, key, token, boardID):
        self.key = key
        self.token = token
        self.boardID = boardID
        self.cards = {}

    def TrelloAPIget(self):
        url = "https://api.trello.com/1/boards/"+str(self.boardID)+"/cards"
        query = {'key': str(self.key),'token': str(self.token)}
        response = requests.request("GET",url,params=query)
        return json.loads(response.text)

    def GetCards(self):
        JsonData = self.TrelloAPIget()

        for PreCard in range(len(JsonData)):
            #,self.Labels.getLabel(JsonData[PreCard]["labels"][0]['id'])
            card = Card(JsonData[PreCard])
            self.cards[card.getID()] = card

    def printCards(self):
        for x in range(len(self.cards)):
            print(self.cards[x].getStrSelf())

    def updateCard(self,event):
        card = self.cards[event.getID()]
        card.setDates(event.getStartDate(),event.getEndDate())
        card.setName(event.getName())

        url = f"https://api.trello.com/1/cards/{card.getID()}"
        headers = {"Accept": "application/json"}
        query = {
            'key': '82fe777c0c901c458eeb2f019a0ead31',
            'token': '8643256dc3060028cae72c4bcd1c24841ad667db3f9d3077f20ea444e6cdf795',
            'name':card.getName(),
            'due':card.getDueDate(),
            'start':card.getStartDate()
        }

        response = requests.request("PUT",url,headers=headers,params=query)
        print(f"Update Card {card.getName()}")

    def returnCards(self):
        return self.cards

    def getCardLength(self):
        return (len(self.cards))

    def getUnpairedCards(self):
        retrnDist = []
        for cardID in self.cards:
            if (self.cards[cardID].getPaired() == False):
                retrnDist[cardID] = self.cards[cardID]
        return retrnDist