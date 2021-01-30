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

#url='https://maoyan.com/board/4'
#html=get_page(url)
#print(html)
t='''<div class="container" id="app" class="page-board/index" >

<div class="content">
    <div class="wrapper">
        <div class="main">
            <p class="update-time">2021-01-26<span class="has-fresh-text">已更新</span></p>
            <p class="board-content">榜单规则：将猫眼电影库中的经典影片，按照评分和评分人数从高到低综合排序取前100名，每天上午10点更新。相关数据来源于“猫眼电影库”。</p>
            <dl class="board-wrapper">
                <dd>
                        <i class="board-index board-index-1">1</i>
    <a href="/films/1200486" title="我不是药神" class="image-link" data-act="boarditem-click" data-val="{movieId:1200486}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/414176cfa3fea8bed9b579e9f42766b9686649.jpg@160w_220h_1e_1c" alt="我不是药神" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1200486" title="我不是药神" data-act="boarditem-click" data-val="{movieId:1200486}">我不是药神</a></p>
        <p class="star">
                主演：徐峥,周一围,王传君
        </p>
<p class="releasetime">上映时间：2018-07-05</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">6</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-2">2</i>
    <a href="/films/1297" title="肖申克的救赎" class="image-link" data-act="boarditem-click" data-val="{movieId:1297}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/8112a8345d7f1d807d026282f2371008602126.jpg@160w_220h_1e_1c" alt="肖申克的救赎" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1297" title="肖申克的救赎" data-act="boarditem-click" data-val="{movieId:1297}">肖申克的救赎</a></p>
        <p class="star">
                主演：蒂姆·罗宾斯,摩根·弗里曼,鲍勃·冈顿
        </p>
<p class="releasetime">上映时间：1994-09-10(加拿大)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-3">3</i>
    <a href="/films/1206605" title="绿皮书" class="image-link" data-act="boarditem-click" data-val="{movieId:1206605}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/movie/c9b280de01549fcb71913edec05880585769972.jpg@160w_220h_1e_1c" alt="绿皮书" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1206605" title="绿皮书" data-act="boarditem-click" data-val="{movieId:1206605}">绿皮书</a></p>
        <p class="star">
                主演：维果·莫腾森,马赫沙拉·阿里,琳达·卡德里尼
        </p>
<p class="releasetime">上映时间：2019-03-01</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-4">4</i>
    <a href="/films/1292" title="海上钢琴师" class="image-link" data-act="boarditem-click" data-val="{movieId:1292}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/609e45bd40346eb8b927381be8fb27a61760914.jpg@160w_220h_1e_1c" alt="海上钢琴师" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1292" title="海上钢琴师" data-act="boarditem-click" data-val="{movieId:1292}">海上钢琴师</a></p>
        <p class="star">
                主演：蒂姆·罗斯,比尔·努恩,克兰伦斯·威廉姆斯三世
        </p>
<p class="releasetime">上映时间：2019-11-15</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">3</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-5">5</i>
    <a href="/films/1216365" title="小偷家族" class="image-link" data-act="boarditem-click" data-val="{movieId:1216365}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/movie/ac8f0004928fbce5a038a007b7c73cec746794.jpg@160w_220h_1e_1c" alt="小偷家族" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1216365" title="小偷家族" data-act="boarditem-click" data-val="{movieId:1216365}">小偷家族</a></p>
        <p class="star">
                主演：中川雅也,安藤樱,松冈茉优
        </p>
<p class="releasetime">上映时间：2018-08-03</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">8.</i><i class="fraction">1</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-6">6</i>
    <a href="/films/1211270" title="哪吒之魔童降世" class="image-link" data-act="boarditem-click" data-val="{movieId:1211270}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/005955214d5b3e50c910d7a511b0cb571445301.jpg@160w_220h_1e_1c" alt="哪吒之魔童降世" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1211270" title="哪吒之魔童降世" data-act="boarditem-click" data-val="{movieId:1211270}">哪吒之魔童降世</a></p>
        <p class="star">
                主演：吕艳婷,囧森瑟夫,瀚墨
        </p>
<p class="releasetime">上映时间：2019-07-26</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">6</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-7">7</i>
    <a href="/films/1203" title="霸王别姬" class="image-link" data-act="boarditem-click" data-val="{movieId:1203}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/61fea77024f83b3700603f6af93bf690585789.jpg@160w_220h_1e_1c" alt="霸王别姬" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1203" title="霸王别姬" data-act="boarditem-click" data-val="{movieId:1203}">霸王别姬</a></p>
        <p class="star">
                主演：张国荣,张丰毅,巩俐
        </p>
<p class="releasetime">上映时间：1993-07-26</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-8">8</i>
    <a href="/films/1303" title="美丽人生" class="image-link" data-act="boarditem-click" data-val="{movieId:1303}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/movie/580d81a2c78bf204f45323ddb4244b6c6821175.jpg@160w_220h_1e_1c" alt="美丽人生" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1303" title="美丽人生" data-act="boarditem-click" data-val="{movieId:1303}">美丽人生</a></p>
        <p class="star">
                主演：罗伯托·贝尼尼,朱斯蒂诺·杜拉诺,赛尔乔·比尼·布斯特里克
        </p>
<p class="releasetime">上映时间：2020-01-03</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">3</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-9">9</i>
    <a href="/films/4055" title="这个杀手不太冷" class="image-link" data-act="boarditem-click" data-val="{movieId:4055}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/movie/6bea9af4524dfbd0b668eaa7e187c3df767253.jpg@160w_220h_1e_1c" alt="这个杀手不太冷" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/4055" title="这个杀手不太冷" data-act="boarditem-click" data-val="{movieId:4055}">这个杀手不太冷</a></p>
        <p class="star">
                主演：让·雷诺,加里·奥德曼,娜塔莉·波特曼
        </p>
<p class="releasetime">上映时间：1994-09-14(法国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">4</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-10">10</i>
    <a href="/films/416" title="盗梦空间" class="image-link" data-act="boarditem-click" data-val="{movieId:416}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/moviemachine/c2496a7290a72eac6081321898c347693550574.jpg@160w_220h_1e_1c" alt="盗梦空间" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/416" title="盗梦空间" data-act="boarditem-click" data-val="{movieId:416}">盗梦空间</a></p>
        <p class="star">
                主演：莱昂纳多·迪卡普里奥,渡边谦,约瑟夫·高登-莱维特
        </p>
<p class="releasetime">上映时间：2010-09-01</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">0</i></p>        
    </div>

      </div>
    </div>

                </dd>
            </dl>

        </div>
            <div class="pager-main">
                
  
  <ul class="list-pager">



  
      <li class="active">
    <a class="page_1"
      href="javascript:void(0);" style="cursor: default"
  >1</a>

</li>
  <li >
    <a class="page_2"
      href="?offset=10"
  >2</a>

</li>
  <li >
    <a class="page_3"
      href="?offset=20"
  >3</a>

</li>
  <li >
    <a class="page_4"
      href="?offset=30"
  >4</a>

</li>
  <li >
    <a class="page_5"
      href="?offset=40"
  >5</a>

</li>

    <li class="sep">...</li>
      <li >
    <a class="page_10"
      href="?offset=90"
  >10</a>

</li>

  

<li>  <a class="page_2"
      href="?offset=10"
  >下一页</a>
</li>
</ul>'''
patten=re.compile('<i.*?board-index-\d+">(\d+)</i>.*?<p class="name"><a.*?data-act="boarditem-click".*?>(.*?)</a></p>.*?<p class="star">\n\s+(.*?)\s+</p>.*?<p class="releasetime">(.*?)</p>',re.S)
results=re.findall(patten,t)
for result in results:
    i=0
    while(i<4):
        print(result[i])
        i+=1

