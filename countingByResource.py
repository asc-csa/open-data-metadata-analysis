import json
import csv
import pandas
import matplotlib.pyplot as plt
from csv import writer
import time

def countingByResource(files, output): 
    date = time.strftime('%Y%m%d')
    
    # Files
    file_jsonl = [name for name in files if name.endswith('.jsonl')]
    file_jsonl = file_jsonl[0]
    infile = file_jsonl
    filename = "CountingByResource_" + date
    outfile = output + '/' + '%s.csv' % filename
    
    def label_graphs(test):
        for p in test.patches:
            height = p.get_height()
            width = p.get_width()
            x, y = p.get_xy()
            test.annotate(f'{height}\n', (x + width/2 , y + height+ 0.15),  ha='center', va='center')
    
    # A bunch of empty lists
    data = []
    dataset_name_en = []
    dataset_name_fr = []
    resource_name_en = []
    resource_name_fr = []
    resource_directorate = []
    resource_division = []
    resource_project = []
    science_admin =[]
        
    ## Code starts here, open the file and add it to the empty 'data' list
    with open(infile, encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line)) #load per line, needed for the jsonl format
            
    # The resources (ie. individual links to specific files)are nested within the larger dataset JSON (CKAN also calls datasets packages, FYI)
    for d in data:
        res = d['resources']
        for r in res:
            dataset_name_en.append(d['title_translated']['en'])
            dataset_name_fr.append(d['title_translated']['fr'])
            resource_name_en.append(r['name_translated']['en'])
            resource_name_fr.append(r['name_translated']['fr'])
            resource_directorate.append(d['directorate'])
            resource_division.append(d['division'])
            resource_project.append(d['project'])
            science_admin.append(d['science_admin'])
    
    resource_division = ["unassigned_division" if x == '' else x for x in resource_division]
    resource_division = [w.replace('_', ' ') for w in resource_division]
    resource_directorate = ["unassigned_directorate" if x == '' else x for x in resource_directorate]
    resource_directorate = [w.replace('_', ' ') for w in resource_directorate]
    
    headers = ["Dataset Name (EN)", "Dataset Name (FR)", "Resource Name (EN)", "Resource Name (FR)", "Directorate", "Division", "Project", "Admin"]
        
    with open(outfile, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(i for i in headers)
        writer.writerows(zip(dataset_name_en,dataset_name_fr,resource_name_en,resource_name_fr,resource_directorate, resource_division, resource_project, science_admin))
    
    col_list = ["Dataset Name (EN)","Directorate", "Division", "Project", "Admin"]
    csv_data = pandas.read_csv(outfile, usecols = col_list)
    
    groupByProject = csv_data.groupby(['Project'])
    projectCounter = groupByProject.count()
    pCounterColumn = projectCounter['Dataset Name (EN)']
    print("Number of datasets in each project:")
    print(pCounterColumn.sort_values(ascending=False))
    pCounterColumn.to_csv(output + '/resourceProjectCount_' + date + '.csv', encoding = 'utf-8')
    
    groupByDivision = csv_data.groupby(['Division'])
    divisionCounter = groupByDivision.count()
    divCounterColumn = divisionCounter['Dataset Name (EN)']
    print("Number of datasets in each division:")
    print(divCounterColumn.sort_values(ascending=False))
    divCounterColumn.to_csv(output + '/resourceDivisionCount_' + date + '.csv', encoding = 'utf-8')
    
    groupByDirectorate = csv_data.groupby(['Directorate'])
    dirCounter = groupByDirectorate.count()
    dirCounterColumn = dirCounter['Dataset Name (EN)']
    print("Number of datasets in each directorate:")
    print(dirCounterColumn.sort_values(ascending=False))
    dirCounterColumn.to_csv(output + '/resourceDirectorateCount' + date + '.csv', encoding = 'utf-8')
    
    plt.rc('font', size=18)
    
    graph_1 = pCounterColumn.sort_values(ascending = False).plot.bar(color = "#ffc107",  figsize=(25, 10))
    label_graphs(graph_1)
    plt.title('Resource Count by Project')
    plt.ylabel('# of Resources')
    plt.xticks(rotation=25, ha='right', wrap = True)
    graph1 = output + "/resourceProjectCount_" + date + ".png"
    plt.savefig(graph1, bbox_inches = "tight")
    plt.show()
    
    graph_2 = divCounterColumn.sort_values(ascending = False).plot.bar(color = "#3663A2",  figsize=(30, 12))
    label_graphs(graph_2)
    plt.title('Resource Count by Division')
    plt.ylabel('# of Resources')
    plt.xticks(rotation=25, ha='right', wrap = True)
    graph2 = output + "/resourceDivisionCount_" + date + ".png"
    plt.savefig(graph2, bbox_inches = "tight")
    plt.show()
    
    graph_3 = dirCounterColumn.sort_values(ascending = False).plot.bar(color = "#e60000",  figsize=(30, 12))
    label_graphs(graph_3)
    plt.title('Resource Count by Directorate')
    plt.ylabel('# of Resources')
    plt.xticks(rotation=25, ha='right', wrap = True)
    graph3 = output + "/resourceDirectorateCount_" + date + ".png"
    plt.savefig(graph3, bbox_inches = "tight")
    plt.show()

