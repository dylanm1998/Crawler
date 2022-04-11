from urllib import request
from http.cookiejar import MozillaCookieJar

# saving
# cookiejar = MozillaCookieJar('cookie.txt')
# handler = request.HTTPCookieProcessor(cookiejar)
# opener = request.build_opener(handler)
# resp = opener.open('http://httpbin.org/cookies/set/dylanmeng/662527')
#
# cookiejar.save(ignore_discard=True, ignore_expires=True)

# loading
cookiejar = MozillaCookieJar('cookie.txt')
cookiejar.load()
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)
resp = opener.open('http://httpbin.org/cookies/set/dylanmeng/662527')

for cookie in cookiejar:
    print(cookie)