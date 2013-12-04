#author@manjush

import csv as csv
import numpy as np

csv_file_object = csv.reader(open('/home/manjush/titanic/titanic/train2.csv', 'rb')) #Load in the csv file
header = csv_file_object.next()    #Skip the fist line as it is a header
data=[]     #Creat a variable called 'data'
for row in csv_file_object:   #Skip through each row in the csv file
    data.append(row[1:])  #adding each row to the data variable
#print data  #before conversion in to array
data = np.array(data)  #Then convert from a list to an array
#print data #after conversion to array
#for i in range(0,len(data),1):
 #print data[i];
fare_ceiling = 40
print data[0::10]
#data[data[0::11].astype(np.float) >= fare_ceiling, 11] = fare_ceiling-1.0
 
