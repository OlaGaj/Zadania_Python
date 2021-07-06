import requests as r
from bs4 import BeautifulSoup 
result=r.get
('https://pogoda.onet.pl/prognoza-pogody/gdynia-287798')
soup = BeautifulSoup(result.content, 'html.parser')
element = soup.find('div', {'class': 'temp'})
print('Temperatura w Gdyni to', element.txt)
