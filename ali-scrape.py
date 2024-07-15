import requests
import json
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup

# 目标网页的URL
# url = 'https://reads.alibaba.com/50-years-of-the-porsche-911-turbo/'


def scrape(url):
    # print(f"Start to extract content from {url}")
    # 获取网页内容
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到tiltle, 

    # 找到 entry-content clear 块
    content_block = soup.find('div', class_='entry-content clear')

    # 提取 <h2>, <h3> 和 <p> 标签的内容
    elements = content_block.find_all(['h2', 'h3', 'p'])
    # 提取关键词、标题、字数、语言等信息
    title = soup.title.string
    estimated_word_count = len(content_block.get_text(strip=True).split())
    json_content = soup.find('script', class_='yoast-schema-graph').string

    # Load the JSON content
    data = json.loads(json_content)

    # Extract the keywords
    keywords = data['@graph'][0]['keywords'] if 'keywords' in data['@graph'][0] else None
    word_count = data['@graph'][0]['wordCount'] if 'wordCount' in data['@graph'][0] else estimated_word_count
    description = data['@graph'][1]['description'] if 'description' in data['@graph'][1] else None
    date_published = data['@graph'][0]['datePublished'] if 'datePublished' in data['@graph'][0] else None
    category = data['@graph'][3]['itemListElement'][2]['name'] if 'itemListElement' in data['@graph'][3] else None

    # 创建一个列表来存储提取的内容
    extracted_content = []

    h2_count = 0
    h3_count = 0
    p_count = 0
    for element in elements:
        if element.name == 'h2':
            h2_count += 1
        if element.name == 'h3':
            h3_count += 1
        if element.name == 'p':
            p_count += 1
        extracted_content.append({
            'tag': element.name,
            'text': element.get_text(strip=True)
        })

    # 收集提取的内容
    collect_content = ''
    for item in extracted_content:
        if item['text'].startswith('Source from') or item['text'].startswith('Disclaimer:') or item['text'].startswith('Was this article helpful?') or len(item['text']) < 3:
            continue
        collect_content += f"<{item['tag']}>{item['text']}</{item['tag']}> \n"

    res = {
        'title': title,
        'keywords': keywords,
        'word_count': word_count,
        'description': description,
        'date_published': date_published,
        'content': collect_content,
        'category': category,
        'estimated_token': len(collect_content)/4,
        'h2_count': h2_count,
        'h3_count': h3_count,
        'p_count': p_count,
        'url': url,
    }
    return res


def res_to_jsonl(res,file_name):
    jsonl_data = {
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a highly skilled SEO and advanced copywriter. Your task is to generate English SEO articles "
                    "based on the provided article titles, core keywords, and related keywords. The writing style must be anthropomorphic. "
                    "-- You must return only the article content, no outline or explanations. -- Core and related keywords must appear at least once. "
                    "-- Do not display the generated title or the <h1> tag. Directly start with the content. -- Do not use markdown syntax. "
                    "You must output in HTML format: -- Subtitles: <h2> tag -- Main text: <p> tag -- Core keywords must be used exactly as provided. "
                    "-- Content must be detailed and comprehensive. -- Article must include an introduction and a conclusion. -- Do not include the <html> tag at the end."
                )
            },
            {
                "role": "user",
                "content": f"title: {res['title']} Keywords: {', '.join(res['keywords'])}"
            },
            {
                "role": "assistant",
                "content": res['content']
            }
        ]
    }

    # 将提取的内容追加到一个 JSONL 文件中
    with open(f'{file_name}.jsonl', 'a') as file:
        file.write(json.dumps(jsonl_data) + '\n')
        

def read_url_txt(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()
    return urls


def craw(file_name='urls'):
    urls = read_url_txt(f'{file_name}.txt')
    res_ls = []
    for url in tqdm(urls):
        tqdm.write(f"Processing: {url}")
        try:
            res = scrape(url)
        except:
            print(f"Failed to extract content from {url}")
            continue
        # 插入数据到DataFrame
        res_ls.append(res)
        if res['h2_count'] + res['h3_count'] < 4 or res['estimated_token'] > 2600 or res['estimated_token'] < 800 or res['keywords'] is None or res['title'] is None :
            continue
        res_to_jsonl(res,file_name)
        # print(f"Successfully extract content from {url}")
    res_df = pd.DataFrame(res_ls)
    res_df.to_excel(f'{file_name}.xlsx', index=False)
        
if __name__ == '__main__':
    file_name = input("Please input the file name: ")
    craw(file_name)

