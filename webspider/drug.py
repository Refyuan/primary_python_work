# import requests
# from bs4 import BeautifulSoup
#
# # 发送 HTTP GET 请求
# url = 'https://www.drugfuture.com/fda/druglist-x.html'
# response = requests.get(url)
#
# # 检查响应状态码
# if response.status_code == 200:
#     # 使用 BeautifulSoup 解析 HTML 内容
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     # 这里你可以根据网页结构使用 BeautifulSoup 提取你需要的数据
#     # 例如，查找特定的标签、类名、ID 等
#     # 示例：
#     drug_list = soup.find_all('div', class_='drug-list')
#
#     # 处理提取到的数据
#     for drug in drug_list:
#         print(drug.text)
# else:
#     print('Failed to retrieve the webpage.')
import requests
from lxml import etree
import time

def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        e = etree.HTML(response.text)
        names = e.xpath('//p/a/@title')
        prices = e.xpath('//p/span[@class="search_pre_price"]/text()')
        results = []
        for name, price in zip(names, prices):
            results.append((name, price))
            print(name, price)
        return results
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def main():
    search_term = input("请输入搜索的内容：")
    all_results = []
    for page in range(1, 10):
        print(f'——————————————————————正在爬取第{page}页内容—————————————————————————————')
        url = f'http://search.dangdang.com/?key={search_term}&page_index={page}'
        all_results.extend(get_html(url))
        time.sleep(2)  # 延时2秒，避免请求过于频繁

    # 保存结果到文件
    with open('results.txt', 'w', encoding='utf-8') as f:
        for result in all_results:
            f.write(f"{result[0]} {result[1]}\n")

if __name__ == '__main__':
    main()
