#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.stats
import math
from scipy.stats import spearmanr, kendalltau

def ouvrirUnFichier(nom):
    with open(nom, "r", encoding='utf-8') as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

def conversionLog(liste):
    log = []
    for element in liste:
        log.append(math.log(element))
    return log

def ordreDecroissant(liste):
    liste.sort(reverse = True)
    return liste

def ordrePopulation(pop, etat):
    ordrepop = []
    for element in range(0, len(pop)):
        if np.isnan(pop[element]) == False:
            ordrepop.append([float(pop[element]), etat[element]])
    ordrepop = ordreDecroissant(ordrepop)
    for element in range(0, len(ordrepop)):
        ordrepop[element] = [element + 1, ordrepop[element][1]]
    return ordrepop

def classementPays(ordre1, ordre2):
    classement = []
    if len(ordre1) <= len(ordre2):
        for element1 in range(0, len(ordre2) - 1):
            for element2 in range(0, len(ordre1) - 1):
                if ordre2[element1][1] == ordre1[element2][1]:
                    classement.append([ordre1[element2][0], ordre2[element1][0], ordre1[element2][1]])
    else:
        for element1 in range(0, len(ordre1) - 1):
            for element2 in range(0, len(ordre2) - 1):
                if ordre2[element2][1] == ordre1[element1][1]:
                    classement.append([ordre1[element1][0], ordre2[element2][0], ordre1[element][1]])
    return classement

def analyseRangs(rangs1, rangs2):
    spearman = spearmanr(rangs1, rangs2)
    kendall = kendalltau(rangs1, rangs2)
    return spearman.correlation, kendall.correlation

# Question 2
print("Question 2")
df = ouvrirUnFichier("data/classement-restaurants-paris-2023-par-enseignes.csv")
print(df)

# Question 3
print("Question 3")
etablissements = df["Nombre d'établissement"]
print(etablissements)

# Question 4
print("Question 4")
etablissements = df["Nombre d'établissement"]
liste_etablissements = list(etablissements)
liste_triee = ordreDecroissant(liste_etablissements)
# print(liste_triee)

# Question 5
print("Question 5")
import matplotlib.pyplot as plt
plt.plot(liste_triee)
plt.title("Loi rang-taille des restaurants à Paris")
plt.xlabel("Rang des enseignes")
plt.ylabel("Nombre d'établissements")
plt.savefig("img/loi-rang-taille.png")
plt.show()

# Question 6
print("Question 6")
rangs = list(range(1, len(liste_triee) + 1))
rangs_log = conversionLog(rangs)
etablissements_log = conversionLog(liste_triee)
plt.figure()
plt.plot(rangs_log, etablissements_log)
plt.title("Loi rang-taille des restaurants à Paris (logarithmique)")
plt.xlabel("Logarithme du rang")
plt.ylabel("Logarithme du nombre d'établissements")
plt.savefig("img/loi-rang-taille-log.png")
plt.show()

# Question 7
print("Question 7")
# Il est possible de vérifier que les rangs sont bien ordonnés et qu'ils ne comportent aucune répétition (test de cohérence).
# Cependant, il n'est pas pertinent d'effectuer un test statistique classique sur les rangs,
# car ils indiquent uniquement un ordre entre les enseignes et ne représentent pas une quantité mesurable,
# le rang étant une variable ordinale.

# Question 9
print("Question 9")
df = ouvrirUnFichier("data/Le-Monde-HS-Etats-du-monde-2007-2026.csv")
print(df)

# Question 10
print("Question 10")
df_selection = df[["État", "Pop 2007", "Pop 2026", "Densité 2007", "Densité 2026"]]
print(df_selection)

# Question 11
print("Question 11")
etats = list(df_selection["État"])
pop2007 = list(df_selection["Pop 2007"])
pop2026 = list(df_selection["Pop 2026"])
densite2007 = list(df_selection["Densité 2007"])
densite2026 = list(df_selection["Densité 2026"])
ordre_pop2007 = ordrePopulation(pop2007, etats)
ordre_pop2026 = ordrePopulation(pop2026, etats)
ordre_densite2007 = ordrePopulation(densite2007, etats)
ordre_densite2026 = ordrePopulation(densite2026, etats)
print("Classement des pays par population en 2007 :")
print(ordre_pop2007)
print("Classement des pays par population en 2026 :")
print(ordre_pop2026)
print("Classement des pays par densité de population en 2007 :")
print(ordre_densite2007)
print("Classement des pays par densité de population en 2026 :")
print(ordre_densite2026)

# Question 12
print("Question 12")
comparaison_population = classementPays(ordre_pop2007, ordre_pop2026)
comparaison_population.sort()
print("Comparaison des classements par population (2007 / 2026) :")
print(comparaison_population)

comparaison_densite = classementPays(ordre_densite2007, ordre_densite2026)
comparaison_densite.sort()
print("Comparaison des classements par densité (2007 / 2026) :")
print(comparaison_densite)

# Question 13
print("Question 13")
classement2007_population = []
classement2026_population = []
for element in comparaison_population:
    classement2007_population.append([element[0], element[2]])
    classement2026_population.append([element[1], element[2]])
print("Classement population 2007 :", classement2007_population)
print("Classement population 2026 :", classement2026_population)

classement2007_densite = []
classement2026_densite = []
for element in comparaison_densite:
    classement2007_densite.append([element[0], element[2]])
    classement2026_densite.append([element[1], element[2]])
print("Classement densité 2007 :", classement2007_densite)
print("Classement densité 2026 :", classement2026_densite)


# Question 14
print("Question 14")
rangs_population_2007 = []
rangs_population_2026 = []
for element in comparaison_population:
    rangs_population_2007.append(element[0])
    rangs_population_2026.append(element[1])
print("Spearman pour la population :", spearmanr(rangs_population_2007, rangs_population_2026))
print("Kendall pour la population :", kendalltau(rangs_population_2007, rangs_population_2026))

rangs_densite_2007 = []
rangs_densite_2026 = []
for element in comparaison_densite:
    rangs_densite_2007.append(element[0])
    rangs_densite_2026.append(element[1])
print("Spearman pour la densité :", spearmanr(rangs_densite_2007, rangs_densite_2026))
print("Kendall pour la densité :", kendalltau(rangs_densite_2007, rangs_densite_2026))

# commenter le résultat dans le rapport d'activités


# Bonus
print("Bonus")
df2017 = ouvrirUnFichier("data/classement-restaurants-paris-2017-par-enseignes.csv")
df2023 = ouvrirUnFichier("data/classement-restaurants-paris-2023-par-enseignes.csv")
enseignes2017 = list(df2017["Enseigne"])
enseignes2023 = list(df2023["Enseigne"])
nb2017 = list(df2017["Nombre d'établissement"])
nb2023 = list(df2023["Nombre d'établissement"])
ordre2017 = ordrePopulation(nb2017, enseignes2017)
ordre2023 = ordrePopulation(nb2023, enseignes2023)

