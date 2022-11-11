import feedparser

blog_url = "https://teawon.github.io/feed.xml"
rss_feed = feedparser.parse(blog_url)

MAX_NUM = 3

latest_posts = ""

for idx, entrie in enumerate(rss_feed['entries']):
  if idx > MAX_NUM:
     break;
  feed_date = entrie['published_parsed']
  latest_posts += f" - [{feed_date.tm_mon}/{feed_date.tm_mday} - {entrie['title']}]({entrie['link']})\n"

print(latest_posts)

preREADME = """
## Tech Stack


 #### Most Interested & experienced
 <p align="left">
<img src="https://img.shields.io/badge/react-61DAFB.svg?style=for-the-badge&logo=react&logoColor=white" />
 <img src="https://img.shields.io/badge/redux-764ABC.svg?style=for-the-badge&logo=redux&logoColor=%white" />
 <img src="https://img.shields.io/badge/typescript-3178C6.svg?style=for-the-badge&logo=typescript&logoColor=white" />
  <img src="https://img.shields.io/badge/javascript-F7DF1E.svg?style=for-the-badge&logo=javascript&logoColor=white" />
</p>
 
 #### Have used 
 <p align="left">
<img src="https://img.shields.io/badge/Django-%2320232a.svg?style=for-the-badge&logo=Django&logoColor=%2361DAFB" />
  <img src="https://img.shields.io/badge/nginx-009639.svg?style=for-the-badge&logo=Nginx&logoColor=white" />
<img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" />
<img src="https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white"  />
<img src="https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white  " />
 <img src="https://img.shields.io/badge/Spring_Boot-F2F4F9?style=for-the-badge&logo=spring-boot" />
</p>

#### studying
 <p align="left">
  <img src="https://img.shields.io/badge/Kotlin-0088CC.svg?style=for-the-badge&logo=Kotlin&logoColor=%#7F52FF" />
 </p>

## Git Stats
![teawon](https://github-readme-stats.vercel.app/api?username=teawon&show_icons=true)
[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=hiyou882)](https://solved.ac/hiyou882/)

## Latest Blog Post
"""

resultREADME = f"{preREADME}{latest_posts}"

with open("README.md", "w", encoding='utf-8') as f :
  f.write(resultREADME)
