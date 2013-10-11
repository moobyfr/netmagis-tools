#!/usr/bin/python
import httplib
import sys
import urllib
import urllib2
import base64
import string
import ConfigParser


config = ConfigParser.ConfigParser()
config.readfp(open('config.cfg'))
URL = config.get('netmagis', 'URL')+"add"
DOMAINE = config.get('netmagis', 'DOMAINE')
IDDHCPPROFIL = config.get('netmagis', 'IDDHCPPROFIL')
HINFO = config.get('netmagis', 'HINFO')
COMMENTAIRE = config.get('netmagis', 'COMMENTAIRE')
REALM = config.get('netmagis', 'REALM')
LOGIN = config.get('netmagis', 'LOGIN')
PASS = config.get('netmagis', 'PASS')


pnom = sys.argv[1]
pnom2 = sys.argv[3]
pdom = sys.argv[2]
pdom2 = sys.argv[4]

# Appel addvhost cname cnamedomain target targetdomain

data = {'action': 'add-alias',
	'domain': pdom,
	'domainref': pdom2,
	'idview': 1,
	'name': pnom,
	'nameref': pnom2
	}
	

auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password(realm=REALM,
                           uri=URL,
			   user=LOGIN,
			   passwd=PASS)
opener = urllib2.build_opener(auth_handler)
file_handle = opener.open(URL, urllib.urlencode(data))

print file_handle.read()













