#!/usr/bin/python
import ConfigParser
import sys

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


naddr = sys.argv[1]
nomreseau = sys.argv[2]
#example
#nomreseau = "130.79.80.0/23 2001:660:4703:2001::/64 (IUT Sud)"

data = {'action': 'add-multi',
	'naddr': naddr,
	'idview': 1,
	'plage': nomreseau,
	}

mynmc = netmagisclient.NetmagisClient(URL,CAS_SERVER)
mynmc.caslogin(LOGIN,PASS)
print(mynmc.looklarge(data))


exit(0)

