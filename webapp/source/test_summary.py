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

for m in test_methods:
    print m, np.mean(test_values[m]), '(%d)' % len(test_values[m])

