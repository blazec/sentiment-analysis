# cross-validate using files partition-1 ... partition-10

def concatenate_arff_files(f,output):

    
    lines = [line.rstrip() for line in arff_file]
    # Data starts at index 26
    lines = lines[26:len(lines)]



for i in range(10):
    filename = 'partition-i' + str(i+1) + '.arff'
    for j in range(0,i) + range(i+1,10):
        
