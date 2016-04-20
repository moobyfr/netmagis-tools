import mechanize


def is_id_form(form):
    return "id" in form.attrs and form.attrs['id'] == "fm1"


class NetmagisClient(object):

    url = None     # Netmagis's URL
    casurl = None  # CAS's URL
    br = None      # the browser reference

    def __init__(self, url, casurl):
        self.url = url
        self.casurl = casurl
        self.br = mechanize.Browser()

    # call the loginURL to authenticate
    def caslogin(self, login, passwd):
        uri = self.casurl+"?service="+self.url+"start"
        print("LOGIN IN PROGRESS : %s", uri)
        self.br.open(uri)
        self.br.select_form(predicate=is_id_form)
        self.br["username"] = login
        self.br["password"] = passwd
        response2 = self.br.submit()
        print("LOGIN ENDED")

    def addvhost(self, data):
        uri = self.url+"add"
        print("ADDVHOST IN PROGRESS : %s", uri)
        self.br.open(uri)
        self.br.select_form(None, None, 2)
        self.br["name"] = data["name"]
        self.br["domain"] = [data["domain"]]
        self.br["nameref"] = data["nameref"]
        self.br["domainref"] = [data["domainref"]]
        r = self.br.submit()
        returnaddvhost = r.read()
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
        self.br.select_form(None, None, 0)
        self.br["name"] = data["name"]
        self.br["domain"] = [data["domain"]]
        self.br["addr"] = data["addr"]
        self.br["mac"] = data["mac"]
        self.br["iddhcpprof"] = [data["iddhcpprof"]]
        self.br["hinfo"] = [data["hinfo"]]
        self.br["comment"] = data["comment"]
        self.br["respname"] = data["respname"]
        self.br["respmail"] = data["respmail"]
        r = self.br.submit()
        returnaddvhost = r.read()
        if 'An error occurred in Netmagis application' in returnaddvhost:
            print("Error")
            returnvalue = 1
        else:
            returnvalue = 0
        print("ADD ENDED")
        return returnvalue

    def deletename(self, data):
        uri = self.url+"del"
        print("DELNAME IN PROGRESS : %s", uri)
        self.br.open(uri)
        self.br.select_form(None, None, 0)
        self.br["name"] = data["name"]
        self.br["domain"] = [data["domain"]]
        r = self.br.submit()
        firstsubmit = r.read()
        if 'An error occurred in Netmagis application' in firstsubmit:
            print("Error")
            returnvalue = 1
        else:
            self.br.select_form(None, None, 0)
            r2 = self.br.submit()
            secondsubmit = r2.read()
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
        self.br.select_form(None, None, 1)
        self.br["addr"] = data["addr"]
        r = self.br.submit()
        firstsubmit = r.read()
        if 'An error occurred in Netmagis application' in firstsubmit:
            print("Error")
            returnvalue = 1
        else:
            self.br.select_form(None, None, 0)
            r2 = self.br.submit()
            secondsubmit = r2.read()
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
        self.br.select_form(None, None, 0)
        c = self.br.form.controls()
        c.set_values(c.items, "plages")
        r = self.br.submit('docsv')
        print r.read()
        print ("EXPORT ENDED")

    def looklarge(self, data):
        uri = self.url+"add"
        print("LOOKLARGE IN PROGRESS : %s", uri)
        self.br.open(uri)
        self.br.select_form(None, None, 1)
        self.br["naddr"] = data["naddr"]
        self.br.set_value_by_label([data["plage"]], name='plage')
        r = self.br.submit()
        returnlooklarge = r.read()
        if 'Aucun bloc' in returnlooklarge:
            returnvalue = 0
        self.br.select_form(None, None, 0)
        returnvalue = self.br.form["addr"]
        print("LOOKLARGE ENDED")
        return returnvalue
