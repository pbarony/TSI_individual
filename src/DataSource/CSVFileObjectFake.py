class CSVFileObjectFake:

    filePathPrefix = "resource/"

    def getFile(self, directory,  fileName):
        dataFile = ['emailAddress,firstName,lastName,password'
                    'derek.somerville@glasgow.ac.uk,Derek,Somerville,1234'
                    'matthew.barr@glasgow.ac.uk,Matt,Barr,4321',
                    'andrew.blair@glasgow.ac.uk,Andrew,Blair,5678']
        return dataFile

    def closeFile(self,dataFile):
        dataFile=[]