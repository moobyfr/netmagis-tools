netmagis-tools
==============

netmagis-tools is a cli interface for netmagis, written in python.
Now, you can script netmagis actions.

Copy config.cfg.default as config.cfg and adapt the values to mach your parameters

VENV needed:

```bash
virtualenv nm
cd nm
. bin/activate
pip install robobrowser lxml Werkzeug==0.16.1
```

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
  - export as CSV some ranges:
```bash
  python netmagis-exportcsv.py
```
  - return the first IP from an empty range(16 at least) (The value '50' is the internal ID from the network, you can find these values in HTML source for the moment)
```bash
  python netmagis-looklarge.py 16 50
```
    
