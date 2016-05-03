__author__ = 's'
__author__ = 's'
import mysql.connector
import numpy as np
import time
import datetime as d
import copy
import sys

#establishing database connection
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                             database='thesis')

# get a cursor to execute sql queries
c = cnx.cursor(buffered= True)

# function to calculate the similarity based on longest common subsequences
# traj1, traj2 are the two input trajectories. Epsilon is the permittable distance between two points and sigma is the permittable
# time gap between two points

def similarity_lcss(traj1,traj2) :
    #print len(traj1),len(traj2)

    score = 0

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
def cal_sim (traj1,traj2) :
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


    return score





#the similarity matrix between 8357 users initialized with value 1
similarity=np.ones((8357,8357))


# list to store all the user ids
lst = []
c.execute("select distinct userid from fulldata")
for a in c :
    lst.append(a)

#read data directly from file
f = open('/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv');
k=0
traj1 = []
traj2 = []
userid = 0
usernum = 0
tuple = []
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
            tuple.append(m[1])
            tuple.append(str(m[2]))
            tuple.append(m[3])
            traj2.append(tuple)

traj1.append(traj2)

print len(traj1)
        #print m[0],m[1],m[2],m[3]
j=0
while j<8356 :
     print j
     user1 = []
     user1 = copy.deepcopy(traj1[j])
     i=j+1
     while(i<8357) :
         user2 = []
         user2 = copy.deepcopy(traj1[i])
         similarity_lcss(user1,user2)
         i +=1
     j = j+1




'''
#  the time difference between the two data points of two diff trajectories
time_diff = 15;

# load all the user ids into a list 'lst'
for a in c :
    lst.append(a)
len(lst)
lst2 = lst
user_num=0
user_id =0
traj1 = []
traj2 = []

while (user_num<len(lst)) :
    for row in  lst[user_num] :
       user_id = row;
    c.execute("select siteid,weekday,timing from fulldata where userid =  " + str(user_id) );
    for siteid,weekday,timing in c :
        tuple = []
        tuple.append(siteid)
        tuple.append(weekday)
        tuple.append(timing)
        traj1.append(tuple)

    next_user = user_num+1
    while (next_user < len(lst)) :
        for row in lst[next_user] :
            user_id = row;

        traj2 = []
        c.execute("select siteid,weekday,timing from fulldata where userid =  " + str(user_id) );
        for siteid,weekday,timing in c :
            tuple = []
            tuple.append(siteid)
            tuple.append(weekday)
            tuple.append(timing)
            traj2.append(tuple)
        print next_user
        similarity_lcss(traj1,traj2)
        next_user +=1
        #break



    break'''

cnx.close()


