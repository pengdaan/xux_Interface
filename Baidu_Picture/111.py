import httplib2
h1 = httplib2.Http(disable_ssl_certificate_validation=True)
resp,content = h1.request("http://tieba.baidu.com/p/5114724523")
print content
