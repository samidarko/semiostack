from HTMLParser import HTMLParser
import urllib, urllib2, cookielib
from xml.dom.minidom import parseString


class HTMLCSRFParser(HTMLParser):
    
    csrf = None
    
    def handle_starttag(self, tag, attrs):
        if tag == 'input' and ('name', 'csrfmiddlewaretoken') in attrs:
            for attr in attrs:
                if attr[0] == 'value':
                    self.csrf = attr[1]
                    
    def getCsrfToken(self):
        return self.csrf


class Semiocoder(object):
    '''
    classdocs
    '''

    def __init__(self, host_url, login_url = '/accounts/login', logout_url = '/accounts/logout', api_url = '/api', verbose = False):
        '''
        Constructor
        '''
        self.host_url = host_url
        self.login_url = login_url
        self.logout_url = logout_url
        self.api_url = api_url
        self.verbose = verbose
        self.csrfparser = HTMLCSRFParser()
        
        
    def computeResult(self, result):
        try:
            dom = parseString(result.read())
        except:
            return 'compute result : An error has occurred'
        if self.verbose:
            print dom.toxml()
        return dom
    
        
    def login(self, username = None, password = None):
        # TODO: ajouter un attribut is connected et tester
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)
        
        login_page = urllib2.urlopen(self.host_url+self.login_url)
        self.csrfparser.feed(login_page.read())
        
        params = urllib.urlencode(dict(username=username, password=password, next=self.api_url, csrfmiddlewaretoken = self.csrfparser.getCsrfToken()))
        
        req = urllib2.Request(self.host_url+self.login_url, data=params, headers={'Content-Type':'application/x-www-form-urlencoded'})
        
        resp = urllib2.urlopen(req)
        
        
    def logout(self):
        r = urllib2.urlopen(self.host_url+self.logout_url)

        
    def getEncoderDetail(self, object_id):
        r = urllib2.urlopen(self.host_url+self.api_url+'?action=getencoderdetail&id='+str(object_id))
        return self.computeResult(r)
        

    
    def getEncoders(self):
        r = urllib2.urlopen(self.host_url+self.api_url+'?action=getencoders')
        return self.computeResult(r)
    
    
    def getExtensionDetail(self, object_id):
        r = urllib2.urlopen(self.host_url+self.api_url+'?action=getextensiondetail&id='+str(object_id))
        return self.computeResult(r)
    
    def getExtensions(self):
        r = urllib2.urlopen(self.host_url+self.api_url+'?action=getextensions')
        return self.computeResult(r)
    
    
    def getJobDetail(self, object_id):
        r = urllib2.urlopen(self.host_url+self.api_url+'?action=getjobdetail&id='+str(object_id))
        return self.computeResult(r)
    
    
    def getJobs(self):
        r = urllib2.urlopen(self.host_url+self.api_url+'?action=getjobs')
        return self.computeResult(r)
        
    
    def getJoblistDetail(self, object_id):
        r = urllib2.urlopen(self.host_url+self.api_url+'?action=getjoblistdetail&id='+str(object_id))
        return self.computeResult(r)
        
    
    def getJoblists(self):
        r = urllib2.urlopen(self.host_url+self.api_url+'?action=getjoblists')
        return self.computeResult(r)
        
    
    def getTaskDetail(self, object_id):
        r = urllib2.urlopen(self.host_url+self.api_url+'?action=gettaskdetail&id='+str(object_id))
        return self.computeResult(r)
        
    
    def getTasks(self):
        r = urllib2.urlopen(self.host_url+self.api_url+'?action=gettasks')
        return self.computeResult(r)
        
    
    def getHistoryDetail(self, object_id):
        r = urllib2.urlopen(self.host_url+self.api_url+'?action=gethistorydetail&id='+str(object_id))
        return self.computeResult(r)
        
    
    def getHistories(self):
        r = urllib2.urlopen(self.host_url+self.api_url+'?action=gethistories')
        return self.computeResult(r)
        
        