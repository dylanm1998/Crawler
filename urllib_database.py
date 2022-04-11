# 1. urlopen
#from urllib import request
#resp = request.urlopen('https://www.sogou.com/')
#print(resp.read())

# 2. urlretrieve
#from urllib import request
#request.urlretrieve('https://www.sogou.com/','sogou.html')
#request.urlretrieve('https://bkimg.cdn.bcebos.com/pic/6a63f6246b600c338744360b491d460fd9f9d62a0bec?x-bce-process=image/resize,m_lfit,w_536,limit_1/format,f_jpg','curry.jpg')

# 3.urlencode
# (1) dictionary
# from urllib import parse
# data = {'name':'翁倩文','greet':'hello world','age':18}
# qs = parse.urlencode(data)
# print(qs)
# decode
# print(parse.parse_qs(qs))
# data1 = {'wd':'斯蒂芬库里'}
# qs1 = parse.urlencode(data1)
# print(qs1)
# url = 'https://www.baidu.com/s?wd=%E6%96%AF%E8%92%82%E8%8A%AC%E5%BA%93%E9%87%8C'
# resp = request.urlopen(url)
# print(resp.read())
# (2) string
# a = '翁倩文'
# b = parse.quote(a)
# print(b)

# 4.urlparse & urlsplit
# from urllib import parse
# url = 'http://www.baidu.com/index.html;user?id=S#comment'
# result = parse.urlparse(url)
# result = parse.urlsplit(url)
# print(result)
# print(result.scheme)
# print(result.netloc)
# print(result.path)
# print(result.params)
# print(result.query)
# print(result.fragment)

# 5. request
# from urllib import request
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
# }
# rq = request.Request('https://www.baidu.com/',headers=header)
# resp = request.urlopen(rq)
# print(resp.read())