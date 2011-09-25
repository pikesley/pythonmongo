#!/usr/bin/env python

from pymongo import Connection
import yaml
import json
import time
import random

# Possible types for out objects
types = ['foo', 'bar', 'baz']

# Dummy class
class Dummy(dict):
    def __init__(self):

# Set some values
        self['ts'] = time.time()
        self['value'] = random.randint(0, 99)
        self['type'] = random.choice(types)
        self['class'] = self.__class__.__name__

        self.set_dimensions()

# Set an embedded dict
    def set_dimensions(self):
        d = {}
        d['x'] = random.randint(0, 10)
        d['y'] = random.randint(0, 10)

        self['dimensions'] = d

# Save to the DB
    def save(self, clxn):
        clxn.insert(self)

# Get our config
yamlpath = 'config/config.yaml'
f = open(yamlpath, 'r')
y = yaml.load(f)
d = y['mongo']

# Mongo connection
cnxn = Connection(d['host'], d['port'])

# A Mongo DB
db = cnxn[d['db']]

# We might wanna authenticate
#db.authenticate(d['user'], d['pass'])

# A Mongo collection
c = db[d['collection']]

# Clean up before we start
c.drop()

# Create and insert some of our objects
for i in range(10):
    d = Dummy()
    d.save(c)

# Find all of the entries of type 'foo'
d = c.find({'type': 'foo'})
for e in list(d):
    print e
