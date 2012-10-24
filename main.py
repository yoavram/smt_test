import ConfigParser
from numpy.random import multinomial
from numpy import array
import csv
import time
import sys

print "Strating"
c = ConfigParser.ConfigParser()
c.read(sys.argv[1])

popsize = c.getint("default","popsize")
fpopsize = float(popsize)
ticks = c.getint("default","ticks")

x = [None]*ticks
x[0] = array([popsize/2, popsize/2])
t = 1

while t < ticks:
    x[t] = multinomial(popsize, x[t-1]/fpopsize)
    t += 1

fout = open("Data/smt-test_"+str(time.time())+".csv","wb")
wr = csv.writer(fout)
wr.writerows(x)
fout.close()
print "Closing"
