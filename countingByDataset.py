import json
import numpy as np
import csv
import requests
import pandas
import matplotlib.pyplot as plt
from csv import writer
import time
import seaborn as sb

# %%
date = time.strftime('%Y%m%d')

# input and output files names
infile = 'C:/Users/harain/Desktop/PythonFiles/Metadata/ckan_metadata_dump_20220526.jsonl'
outfile = "CountingByDataset_" + date + ".csv"

views_infile = 'C:/Users/harain/Desktop/PythonFiles/Metadata/json_merged.csv'

# %%
directorate = ["communications","corporate_services_and_hr","finance","human_resources","programs_and_integrated_planning","information_management_and_technology_management",
               "policy","space_exploration","space_science_and_technology","space_utilization","vicepresidents_office"]
division = ["cio_acces_to_information_and_open_data","com_public_affairs","corh_security_and_facilities","expl_astronauts_life_sciences_and_space_medicine","expl_director_generals_office",
            "expl_space_exploration_development","expl_space_exploration_operations_and_infrastructure", "fin_accounting_policies_and_financial_systems","fin_planning_and_management_financial_resources",
            "fin_procurement_and_contract_administration_and_material_management","pcy_director_general_office","pcy_economic_analysis_international_and_regulatory_affairs","pcy_strategic_policy_and_domestic_affairs",
            "pip_director_generals_office","st_david_florida_laboratory","sst_intellectual_property","st_engineering_development","util_satellite_operations_infrastructure_and_applications", "util_space_exploitation",
            "util_sunearth_system_sciences","corh_information_management_and_technology_management","rh_staff_relations_and_pay_and_benefits","rh_staffing_and_systems", "vp_corporate_services_and_human_resources"]

# %%
def label_graphs(test):
    for p in test.patches:
        height = p.get_height()
        int(height)
        width = p.get_width()
        x, y = p.get_xy()
        test.annotate(f'{int(height)}\n', (x + width/2 , y + height+ 0.15),  ha='center', va='center')

# %%
# empty lists, data from file will be appended to the following lists
data = []
dataset_name_en = []
dataset_name_fr = []
resource_name_en = []
resource_name_fr = []
dataset_steward = []
dataset_directorate = []
dataset_division = []
dataset_project = []
science_admin =[]
data_stewards = []
release_date = []
views = []

# %%
# Code starts here, open the file and add it to the empty 'data' list
with open(infile, encoding='utf-8') as f:
    for line in f:
        data.append(json.loads(line)) #load per line, needed for the jsonl format
        
# The resources (ie. individual links to specific files)are nested within the larger dataset JSON (CKAN also calls datasets packages, FYI)
for d in data:
        dataset_name_en.append(d['title_translated']['en'])
        dataset_name_fr.append(d['title_translated']['fr'])
        dataset_directorate.append(d['directorate'])
        dataset_division.append(d['division'])
        dataset_project.append(d['project'])
        science_admin.append(d['science_admin'])
        data_stewards.append(d['data_steward'])    
        release_date.append(d['date_published'])

# Replacing unassigned division/directorate with appropriate labels and replacing underscores with spaces
dataset_division = ["unassigned division" if x == '' else x for x in dataset_division]
dataset_division = [w.replace('_', ' ') for w in dataset_division]
dataset_directorate = ["unassigned directorate" if x == '' else x for x in dataset_directorate]
dataset_directorate = [w.replace('_', ' ') for w in dataset_directorate]
data_stewards = ["unassigned steward" if x == '' else x for x in data_stewards]

directorate = [w.replace('_', ' ') for w in directorate]
division = [w.replace('_', ' ') for w in division]

# %%

headers = ["Dataset Name (EN)", "Dataset Name (FR)", "Directorate", "Division", "Project", "Science Admin", "Data Steward", "Release_Date"]

# new file generated with all relevant lists appended to csv file
with open(outfile, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(i for i in headers)
    writer.writerows(zip(dataset_name_en,dataset_name_fr,dataset_directorate, dataset_division, dataset_project, science_admin, data_stewards, release_date))

#reading csv file generated from list into dataframe
col_list = ["Dataset Name (EN)","Directorate", "Division", "Project", "Science Admin", "Data Steward", "Release_Date"]
csv_data = pandas.read_csv(outfile, usecols = col_list)

views_list = ['title', 'total views']
read_views = pandas.read_csv(views_infile, usecols = views_list)

# %%

csv_data.Release_Date = pandas.to_datetime(csv_data.Release_Date)
csv_data.Release_Date = csv_data['Release_Date'].dt.year
groupByDate = csv_data.groupby(['Release_Date'])
dateCounter = groupByDate.count()
groupByDateColumn = dateCounter['Dataset Name (EN)']
print(groupByDateColumn.sort_values(ascending=False))

groupByDateDirectorate = csv_data.groupby(['Release_Date', 'Directorate'])
dateDirectorateCounter = groupByDateDirectorate.count()
groupByDateDirectorateColumn = dateDirectorateCounter['Dataset Name (EN)']
print(groupByDateDirectorateColumn.sort_values(ascending=False))

groupByDataSteward = csv_data.groupby(['Data Steward'])
dataStewardCounter = groupByDataSteward.count()
dataStewardCounterColumn = dataStewardCounter['Dataset Name (EN)']
dataStewardCounterColumn.to_csv('dataSteward_' + date + '.csv', encoding = 'utf-8')
print(dataStewardCounterColumn.sort_values(ascending=False))

# grouping by categories, saving relevant information to dataframe and then external csv files

groupByAdminDivision = csv_data.groupby(['Division', 'Science Admin'])
adminCounterDivision = groupByAdminDivision.count()
adminCounterColumnDivision = adminCounterDivision['Dataset Name (EN)']
adminCounterColumnDivision.to_csv('scienceAdminDivision_' + date + '.csv', encoding = 'utf-8')

groupByAdminDirectorate = csv_data.groupby(['Directorate', 'Science Admin'])
adminCounterDirectorate = groupByAdminDirectorate.count()
adminCounterColumnDirectorate = adminCounterDirectorate['Dataset Name (EN)']
adminCounterColumnDirectorate.to_csv('scienceAdminDirectorate_' + date + '.csv', encoding = 'utf-8')

groupByProject = csv_data.groupby(['Project'])
projectCounter = groupByProject.count()
pCounterColumn = projectCounter['Dataset Name (EN)']
print(pCounterColumn.sort_values(ascending=False))
pCounterColumn.to_csv('datasetProjectCount' + date + '.csv', encoding = 'utf-8')

groupByDivision = csv_data.groupby(['Division'])
divisionCounter = groupByDivision.count()
divCounterColumn = divisionCounter['Dataset Name (EN)']
print(divCounterColumn.sort_values(ascending=False))
divCounterColumn.to_csv('datasetDivisionCount' + date + '.csv', encoding = 'utf-8')

groupByDirectorate = csv_data.groupby(['Directorate'])
dirCounter = groupByDirectorate.count()
dirCounterColumn = dirCounter['Dataset Name (EN)']
print(dirCounterColumn.sort_values(ascending=False))
dirCounterColumn.to_csv('datasetDirectorateCount' + date + '.csv', encoding = 'utf-8')

# %%

# read # of views for each dataset and if # of views is greater than 30, then include in graph, else include in csv 
viewCounterColumn = pandas.DataFrame(data=read_views)

viewCounterColumn.rename(columns = {'total views':'total_views'}, inplace = True)
high_views = pandas.DataFrame()
low_views = pandas.DataFrame()

viewCounterColumn = viewCounterColumn.sort_values(['total_views'], ascending=[False], ignore_index = True)
print(viewCounterColumn)

for i in range(len(viewCounterColumn)):
    if viewCounterColumn.total_views[i] > 30:
        high_views = high_views.append(viewCounterColumn.loc[i,:], ignore_index = True)
    if viewCounterColumn.total_views[i] <= 30:
        low_views = low_views.append(viewCounterColumn.loc[i,:], ignore_index = True)

low_views.to_csv('datasetViews_' + date + '.csv', encoding = 'utf-8')

high_views_graph = high_views.plot.bar(figsize=(20, 10), x = 'title')
plt.title('Dataset Views')
plt.ylabel('# of Datasets')
label_graphs(high_views_graph)
plt.xticks(rotation=25, ha='right')
high_views_graph = "datasetViews_" + date + ".png"
plt.savefig(high_views_graph, bbox_inches = "tight")
plt.show()

# %%

# using relevant information from dataframes to turn into graphs

plt.rc('font', size=14)

graph_1 = pCounterColumn.sort_values(ascending = False).plot.bar(color = "#ffc107", figsize=(15, 9),  align='center')
label_graphs(graph_1)
plt.title('Dataset Count by Project')
plt.ylabel('# of Datasets')
plt.xticks(rotation=25, ha='right')
graph1 = "datasetProjectCount_" + date + ".png"
plt.savefig(graph1, bbox_inches = "tight")
plt.show()

graph_2 = divCounterColumn.sort_values(ascending = False).plot.bar(color = "#3663A2", figsize=(30, 12))
label_graphs(graph_2)
plt.title('Dataset Count by Division')
plt.ylabel('# of Datasets')
plt.xticks(rotation=25, ha='right', wrap = True)
graph2 = "datasetDivisionCount_" + date + ".png"
plt.savefig(graph2, bbox_inches = "tight")
plt.show()

graph_3 = dirCounterColumn.sort_values(ascending = False).plot.bar(color = "#e60000", figsize=(20, 9))
label_graphs(graph_3)
plt.title('Dataset Count by Directorate')
plt.ylabel('# of Datasets')
plt.xticks(rotation=25, ha='right', wrap = True)
graph3 = "datasetDirectorateCount_" + date + ".png"
plt.savefig(graph3, bbox_inches = "tight")
plt.show()

# creating dataframe from csv file 
divisionAdminData = pandas.read_csv('scienceAdminDivision_' + date + '.csv')
directorateAdminData = pandas.read_csv('scienceAdminDirectorate_' + date +'.csv')

# creating more graphs from dataframes sorted further by Science or Management
plt.rc('font', size=20)

managementDivision = divisionAdminData[divisionAdminData['Science Admin'].astype(str).str.contains("False")]
graph_4 = managementDivision.sort_values(by='Dataset Name (EN)', ascending = False).plot.bar(x="Division", legend = False, color = "#3663A2", figsize=(18, 15))
label_graphs(graph_4)
plt.title('Management: Dataset Count by Division')
plt.ylabel('# of Datasets')
plt.xticks(rotation=25, ha='right', wrap = True)
graph4 = "ManagementDivisionCount_" + date + '.png'
plt.savefig(graph4, bbox_inches = "tight")
plt.show()

scienceDivision = divisionAdminData[divisionAdminData['Science Admin'].astype(str).str.contains("True")]
graph_5 = scienceDivision.sort_values(by='Dataset Name (EN)', ascending = False).plot.bar(x="Division", legend = False, color = "#3663A2", figsize=(18, 15))
label_graphs(graph_5)
plt.title('Science: Dataset Count by Division')
plt.ylabel('# of Datasets')
plt.xticks(rotation=25, ha='right', wrap = True)
graph5 = "ScienceDivisionCount_" + date + '.png'
plt.savefig(graph5, bbox_inches = "tight")
plt.show()

plt.rc('font', size=22)
managementDirectorate = directorateAdminData[directorateAdminData['Science Admin'].astype(str).str.contains("False")]
graph_6 = managementDirectorate.sort_values(by='Dataset Name (EN)', ascending = False).plot.bar(x="Directorate", legend = False, color = "#e60000", figsize=(18, 15))
label_graphs(graph_6) 
plt.title('Management: Dataset Count by Directorate')
plt.ylabel('# of Datasets')
plt.xticks(rotation=25, ha='right', wrap = True)
graph6 = "ManagementDirectorateCount_" + date + '.png'
plt.savefig(graph6, bbox_inches = "tight")
plt.show()

scienceDirectorate = directorateAdminData[directorateAdminData['Science Admin'].astype(str).str.contains("True")]
graph_7 = scienceDirectorate.sort_values(by='Dataset Name (EN)', ascending = False).plot.bar(x="Directorate", legend = False, color = "#e60000", figsize=(18, 15)) # figsize=(5, 5)
label_graphs(graph_7)
plt.title('Science: Dataset Count by Directorate')
plt.ylabel('# of Datasets')
plt.xticks(rotation=25, ha='right', wrap = True)
plt.yticks(np.arange(0, 21, 5))
graph7 = "ScienceDirectorateCount_" + date + '.png'
plt.savefig(graph7, bbox_inches = "tight")
plt.show()

graph_8 = groupByDateColumn.plot.bar(figsize=(18, 15)) # figsize=(5, 5)
label_graphs(graph_8)
plt.title('Dataset Publication Count by Year')
plt.ylabel('# of Datasets')
plt.xlabel('Release Year')
plt.xticks(rotation=25, ha='right', wrap = True)
graph8 = "DatasetPerYear_" + date + '.png'
plt.savefig(graph7, bbox_inches = "tight")
plt.show()

# %%
# Printing missing directorates and divisions

missing_directorates = list(set(directorate)^set(dataset_directorate))
missing_directorates.remove("unassigned directorate")
print(missing_directorates)  

missing_divisions = list(set(division)^set(dataset_division))
missing_divisions.remove("unassigned division")
print(missing_divisions) 

# %%

print('done')