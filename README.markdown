Experiments with Python and MongoDB
===================================

MongoDB 2.0 and pymongo installation:
-------------------------------------

* `sudo apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10`
* `echo "deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen" >> /etc/apt/sources.list`
* `apt-get update`
* `apt-get install mongodb-10gen python-setuptools`
* `easy_install pymongo`

Tagaliser
---------

Indexes your (properly tagged) mp3s/oggs in Mongo. Probably useful for something.

`./tagaliser.py -h`
