import requests
import json
from bs4 import BeautifulSoup
import cloudscraper
from cloudscraper import CloudScraper
import os
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# scraper = cloudscraper.create_scraper()
# url = 'https://www.indeed.com/q-odoo-remote-jobs.html?vjk=6a129b83abd8da73'
# s = requests.session()
# r = scraper(url)
# res = s.get(url)
# print(res.status_code)
# sp = BeautifulSoup(r.text,'html.parser')
# print(sp.title.text)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'}

url = 'https://www.jobstreet.co.id/id/python-jobs/in-Jakarta-Raya'
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')


def get_total_page(query, location):
    params :{
        'q': 'query',
        'l': 'location'
    }
    res = requests.get(url,params=params, headers=headers)

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()

    total_pages = []
    # scraping step
    soup = BeautifulSoup(res.text, 'html.parser')
    tes = soup.find_all('option')
    for tes1 in tes:
        total_pages.append(tes1.text)

    total = max(total_pages)
    return total


def get_all_items(query, location):
    params = {
        'q': 'query',
        'l': 'location'

    }
    res = requests.get(url,params=params, headers=headers)

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()

    soup = BeautifulSoup(res.text, 'html.parser')
    content=soup.find_all('div','z1s6m00 _1hbhsw65a _1hbhsw6ga _1hbhsw6n _1hbhsw60 _1hbhsw662')

    jobs_list = [] #membuat tipe list
    i =1
    for item in content:
        title = item.find('h1', 'z1s6m00 _1hbhsw64y y44q7i0 y44q7i3 y44q7i21 y44q7ii')

        #title = item.find('span', 'z1s6m00 rqoqz5')
        company = item.find('span', 'z1s6m00 bev08l1 _1hbhsw64y _1hbhsw60 _1hbhsw6r')
        #link = item.find('h1','z1s6m00 _1hbhsw64y y44q7i0 y44q7i3 y44q7i21 y44q7ii')
        #link1 = link.find('a', href=True)['href']

        #if 'www' in link2:
            #link3 = link2
        #else:
            #link3 = 'link is not available'


        #membuat tipe dictionary/sorting data
        dict = {
            'no': i,
            'title': title.text,
            'company': company.text
            #'link': link1



        }

        i=i+1
        jobs_list.append(dict) #membuat tipe list

    #print(jobs_list)
    #membuat json file, json = list
    try:
        os.mkdir('json_result')
    except FileExistsError:
        pass

    with open('json_result/{query}_in_{location}.json', 'w+') as json_data:
        json.dump(jobs_list, json_data)
    print('jaon created')

    return jobs_list

def create_document(dataFrame, filename):
    try:
        os.mkdr('data_result')
    except FileExistsError:
        pass

    df = pd.DataFrame(jobs_list)
    df.to_csv(f'data_result/{filename}.csv', index=False)
    df.to_csv(f'data_result/{filename}.xlsx', index=False)

    print(f'file{filename}.csv and {filename}.xlsx succesfully created ')

def run():
    query = input('Enter Your Query: ')
    location = input('Enter Your location: ')

    total = get_total_page(query, location)

if __name__ == '__main__':
    get_total_page(query, location)
    get_all_items()
