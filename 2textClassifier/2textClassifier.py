import tensorflow
import itertools
from trainDataset import TrainDataset
from classifiedStringsDatasetTensorFlowData import ClassifiedStringsDatasetTensorFlowData
    
def inputDatasetFunction():
    
    global trainDatasetData
    global inputString 
    
    inputDatasetDictionary = {}
    
    ClassifiedStringsDatasetTensorFlowData.appendCharactersListToFeaturesDictionary(inputString, inputDatasetDictionary, trainDatasetData.datasetLineMaxLength())
    
    return inputDatasetDictionary
    
def main():
    
    global trainDatasetData
    global inputString
    
    inputString = "metallica"    
    
    print("TensorFlow text classifier by demensdeum 2017 (demensdeum@gmail.com)")
    
    trainDataset = TrainDataset()
    trainDatasetData = trainDataset.trainDatasetData()

    classifier = tensorflow.estimator.DNNClassifier(feature_columns = trainDatasetData.feature_columns(), model_dir=".", hidden_units = [512, 256, 128], n_classes = trainDatasetData.n_classes())
    classifier.train(input_fn = trainDataset.trainDatasetFunction, steps = 200000)
    
    while True:
    
        inputString = input("Text to classify: ")
    
        if len(inputString) < 1:
            print("Exit...")
            exit(0)
    
        generator = classifier.predict(input_fn = inputDatasetFunction)
    
        results = list(itertools.islice(generator, 1))

        i = 0
        for result in results:
            index = result["class_ids"][0]
            print("number: %s classified as %s" % (inputString, trainDatasetData.labelsStrings()[index]))
            i += 1

main()