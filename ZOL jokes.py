import requests
from lxml import etree
import time
import json_ex

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

domain = "https://xiaohua.zol.com.cn"
joke_list = []

def parse_page(page_url):
    resp = requests.get(page_url,headers=headers)
    text = resp.text
    parser = etree.HTML(text)
    detail_url_suffix_list = parser.xpath("//ul[@class='article-list']/li[@class='article-summary']//a[@class= 'all-read']/@href")
    for detail_url_suffix in detail_url_suffix_list:
        detail_url = domain + detail_url_suffix
        parse_detail(detail_url)
        time.sleep(2)

def parse_detail(detail_url):
    resp = requests.get(detail_url,headers=headers)
    text = resp.text
    parser = etree.HTML(text)
    joke_title = parser.xpath("//h1[@class= 'article-title']/text()")[0]
    joke_content = "".join(parser.xpath("//div[@class= 'article-text']//text()")).strip()
    joke_list.append({
        "title": joke_title,
        "comtent": joke_content
    })
    print(f"{joke_title}Download complete! ")

def main():
    for page in range(1,11):
        page_url = f"https://xiaohua.zol.com.cn/new/{page}.html"
        parse_page(page_url)
        time.sleep(1)

    with open("joke.json","w",encoding='utf-8') as fp:
        # ensure_ascii: If it is not set to False, the Chinese saved in the json file will be stored as a Unicode string
        json.dump(joke_list,fp,ensure_ascii=False)
    print("="*30)
    print("The joke data is crawled complete!")

if __name__ == '__main__':
    main()