import requests
from bs4 import BeautifulSoup
import os
import re


def Corpus(url):
  req = requests.get(url)
  soup = BeautifulSoup(req.content, 'html.parser')

  titrePage = soup.find("h1", class_="firstHeading").text
  #Création du fichier texte pour sauvegarder les données du texte
  f = open(f"{titrePage}.txt", "w", encoding="utf-8")
  f.write(f"//{url}\n--{titrePage}--\n\n")

  # Scrape
  for information in soup.descendants:
      if information.name == "span":
          try:
              if information["class"][0] == "mw-headline":
                  headline = information.get_text()
                # print(f"{headline}")
                  f.write(f"\n{headline}:\n\n")   
          except KeyError: 
              pass
      #on scrape les paragraphes
      elif information.name == "p":
          text = information.get_text()
          #print(f"{text}")
          f.write(f"{text}")

      #on scrape les balises ul qui ne possedent pas d'id et qui n'on pas de class    
      elif information.name == "ul":
            if information.get('id') == None:
              if information.has_attr('class') == False:
                text2 = information.get_text()
                #print(f"{text2}") #Print le texte
                f.write(f"{text2}")
  f.close() #fermeture du fichier txt
# je liste le noms de mes fichiers dans corpus 
mesFichiers = os.listdir('fichiers/corpus')
#pour chacun de mes fichiers je fait l'action d'ouvrir le txt prendre le lien wikipedia
for fichier in mesFichiers :
  file1 = open('fichiers/corpus/' + fichier + "/lien_source_google.txt","r")
  urlRegex = re.search(r"https\:\/\/([\w\.]+)wikipedia.org\/wiki\/([\w]+\_?)+",file1.read())
  if urlRegex :
    urlTemp = urlRegex.group()
    Corpus(urlTemp)