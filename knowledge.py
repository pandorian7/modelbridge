from abc import abstractmethod, ABC
import os.path
import json

class Knowledge(ABC):
    Knowledge_Path: str = None
    def __init__(self):
        if not os.path.isfile(self.Knowledge_Path):
            raise ImportError("Knowledge file does not exist")
        
        self.__readonly = False
        self.__in_context = False
    
    def readData(self):
        with open(self.Knowledge_Path) as file:
            return json.load(file)
        
    def writeData(self, data:dict):
        if not self.__in_context:
            raise Exception('not in context')
        with open(self.Knowledge_Path, 'w') as file:
            json.dump(data, file)

    @abstractmethod
    def loadData(self):
        ...

    @abstractmethod
    def unloadData(self, data):
        ...

    @property
    def data(self): return self.__knowledge

    @property
    def ro(self):
        self.__readonly = True
        return self

    def __enter__(self):
        self.__knowledge = self.loadData()
        self.__in_context = True

        return self.data

    def __exit__(self, *rest):
        if not self.__readonly:
            self.writeData(self.unloadData(self.__knowledge))
        self.__knowledge = None
        self.__in_context = False
        self.__readonly = False
