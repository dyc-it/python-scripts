import httplib, urllib
import hmac
import hashlib
import base64

# timeStr = "Mon, 1 Feb 2016 13:44:41 +0800"
timeStr = "Mon, 01 Feb 2016 14:02:52 +0800"
access_key = 'Z2ETKC4RQFTR4XBQ1A72'
secret_key = 'vqdQGtmruGW855mduffA8lsLx+ot9iXIb9QTtT2I'
stringToSign="GET\n\n\n" + timeStr + "\n/"
signature = base64.b64encode(hmac.new(secret_key, stringToSign.encode('utf-8'), hashlib.sha1).digest())
print signature



headers = {"Host": "10.192.40.29",
           "Date": timeStr,
           "Authorization": "AWS Z2ETKC4RQFTR4XBQ1A72:"+signature}
conn = httplib.HTTPConnection("10.192.40.29:80")
conn.request("GET", "/", headers=headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
print data
conn.close()
