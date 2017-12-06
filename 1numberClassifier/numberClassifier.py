import tensorflow
import itertools
import random
from classifiedNumber import ClassifiedNumber
from classifiedNumber import classifiedAsString
from time import time

def trainDatasetFunction():
    
    trainNumbers = []
    trainNumberLabels = []
    
    for i in range(-1000, 1001):    
        number = ClassifiedNumber(i)
        trainNumbers.append(number.number())
        trainNumberLabels.append(number.classifiedAs())
    
    return ( {"number" : trainNumbers } , trainNumberLabels )

def inputDatasetFunction():
    
    global randomSeed
    random.seed(randomSeed) # to get same result
    
    numbers = []
    
    for i in range(0, 4):
        numbers.append(random.randint(-9999999, 9999999))
    
    return {"number" : numbers }
    
def main():
    
    print("Tensorflow Positive-Negative-Zero numbers classifier test by demensdeum 2017 (demensdeum@gmail.com)")
    
    inputDataset = inputDatasetFunction()
    
    numberFeature = tensorflow.feature_column.numeric_column("number")
    classifier = tensorflow.estimator.DNNClassifier(feature_columns = [numberFeature], hidden_units = [10, 20, 10], n_classes = 4)
    generator = classifier.train(input_fn = trainDatasetFunction, steps = 1000).predict(input_fn = inputDatasetFunction)
    
    results = list(itertools.islice(generator, len(inputDatasetFunction()["number"])))
    
    i = 0
    for result in results:
        print("number: %d classified as %s" % (inputDataset["number"][i], classifiedAsString(result["class_ids"][0])))
        i += 1

randomSeed = time()

main()