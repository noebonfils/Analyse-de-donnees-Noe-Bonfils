#coding:utf8

import pandas as pd
import math
import scipy
import scipy.stats
from scipy.stats import shapiro
import matplotlib.pyplot as plt

# C'est la partie la plus importante dans l'analyse de données. D'une part, elle n'est pas simple à comprendre tant mathématiquement que pratiquement. D'autre, elle constitue une application des probabilités. L'idée consiste à comparer une distribution de probabilité (théorique) avec des observations concrètes. De fait, il faut bien connaître les distributions vues dans la séance précédente afin de bien pratiquer cette comparaison. Les probabilités permettent de définir une probabilité critique à partir de laquelle les résultats ne sont pas conformes à la théorie probabiliste.
# Il n'est pas facile de proposer des analyses de données uniquement dans un cadre univarié. Vous utiliserez la statistique inférentielle principalement dans le cadre d'analyses multivariées. La statistique univariée est une statistique descriptive. Bien que les tests y soient possibles, comprendre leur intérêt et leur puissance d'analyse dans un tel cadre peut être déroutant.
# Peu importe dans quelle théorie vous êtes, l'idée de la statistique inférentielle est de vérifier si ce que vous avez trouvé par une méthode de calcul est intelligent ou stupide. Est-ce que l'on peut valider le résultat obtenu ou est-ce que l'incertitude qu'il présente ne permet pas de conclure ? Peu importe également l'outil, à chaque mesure statistique, on vous proposera un test pour vous aider à prendre une décision sur vos résultats. Il faut juste être capable de le lire.

# Par convention, on place les fonctions locales au début du code après les bibliothèques.

def ouvrirUnFichier(nom):
    with open(nom, "r", encoding="utf-8") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu
df = ouvrirUnFichier("data/Echantillonnage-100-Echantillons.csv")

# Question 1 : Théorie de l'échantillonnage (intervalles de fluctuation)
# L'échantillonnage se base sur la répétitivité.
print("Question 1")

moyennes = df.select_dtypes(include="number").mean().round()
for colonne in moyennes.index:
    print("Moyenne des échantillons -", colonne, ":", moyennes[colonne])


total_moyennes = moyennes.sum()
for colonne in moyennes.index:
    frequence = round(moyennes[colonne] / total_moyennes, 2)
    print("Fréquence moyenne des échantillons -", colonne, ":", frequence)



population = {
    "Pour": 852,
    "Contre": 911,
    "Sans opinion": 422
}
total_population = sum(population.values())
for opinion in population:
    frequence = round(population[opinion] / total_population, 2)
    print("Fréquence de la population mère -", opinion, ":", frequence)



zc = 1.96
n = 1000
for opinion in population:
    frequence = population[opinion] / total_population
    ecart = zc * (frequence * (1 - frequence) / n) ** 0.5
    borne_inf = frequence - ecart
    borne_sup = frequence + ecart
    print("Intervalle de fluctuation -", opinion, ":",
          round(borne_inf, 3), "-", round(borne_sup, 3))

# Dans le rapport: expliquer le lien entre l'intervalle de fluctuation et les valeurs réelles de la population mère
print("Résultat sur le calcul d'un intervalle de fluctuation")



# Question 2 : Théorie de l'estimation (intervalles de confiance)
#L'estimation se base sur l'effectif.
print("Question 2")

echantillon = list(df.iloc[0])
print("Premier échantillon :", echantillon)

total_echantillon = sum(echantillon)
print("Total du premier échantillon :", total_echantillon)

for effectif in echantillon:
    frequence = round(effectif / total_echantillon, 2)
    print("Fréquence :", frequence)


marge = 1 / (total_echantillon ** 0.5)
for i in range(len(echantillon)):
    frequence = echantillon[i] / total_echantillon
    borne_inf = frequence - marge
    borne_sup = frequence + marge
    print("Intervalle de confiance -", df.columns[i], ":",
          round(borne_inf, 3), "-", round(borne_sup, 3))

# Dans le rapport, interpréter le résultat obtenu


# Question 3 : Théorie de la décision (tests d'hypothèse)
# La décision se base sur la notion de risques alpha et bêta.
# Comme à la séance précédente, l'ensemble des tests se trouve au lien : https://docs.scipy.org/doc/scipy/reference/stats.html
print("Question 3")
df1 = ouvrirUnFichier("data/Loi-normale-Test-1.csv")
df2 = ouvrirUnFichier("data/Loi-normale-Test-2.csv")
resultat1 = shapiro(df1.iloc[:, 0])
resultat2 = shapiro(df2.iloc[:, 0])
print("Test 1 :", resultat1)
print("Test 2 :", resultat2)

# Expliquer dans le rapport laquelle est une distribution normale

# Question bonus
print("Question bonus")

df1.hist()
plt.title("Distribution - Test 1")
plt.savefig("histogramme-test1.png")
plt.show()

df2.hist()
plt.title("Distribution - Test 2")
plt.savefig("histogramme-test2.png")
plt.show()