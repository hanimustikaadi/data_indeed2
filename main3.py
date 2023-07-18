import requests
from bs4 import BeautifulSoup
import cloudscraper
from cloudscraper import CloudScraper
import os

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


def get_total_page():
    res = requests.get(url, headers=headers)

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


def get_all_items():
    res = requests.get(url, headers=headers)

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()

    soup = BeautifulSoup(res.text, 'html.parser')
    content=soup.find_all('div','z1s6m00 _1hbhsw65a _1hbhsw6ga _1hbhsw6n _1hbhsw60 _1hbhsw662')
    i =1
    for item in content:
        title = item.find('h1', 'z1s6m00 _1hbhsw64y y44q7i0 y44q7i3 y44q7i21 y44q7ii')

        #title = item.find('span', 'z1s6m00 rqoqz5')
        company = item.find('span', 'z1s6m00 bev08l1 _1hbhsw64y _1hbhsw60 _1hbhsw6r')
        #link = company.find('a', href=True)['href']

        #if 'www' in link2:
            #link3 = link2
        #else:
            #link3 = 'link is not available'



        dict = {
            'no': i,
            'title': title.text,
            'company': company.text



        }

        print(dict)
        i=i+1






if __name__ == '__main__':
    get_total_page()
    get_all_items()
