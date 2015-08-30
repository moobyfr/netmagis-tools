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
    def caslogin(self,login,passwd):
        uri=self.casurl+"?service="+self.url+"start"
        print("LOGIN IN PROGRESS : %s", uri)
        self.br.open(uri)
        self.br.select_form(predicate=is_id_form)
        self.br["username"]=login
        self.br["password"]=passwd
        response2 = self.br.submit()
        #print(response2.read())
        print("LOGIN ENDED")


    def addvhost(self,data):
        uri=self.url+"add"
        print("ADDVHOST IN PROGRESS : %s", uri)
        self.br.open(uri)
        self.br.select_form(None,None,2)
        self.br["name"]= data["name"]
        self.br["domain"]=[data["domain"]]
        self.br["nameref"]=data["nameref"]
        self.br["domainref"]=[data["domainref"]]
        r = self.br.submit()
        returnaddvhost=r.read()
        if 'An error occurred in Netmagis application' in returnaddvhost:
            print("Error")
            returnvalue=1
        else:
            returnvalue=0
        print("ADDVHOST ENDED")
        return returnvalue



    def add(self,data):
        uri=self.url+"add"
        print("ADD IN PROGRESS : %s", uri)
        self.br.open(uri)
        self.br.select_form(None,None,0)
        #self.br["action"]= "add"

        self.br["name"]= data["name"]
        self.br["domain"]=[data["domain"]]
        self.br["addr"]= data["addr"]
        self.br["mac"]=data["mac"]
        self.br["iddhcpprof"]=[data["iddhcpprof"]]
        self.br["hinfo"]=[data["hinfo"]]
        self.br["comment"]=data["comment"]
        self.br["respname"]=data["respname"]
        self.br["respmail"]=data["respmail"]
        r = self.br.submit()
        if 'An error occurred in Netmagis application' in returnaddvhost:
            print("Error")
            returnvalue=1
        else:
            returnvalue=0
        print("ADD ENDED")
        return returnvalue