import requests
import re

def parse_url(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'cookie': 'f=n; commontopbar_new_city_info=228%7C%E7%83%9F%E5%8F%B0%7Cyt; userid360_xml=1958D4CAE059F8115836067C221F007D; time_create=1644648313870; f=n; id58=CrIIJ2HfyY01G9FtDIOYAg==; 58tj_uuid=dd297657-7fe0-42ba-a4d0-7546e7a0373d; new_uv=1; als=0; commontopbar_new_city_info=228%7C%E7%83%9F%E5%8F%B0%7Cyt; wmda_uuid=18ea5be7106524f1f3041f054f800ad1; wmda_new_uuid=1; commontopbar_ipcity=yt%7C%E7%83%9F%E5%8F%B0%7C0; BAIDU_SSP_lcr=https://yt.ganji.com/; xxzl_deviceid=csHlBgrRiWb3aICHi4K%2FTGbUkwRHwBjZ5vtEPLak5GfRDwfL9dcmhptOC0JMKdcw; fzq_h=84e98bcc87ad27f366ed5461ab985be8_1642056132964_7efce44608684a53819fcad785534a5a_1894696375; sessionid=82b859f5-d4ae-4bd2-bb70-a41bb9133caf; fzq_js_usdt_infolist_car=be5913b92724962c4255767cbfb4561b_1642056134601_9; 58home=yt; wmda_visited_projects=%3B2385390625025%3B11187958619315%3B1732038237441%3B10104579731767; www58com="UserID=85147631930669&UserName=dylanmeng1998"; 58cooper="userid=85147631930669&username=dylanmeng1998"; 58uname=dylanmeng1998; passportAccount="atype=0&bstate=0"; xxzl_smartid=e47728329d9474602f2598c1415c1f24; ppStore_fingerprint=DAF3541C4F76D177A9C7F89FD7A48B6D6EC5F6EC3741D952%EF%BC%BF1642057682951; xxzl_cid=a18b7af8a1fb46a0b711b2d09f6310d6; xzuid=0433d533-5be6-4dc7-8b8f-1f4156dec4ec; PPU=UID=85147631930669&UN=dylanmeng1998&TT=153ebc1ea54a375240c8c5019ea62216&PBODY=cqNYRiZ7s8D-LrofLLVzyKg_kWE2VDjUNrEzkjxjdac3w0-BVNHwlebthmMz89KuIGFg9dSKc5eG4Uedl2zaUlEiJywxyFgZEtr2ivssaJCumrfbFYlYLw9kGxhqSXSNcNd33FLUmBocl_Zj8vDPKEHGgcA-Hw1Q5Eudv2-jI-4&VER=1&CUID=LLII5wum2L7r-GtiaY6Yyw'
    }
    resp = requests.get(url,headers=headers)
    text = resp.text
    #new_text = text.replace(u'\xa0', u' ')
    new_text = re.sub(u'\xa0', u' ', text)
    houses = re.findall(r"""
    <li.+?realverify".+?<a.+?strongbox".+?>(.+?)</a>
    .+?<p.+?room"(.+?)</p>
    .+?<div(.+?)money"(.+?)<b.+?strongbox"(.+?)</b>(.+?)</div>
    """,new_text,re.VERBOSE|re.DOTALL)

    for house in houses:
        print(house)

def main():
    base_url = 'https://yt.58.com/chuzu/pn{}/'
    for x in range(1,11):
        page_url = base_url.format(x)
        parse_url(page_url)
        break

if __name__ =='__main__':
    main()


# Summarize:
# 1. If you want . to represent all characters, you need to add re.DOTALL after the function to represent it, otherwise it will not represent \n, which is a newline.
# 2. When fetching data, use non-greedy mode.
# 3. If the regex is written incorrectly, then the result will not be obtained, and the program will feign death. At this time, you can delete the regex you just wrote, run it again, and see if the program will suspend the suspended animation.
#    If there is no suspended animation, it means that there is a problem with the regular writing, and it is necessary to adjust it.
# 4. If there is a problem with the regular writing, then don't go to the horns, just change a way of thinking.
