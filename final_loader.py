
import numpy as np
f = open("distance_matrix_full.csv","r+")
j=0
i=0
lst_users = []
distance = np.zeros((8357,8357))
for line in iter(f) :
    a = []
    j=0
    k=1
    a = line.split(",")
    lst_users.append(a[0])
    while(k<len(a)):
        distance[i][j] = a[k]
        distance[j][i] = distance [i][j]
        j +=1
        k +=1
    i +=1
temp = 0
f1 = open("distance_matrix_1698.csv","r+")
for line in iter(f1) :
    print i
    a = []
    k=1
    j=i
    a = line.split(",")
    lst_users.append(a[0])
    while(k<len(a)):
        if i == 8356 :
            print k,j
        distance[i][j] = a[k]
        distance[j][i] = distance [i][j]
        j+=1
        k+=1

    i+=1
i=0
f2 = open("distance_matrix_final.csv","r+")
f3 = open("distance_matrix_final_withoutid.csv","r+")
while i<8357:
    j=0
    f2.write(str(lst_users[i]))
    f2.write(",")
    f2.write(str(distance[i][j]))
    f3.write(str(distance[i][j]))
    j=1
    while j<8357:
        f2.write(",")
        f2.write(str(distance[i][j]))
        f3.write(",")
        f3.write(str(distance[i][j]))
        j+=1
    f2.write("\n")
    f3.write("\n")
    i+=1

