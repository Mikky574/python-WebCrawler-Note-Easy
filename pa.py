#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re
from bs4 import BeautifulSoup
import requests
import json

import time
localtime = time.asctime( time.localtime(time.time()) )
date=time.strftime("%Y-%m-%d", time.localtime())
print (date)

def get_one_page(url):
    response = requests.get(url)
    return response.text

html_doc =get_one_page("https://www.bilibili.com/ranking/all/0/0/3")

soup=BeautifulSoup(html_doc,'lxml')
i=0
d=[]
l1=soup.find_all('div',attrs={'class':'num'})
l2=soup.find_all('a',attrs={'class':'title'})
while True: #创造死循环，一直到i突破列表上限，会IndexError，然后执行except退出循环
    try:
        dic={}
        for m in l1[i]: #这里取出div框里的数据
            dic["rank"]=m
        for k in l2[i]:
            dic["name"]=k.replace("'",'\"') #这里取出a框里的数据
        href =l2[i]["href"] #这里取出a框的href属性的属性值
        dic["href"]=href
        d.append(dic)
        i+=1
    except:
        for i in d:
            print(i)
        json_d = json.dumps(d,ensure_ascii=False)   #结果整合为json格式，其实这步对于本程序完全不必要，主要为了方便有需要的人输出json文件
        break

data=json.loads(json_d) #再解压为list型数据，所以其实用上面的d就可以的，这里展示json数据(原为str数据类型)的解压

import psycopg2
import getpass

database='xialixiali'
user='postgres'
password=getpass.getpass('password:')

"""
database:University
user:postgres
password:
"""

conn=psycopg2.connect(database=database, user=user, password=password)  #connect to the database
cur = conn.cursor()
print("connect successfully")

cur.execute("insert into Time(day) values (%r)" %(str(date)))    #execute() for entering one line command of SQL
print("Date enter")
for i in data:
    cur.execute("insert into rank(day,rank,name,href) values (%r,%r,%r,%r)" %(str(date),i["rank"],i["name"],i["href"])) #insert data
print("Data enter")
conn.commit()
conn.close()
input()