import pandas as pd

def merging_json_to_csv(files, output):
    
    file_json = [name for name in files if name.endswith('.json')]
    file_json = file_json[0]
    file_csv = [name for name in files if name.endswith('.csv')]
    file_csv = file_csv[0]
    
    df1 = pd.read_json(file_json, lines=True)
    df1.head()
    
    df2 = pd.read_csv(file_csv)
    df2.head()
    
    #appending json to dataframe
    df3 = pd.merge(df1, df2, how='left', left_on='name', right_on='dataset name')
    df3.head()
    
    columns = ['dataset id', 'dataset name']
    df3.drop(columns, inplace=True, axis=1)
    
    csv_name = output + '\json_merged.csv'
    df3.to_csv(csv_name, sep=',', encoding='utf-8')
    json_name = output + '\json_merged.json'
    df3.to_json(json_name)
