#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re
from bs4 import BeautifulSoup
import requests
import json

import time

localtime = time.asctime(time.localtime(time.time()))
date = time.strftime("%Y-%m-%d", time.localtime())
print(date)


def get_one_page(url):
    response = requests.get(url)
    return response.text


html_doc = get_one_page("https://www.bilibili.com/ranking/all/0/0/3")

soup = BeautifulSoup(html_doc, 'lxml')
i = 0
d = []
l1 = soup.find_all('div', attrs={'class': 'num'})
l2 = soup.find_all('a', attrs={'class': 'title'})
while True:
    try:
        dic = {}
        for m in l1[i]:
            dic["rank"] = m
        for k in l2[i]:
            dic["name"] = k.replace("'", '\"')
            # l1=re.findall(r'div class="num">(.?)*</div>',soup)
        href = l2[i]["href"]
        dic["href"] = href
        d.append(dic)
        i += 1
    except:
        for i in d:
            print(i)
        json_d = json.dumps(d, ensure_ascii=False)
        break

data = json.loads(json_d)
# print(data[0]["name"])

# cursor.execute("insert into people values (%s, %s)", (who, age))

import psycopg2
import getpass

database = 'xialixiali'
user = 'postgres'
password = getpass.getpass('password:')

"""
database:University
user:postgres
password:
"""

conn = psycopg2.connect(database=database, user=user, password=password)  # connect to the database
cur = conn.cursor()
print("connect successfully")
# cursor.execute("insert into people values (%s, %s)", (who, age))

cur.execute("insert into Time(day) values (%r)" % (
    str(date)))  # execute() for entering one line command of SQL
print("Date enter")
for i in data:
    cur.execute("insert into rank(day,rank,name,href) values (%r,%r,%r,%r)" % (
        str(date), i["rank"], i["name"], i["href"]))
print("Data enter")
conn.commit()
conn.close()
input()