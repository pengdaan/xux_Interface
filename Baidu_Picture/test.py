# -*- coding:utf-8 -*-
import httplib, ssl, urllib2, socket,re,urllib,os
class HTTPSConnectionV3(httplib.HTTPSConnection):
    def __init__(self, *args, **kwargs):
        httplib.HTTPSConnection.__init__(self, *args, **kwargs)

    def connect(self):
        sock = socket.create_connection((self.host, self.port), self.timeout)
        if self._tunnel_host:
            self.sock = sock
            self._tunnel()
        try:
            self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, ssl_version=ssl.PROTOCOL_SSLv3)
        except ssl.SSLError, e:
            print("Trying SSLv3.")
            self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, ssl_version=ssl.PROTOCOL_SSLv23)
             
class HTTPSHandlerV3(urllib2.HTTPSHandler):
    def https_open(self, req):
        return self.do_open(HTTPSConnectionV3, req)
# install opener
#urllib2.install_opener(urllib2.build_opener(HTTPSHandlerV3()))





if __name__ == "__main__":
    urllib2.install_opener(urllib2.build_opener(HTTPSHandlerV3()))
    r = urllib2.urlopen("https://tieba.baidu.com/p/5114724523")
    print(r.read())
    html=r.read()
    #reg = '<img class="BDE_Image" src="(.+?\.jpg)" '
    #reg = r'src="(imgsa.baidu.com(.*?).jpg)" '
    imgre = re.compile(r'.*/(.*?)\.jpg',re.S)
    #imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    print imglist
    x = 1
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1