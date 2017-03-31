#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print len(enron_data.keys())
print len(enron_data.values()[0])
poi = 0
for k,v in enron_data.items():
	if enron_data[k]["poi"] is True:
		poi = poi +1
print poi

poi_names = open("../final_project/poi_names.txt").read().split('\n')
poi_y = [name for name in poi_names if "(y)" in name]
poi_n = [name for name in poi_names if "(n)" in name]
print("poi_names_count:", len(poi_y+poi_n))
print enron_data["PRENTICE JAMES"]["total_stock_value"]	
#print enron_data["COLWELL WESLEY"]
print enron_data["SKILLING JEFFREY K"]
poi = 0
for k in enron_data.keys():
	if enron_data[k]["salary"] != 'NaN':
		poi = poi +1
print poi
poi =0
for k in enron_data.keys():
        if enron_data[k]["email_address"] != 'NaN':
                poi = poi +1
print poi		
