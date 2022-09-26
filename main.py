from file_path_folder import *   
from merging_json_to_csv import * 
from generateWordcloud import *
from countingByResource import *
from countingByDataset import *
     
if __name__ == "__main__":
    
    files, output = file_path_folder()
    
    merging_json_to_csv(files, output) 
    generateWordcloud(files, output)
    countingByResource(files, output)
    countingByDataset(files, output)

    print('Meta Data Analysis Complete')


