__author__ = 's'
import numpy as np
f = open('/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv');
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
print "loading done"
f1 = open('distance_matrix_final.csv')
distance = np.zeros((8357,8357))
i=0
for line in iter(f1):
   a = []
   a = line.split(",")

   if lst_users[i]!=a[0] :
       print 'error',i
   j=0
   k=1
   while k<len(a):
       if float(a[k]) == float(0) :
           if i!=k-1:
               print "error at ",i,k-1
       distance[i][j] = a[k]
       j+=1
       k+=1
   i+=1
i=0
j=0
while i<8357:

    j=0
    while j<8357:
            if distance[i][j] != distance[j][i] :
                print "error at" , i,j
            j+=1
    i+=1