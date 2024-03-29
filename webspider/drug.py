


import requests
from bs4 import BeautifulSoup

def scrape_drugfuture_fda():
    base_url = 'https://www.drugfuture.com/fda/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    # 发起请求
    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        # 解析网页内容
        soup = BeautifulSoup(response.content, 'html.parser')

        # 在这里编写代码来提取您需要的信息
        # 例如：查找特定标签、类或ID，并提取文本内容
        # 示例：
        # 使用 soup.find_all() 方法，而不是 BeautifulSoup.find_all() 方法
        results = soup.find_all(id="link2")
        for result in results:
            print(result.text)
    else:
        print("Failed to retrieve page")

if __name__ == "__main__":
    scrape_drugfuture_fda()


# [<a class="sister" href="http://example.com/lacie" id="link2" rel="nofollow ugc">Lacie</a>]

