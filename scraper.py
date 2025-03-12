import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_articles():
    url = "https://www.agenceecofin.com/"
    response = requests.get(url)
    links = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        for a in soup.find_all('a', href=True):
            link = a['href']
            if not link.startswith(('http://', 'https://')):
                link = 'https://www.agenceecofin.com' + link
            links.append(link)
    else:
        print("Erreur lors de la récupération de la page :", response.status_code)

    df = pd.DataFrame(links, columns=['Links'])
    df = df.drop_duplicates().reset_index(drop=True)
    df = df[df['Links'].str.startswith('https://www.agenceecofin.com/')]
    return df['Links'].tolist()

def process_articles(links):
    contents = []
    for link in links:
        response = requests.get(link)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.find('h1').get_text(strip=True) if soup.find('h1') else 'Titre non trouvé'
            texts = []
            for element in soup.find_all(['em', 'span'], style=True):
                texts.append(element.get_text(strip=True))

            contents.append({'title': title, 'content': '\n'.join(texts)})
        else:
            print(f"Erreur lors de la récupération de la page {link} :", response.status_code)
    return contents
