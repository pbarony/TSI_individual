import csv
import subprocess
import os

from DataSource.CSVFileObject import CSVFileObject


class ReadCSVFile :

    filePathPrefix = "resource/"

    def getFileData(self, directory,  fileName, objectType=CSVFileObject):
        fileData = []
        dataFile = objectType.getFile(self,directory,fileName)
        fileReader = csv.reader(dataFile)
        for row in fileReader:
            fileData.append(row)
        objectType.closeFile(self,dataFile)
        return fileData

    def getLastLines(self,directory, fileName, numerOfLines, objectType=CSVFileObject):
        return self.getFileData(directory, fileName, objectType)[-1*numerOfLines]
