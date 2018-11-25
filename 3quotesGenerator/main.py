from textgenrnn import textgenrnn
from os import path

print("Textgenrnn quotes text generator by demensdeum 2018 (demensdeum@gmail.com)")

state = input("train/generate? ")

weights_filename = "textgenrnn_weights.hdf5"
vocab_filename = "textgenrnn_vocab.json"
config_filename = "textgenrnn_config.json"

default_dataset_filename = "dataset_quotes_ru.txt"

if state == "train":
    reset_model = False

    train_state = "reset"
    
    if path.exists(weights_filename):
        train_state = input("reset/resume? ")
    
    if train_state == "reset":
        reset_model = True
        textgen = textgenrnn()
        
    elif train_state == "resume":
        reset_model = False
        textgen = textgenrnn(weights_filename)

    else:
        print("Write reset or result... Exit")
        exit(2)
        
    dataset_file = input("dataset filename? (%s) " % default_dataset_filename)
        
    if len(dataset_file) < 1:
        dataset_file = default_dataset_filename
        
    while True:
        print("Endless train mode, every 4 epochs will be saved. CTRL+C to exit")
        textgen.train_from_file(dataset_file, num_epochs=4, new_model = reset_model)      
    
elif state == "generate":
    if path.exists(weights_filename) ==  False:
    	print("There is no weights to generate, train first... Exit")
    	exit(3)

    textgen = textgenrnn(weights_path = weights_filename, vocab_path = vocab_filename,
             config_path = config_filename)
    textgen.generate()
    
else:
    print("Write train or generate... Exit")
    exit(1)