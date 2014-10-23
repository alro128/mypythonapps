#!/usr/bin/python
# -*- coding: utf-8 -*-


str = "España Comunicación. Nüremberg! á é í ó ú Ñu"

str2 = "Espa\xf1a , 12345, C/ Comunicaci\xf3n"

print str

print
print "Con UTF-8 decode:" + str.decode('utf-8')

print "Con ASCII encode:" + str.decode('utf-8').encode('ascii', 'xmlcharrefreplace')

print str2

print "Con UTF-8 decode:" + str2.decode('Latin-1')

print "Con ASCII encode:" + str2.decode('Latin-1').encode('ascii', 'xmlcharrefreplace')
