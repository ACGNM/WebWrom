import urllib
import urllib2

values = {"username":"aria_m1911@126.com","password":"618618618Qw+"}
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()