import ConfigParser
from numpy.random import multinomial
from numpy import array
import csv
import time
import sys
from sumatra.projects import load_project
from sumatra.parameters import build_parameters

def main(parameters):
    popsize = parameters["pop.size"]
    fpopsize = float(popsize)
    ticks = parameters["ticks"]

    x = [None]*ticks
    x[0] = array([popsize/2, popsize/2])
    t = 1

    while t < ticks:
        x[t] = multinomial(popsize, x[t-1]/fpopsize)
        t += 1
    fout_name = "Data/smt_test_%s.csv" % parameters["sumatra_label"]
    fout = open(fout_name,"wb")
    wr = csv.writer(fout)
    wr.writerows(x)
    fout.close()

parameter_file = sys.argv[1]
parameters = build_parameters(parameter_file)
print parameters
project = load_project()
record = project.new_record(parameters=parameters,
                            main_file=__file__,
                            reason="reason for running this simulation")
                            
parameters.update({"sumatra_label": record.label})
start_time = time.time()

main(parameters)

record.duration = time.time() - start_time
record.output_data = record.datastore.find_new_data(record.timestamp)
project.add_record(record)

project.save()
