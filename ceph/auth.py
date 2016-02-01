import urllib
import hmac
import hashlib
import base64

access_key = 'Z2ETKC4RQFTR4XBQ1A72'
secret_key = 'vqdQGtmruGW855mduffA8lsLx+ot9iXIb9QTtT2I'
stringToSign="GET\n\n\nMon, 1 Feb 2016 13:25:41 +0000\n/"
signature = base64.b64encode(hmac.new(secret_key, stringToSign.encode('utf-8'), hashlib.sha1).digest())
print signature

# hstr = ''.join(hs)
# print('hstr:%s' % (hstr,))
#
# key = bytearray(secret_key, 'utf-8')
#
# hres = hmac.new(key, hstr.encode('utf-8'), hashlib.sha1).digest()
#
#
# print('type:%s' % (type(hres, )))
#
# hres = base64.b64encode(hres)
#
# hres = hres.decode('utf-8')
# print('hres:%s' % (hres,))


