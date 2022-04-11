from urllib import request
from urllib import parse
from http.cookiejar import CookieJar
# personal web page

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
# 1. login
# 1.1 Create cookiejar object
cookiejar = CookieJar()
# 1.2 Use cookiejar to create an HTTPCookieProcessor object
handler = request.HTTPCookieProcessor(cookiejar)
# 1.3 Create an opener using the handler created in the previous step
opener = request.build_opener(handler)
# 1.4 Use opener to send login request
post_url = 'https://i.meishi.cc/login_t.php?username=15589552242&login_type=1&password=108172'
post_data = parse.urlencode({
    'username':'15589552242',
    'password': '108172'
})
req = request.Request(post_url,data=post_data.encode('utf-8'))
opener.open(req)

# 2.Visit personal web page
url = 'https://www.meishij.net/?from=space_block'

rq = request.Request(url,headers = headers)
resp = opener.open(rq)
print(resp.read().decode('utf-8'))