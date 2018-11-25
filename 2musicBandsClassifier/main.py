import tensorflow
import itertools
from trainDataset import TrainDataset
from classifiedStringsDatasetTensorFlowData import ClassifiedStringsDatasetTensorFlowData
    
import logging
logging.getLogger().setLevel(logging.INFO)
    
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
    
    print("TensorFlow music bands classifier by demensdeum 2017 (demensdeum@gmail.com)")
    
    trainDataset = TrainDataset()
    trainDatasetData = trainDataset.trainDatasetData()

    classifier = tensorflow.estimator.DNNClassifier(feature_columns = trainDatasetData.feature_columns(), model_dir="model", hidden_units = [128, 128, 128, 128, 128, 128], n_classes = trainDatasetData.n_classes())
    
    state = input("train/classify? ")
    
    if state == "train":
        print("Endless train mode, every 4000 steps will be saved. CTRL+C to exit")
        
        while True:
            classifier.train(input_fn = trainDataset.trainDatasetFunction, steps = 4000) # to save every 4000 steps
	
    elif state == "classify":
        print("Text classify mode, empty text input to exit")
	
    else:
        print("Write train or classify... Exit")
        exit(1)
    
    while True:
    
        inputString = input("Text to classify: ")
    
        if len(inputString) < 1:
            print("Empty text to classify. Exit...")
            exit(0)
	    
        elif (len(inputString) > trainDatasetData.datasetLineMaxLength()):
            print("Input text is too long")
            continue
    
        generator = classifier.train(input_fn = trainDataset.trainDatasetFunction, steps = 1).predict(input_fn = inputDatasetFunction)
    
        results = list(itertools.islice(generator, 1))

        i = 0
        for result in results:
            index = result["class_ids"][0]
            print("number: %s classified as %s" % (inputString, trainDatasetData.labelsStrings()[index]))
            i += 1

main()