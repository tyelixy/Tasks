import requests
import re
def get_page(url):
    headers={
        "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56'
    }
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        return response.text
    else:
        return None

url='https://maoyan.com/board/4'
html=get_page(url)
print(html)
patten=re.compile('<i.*?board-index-\d">(\d+)</i>',re.S)
results=re.findall(patten,html)
print(results)
#<i.*?board-index-\d">(\d+)</i>
#<p class="name"><a*?data-act="boarditem-click".*?>(.*?)</a></p><p class="star">(.*?)</p><p class="releasetime">(.*?)</p>