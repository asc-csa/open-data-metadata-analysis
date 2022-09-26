# -*- coding: utf-8 -*-
import os

def file_path_folder(): 
    full_path = os.path.realpath(__file__)
    path, _ = os.path.split(full_path)
    
    input_path = path + '\input'
    
    raw_files = [os.path.join(input_path, file) for file in os.listdir(input_path)]
    
    new_path = path + '\meta_data_results'
    
    if not os.path.isdir(new_path):
        os.mkdir(new_path)
        
    return raw_files, new_path


