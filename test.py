import requests
from bs4 import BeautifulSoup

# URL de la page web à scraper
url = 'https://capacitorjs.com/docs/basics/workflow'

# Faire une requête GET pour obtenir le contenu de la page
response = requests.get(url)

# Vérifier que la requête a réussi
if response.status_code == 200:
    # Parser le contenu HTML de la page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Trouver toutes les balises <h2>
    h2_tags = soup.find_all('h2')
    
    # Afficher le texte de chaque balise <h2>
    for tag in h2_tags:
        print(tag.text)
else:
    print(f"Erreur : Impossible d'accéder à la page. Statut : {response.status_code}")
