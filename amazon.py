import requests
from bs4 import BeautifulSoup
import time

'''

Recupère le code source de la page et le parse afin de recupèrer le titre et le prix de l'article selon l'url entrée
Entrée : url
Sortie : titre, prix

'''
def recherche(url):
    
    # Les en-tête de la requête
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.320'}

    #On recupère la reponse à la requête
    response = requests.get(url, headers=headers)

    #Si on a une bonne réponse du serveur et donc un code 200
    if response.ok :
        soup = BeautifulSoup(response.content, 'html.parser')

        # On recupère le titre
        title = soup.find(id="productTitle").text.strip().replace(","," ")

        # On recupère le prix
        prix = soup.find(id="price_inside_buybox").text.strip().replace(",",".")

        
        print("\ntitre : "+title)

        print("\nprix : "+prix)

    return title,prix

'''

Ecrit dans un fichier .csv l'url, le titre et le prix
Entrée : url, titre, prix

'''
def enrengistrement(url,titre,prix):
     with open('amazonSheet.csv', 'w') as outf:
        outf.write('url,titre,prix\n')
        outf.write(url+","+titre.replace(","," ")+","+prix+"\n")

while(1):

    print("1 - Recuperer Prix et titre")
    print("q - Quitter")
    choix = input("Entrer votre choix ?\n")

    if choix == '1':
        url = input("\nEntrer l'url : ")
        titre , prix = recherche(url)
        enrengistrement(url,titre,prix)


    if choix == 'q':
        exit()
