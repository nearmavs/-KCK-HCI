import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import aseegg as ag

def kaspowtorki(tablica):
    j=1
    for j in range(len(tablica)-1):
        if tablica[j]==tablica[j-1]:
            cos=0
        else:
            print(tablica[j])

dane = pd.read_csv(r"sub1trial5.csv", delimiter=',', engine='python')
sygnal=dane[" sygnal"]
liczba=dane[" liczba"]

t=np.linspace(0,37.89, 200*37.89)
filtrzaporowy=ag.pasmowozaporowy(sygnal,200,49,51)
filtrprzepustowy=ag.pasmowoprzepustowy(filtrzaporowy,200,1,50)
plt.plot(t,sygnal)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.show()
ag.spektrogram(sygnal,200)
plt.plot(t,filtrzaporowy)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.show()
ag.spektrogram(filtrzaporowy,200)
plt.plot(t,filtrprzepustowy)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.show()
ag.spektrogram(filtrprzepustowy,200)
plt.plot(t,liczba)
plt.show()
liczby=[]

for i in range(len(filtrprzepustowy)):
    if filtrprzepustowy[i] >= 0.1:
        liczby.append(liczba[i])
print("Wymrugane cyfry:")
kaspowtorki(liczby)
