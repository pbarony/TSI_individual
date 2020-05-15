import unittest, csv
from unittest import mock
from unittest.mock import MagicMock

from DataSource.CSVFileObject import CSVFileObject
from DataSource.CSVFileObjectFake import CSVFileObjectFake
from DataSource.ReadCSVFileStub import ReadCSVFileStub
from src.DataSource.ReadCSVFile import ReadCSVFile
from src.DataSource.DataSourceConstants import *
import os


class TestReadCSVFile(unittest.TestCase):
    os.chdir("..")

    def test_getCustomerDataFromFile(self):
        readCSVFile = ReadCSVFile()
        fileData = readCSVFile.getFileData(ENTITIES_FOLDER,"customer" + ".csv")
        self.assertEqual( fileData[1] ,['derek.somerville@glasgow.ac.uk', 'Derek', 'Somerville', '1234'])

    def test_getLastLinesFromFile(self):
        readCSVFile = ReadCSVFile()
        fileLines = readCSVFile.getLastLines( ENTITIES_FOLDER, "customer" + ".csv",1)
        self.assertEqual( fileLines ,['matthew.barr@glasgow.ac.uk', 'Matt', 'Barr', '4321'])

    def test_getLastLinesFromFileStub(self):
        readCSVFile = ReadCSVFileStub()
        fileLines = readCSVFile.getLastLines(ENTITIES_FOLDER, "customer" + ".csv", 1)
        self.assertEqual(fileLines, ['andrew.blair@glasgow.ac.uk', 'Andrew', 'Blair', '5678'])

    def test_getLastLinesFromFileMock(self):
        readCSVFile = ReadCSVFile()
        readCSVFile.getLastLines = MagicMock(return_value=['andrew.blair@glasgow.ac.uk', 'Andrew', 'Blair', '5678'])

        fileLines = readCSVFile.getLastLines(ENTITIES_FOLDER, "customer" + ".csv", 1)
        self.assertEqual(fileLines, ['andrew.blair@glasgow.ac.uk', 'Andrew', 'Blair', '5678'])

    def test_getLastLinesFromFileFake(self):
        readCSVFile = ReadCSVFile()
        fileLines = readCSVFile.getLastLines(ENTITIES_FOLDER, "customer" + ".csv", 1, CSVFileObjectFake)
        self.assertEqual(fileLines, ['andrew.blair@glasgow.ac.uk', 'Andrew', 'Blair', '5678'])

def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()

