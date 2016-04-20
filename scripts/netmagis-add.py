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
CAS_SERVER = config.get('netmagis', 'CAS_SERVER')

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
        'respmail': ''
        }

mynmc = netmagisclient.NetmagisClient(URL, CAS_SERVER)
mynmc.caslogin(LOGIN, PASS)
mynmc.add(data)

exit(0)
