__author__ = 's'
import mysql.connector
import numpy as np
import time
import datetime as d
import copy
import sys

#establishing database connection
#cnx = mysql.connector.connect(user='root', password='',
#                              host='127.0.0.1',
#                             database='thesis')

# get a cursor to execute sql queries
#c = cnx.cursor(buffered= True)

# function to calculate the similarity based on longest common subsequences
# traj1, traj2 are the two input trajectories. Epsilon is the permittable distance between two points and sigma is the permittable
# time gap between two points

def similarity_lcss(traj1,traj2) :
    #print len(traj1),len(traj2)

    score = 0
    min_traj = 0
    if(len(traj1)>len(traj2)) :
        min_traj = len(traj2)
    else :
        min_traj = len(traj1)

    # variables to store trajectories of different days
    traj1_fri = []
    traj1_sat = []
    traj1_sun = []
    traj1_mon = []
    traj1_tue = []
    traj1_wed = []
    traj1_thu = []

    traj2_fri = []
    traj2_sat = []
    traj2_sun = []
    traj2_mon = []
    traj2_tue = []
    traj2_wed = []
    traj2_thu = []

    # dividing the user trajectories into different days
    for row in traj1 :
        if row[1] == '"Fri"' :
            #print "inside fri"
            traj1_fri.append(row)
        elif row[1] == '"Sat"' :
            #print "inside fri"
            traj1_sat.append(row)
        elif row[1] == '"Sun"' :
            #print "inside fri"
            traj1_sun.append(row)
        elif row[1] == '"Mon"' :
            #print "inside fri"
            traj1_mon.append(row)
        elif row[1] == '"Tue"' :
            #print "inside fri"
            traj1_tue.append(row)
        elif row[1] == '"Wed"' :
            #print "inside fri"
            traj1_wed.append(row)
        elif row[1] == '"Thu"' :
            #print "inside fri"
            traj1_thu.append(row)
    for row in traj2 :
        if row[1] == '"Fri"' :
            traj2_fri.append(row)
        elif row[1] == '"Sat"' :
            traj2_sat.append(row)
        elif row[1] == '"Sun"' :
            traj2_sun.append(row)
        elif row[1] == '"Mon"' :
            traj2_mon.append(row)
        elif row[1] == '"Tue"' :
            traj2_tue.append(row)
        elif row[1] == '"Wed"' :
            traj2_wed.append(row)
        elif row[1] == '"Thu"' :
            traj2_thu.append(row)

    if len(traj1_fri)<len(traj2_fri) :
        score = score + cal_sim(traj1_fri,traj2_fri)
    else :
        score = score + cal_sim(traj2_fri,traj1_fri)
    if len(traj1_sat)<len(traj2_sat) :
        score = score + cal_sim(traj1_sat,traj2_sat)
    else :
        score = score + cal_sim(traj2_sat,traj1_sat)
    if len(traj1_sun)<len(traj2_sun) :
        score = score + cal_sim(traj1_sun,traj2_sun)
    else :
        score = score + cal_sim(traj2_sun,traj1_sun)
    if len(traj1_mon)<len(traj2_mon) :
        score = score + cal_sim(traj1_mon,traj2_mon)
    else :
        score = score + cal_sim(traj2_mon,traj1_mon)
    if len(traj1_tue)<len(traj2_tue) :
        score = score + cal_sim(traj1_tue,traj2_tue)
    else :
        score = score + cal_sim(traj2_tue,traj1_tue)
    if len(traj1_wed)<len(traj2_wed) :
        score = score + cal_sim(traj1_wed,traj2_wed)
    else :
        score = score + cal_sim(traj2_wed,traj1_wed)
    if len(traj1_thu)<len(traj2_thu) :
        score = score + cal_sim(traj1_thu,traj2_thu)
    else :
        score = score + cal_sim(traj2_thu,traj1_thu)

    #print "the score is ",score
    distance = float(score)/min_traj
    distance = float(1) - float(distance)
    return distance

'''def cal_sim (traj1,traj2) :
    score = 0

    while len(traj1)>0 and len(traj2)>0 :

            if traj1[len(traj1)-1][2] == traj2[len(traj2)-1][2] and traj1[len(traj1)-1][0] == traj2[len(traj2)-1][0]:
                score +=1
                traj1.pop()
                traj2.pop()
            elif traj1[len(traj1)-1][2] > traj2[len(traj2)-1][2] :
                traj1.pop()
            elif traj1[len(traj1)-1][2] < traj2[len(traj2)-1][2]:
                traj2.pop()
            elif traj1[len(traj1)-1][2] == traj2[len(traj2)-1][2] :
                i = 2

                #print traj1[len1][2],traj1[len1-1][2],traj2[len2][2],len1,len2,traj2[len2-1][2]
                if traj1[len(traj1)-2][2] == traj2[len(traj2)-1][2] :
                    traj1.pop()
                elif traj1[len(traj1)-1][2] == traj2[len(traj2)-2][2] :
                    traj2.pop()
                else :
                    traj1.pop()
                    traj2.pop()


    return score'''

'''def cal_sim(traj1,traj2) :
    score = 0
    len2 = len(traj2)-1
    while len(traj1)>0 :
        while len2>-1 :
            if traj1[len(traj1)-1][2] == traj2[len2][2] :
                if traj1[len(traj1)-1][0]== traj2[len2][0] :
                    score += 1
                len2 -=1
            elif traj1[len(traj1)-1][2] > traj2[len2][2] :
                break
            elif traj1[len(traj1)-1][2] < traj2[len2][2] :
                len2 -=1
        traj1.pop()

    return score'''

def cal_sim(traj1,traj2) :
    score = 0
    temp =0
    while len(traj2)>0 :
        len2 = len(traj1)-1
        while len2>-1 :
            if traj2[len(traj2)-1][2] == traj1[len2][2] :
                if traj2[len(traj2)-1][0]== traj1[len2][0] :
                    score += 1
            len2 -=1
        traj2.pop()
    return score

'''def cal_sim(traj1,traj2) :
    score = 0
    temp = len(traj2)-1
    while len(traj1)>0 :
        len2 = temp
        while len2>-1 :
            if traj1[len(traj1)-1][2] == traj2[len2][2] :
                if traj1[len(traj1)-1][0]== traj2[len2][0] :
                    score += 1
                temp = len2
            len2 -=1
        traj1.pop()
    return score'''
#the similarity matrix between 8357 users initialized with value 1
distance=np.zeros((8357,8357))


# list to store all the user ids
'''lst = []
c.execute("select distinct userid from fulldata")
for a in c :
    lst.append(a)'''

#read data directly from file
f = open('/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv');
f1 = open('distance_matrix_full.csv','r+')
f2 = open('distance_matrix_full_withoutid.csv','r+')

k=0
traj1 = []
traj2 = []
userid = 0
usernum = 0
tuple = []
lst_users = []
for line in iter(f):
    if(k==0):
        k= k+1

    else :
        m=line.split(",")
        if userid == int(m[0]) :
            tuple = []
            #tuple.append(m[0])
            tuple.append(m[1])
            tuple.append(str(m[2]))
            tuple.append(m[3])
            traj2.append(tuple)
        else :

            userid = int(m[0])
            if len(traj2)>0 :
                traj1.append(traj2)
            traj2 = []
            tuple = []
            #tuple.append(m[0])
            lst_users.append(m[0])
            tuple.append(m[1])
            tuple.append(str(m[2]))
            tuple.append(m[3])
            traj2.append(tuple)

traj1.append(traj2)
print lst_users[1697]
temp=0
for line in iter(f2) :

        #print m[0],m[1],m[2],m[3]
j=0

while j<8356 :
     print "j=",j
     user1 = []
     user1 = copy.deepcopy(traj1[j])
     i=j+1
     s = []
     while(i<8357) :
         user2 = []
         user2 = copy.deepcopy(traj1[i])
         distance[j][i] = similarity_lcss(user1,user2)
         distance[i][j] = distance[j][i]
         i +=1
     k=0
     f1.write(str(lst_users[j]))
     f1.write(",")
     f1.write(str(distance[j][k]))

     f2.write(str(distance[j][k]))
     k = 1
     while k< 8357:
         f1.write(",")
         f1.write(str(distance[j][k]))
         f2.write(",")
         f2.write(str(distance[j][k]))
         k +=1
     f1.write("\n")
     f2.write("\n")
     j += 1
k=0
f1.write(str(lst_users[j]))
f1.write(",")
while k<8357 :
    f1.write(str(distance[8356][k]))
    f1.write(",")
    f2.write(str(distance[8356][k]))
    f2.write(",")
    k +=1'''
