f1 = input("Please type the exact name of the text file you want to import data from:")
splitter = input("What is the data split by? ")
f2 = input("Please type the exact name of the csv file you want to export data to:")
all_data = list()
with open(f1) as f:
    for line in f:
        if splitter in line:
            all_data.append(line.split(splitter))
with open(f2, 'w') as f:
    for val in all_data: 
        toWrite = ""
        for v in val:
            if not v == val[-1]:
                toWrite += v + ","
            else:
                toWrite += v
        f.write(toWrite)
