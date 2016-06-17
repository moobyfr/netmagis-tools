from robobrowser import RoboBrowser


def is_id_form(form):
    return "id" in form.attrs and form.attrs['id'] == "fm1"


class NetmagisClient(object):

    url = None     # Netmagis's URL
    casurl = None  # CAS's URL
    br = None      # the browser reference
    c = None
    s = None

    def __init__(self, url, casurl):
        self.url = url
        self.casurl = casurl
        self.br = RoboBrowser()

    # call the loginURL to authenticate
    def caslogin(self, login, passwd):
        uri = self.casurl+"?service="+self.url+"start"
        print("LOGIN IN PROGRESS : %s" % uri)
        self.br.open(uri)
        form = self.br.get_form()
        form['username'].value = login
        form['password'].value = passwd
        response2 = self.br.submit_form(form)
        print(response2)
        print("LOGIN ENDED")

    def addvhost(self, data):  # XXX
        uri = self.url+"add"
        print("ADDVHOST IN PROGRESS : %s", uri)
        self.br.open(uri)
        f = self.br.get_forms()[2]
        f["name"] = data["name"]
        f["domain"] = data["domain"]
        f["nameref"] = data["nameref"]
        f["domainref"] = data["domainref"]
        self.br.submit_form(f)
        returnaddvhost = self.br.response.content.decode('utf8')
        if 'An error occurred in Netmagis application' in returnaddvhost:
            print("Error")
            returnvalue = 1
        else:
            returnvalue = 0
        print("ADDVHOST ENDED")
        return returnvalue

    def add(self, data):
        uri = self.url+"add"
        print("ADD IN PROGRESS : %s", uri)
        self.br.open(uri)
        f = self.br.get_forms()[0]
        f["name"] = data["name"]
        f["domain"] = data["domain"]
        f["addr"] = data["addr"]
        f["mac"] = data["mac"]
        f["iddhcpprof"] = data["iddhcpprof"]
        f["hinfo"] = data["hinfo"]
        f["comment"] = data["comment"]
        f["respname"] = data["respname"]
        f["respmail"] = data["respmail"]
        self.br.submit_form(f)
        returnaddvhost = self.br.response.content.decode('utf8')
        catchable_errors = ['There is already a host named',
                            'An error occurred in Netmagis application'
                            ]
        if any(x in returnaddvhost for x in catchable_errors):
            print("Error")
            returnvalue = 1
        else:
            print(returnaddvhost)
            returnvalue = 0
        print("ADD ENDED")
        return returnvalue

    def deletename(self, data):
        uri = self.url+"del"
        print("DELNAME IN PROGRESS : %s", uri)
        self.br.open(uri)
        f = self.br.get_forms()[0]
        f["name"] = data["name"]
        f["domain"] = data["domain"]
        self.br.submit_form(f)
        firstsubmit = self.br.response.content.decode('utf8')
        if 'An error occurred in Netmagis application' in firstsubmit:
            print("Error")
            returnvalue = 1
        else:
            f2 = self.br.get_form()
            self.br.submit_form(f2)
            secondsubmit = self.br.response.content.decode('utf8')
            if 'An error occurred in Netmagis application' in secondsubmit:
                print("Error")
                returnvalue = 1
            else:
                returnvalue = 0
        print("DELNAME ENDED")
        return returnvalue

    def deleteip(self, data):
        uri = self.url+"del"
        print("DELIP IN PROGRESS : %s", uri)
        self.br.open(uri)
        form = self.br.get_forms()[1]
        form["addr"] = data["addr"]
        self.br.submit_form(form)
        firstsubmit = self.br.response.content.decode('utf8')
        if 'An error occurred in Netmagis application' in firstsubmit:
            print("Error")
            returnvalue = 1
        else:
            f2 = self.br.get_form()
            self.br.submit_form(f2)
            secondsubmit = self.br.response.content.decode('utf8')
            if 'An error occurred in Netmagis application' in secondsubmit:
                print("Error")
                returnvalue = 1
            else:
                returnvalue = 0
        print("DELIP ENDED")
        return returnvalue

    def exportcsv(self, data):
        uri = self.url+"net"
        print("EXPORT IN PROGRESS : %s", uri)
        self.br.open(uri)
        form = self.br.get_form(action='net')
        form['plages'].value = data['plage']
        self.br.submit_form(form, submit=form['docsv'])
        print(self.br.response.content.decode('utf8'))
        print ("EXPORT ENDED")

    def looklarge(self, data):
        uri = self.url+"add"
        print("LOOKLARGE IN PROGRESS : %s", uri)
        self.br.open(uri)
        form = self.br.get_forms()[1]
        form['naddr'] = data['naddr']
        form['plage'] = data['plage']
        self.br.submit_form(form, submit=form['dosearch'])
        returnlooklarge = self.br.response.content.decode('utf8')
        if 'Aucun bloc' in returnlooklarge:
            return 0
        f2 = self.br.get_forms()[0]
        returnvalue = f2.fields['addr'].value
        print("LOOKLARGE ENDED")
        return returnvalue
