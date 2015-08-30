netmagis-tools
==============

netmagis-tools is a cli interface for netmagis, written in python.
Now, you can script netmagis actions.

Adapt the config.ini from reference, to mach your parameters

Examples:

add an new entry

  python netmagis-add.py foo 192.168.1.1 11:22:33:44:55:66

add a cname

  python netmagis-addvhost.py foo u-strasbg.fr bar unistra.fr

delete an ip

  python netmagis-deleteip.py 192.168.1.1

delete a name

  python netmagis-deletename.py foo u-strasbg.fr

