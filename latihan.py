import requests
from bs4 import BeautifulSoup

url = 'https://www.jobstreet.co.id/id/python-jobs/in-Jakarta-Raya'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
#print(soup.find('title'))

#print(soup.find('h1'))

#tes = soup.find_all('a', href=True)
#for link in tes:
    #print(link)

#print(soup.find(id="header"))

#print(soup.find_all('div', {'class': 'panel-header'}))

#print(soup.find_all('div', {'class': 'panel-header'})[0])

#boxes = soup.find_all('div', {'class': 'panel'})
#box_names = []
#for box in boxes:
    #title = box.find('h3')
    #box_names.append(title.text)
#print(box_names[:5])

#logo = soup.find('a', {'id': 'logo'})
#print(logo.text)

# Parsing using HTML tag attributes
#description = soup.find('meta', attrs={'name':'description'})
#meta_robots =  soup.find('meta', attrs={'name':'robots'})
#print('description: ',description)
#print('meta robots: ',meta_robots)

#tes = soup.find_all('option')
#for tes1 in tes:
    #print(tes1.text)

#a_child = soup.find_all('a')[0]
#print(a_child.findChild())
