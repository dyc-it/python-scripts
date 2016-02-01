import urllib
import hmac
import hashlib
import base64

access_key = 'AKIAIOSFODNN7EXAMPLE'
secret_key = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'


#stringToSign="GET\n\n\nMon, 1 Feb 2016 13:06:18 +0000\n/"
stringToSign="GET\n\n\nTue, 27 Mar 2007 19:36:42 +0000\n/johnsmith/photos/puppy.jpg"

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


