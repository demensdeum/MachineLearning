from classifiedStringsDataset import ClassifiedStringsDataset
from classifiedStringsDatasetTensorFlowData import ClassifiedStringsDatasetTensorFlowData

class TrainDataset():

 def trainDatasetData(self):

  dataset = ClassifiedStringsDataset()
  dataset.loadDatasetFromFile("dataset.txt")
    
  data = ClassifiedStringsDatasetTensorFlowData(dataset)
    
  return data

 def trainDatasetFunction(self):
    
  data = self.trainDatasetData()
        
  return (data.features(), data.labels())