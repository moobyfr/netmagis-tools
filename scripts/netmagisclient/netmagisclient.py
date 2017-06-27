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
        self.br = RoboBrowser(history=True, parser='lxml')

    # call the loginURL to authenticate
    def caslogin(self, login, passwd):
        uri = self.casurl+"?service="+self.url+"start"
        self.br.open(uri)
        form = self.br.get_form()
        form['username'].value = login
        form['password'].value = passwd
        self.br.submit_form(form)

    def addvhost(self, data):  # XXX
        uri = self.url+"add"
        self.br.open(uri)
        f = self.br.get_forms()[2]
        f["name"] = data["name"]
        f["domain"] = data["domain"]
        f["nameref"] = data["nameref"]
        f["domainref"] = data["domainref"]
        self.br.submit_form(f)
        returnaddvhost = self.br.response.content.decode('utf8')
        if 'An error occurred in Netmagis application' in returnaddvhost:
            returnvalue = 1
        else:
            returnvalue = 0

        return returnvalue

    def add(self, data):
        uri = self.url+"add"
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
        catchable_errors = ['An error occurred in Netmagis application']
        if any(x in returnaddvhost for x in catchable_errors):
            returnvalue = 1
        else:
            if 'There is already a host named' in returnaddvhost:
                f2 = self.br.get_forms()[0]
                self.br.submit_form(f2)
                self.br.response.content.decode('utf8')
                returnvalue = 0
            else:
                returnvalue = 0

        return returnvalue

    def deletename(self, data):
        uri = self.url+"del"
        self.br.open(uri)
        f = self.br.get_forms()[0]
        f["name"] = data["name"]
        f["domain"] = data["domain"]
        self.br.submit_form(f)
        firstsubmit = self.br.response.content.decode('utf8')
        if 'An error occurred in Netmagis application' in firstsubmit:
            returnvalue = 1
        else:
            f2 = self.br.get_form()
            self.br.submit_form(f2)
            secondsubmit = self.br.response.content.decode('utf8')
            if 'An error occurred in Netmagis application' in secondsubmit:
                returnvalue = 1
            else:
                returnvalue = 0
        return returnvalue

    def deleteip(self, data):
        uri = self.url+"del"
        self.br.open(uri)
        form = self.br.get_forms()[1]
        form["addr"] = data["addr"]
        self.br.submit_form(form)
        firstsubmit = self.br.response.content.decode('utf8')
        if 'An error occurred in Netmagis application' in firstsubmit:
            returnvalue = 1
        else:
            f2 = self.br.get_form()
            self.br.submit_form(f2)
            secondsubmit = self.br.response.content.decode('utf8')
            if 'An error occurred in Netmagis application' in secondsubmit:
                returnvalue = 1
            else:
                returnvalue = 0
        return returnvalue

    def exportcsv(self, data):
        uri = self.url+"net"
        self.br.open(uri)
        form = self.br.get_form(action='net')
        form['plages'].value = data['plage']
        self.br.submit_form(form, submit=form['docsv'])
        print(self.br.response.content.decode('utf8'))

    def looklarge(self, data):
        uri = self.url+"add"
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
        return returnvalue
