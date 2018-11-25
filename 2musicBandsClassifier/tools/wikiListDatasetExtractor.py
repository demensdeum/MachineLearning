filepath = "List of alternative rock artists - Wikipedia.html"
classifiedAs = "alternative rock"

file = open(filepath)

outputLines = []


for line in file:
    if "</a></li>" in line:
        outputLine = line.split("</a></li>")[0].split(">").pop() + " - " + classifiedAs
        outputLines.append(outputLine)
        
file.close()

outputFile = open("outputDataset.txt", "w")

outputFile.write("\n".join(outputLines))

outputFile.close()