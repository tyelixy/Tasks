import requests
import json
import os
import time
from urllib.parse import urlencode
from hashlib import md5
def get_page(offset):
    params={
        'aid':'24',
        'app_name':'web_search',
        'offset':offset,
        'format':'json',
        'keyword':'街拍',
        "autoload":'true',
        'count':'20',
        'en_qc':'1',
        'cur_tab':'1',
        'from':'search_tab',
        'pd':'synthesis',
    }
    headers={
        "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56'
    }
    url='https://www.toutiao.com/api/search/content/?'+urlencode(params)
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError:
        return None

def get_image(json):#生成器
    if json.get('data'):
        for item in json.get('data'):
            title=item.get('title')
            images=item.get('image_list') 
            if images:
                for image in images:
                    yield{#返回
                        'image':image.get('url'),
                        'title':title
                    }

def save_image(item):
    if not os.path.exists("{0}".format(item.get('title'))):#判断文件是否存在??
        os.mkdir("{0}".format(item.get('title')))#根据title创建文件夹
    try:
        response=requests.get(item.get('image'))
        if response.status_code==200:
            file_path='{0}/{1}.{2}'.format(item.get('title'),md5(response.content).hexdigest(),'jpg')
            #MD5签名是一个哈希函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）(?)；可用于文件命名(去除重复),传入参数：bytes类型
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
            else:
                print('Already download.',file_path)
    except requests.ConnectionError:
        print('Fail to save the image')

i=0
while i<3:
    json=get_page(i*20)
    for item in get_image(json):
        print(item)
        save_image(item)
    i+=1
    time.sleep(1)