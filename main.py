import ConfigParser
from numpy.random import multinomial
from numpy import array
import csv
import time
import sys
from sumatra.projects import load_project
from sumatra.parameters import build_parameters
from os import popen

parameter_file = sys.argv[1]
parameters = build_parameters(parameter_file)
parameters.update({"parameter_file":parameter_file})

project = load_project()
record = project.new_record(parameters=parameters,
                            main_file=__file__,
                            reason="reason for running this simulation")
                            
parameters.update({"sumatra_label": record.label})
start_time = time.time()

cmd = r"/c/program files/R/R-2.15.0/bin/Rscript.exe main.r %s %s" % (parameter_file,record.label)
print "Running command", cmd
fin = popen(cmd)
print fin.read()
fin.close()

record.duration = time.time() - start_time
record.output_data = record.datastore.find_new_data(record.timestamp)
project.add_record(record)

project.save()
print parameters
