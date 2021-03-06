from DataSource.CSVFileInterface import CSVFileInterface

class CSVFileObject(CSVFileInterface):

    filePathPrefix = "resource/"

    def getFile(self, directory,  fileName):
        dataFile = open(self.filePathPrefix + directory + fileName, 'rt')
        return dataFile

    def closeFile(self,dataFile):
        dataFile.close()