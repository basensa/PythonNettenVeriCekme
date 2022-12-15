import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.turkiye.gov.tr/doviz-kurlari"

r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")

parabirimi1 = soup.find_all("tr")

liste= list()
for kur in range(1,(int(len(parabirimi1)/2))):  # "tr" BAŞLIĞI ALTINDAKİ SADECE İLK 22 VERİYİ İSTİYORUZ
    parabirimi1[kur] = ((parabirimi1[kur].text).strip())
    liste.append(parabirimi1[kur])
    liste[kur-1] = liste[kur-1].split("\n")  # GELEN VERİMİZİ LİSTE HALİNE GETİRİYORUZ

pliste = pd.DataFrame(liste,columns = ["DÖVİZCİNSİ","DÖVİZALIŞ","DÖVİZSATIŞ","EFEKTİFALIŞ","EFEKTİFSATIŞ"])
print(pliste.head(10))
#print(liste[0])




