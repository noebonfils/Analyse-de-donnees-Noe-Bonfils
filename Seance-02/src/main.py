#coding:utf8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def listedesterritoires(territoiretest, exportationUSD, importationUSD):
    listedesterritoires = [[territoiretest[0], 0]]
    pos = 0
    for element in range(0,len(territoiretest)):
        if territoiretest[element] != listedesterritoires[pos][0]:
            listedesterritoires.append([territoiretest[element], element])
            pos += 1
    lignes = []
    for element in range(1,len(listedesterritoires)):
        lignes.append(listedesterritoires[element][1] - 1)
    lignes.append(len(territoiretest))
    liste = []
    for element in range(0,len(listedesterritoires)):
        liste.append([listedesterritoires[element][0], listedesterritoires[element][1], lignes[element]])
    totalparterritoire = []
    for element in range(0,len(liste)):
        totalparterritoire.append([liste[element][0], exportationUSD[liste[element][1]:liste[element][2]].sum(), importationUSD[liste[element][1]:liste[element][2]].sum()])
    return totalparterritoire

def nettoyage(colonne):
    colonne2 = []
    for element in colonne:
        if element == 'Sans objet' or element =='-':
            colonne2.append(float(0))
        else:
            colonne2.append(float(element))
    return colonne2

def getliste(territoiretest):
    listedesterritoires = [[territoiretest[0], 0]]
    pos = 0
    for element in range(0,len(territoiretest)):
        if territoiretest[element] != listedesterritoires[pos][0]:
            listedesterritoires.append([territoiretest[element], element])
            pos += 1
    lignes = []
    for element in range(1,len(listedesterritoires)):
        lignes.append(listedesterritoires[element][1] - 1)
    lignes.append(len(territoiretest))
    liste = []
    for element in range(0,len(listedesterritoires)):
        liste.append([listedesterritoires[element][0], listedesterritoires[element][1], lignes[element]])
    return liste

# Question 4
print("Question 4")
# Source des données : https://www.cepii.fr/CEPII/en/bdd_modele/bdd_modele_item.asp?id=37
with open("./data/Produits-alimentaires-2024.csv", "r", encoding="utf-8") as fichier:
    contenu = pd.read_csv(fichier)

# Question 5
print("Question 5")
print(contenu)

# Question 6
print("Question 6")
Nombre_de_lignes = len(contenu)
Nombre_de_colonnes = len(contenu.columns)
print("Nombre de lignes: ", Nombre_de_lignes)
print("Nombre de colonnes : ", Nombre_de_colonnes)

# Question 7
print("Question 7")
print(list(contenu.head(0).columns))

# Question 8
print("Question 8")
types_colonnes = [
    ['year',  "int"],
    ['origin_id', "str"],
    ['dest_id', "str"],
    ['Dist_VO (km)', "int"],
    ['hs92_Section_id', "str"],
    ['hs92_HS02_id', "str"],
    ['hs92_HS04_id', "str"],
    ['hs92_HS06_id', "str"],
    ['export_val', "int"],
    ['import_val', "int"],
    ['export_ton', "float"],
    ['import_ton', "float"],
]
print(types_colonnes)

# Contenu des colonnes
# "year" : année
# "origin_id" : territoire de référence
# "dest_id" : territoire partenaire
# "Dist_VO (km)" : distance intercentroïde entre les deux territoires
# "hs92_Section_id" : code Section du produit
# "hs92_HS02_id" : code 2-digit du produit
# "hs92_HS04_id" : code 4-digit du produit
# "hs92_HS06_id" : code 6-digit du produit
# "export_val" : valeur des exportations du territoire de référence vers le territoire partenaire en dollars courants
# "import_val" : valeur des importations du territoire partenaire vers le territoire de référence en dollars courants
# "export_ton" : valeur des exportations du territoire de référence vers le territoire partenaire en tonnes
# "import_ton" : valeur des importations du territoire partenaire vers le territoire de référence en tonnes

# Question 9
print("Question 9")
print(contenu[["export_ton", "import_ton"]])

# Question 10
print("Question 10")
total1 = 0
total2 = 0

for valeur in contenu["export_ton"]:
    if valeur != "-":
        total1 = total1 + float(valeur)

for valeur in contenu["import_ton"]:
    if valeur != "-":
        total2 = total2 + float(valeur)

print("Total des exportations :", total1)
print("Total des importations :", total2)


# Question 11
# Appliquer la fonction listedesterritoires(...) sur vos colonnes ici
#print("Question 11")

#colonnes = contenu[["origin_id", "export_val", "import_val"]]

#liste = []

#for territoire in colonnes["origin_id"]:
    #if territoire not in liste:
        #liste.append(territoire)

#print(liste)

#for territoire in liste:
    #lignes = contenu[contenu["origin_id"] == territoire]
    #exportations = lignes ["export_val"].sum()
    #importations = lignes["import_val"].sum()
    #plt.pie([exportations, importations], labels=["Exportations : " + str(exportations) + "USD", "Importations : " + str(importations) + "USD"], textprops={"fontsize": 8})
    #plt.title(territoire)
    #plt.savefig("img/" + str(territoire) +".png")
    #plt.close()

# Questions 12 et 14
print("Questions 12 et 14")

donnees2titre = [
    "distance",
    "export_val_2",
    "import_val_2",
    "export_ton_2",
    "import_ton_2"
]

# Appliquer la fonction :
# liste = getliste(...)

liste = getliste(contenu["origin_id"])

# Application la fonction nettoyage(...) sur vos colonnes ici

liste_distances = nettoyage(contenu["Dist_VO (km)"])
liste_export_val = nettoyage(contenu["export_val"])
liste_import_val = nettoyage(contenu["import_val"])
liste_export_ton = nettoyage(contenu["export_ton"])
liste_import_ton = nettoyage(contenu["import_ton"])

# Mettre le code nouveau DataFrame ici et appeler la liste donnees2

donnees2 = pd.DataFrame({
    donnees2titre[0]: liste_distances,
    donnees2titre[1]: liste_export_val,
    donnees2titre[2]: liste_import_val,
    donnees2titre[3]: liste_export_ton,
    donnees2titre[4]: liste_import_ton
})


parametres = []
quartiles = []
deciles = []

for element in range(0,len(donnees2.columns)):
    parametres2 = []
    distanceinterquartile = []
    distanceinterdecile = []
    for element2 in range(0,len(liste)):
        codeiso = liste[element2][0]
        data2 = donnees2.iloc[liste[element2][1]:liste[element2][2],element]

        moyenne = data2.mean()
        mediane = data2.median()
        mode = data2.mode().iloc[0]
        ecarttype = data2.std()
        ecartabsolumoyen = (data2 - moyenne).abs().mean()
        etendue = data2.max() - data2.min()
        parametres2.append([codeiso, moyenne, mediane, mode, ecarttype, ecartabsolumoyen, etendue])

        quartile = data2.quantile([0.25, 0.75])
        distanceinterquartile.append([codeiso, (quartile[0.75] - quartile[0.25]).round(decimals=2)])
        decile = data2.quantile([0.1, 0.9])
        distanceinterdecile.append([codeiso, (decile[0.9] - decile[0.1]).round(decimals=2)])
    parametres.append(parametres2)
    quartiles.append(distanceinterquartile)
    deciles.append(distanceinterdecile)


# Compléter la boucle à partir des différents éléments précédents. Le nom des listes est celle proposée dans les commentaires.
# parametres = []
# quartiles = []
# deciles = []
# for element in range(0,len(donnees2.columns)):
#     parametres2 = []
#     distanceinterquartile = []
#     distanceinterdecile = []
#     for element2 in range(0,len(liste)):
#         codeiso = liste[element2][0]
#         data2 = donnees2.iloc[liste[element2][1]:liste[element2][2],element]

#         moyenne = 
#         mediane = 
#         mode = 
#         ecarttype = 
#         ecartabsolumoyen = 
#         etendue = 
#         parametres2.append([codeiso, moyenne, mediane, mode, ecarttype, ecartabsolumoyen, etendue])

#         quartile = 
#         distanceinterquartile.append([codeiso, (quartile[0.75] - quartile[0.25]).round(decimals=2)])
#         decile = 
#         distanceinterdecile.append([codeiso, (decile[0.9] - decile[0.1]).round(decimals=2)])
#     parametres.append(parametres2)
#     quartiles.append(distanceinterquartile)
#     deciles.append(distanceinterdecile)

# Question 13
print("Question 13")
# print(parametres)

# Question 14
# print("Question 14")

# Question 15
print("Question 15")
# for element in range(len(donnees2.columns)):
#     plt.figure
#     plt.boxplot(donnees2.iloc[:, element])
#     plt.savefig("img/boite_" + str(element) + ".png")
#     plt.close()

# Question 16
print("Question 16")
# Source des données : BDCOM, https://www.apur.org/fr/open-data-cartes/open-data/base-donnees-commerces-parisiens
with open("./data/restaurants-paris-2023.csv", "r", encoding="utf-8") as fichier:
    contenu2 = pd.read_csv(fichier)

categories = [0, 0, 0]
for surface in contenu2["surf"]:
    if surface == 1: categories[0] += 1
    elif surface == 2: categories[1] += 1
    elif surface == 3: categories[2] += 1
print("Code 1 :", categories[0], "restaurants")
print("Code 2 :", categories[1], "restaurants")
print("Code 3 :", categories[2], "restaurants")
# voir l'organigramme

# Question bonus
print("Question bonus")

noms_pays = pd.read_excel("./data/country_names.xls")
print(noms_pays.head())