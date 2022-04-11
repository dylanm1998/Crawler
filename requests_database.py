# 1.
#import requests
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
# }
# kw = {'wd':'烟台'}
# params receives the query times of a dictionary or string, the dictionary is automatically converted to url encoding, no urlencode() is required
# response = requests.get('https://www.baidu.com/s', headers=headers, params=kw)
# print(response)

# Query corresponding content
# print(type(response.text)) # Return data in unicode format
# print(type(response.content)) # Return byte stream data
# print(response.url)


# 2. post
# import requests
# url = 'https://i.meishi.cc/login_t.php?username=15589552242&login_type=1&password=634009'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
# }
# data = {
#     'redirect': 'https://www.meishij.net/',
#     'username': '15589552242',
#     'password': '634009'
# }
# resp = requests.post(url,headers=headers,data=data)
# print(resp.text)

# 3. Proxy
# import requests
#
# proxy = {
#     'http://': '14.126.30.69:8888'
# }
# url = 'http://httpbin.org/ip'
# resp = requests.get(url,proxies=proxy)
# print(resp.text)

# 4. cookie
import requests

# resp = requests.get('https://www.baidu.com/')
# print(resp.cookies)
# print(resp.cookies.get_dict())

  # example 1
# url = 'https://www.zhihu.com/hot'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
#     'cookie': '_zap=a666fe21-b3a3-443f-ab94-21a7faba3cab; d_c0="AMAcsflm_xOPTlqP2skBMdo3-ZJHPZob7Gs=|1636337269"; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=cQBuy8TE8uNEVERBEEJq8P62ZKeVi8Yu; _xsrf=8peRIV2CVo4r2pN0R5OZLI0ZpoyW1KGH; captcha_session_v2="2|1:0|10:1639969483|18:captcha_session_v2|88:bFQvR0w3RHI2eFRsaVBRNTZMMDNJbUlIdHYzS2lYMldSVy9xbEs5NHpVRDRYcklmZys4a3pXMktFcGg4OXJjTQ==|5d386a26d8c97a76e7cf1c63333d0d8ff976169126b315979833385cd1a0cc75"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1639111980,1639228542,1639311093,1639969485; SESSIONID=odCKKmXwFKbwcWWyHp54BDwIbSvqZQb1ARX1U8nkXVh; JOID=W1ocAEN_squAi9EjGnUIdZx1vdYJG93iwMG3cGc48sL944d_aLNBFeuB0SIbJntYUmGOvnfA26Y34A-7Apk34s4=; osd=UlsSBUp2s6WFgtgiFHABfJ17uN8AGtPnyci2fmIx-8Pz5o52ab1EHOKA3ycSL3pWV2iHv3nF0q827gqyC5g558c=; __snaker__id=tXKbmqGAkIoDZQXh; gdxidpyhxdE=NBaKvbwQtV%5CwUZpLxK6RqJxi7ANwuYH%5Cp9BN0XvYnI0QdC9848HzOokyzrBnby8I%2BYDcMsuv%2Fo6UHMUOtu1xC18%2Fse6OI71JI9dJnJSt2qd7TtXqZYaGbOB8iYBh0RdHwJ77d1utv4tegP54PZNR6%2BJT6sqzsRU3aQqAE%2FgEnQ7C9J6T%3A1639970385827; YD00517437729195%3AWM_NI=7KGECC1vSa8KPTxQXxODpA7VPBwnSuMrNdK9TRjWJ%2FxymrZ0thdpZLzziYbDXFuXT7Ux4F9qSh65pK%2F1y4wfZZCwVyKQSxu8sftcEzvTW9DEx5%2F7x2hI%2Bl2oHVlL9yZyTVE%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeb6b33b8a939dd0aa3fa7928fa3c45b868b9f85b534b686a7d5ca5bb389f984c52af0fea7c3b92af59589a6c249f3aa9d82bb41948cb8b2db748d9cc0a2b65e949eb98fd27f8fae8285ca33988ea6b8c925bca7a393d93cb8b8ac91d948baa6a7bae1509c9abbb9d73d97a8fca7bc7b91b8fad6f341edefb7d5f66e9a868d98d573898f9d99f834b1babc84c872b68c99dac74fbcebe1d8fb3aac97e58db1658c8aa4adbc739aa79cb7c837e2a3; captcha_ticket_v2="2|1:0|10:1639969502|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfZW5jTzV6VE5reGl3d2FOVlpRVGFDNUJTdVRzV1BnZ3JEbC5ESEZHeEVWMUR2cVFZSXhHMEgtWThTWmFjbDVtcGwySUZ2VGF2Y2JGeUlfUHRVZWEwc2tiZk9tdEdIUXF1SXg0Z1pSRERJVGd6ZEtpNWtIQ0dNVk1aWGJUQmY2bjBLbHV4S2dSTVRJMU1ycmxkUG9FS2dKZkV5eUNJUUxfLVBRWGdvejhaa2J3eUpxLUtORmpaczgyN0pIbGVuX1NIeTZ4TnZDRHY2dGVpN1N3SGhGY1NZQkI4dVJva2NtODZVYktvVTJsTWhaOW92VWxVd3N5Ty5YcEl2ODJFRWVJVnhHMFZLWGpGbVV3RTltdTFTOWpLV3A0UmdqeGpCWDU3V1VjTm9nSE9ydHRNWXpNN3hTLlUtZzZVdkNWeklnall5UDRWQjZpcHVUSUE2Y0tEOUguVGxfbGJZaWJ1LXFpODY0R1JmMC1aSkNQeTFsZ2hwZ19obkZXZEFidmpDVzVGQ2ktWEpEeWRHZ0xkbndfb0VKSXZqUFhIY2JULkVESmpUcWFCWXZMSGViUlVQbmMtQUJ3cmtyX28tbkU1Z3VGYnNlaTEtb0FuYWM5Yi00SDlPVWpwbW81NFpnSXFKT19hWS1palZGZXRQNmFxY0RqcDB6Y3BkUnE4RHRqMyJ9|23f1b31144f79f998ce495c7a51c56e7a9826dce6dd7a40455003c9e863f8657"; z_c0="2|1:0|10:1639969579|4:z_c0|92:Mi4xdHUzbU5BQUFBQUFBd0J5eC1XYl9FeVlBQUFCZ0FsVk5LMEd0WWdCUUtQM2V4TV9CdmJveUphVXNoZ2pNN2JfQmRR|80e0807ae56f2c571d0df5fc1ed708aa347416722207568add35e397841cbe62"; tst=h; NOT_UNREGISTER_WAITING=1; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1639976974; KLBRSID=fb3eda1aa35a9ed9f88f346a7a3ebe83|1639976977|1639969483'
# }
# resp = requests.get(url,headers=headers)
# print(resp.text)

  #example 2

# post_url = 'https://i.meishi.cc/login_t.php?username=15589552242&login_type=1&password=974496'
# post_data = {
#     'username':'15589552242',
#     'password': '974496'
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
# }
#
#     #login
# session = requests.session()
# session.post(post_url,headers=headers,data=post_data)
#
#     #visit personal web site
# url = 'https://www.meishij.net/?from=space_block'
# resp = session.get(url)
# print(resp.text)

# 5. SSL
import requests
import urllib3

urllib3.disable_warnings()
url = 'https://inv-veri.chinatax.gov.cn/'
resp = requests.get(url,verify=False)
print(resp.content.decode('utf-8'))