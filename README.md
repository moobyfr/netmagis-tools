netmagis-tools
==============

netmagis-tools is a cli interface for netmagis, written in python.
Now, you can script netmagis actions.

Adapt the config.ini from reference, to mach your parameters

Examples:
-----

With the basic .py files:

  - add an new entry
```bash
  python netmagis-add.py foo 192.168.1.1 11:22:33:44:55:66
```
  - add a cname
```bash
  python netmagis-addvhost.py foo u-strasbg.fr bar unistra.fr
```
  - delete an ip
```bash
  python netmagis-deleteip.py 192.168.1.1
```
  - delete a name
```bash
  python netmagis-deletename.py foo u-strasbg.fr
```
