import requests
import re
import json
import time

def get_page(url):
    headers={
        "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56'
    }
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        return response.text
    else:
        return None

def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
      f.write(json.dumps(content,ensure_ascii=False)+'\n')

offset=0
while(offset<10):
    url='https://maoyan.com/board/4?offset='+str(offset*10)
    html=get_page(url)
    patten=re.compile('<i.*?board-index-\d+">(\d+)</i>.*?<p class="name"><a.*?data-act="boarditem-click".*?>(.*?)</a></p>.*?<p class="star">\n\s+(.*?)\s+</p>.*?<p class="releasetime">(.*?)</p>',re.S)
    results=re.findall(patten,html)
    write_to_file(results)
    for result in results:
        i=0
        while(i<4):
            print(result[i])
            i+=1
    offset+=1
    time.sleep(1)

