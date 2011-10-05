#!/usr/bin/env python

from pymongo import Connection
import yaml
import tagpy
import sys
import hashlib
import os
import re

class Track(dict):
    def __init__(self, path):
        self['path'] = path
        self.fileref = tagpy.FileRef(self['path'])

        self.tags = self.fileref.tag()

        self['artist'] = self.tags.artist
        self['track'] = self.tags.track
        self['title'] = self.tags.title
        self['album'] = self.tags.album
        self['year'] = self.tags.year
        self['md5'] = hashlib.md5(self['path']).hexdigest()
        self['file_type'] = self['path'].split('.')[-1]

def populate(drop_first=False):
    if drop_first:
        clxn.drop()

    for d in os.walk(y['paths']['music']):
        for t in d[2]:
            if t.endswith("ogg") or t.endswith("mp3"):
                track = Track(os.path.join(d[0], t))
                if not len(list(clxn.find({'md5': '%s' % track['md5']}))) > 0:
                    clxn.insert(track)
                else:
                    print "%s already exists" % track['path']

    t = clxn.find_one()
    for k in t.keys():
        print "Creating index '%s'" % (k)
        clxn.create_index(k)

yamlpath = 'config/config.yaml'
f = open(yamlpath, 'r')
y = yaml.load(f)
d = y['mongo']

cnxn = Connection(d['host'], d['port'])

db = cnxn[d['db']]
clxn = db[d['collection']]

if __name__ == '__main__':
    populate(False)
#    t = clxn.find({'artist': 'The Beatles'})
#   for x in list(t):
#       print x
