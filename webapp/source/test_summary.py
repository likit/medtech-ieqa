import pymongo
import numpy as np
import sys

db = pymongo.Connection()['ieqa-dev']
test_name = sys.argv[1]
test_method = '%s_method' % test_name

test_methods = set()
for r in db.results.find():
    if r[test_method]:
        test_methods.add(r[test_method])

test_values = {}
for m in test_methods:
    tests = []
    for r in db.results.find({test_method: m}):
        if r[test_name]:
            tests.append(r[test_name])
    test_values[m] = tests

all_methods = []


def calculate(values, principle):
    mean = np.mean(values)
    std = np.std(values)
    print '\n' + principle
    print '-----------------'
    print 'N = %d' % (len(values))
    print "mean = {0:f}".format(mean)
    print "SD = {0:f}".format(std)
    print "%CV = {0:f}".format(std / mean * 100.0)
    print "mean + 1.5SD = {0:f}".format(mean + 1.5 * std)
    print "mean - 1.5SD = {0:f}".format(mean - 1.5 * std)


for m in test_methods:
    calculate(test_values[m], m)
    all_methods += test_values[m]

principle = "All"

calculate(all_methods, principle)
