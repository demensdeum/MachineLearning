import tensorflow

class ClassifiedStringsDatasetTensorFlowData:
    
    def __init__(self, classifiedStringsDataset):
        
        self.__features = {}
        self.__feature_columns = []
    
        self.__labels = []
        self.__labelsStrings = []
        
        classifiedStrings = classifiedStringsDataset.classifiedStrings()
                
        classifiedStrings.sort(key=lambda x: len(x.string()), reverse=True)
        
        gridWidth = len(classifiedStrings[0].string())
        gridHeight = len(classifiedStrings)
        
        grid = [ [ 0 for x in range(gridWidth) ] for y in range(gridHeight) ]
                
        self.__datasetLineMaxLength = gridWidth
                
        # populate grid
                
        labelsSet = set()
                
        for y in range(0, len(classifiedStrings)):
            
            classifiedString = classifiedStrings[y]
            
            string = classifiedString.string()
            classifiedAsString = classifiedString.classifiedAsString()
            
            labelsSet.add(classifiedAsString)
            
            for x in range(0, len(string)):

                character = string[x:x+1]               
                grid[y][x] = character

        # populate features
        
        featureColumnsSet = set()

        for y in range(0, len(grid)):
            
            line = grid[y]
            
            for x in range(0, len(line)):
        
                character = ord("%c" % (line[x]))
                key = "character-%d" % (x)
                featureColumnsSet.add(key)
                
            ClassifiedStringsDatasetTensorFlowData.appendCharactersListToFeaturesDictionary(line, self.__features, self.datasetLineMaxLength())
                
        for featureColumn in featureColumnsSet:
                
            column = tensorflow.feature_column.numeric_column(featureColumn)

            self.__feature_columns.append(column)
        
        
        # populate labels

        labelsList = list(labelsSet)

        for classifiedString in classifiedStrings:
            
            index = labelsList.index(classifiedString.classifiedAsString())
            
            self.__labels.append(index)
            
        self.__labelsStrings = labelsList
        
            
    def features(self):
        
        return self.__features
    
    def feature_columns(self):
        
        return self.__feature_columns
    
    def labels(self):
        
        return self.__labels
    
    def labelsStrings(self):
        
        return self.__labelsStrings
    
    def n_classes(self):
        
        return len(self.labels()) + 1
    
    def datasetLineMaxLength(self):
        
        return self.__datasetLineMaxLength
    
    @staticmethod
    def appendCharactersListToFeaturesDictionary(string, featuresDictionary, lineWidth):
        
        string = list(string)
        
        if (len(string) > lineWidth):
            raise Exception("ClassifiedStringsDatasetTensorFlowData appendCharactersListToFeaturesDictionary: line is out lineWidth range (probably training dataset is too short for this request)")
        
        addSymbolsCount = lineWidth - len(string)
        
        for x in range(0, addSymbolsCount):
            string.append(0)
        
        for x in range(0, len(string)):
        
            character = ord("%c" % (string[x]))
            key = "character-%d" % (x)
                
            value = featuresDictionary.get(key,[])
            value.append(character)
            
            featuresDictionary[key] = value
        