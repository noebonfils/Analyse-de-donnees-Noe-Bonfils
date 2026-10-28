#coding:utf8

import numpy as np
import pandas as pd
import scipy
import scipy.stats
import matplotlib.pyplot as plt


#https://docs.scipy.org/doc/scipy/reference/stats.html

dist_names = ['norm', 'beta', 'gamma', 'pareto', 't', 'lognorm', 'invgamma', 'invgauss',  'loggamma', 'alpha', 'chi', 'chi2', 'bradford', 'burr', 'burr12', 'cauchy', 'dweibull', 'erlang', 'expon', 'exponnorm', 'exponweib', 'exponpow', 'f', 'genpareto', 'gausshyper', 'gibrat', 'gompertz', 'gumbel_r', 'pareto', 'pearson3', 'powerlaw', 'triang', 'weibull_min', 'weibull_max', 'bernoulli', 'betabinom', 'betanbinom', 'binom', 'geom', 'hypergeom', 'logser', 'nbinom', 'poisson', 'poisson_binom', 'randint', 'zipf', 'zipfian']

print(dist_names)


# Fonction pour calculer la moyenne d'une loi discrète (question 2)
def moyenne_discrete(valeurs, probabilites):
    somme = 0
    for i in range(len(valeurs)):
        somme = somme + valeurs[i] * probabilites[i]
    return somme


# Fonction pour calculer l'écart-type d'une loi discrète (question 2)
def ecart_type_discrete(valeurs, probabilites):
    m = moyenne_discrete(valeurs, probabilites)
    somme = 0
    for i in range(len(valeurs)):
        somme = somme + probabilites[i] * (valeurs[i] - m) ** 2
    variance = somme
    resultat = variance ** 0.5
    return resultat

# Fonction pour calculer la moyenne d'une loi continue (question 2)
def moyenne_continue(distribution):
    return distribution.mean()

# Fonction pour calculer l'écart-type d'une loi continue (question 2)
def ecart_type_continue(distribution):
    return distribution.std()

# Question 1
print("Question 1")

# loi de Dirac
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
p = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
plt.bar(x, p)
plt.title("Loi de Dirac")
plt.savefig("img/dirac.png")
plt.close()

# loi uniforme discrète
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
p =[1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9]
plt.bar(x, p)
plt.xticks(x)
plt.title("Loi uniforme discrète")
plt.ylabel("Probabilité")
plt.ylim(0, 0.2)
plt.savefig("img/uniforme_discrète.png")
plt.close()

# loi binomiale
x = [0, 1, 2, 3, 4, 5]
p = scipy.stats.binom.pmf(x, 5, 0.5)
plt.bar(x, p)
plt.xticks(x)
plt.xlabel("Valeurs")
plt.title("Loi binomiale")
plt.ylabel("Probabilité")
plt.savefig("img/binomiale.png")
plt.close()

# loi de Poisson
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
p = scipy.stats.poisson.pmf(x, 4)
plt.bar(x, p)
plt.xticks(x)
plt.title("Loi de Poisson")
plt.xlabel("Valeurs")
plt.ylabel("Probabilité")
plt.savefig("img/poisson.png")
plt.close()

# loi de Zipf-Mandelbrot
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
p = [1 / (valeur + 1) ** 2 for valeur in x]
total = sum(p)
p= [valeur / total for valeur in p]
plt.bar(x, p)
plt.xticks(x)
plt.title("Loi de Zipf-Mandelbrot")
plt.ylabel("Probabilité")
plt.xlabel("Valeurs")
plt.savefig("img/zipf_mandelbrot.png")
plt.close()

# loi normale
x = np.linspace(-5, 5, 100)
p = scipy.stats.norm.pdf(x, loc=0, scale=1)
plt.plot(x, p)
plt.title("Loi normale")
plt.xlabel("Valeurs")
plt.ylabel("Densité de probabilité")
plt.savefig("img/loi-normale.png")
plt.close()

# loi log-normale
x = np.linspace(0, 10, 100)
p = scipy.stats.lognorm.pdf(x, s=1, loc=0, scale=1)
plt.plot(x, p)
plt.title("Loi log-normale")
plt.xlabel("Valeurs")
plt.ylabel("Densité de probabilité")
plt.savefig("img/lognormale.png")
plt.close()


# loi uniforme continue
x = np.linspace(0, 1, 100)
p = scipy.stats.uniform.pdf(x, loc=0, scale=1)
plt.plot(x, p)
plt.title("Loi uniforme continue")
plt.xlabel("Valeurs")
plt.ylabel("Densité de probabilité")
plt.savefig("img/uniforme-continue.png")
plt.close()

# loi du khi-deux
x = np.linspace(0, 10, 100)
p = scipy.stats.chi2.pdf(x, df=5)
plt.plot(x, p)
plt.xlabel("Valeurs")
plt.ylabel("Densité de probabilité")
plt.title("Loi du khi-deux")
plt.savefig("img/loi-khi-deux.png")
plt.close()


# loi de Pareto
x = np.linspace(1, 10, 100)
p = scipy.stats.pareto.pdf(x, b=5)
plt.plot(x, p)
plt.xlabel("Valeurs")
plt.title("Loi de Pareto")
plt.ylabel("Densité de probabilité")
plt.savefig("img/loi-pareto.png")
plt.close()

# Question 2
print("Question 2")

# Loi de Dirac
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
p = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
print("Loi de Dirac :")
print("Moyenne :", moyenne_discrete(x, p))
print("Ecart-type :", ecart_type_discrete(x, p))

# Loi uniforme discrète
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
p = [1/9] * 9
print("Loi uniforme discrète :")
print("Moyenne :", moyenne_discrete(x, p))
print("Écart-type :", ecart_type_discrete(x, p))

# Loi binomiale
x = [0, 1, 2, 3, 4, 5]
p = scipy.stats.binom.pmf(x, 5, 0.5)
print("Loi binomiale :")
print("Moyenne :", moyenne_discrete(x, p))
print("Écart-type :", ecart_type_discrete(x, p))

# Loi de Poisson
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
p = scipy.stats.poisson.pmf(x, 4)
print("Loi de Poisson")
print("Moyenne :", moyenne_discrete(x, p))
print("Écart-type :", ecart_type_discrete(x, p))

# Loi de Zipf-Mandelbrot
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
p = [1 / (valeur + 1) ** 2 for valeur in x]
total = sum(p)
p = [valeur / total for valeur in p]
print("Loi de Zipf-Mandelbrot")
print("Moyenne :", moyenne_discrete(x, p))
print("Écart-type :", ecart_type_discrete(x, p))

# Loi normale
distribution = scipy.stats.norm(loc=0, scale=1)
print("Loi normale :")
print("Moyenne :", moyenne_continue(distribution))
print("Écart-type :", ecart_type_continue(distribution))

# Loi log-normale
x = np.linspace(0, 5, 100)
p = scipy.stats.lognorm.pdf(x, s=1, loc=0, scale=1)
distribution = scipy.stats.lognorm(s=1, loc=0, scale=1)
print("Loi log-normale :")
print("Moyenne :", moyenne_continue(distribution))
print("Écart-type :", ecart_type_continue(distribution))

# Loi uniforme continue
x = np.linspace(0, 1, 100)
p = scipy.stats.uniform.pdf(x, loc=0, scale=1)
distribution = scipy.stats.uniform(loc=0, scale=1)
print("Loi uniforme continue :")
print("Moyenne :", moyenne_continue(distribution))
print("Écart-type :", ecart_type_continue(distribution))

# Loi du khi-deux
x = np.linspace(0, 15, 100)
p = scipy.stats.chi2.pdf(x, df=3)
distribution = scipy.stats.chi2(df=3)
print("Loi du khi-deux" :)
print("Moyenne :", moyenne_continue(distribution))
print("Écart-type :", ecart_type_continue(distribution))

# Loi de Pareto
x = np.linspace(1, 10, 100)
p = scipy.stats.pareto.pdf(x, b=3)
distribution = scipy.stats.pareto(b=3)
print("Loi de Pareto :")
print("Moyenne :", moyenne_continue(distribution))
print("Écart-type :", ecart_type_continue(distribution))