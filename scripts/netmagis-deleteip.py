#!/usr/bin/python
import configparser
import sys

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

nip = sys.argv[1]

data = {'addr': nip, }

mynmc = netmagisclient.NetmagisClient(URL, CAS_SERVER)
mynmc.caslogin(LOGIN, PASS)
mynmc.deleteip(data)
exit(0)
