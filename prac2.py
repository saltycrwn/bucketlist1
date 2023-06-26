import requests
from bs4 import BeautifulSoup


url = "https://www.airbnb.com/s/Seoul/homes?place_id=ChIJzWXFYYuifDUR64Pq5LTtioU&query=Seoul&refinement_paths%5B%5D=%2Fhomes&tab_id=home_tab"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers=headers)

req = data.text
soup = BeautifulSoup(req, 'html.parser')

images = soup.select('img')
for image in images:
    print(image['src'])


