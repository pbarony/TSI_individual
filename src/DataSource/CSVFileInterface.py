from abc import ABC, abstractmethod

class CSVFileInterface(ABC):

    @abstractmethod
    def getFile(self, directory,  fileName):
        pass