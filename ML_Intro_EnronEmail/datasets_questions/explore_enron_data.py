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
import sys
import pickle
import math

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
#print enron_data["LAY KENNETH L"]
noneCt = 0
validCt = 0

for key, value in enron_data.iteritems() : 
    salary = float(value["total_payments"])
    if math.isnan(salary) :
        noneCt = noneCt + 1
    else :
        validCt = validCt + 1

bigEso = 0.0
smallEso = sys.maxint
for key, value in enron_data.iteritems() : 
    eso = float(value["exercised_stock_options"])
    if math.isnan(eso) : continue
    if eso < smallEso :
        smallEso = eso
    if eso > bigEso :
        bigEso = eso

print "smallEso", smallEso
print "bigEso", bigEso
        
print noneCt , validCt        
ratio = noneCt / ((noneCt + validCt) * 1.0)
print ratio

#print emailCt
#print salaryCt
        


        

