import feedparser

blog_url = "https://teawon.github.io/feed.xml"
rss_feed = feedparser.parse(blog_url)

MAX_NUM = 2

latest_posts = ""

for idx, entrie in enumerate(rss_feed['entries']):
  if idx > MAX_NUM:
     break;
  feed_date = entrie['published_parsed']
  latest_posts += f" - [{feed_date.tm_mon}/{feed_date.tm_mday} - {entrie['title']}]({entrie['link']})\n"

print(latest_posts)

preREADME = """
## Tech Stack
<p align="left">
<img src="https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB" />
<img src="https://img.shields.io/badge/Spring_Boot-F2F4F9?style=for-the-badge&logo=spring-boot" />
<img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" />
<img src="https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white"  />
<img src="https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white  " />

</p>

## Git Stats
![teawon](https://github-readme-stats.vercel.app/api?username=teawon&show_icons=true)
[![teawon](https://github-readme-stats.vercel.app/api/top-langs/?username=teawon&show_icons=true&hide_border=true&title_color=004386&icon_color=004386&layout=compact)](https://github.com/teawon)

[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=hiyou882)](https://solved.ac/hiyou882/)

## Latest Blog Post
"""

resultREADME = f"{preREADME}{latest_posts}"

with open("README.md", "w", encoding='utf-8') as f :
  f.write(resultREADME)
