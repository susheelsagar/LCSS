__author__ = 's'
import numpy as n
f = open("distance2.csv", "r+")
s = []
s.append(0)
s.append(",")
s.append(1)

f.write(str(s))
f.write("hello")
f.write("\n")
f.write(str(s))
similarity = n.zeros((2,2))
similarity[1][0] = 2
similarity [0][1] = similarity [1][0]
similarity[1][0] -= 1
print similarity[1][0],similarity[0][1]

