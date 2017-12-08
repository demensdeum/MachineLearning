from classifiedString import ClassifiedString

class ClassifiedStringsDataset:

    def __init__(self):
        
        self.__classifiedStrings = []
    
    def loadDatasetFromFile(self, datasetFilePath):
        
        datasetFile = open(datasetFilePath)
    
        for line in datasetFile:
            
            self.addRawClassifiedString(line)
    
    def addRawClassifiedString(self, rawClassifiedString):
        
        classifiedString = ClassifiedString(rawClassifiedString)
        self.__classifiedStrings.append(classifiedString)
        
    def classifiedStrings(self):
        
        return self.__classifiedStrings
        
