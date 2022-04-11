from bs4 import BeautifulSoup

html = """
<table class="tablelist" cellpadding="0" cellspacing="0">
    <tbody>
        <tr class="h">
            <td class="l" width="374">职位名称</td>
            <td>职位类别</td>
            <td>人数</td>
            <td>地点</td>
            <td>发布时间</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=33824&keywords=python&tid=87&lid=2218">22989-金融云区块链高级研发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=29938&keywords=python&tid=87&lid=2218">22989-金融云高级后台开发</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=31236&keywords=python&tid=87&lid=2218">SNG16-腾讯音乐运营开发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=31235&keywords=python&tid=87&lid=2218">SNG16-腾讯音乐业务运维工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=34531&keywords=python&tid=87&lid=2218">TEG03-高级研发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=34532&keywords=python&tid=87&lid=2218">TEG03-高级图像算法研发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=31648&keywords=python&tid=87&lid=2218">TEG11-高级AI开发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>4</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=32218&keywords=python&tid=87&lid=2218">15851-后台开发工程师</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=32217&keywords=python&tid=87&lid=2218">15851-后台开发工程师</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a id="test" class="test" target='_blank' href="position_detail.php?id=34511&keywords=python&tid=87&lid=2218">SNG11-高级业务运维工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
    </tbody>
</table>
"""

soup = BeautifulSoup(html,'lxml')

# 1. Get all tr tags
# print(soup.tr)
# print(soup.find('tr'))
# trs = soup.find_all('tr')
# for tr in trs:
#     print(tr)
#     print('-'*50)
# trs = soup.select('tr')
# print(trs)
# 2. Get second tr tag
# tr = soup.find_all('tr',limit=2)[1]
# print(tr)
# tr = soup.select('tr')[1]
# print(tr)
# 3. Get all tr tags with class equal to even
#trs = soup.find_all('tr',class_= 'even')
# trs = soup.find_all('tr',attrs={'class':'even'})
# for tr in trs:
#     print(tr)
#     print('-'*50)
#tr = soup.select('.even')
# tr = soup.select('tr[class="even"]')
# print(tr)
# 4. Extract all <a> tags with id equal to test and class equal to test
# list = soup.find_all('a',id='test',class_='test')
# list = soup.find_all('tr',attrs={'id':'test','class':'test'})
# for a in list:
#     print(a)
# alist = soup.select('a')
# for a in alist:
#     href = a['href']
#     print(href)

# 5. Get the href attribute of all a tags
# alist = soup.find_all('a')
# for a in alist:
#     # 1.
#     # href = a['href']
#     # print(href)
#
#     # 2.
#     href = a.attrs['href']
#     print(href)

# 6.Get all job information (plain text)
# trs = soup.find_all('tr')[1:]
# lists = []
# for tr in trs:
#     info = {}
    #method 1
    # tds = tr.find_all('td')
    # name = tds[0].string
    # category = tds[1].string
    # info['name']=name
    # info['category']=category

    #method 2
    # infos = list(tr.stripped_strings)
    # print(infos)
#     lists.append(infos)
# print(list)

trs = soup.select('tr')
for tr in trs:
    info = list(tr.stripped.strings)
    print(info)