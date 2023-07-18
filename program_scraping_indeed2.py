import time
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import json
from bs4 import BeautifulSoup
import cloudscraper
from cloudscraper import CloudScraper
import os
import pandas as pd

""" Konsep :
1. scraping indeed.com
py
2. user input :
2a. user input pekerjaan DONE
2b. user input lokasi DONE
2c. user input halaman DONE
3. dapatkan data html
4. scraping hasil html
5. masukan ke 
"""
"""
https://id.indeed.com/jobs?q={input pekerjaan}&l={input lokasi}&start={input halaman}&vjk=671ad2f62cc25cac
"""


def driver():
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(200)
    driver.implicitly_wait(120)
    return driver


def target_url(url):
    driver.get(url)
    html_content = driver.page_source
    with open('target.html', 'w', encoding='utf-8') as file:
        soup = BeautifulSoup(html_content, 'html.parser')
        file.writelines(soup.prettify())


def input_url():
    url = input("Masukan url :")
    return url

def scraping(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    content = soup.find_all('div', 'z1s6m00 _1hbhsw65a _1hbhsw6ga _1hbhsw6n _1hbhsw60 _1hbhsw662')
    jobs_list = []  # membuat tipe list
    i = 1
    for item in content:
        title = item.find('h1', 'z1s6m00 _1hbhsw64y y44q7i0 y44q7i3 y44q7i21 y44q7ii')
        company = item.find('span', 'z1s6m00 bev08l1 _1hbhsw64y _1hbhsw60 _1hbhsw6r')
        dict = {
            'no': i,
            'title': title.text,
            'company': company.text

        }
        i = i + 1
        jobs_list.append(dict)

    try:
        os.mkdir('json_result')
    except FileExistsError:
        pass

    with open('json_result/job_list1.json', 'w+') as json_data:
        json.dump(jobs_list, json_data)
    print('jaon created')

        # create csv
    df = pd.DataFrame(jobs_list)
    df.to_csv('indeed_data1.csv', index=False)
    df.to_csv('indeed_data1.xlsx', index=False)

        # data created
    print('data created succes')






if __name__ == "__main__":
    url = input_url()
    scraping(url)
    driver = driver()
    target_url(url=url)
    time.sleep(60)
