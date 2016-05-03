__author__ = 's'

f = open("distance_matrix_1698.csv","r+")
a = []
k=0
for line in iter(f):
    if (k==5) :
        break
    k +=1


a = line.split(",")
print len(a)+1698
print a[2]







