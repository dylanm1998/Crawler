from urllib import request
url = 'https://www.biedoul.com/'

resp = request.urlopen(url)
print(resp.read().decode())

for i in range(8717,8720):
    url = 'https://www.biedoul.com/index/'+str(i)
    resp = request.urlopen(url)
    print(resp.read().decode())