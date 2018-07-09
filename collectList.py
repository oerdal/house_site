import csv

# open file containing active house roster
class activeListCollector:
    def __init__(self, csvfile):
        self.activeList = open(csvfile)
        self.reader = csv.DictReader(self.activeList, fieldnames=["number", "name", "status", "class", "line", "quarter"])
    
    def getList(self):
        return self.reader