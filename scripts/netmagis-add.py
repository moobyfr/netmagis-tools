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
URL = config.get('netmagis', 'URL')
DOMAINE = config.get('netmagis', 'DOMAINE')
IDDHCPPROFIL = config.get('netmagis', 'IDDHCPPROFIL')
HINFO = config.get('netmagis', 'HINFO')
COMMENTAIRE = config.get('netmagis', 'COMMENTAIRE')
REALM = config.get('netmagis', 'REALM')
LOGIN = config.get('netmagis', 'LOGIN')
PASS = config.get('netmagis', 'PASS')



nnom = sys.argv[1]
nip = sys.argv[2]
nmac = sys.argv[3]


data = {'action': 'add-host',
	'confirm': 'no',
	'naddr': '1',
	'name': nnom,
	'domain': DOMAINE,
	'addr': nip,
	'idview': 1,
	'ttl': '',
	'mac': nmac,
	'iddhcpprof': IDDHCPPROFIL,
	'hinfo': HINFO,
	'comment': COMMENTAIRE,
	'respname': '',
	'respmail': ''}
	

auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password(realm=REALM,
                           uri=URL,
			   user=LOGIN,
			   passwd=PASS)
opener = urllib2.build_opener(auth_handler)
file_handle = opener.open(URL, urllib.urlencode(data))

print file_handle.read()

