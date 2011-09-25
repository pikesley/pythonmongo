#!/usr/bin/env python

from pymongo import Connection
import yaml
import json
import time
import random

types = ['foo', 'bar', 'baz']

class Dummy(dict):
    def __init__(self):
        self['ts'] = time.time()
        self['value'] = random.randint(0, 99)
        self['type'] = random.choice(types)

        self.set_dimensions()

    def set_dimensions(self):
        d = {}
        d['x'] = random.randint(0, 10)
        d['y'] = random.randint(0, 10)

        self['dimensions'] = d

    def save(self, clxn):
        clxn.insert(self)

yamlpath = 'config/config.yaml'
f = open(yamlpath, 'r')
y = yaml.load(f)
d = y['mongo']

cnxn = Connection(d['host'], d['port'])

db = cnxn[d['db']]
#db.authenticate(d['user'], d['pass'])

c = db[d['collection']]

for i in range(10):
    d = Dummy()
    d.save(c)

d = c.find({'type': 'foo'})
for e in list(d):
    print e
