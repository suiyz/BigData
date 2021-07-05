# encoding utf-8
import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
}
url1 = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A0O0G02%22%7D%5D&k1=1624327614963&h=1"
url2 = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A0O0H02%22%7D%5D&k1=1625190765831&h=1"

url3 = "https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A0201%22%7D%5D&k1=1625465516079&h=1"
def crawl(url,filename):

    # 爬取https需要添加参数    verify = False
    resp = requests.get(url, headers=headers, verify=False)
    # 返回JSON格式
    # print(resp.content.decode())
    # 下面的这种转换方式报错（JSON格式有问题：jsonp1（头部信息问题，不是真正的JSON格式，jsonp1跨域访问技术

    # json_obj = resp.json()
    # with open(filename+"1.json", "w", encoding="utf-8") as f:
    #     json.dump(json_obj, f, ensure_ascii=False, indent=4)  # 显示中文且以缩进形式显示

    json_str = resp.content.decode()
    with open(filename+".json", "w", encoding="utf-8") as f:
        f.write(json_str)

# crawl(url=url1,filename="citydata")
# crawl(url=url2,filename="ruraldata")

crawl(url3,filename="gdpdata")