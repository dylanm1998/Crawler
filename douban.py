import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'cookie': 'id=224c6bae97ce0032||t=1636211694|et=390|cs=002213fd48ea0d35ae924f0efa; DSID=AAO-7r7SzQqFC7-jXUR3DZv02fvEeDoXkDTfjCDjq2AmwncRmuBMiXiGdsGWiHn8ImrLlLLfmkoOyRPfCI0tYBGxGU7woSMDq8SxRviJJB1U6NAMe7U8gt1EqCTCVnlmbtUL0aMvy1oFpcicmb40Q0DgJaydEoyJzKCs64FB7FpXgd-Ba8qgV_p-HSRaT47ozrE7vkWsLCQFSH4BjZ__PBBvZtNzx74U8tZl3ouqc_a9sjPi9BTDVGmZ5hkl2aCUMJep-bojz2T312wRcIxdnth0oJV3FkmX1OD3R-8JNR9Y8ggimIvvcdc'
}

# Get details page url
def get_detail_urls(url):
    resp = requests.get(url, headers=headers)

    html = resp.text
    soup = BeautifulSoup(html, 'lxml')
    lis = soup.find('ol', class_='grid_view').find_all('li')
    detail_urls = []
    for li in lis:
        detail_url = li.find('a')['href']
        #print(detail_url)
        detail_urls.append(detail_url)
    return detail_urls

def parse_detail_url(url,f):
    # Analysis detail urls content
    resp = requests.get(url, headers=headers)
    html = resp.text
    soup = BeautifulSoup(html, 'lxml')
    # movie name
    name = list(soup.find('div', id='content').find('h1').stripped_strings)
    name = ''.join(name)
    # print(name)
    # director
    director = list(soup.find('div', id='info').find('span').find('span', class_='attrs').stripped_strings)
    director = ''.join(director)
    # print(director)
    # screenwriter
    screenwriter = list(soup.find('div', id='info').find_all('span')[3].find('span', class_='attrs').stripped_strings)
    screenwriter = ''.join(screenwriter)
    # print(screenwriter)
    # actor
    actor = list(soup.find('span', class_='actor').find('span', class_='attrs').stripped_strings)
    actor = ''.join(actor)
    # print(actor)
    # score
    score = soup.find('strong', class_='ll rating_num').string
    score = ''.join(score)
    # print(score)
    f.write('{},{},{},{},{}\n'.format(name,screenwriter,director,actor,score))
def main():
    base_url = 'https://movie.douban.com/top250?start={}&filter='
    with open('Top250.csv','a',encoding='utf-8') as f:
        for x in range(0,251,25):
            url = base_url.format(x)
            detail_urls = get_detail_urls(url)
            for detail_url in detail_urls:
                parse_detail_url(detail_url,f)

if __name__ =='__main__':
    main()