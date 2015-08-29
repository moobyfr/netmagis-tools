#!/usr/bin/python

import sys
import ConfigParser
from netmagisclient import netmagisclient


config = ConfigParser.ConfigParser()
config.readfp(open('config.cfg'))
URL = config.get('netmagis', 'URL')
DOMAINE = config.get('netmagis', 'DOMAINE')
IDDHCPPROFIL = config.get('netmagis', 'IDDHCPPROFIL')
HINFO = config.get('netmagis', 'HINFO')
COMMENTAIRE = config.get('netmagis', 'COMMENTAIRE')
LOGIN = config.get('netmagis', 'LOGIN')
PASS = config.get('netmagis', 'PASS')
CAS_SERVER = config.get('netmagis','CAS_SERVER')


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

mynmc = netmagisclient.NetmagisClient(URL,CAS_SERVER)
mynmc.caslogin(LOGIN,PASS)
mynmc.addvhost(data)
