from Label import Label
import json
import requests

class Labels:
    def __init__(self, key, token,boardID):
        self.Labels = {}
        self.key = key
        self.token = token
        self.boardID = boardID

        self.retreiveLabels()

    def retreiveLabels(self):
        url = f"https://api.trello.com/1/boards/{self.boardID}/labels"
        
        query = {'key': self.key,'token': self.token}
        response = requests.request("GET",url,params=query)
        Labels = json.loads(response.text)

        for var in Labels:
            if (var['name'] != ''):
                self.addLabel(var)

    def addLabel(self,json):
        newLabel = Label(json)
        self.Labels[newLabel.getID()] = newLabel

    def getLabel(self,labelId):
        if (len(labelId) == 1):
            for key in self.Labels:
                if (int(self.Labels[key].getCalenderColor()) == int(labelId)):
                    return self.Labels[key]
            return None
        else: 
            if labelId in self.Labels:
                    return self.Labels[labelId]
            return None
        
        """
        if (len(labelId) == 1):
            for key in self.Labels:
                if (int(self.Labels[key].getCalenderColor()) == int(labelId)):
                    return self.Labels[key]
        elif (not (labelId in self.Labels)):
            self.addLabel(self.retreiveLabel(labelId))

        return self.Labels[labelId]
        """
    
            