from urllib import request

# No proxy
# url = 'http://httpbin.org/ip'
# resp = request.urlopen(url)
# print(resp.read())

# Use proxy
url = 'http://httpbin.org/ip'
# a. Use ProxyHandler, pass in the proxy to construct a handler
handler = request.ProxyHandler({'http':'222.242.106.7:80'})
# b. Use the handler created above to build an opener
opener = request.build_opener(handler)
# c. Use opener to send a request、
resp =  opener.open(url)
print(resp.read())