import requests
from bs4 import BeautifulSoup

base_url: str = "https://www.indeed.com/jobs?"
site = "https://www.indeed.com"

# site counter
counter = 10

# headers section
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    # "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "cookie": 'CTK=1fie6341bo1n0800; INDEED_CSRF_TOKEN=8OxUL9mEPqMVKVm9DSvT6gi0Rbm9SuvM; loctip=1; SHARED_INDEED_CSRF_TOKEN=8OxUL9mEPqMVKVm9DSvT6gi0Rbm9SuvM; CO=US; MICRO_CONTENT_CSRF_TOKEN=PseL8mahc9AEhM5Yug8IHNJAR4QqZHEd; pjps=1; CO=US; CSRF=Jj07tn4dRcKt8v4PZyeTLp7JD8iAjkzQ; indeed_rcc="PREF:LV:CTK:CO:UD:RQ"; RJAS=v5898fd39bb9547b9; cp=1; RQ="q=&l=new+york&ts=1634711450105:q=python&l=Surabaya&ts=1634711432596:q=Disability&l=Work+At+Home&ts=1634711272279:q=Disability+Services&l=&ts=1634711246829:q=Part+Time+Disability&l=&ts=1634711221807"; jaSerpCount=8; PREF="TM=1634711453071:L="; ac=Rs0/8DFvEeymfSnG9ya5GA#Rs7toDFvEeymfSnG9ya5GA; LV="LA=1634711450:CV=1634711244:TS=1634711212"; UD="LA=1634711450:CV=1634711244:TS=1634711212"; JSESSIONID=4D92198EF2F38F3CFCCCB6724EFDA416; PTK=tk=1fie6acfhpi3p800&type=jobsearch&subtype=topsearch',
    "referer": "https://www.indeed.com/jobs?q&l=new%20york&vjk=b95dd89ede1a410a",
    "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
}

params = {"q": "python developer", "l": "new york"}
res = requests.get(base_url, params=params, headers=headers)

# scraping process
soup = BeautifulSoup(res.text, "html.parser")
pages = soup.find('ul', attrs={'class': 'pagination-list'}).find_all('li')
total = [ page.text for page in pages]
print(max(total))

job_list: list = []
#params: dict = {"q": keywors, "l": location, "start": start}
res = requests.get(base_url, params=params, headers=headers)

soup = BeautifulSoup(res.text, "html.parser")
products = soup.find_all("table", attrs={"class": "jobCard_mainContent big6_visualChanges"})
print(f"item found: {len(products)}")

list = []
for item in products:
    title = item.find("h2", attrs={"class": "jobTitle"}).text.strip()
    company = item.find("span", attrs={"class": "companyName"})
    company_name = company.text.strip()
    try:
       company_link = site + company.find("a")["href"]
    except:
       company_link = "Link not available"
    company_address = item.find(
           "div", attrs={"class": "companyLocation"}
    ).text.strip()

            # reformating data on dictionary
    data_dict: dict = {
        "job title": title,
        "company name": company_name,
        "company profile": company_link,
         "address": company_address.replace("•", ""),
     }

    print(data_dict)


judul= item.find("h2", attrs={"class": "jobTitle"}).text.strip()
