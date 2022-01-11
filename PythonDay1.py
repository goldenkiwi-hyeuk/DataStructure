#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests # 웹연결 라이브러리


# In[3]:


from bs4 import BeautifulSoup as bs # 분석을 용이하게 다듬어주는 라이브러리


# In[4]:


import pandas as pd # 데이터 분석 관련 라이브러리


# In[5]:


url = "https://music.bugs.co.kr/chart?wl_ref=M_left_02_01" # 벅스, 지니, 멜론
html = requests.get(url)


# In[6]:


soup = bs(html.text, 'html.parser') # html.text 덩어리진 html의 글자를 불러와서 html로 잘라라(html.parser)


# In[7]:


print(soup)


# In[8]:


# tr은 한 줄
# td는 한 칸
len(soup.select('tr')) # soup에서 tr태그가 들어가있는 애들을 선택해라
# html tage(code)를 선택할때는 select을 사용
# 만약 BeautifulSoup를 사용하지 않으면 tr태그와 tr이 들어간 단어를 구분하지 못함 why? BeautifulSoup를 사용하지 않으면 그냥 글자이기 때문에


# In[9]:


songs = soup.select('tr') # 그냥 tr태그 모두 긁어오기
len(songs)


# In[10]:


print(songs)


# In[11]:


# 범위 줄이기
songs = soup.select('tbody > tr') # tbody안에 있는 tr태그들을 긁어오기
len(songs)


# In[12]:


# 범위 줄이기
songs = soup.select('table.byChart > tbody > tr')
# table의 클래스(참고로 클래스는 .으로 표현함)로 범위 줄이기
# byChart라는 클래스 활용(모든 풀네임을 적지 않아도 괜찮음)
# tbody안에 있는 tr태그들을 긁어오기
len(songs)


# In[19]:


song = songs[0]


# In[20]:


# a 태그는 링크를 연결하는 것
title = song.select('a')


# In[21]:


len(title)


# In[23]:


# 범위 줄이기
title = song.select('p > a')
# p태그는 문단을 나타내는 것
len(title)


# In[24]:


title


# In[25]:


# 범위 줄이기
title = song.select('p.title > a')
len(title)


# In[26]:


title


# In[28]:


title = song.select('p.title > a')[0].text # 해당 내용에서 html 말고 글자만 뽑아내라
title


# In[30]:


singer = song.select('p.artist > a')[0].text
singer


# In[32]:


song_data = []
rank = 1

songs = soup.select('table.byChart > tbody > tr')

for song in songs:
    title = song.select('p.title > a')[0].text
    singer = song.select('p.artist > a')[0].text
    song_data.append(['Bugs', rank, title, singer])
    rank += 1

df = pd.DataFrame(song_data)
df


# In[ ]:


song

