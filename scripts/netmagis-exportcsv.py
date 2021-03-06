#!/usr/bin/python
import configparser

from netmagisclient import netmagisclient

config = configparser.ConfigParser()
config.readfp(open('config.cfg'))
URL = config.get('netmagis', 'URL')
DOMAINE = config.get('netmagis', 'DOMAINE')
IDDHCPPROFIL = config.get('netmagis', 'IDDHCPPROFIL')
HINFO = config.get('netmagis', 'HINFO')
COMMENTAIRE = config.get('netmagis', 'COMMENTAIRE')
LOGIN = config.get('netmagis', 'LOGIN')
PASS = config.get('netmagis', 'PASS')
CAS_SERVER = config.get('netmagis', 'CAS_SERVER')

data = {'plage': ['50', '51']}

mynmc = netmagisclient.NetmagisClient(URL, CAS_SERVER)
mynmc.caslogin(LOGIN, PASS)
mynmc.exportcsv(data)
exit(0)
