#!/usr/bin/env python

from pymongo import Connection
import yaml

yamlpath = 'config/config.yaml'
f = open(yamlpath, 'r')
y = yaml.load(f)
d = y['mongo']

cnxn = Connection(d['host'], d['port'])

db = cnxn[d['db']]
#db.authenticate(d['user'], d['pass'])

c = db['foo']

x = {'name': 'Perl', 'type': 'Degu'}
y = {'name': 'Ruby', 'type': 'Degu'}

c.insert(x)
c.insert(y)
c.save(x)
c.save(y)

print list(c.find())

v = list(c.find(fields='_id'))
for u in v:
    c.remove(u['_id'])
