from knowledge import Knowledge
from functools import reduce

class ExtensionCatagory(Knowledge):
    Knowledge_Path = "../knowledge/extensionCatagory.json"

    def loadData(self):
        return {value: key  for key, values in self.readData().items() for value in values}
    
    def unloadData(self, data):
        new_data = {}
        for key, value in data.items():
            if value not in new_data:
                new_data[value] = []
            new_data[value].append(key)
        return new_data
    
    def folders(self):
        return list(self.readData().keys())
    
    def exts(self):
        return reduce(lambda prv, nxt:prv+nxt, self.readData().values(), [])
            
