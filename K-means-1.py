import csv
import random
from random import randint
with open('C:\\Users\\Sharad\\Desktop\\deltaclean2.csv') as datafile:
    reader = csv.reader(datafile) #import csv file
    datalist = [] 
    centroidlist=[]
    n=0
    k=5
    I=20
    for row in reader:
        newrow=list(map(int,row))
        datalist.append(newrow); #Insert data
        n=n+1                   #Get data size

def initialize(centroidlist, k): #initialize clusters
    for i in range(0,k):
        temp = [i]
        for j in range(1,9): #needs to be changed in case of length of tuple changes
            temp.append(random.randint(1,10))
        centroidlist.append(temp)


def distance(datapoint, centroid):  #m is tuple length, will need to be changed in case columns are deleted
    distance=0
    for i in range(1,9):
        distance=distance+((datapoint[i]-centroid[i])**2)
    return (distance**1/2)

class cluster(): #cluster object 
    def __init__(self):
        self.centroid=[]
        self.datapoints=[]
        self.b=0
        self.m=0
        self.error=0

#print([sum(e)/len(e) for e in zip(*x.datapoints)])


initialize(centroidlist,5)

cluster_list=[]
for i in range(0,k):
    cluster_list.append(cluster())# for i in range(k)] # List of clusters
    cluster_list[i].centroid=centroidlist[i]
#    print(cluster_list[i].centroid) #print centroids

for x in range(I): #Main Loop
    for i in range(0,n):
        dist=9999
        temp=0
        for j in range(0,k):
            if distance(datalist[i],cluster_list[j].centroid)<dist: #check for minimum distance
                dist=distance(datalist[i],cluster_list[j].centroid)
                temp=j
 #       print(dist, temp, datalist[i], centroidlist[temp])
        cluster_list[temp].datapoints.append(datalist[i]) #Append data points to cluster
    for y in range(k):
        #print(i,cluster_list[i].datapoints)
        cluster_list[y].centroid=[sum(e)/len(e) for e in zip(*cluster_list[y].datapoints)]
        if (x!=(I-1)):
            cluster_list[y].datapoints=[]

          
#for i in range(k):
#    print(cluster_list[i].centroid)
#    print(cluster_list[i].datapoints)

total_error=0
cl=0
for i in cluster_list:
    for j in i.datapoints:
        if(j[8]==2):
            i.b+=1
        else:
            i.m+=1
    if(i.b>i.m):
        i.error=i.m/(i.b+i.m)
    else:
        i.error=i.b/(i.b+i.m)
    total_error=total_error+i.error
    print("Cluster",cl,":Benign",i.b," Malignant",i.m,"Error Rate",i.error)
    cl+=1
print("Total Error Rate for K:",k,total_error)
