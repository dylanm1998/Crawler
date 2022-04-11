from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
def get_detail_urls(url):
    resp = requests.get(url, headers=headers)
    html = resp.text
    soup = BeautifulSoup(html, 'lxml')
    detail_urls = []
    for x in range(1, 11):
        detail_url = 'https://www.kuaidaili.com/free/inha/{}/'.format(x)
        detail_urls.append(detail_url)
    return detail_urls

def parse_detail_url(url,f):
    resp = requests.get(url, headers=headers)
    html = resp.text
    soup = BeautifulSoup(html,'lxml')
    #print(soup.text)
    IP = list(soup.find('tbody').find_all('td')[0].stripped_strings)
    PORT = list(soup.find('tbody').find_all('td')[1].stripped_strings)
    Anonymity = list(soup.find('tbody').find_all('td')[2].stripped_strings)
    Type = list(soup.find('tbody').find_all('td')[3].stripped_strings)
    Location = list(soup.find('tbody').find_all('td')[4].stripped_strings)
    Reponse_speed = list(soup.find('tbody').find_all('td')[5].stripped_strings)
    Last_verification_time = list(soup.find('tbody').find_all('td')[6].stripped_strings)
    #page_url.append([IP]+[PORT]+[Anonymity]+[Type]+[Location]+[Reponse_speed]+[Last_verification_time])
    f.write('{},{},{},{},{}\n'.format(IP, PORT, Anonymity, Type, Location, Reponse_speed, Last_verification_time))


def main():
    base_url = 'https://www.kuaidaili.com/free/inha/{}/'
    with open('IP.csv','a',encoding='utf-8') as f:
        for x in range(1, 11):
            url = base_url.format(x)
            detail_urls = get_detail_urls(url)
            for detail_url in detail_urls:
                parse_detail_url(detail_url, f)

if __name__ == '__main__':
    main()
