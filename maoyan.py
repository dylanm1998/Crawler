from urllib import request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
url = 'https://piaofang.maoyan.com/dashboard-ajax?orderType=0&uuid=17da4889f85c8-092d38434ca57f-978153c-144000-17da4889f85c8'
rq = request.Request(url,headers = headers)
#print(rq)
resp = request.urlopen(rq)
print(resp.read().decode('utf-8'))