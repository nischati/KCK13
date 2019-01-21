import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import aseegg as ag
import pandas as pd
import csv

plt.rcParams.update({"font.size":15})


t = np.linspace (0, 7.91, 200*7.91)



dane = pd.read_csv(r"sub-01_trial-04n - sub-01_trial-04.csv", delimiter=',', engine='python')
t = np.linspace (0, 7.91, 200*7.91)
mojeDane = dane['kol2']
liczby = dane["kol6"]



przefiltrowany = ag.pasmowoprzepustowy(mojeDane, 200, 1, 50)
przefiltrowany2 = ag.pasmowozaporowy(mojeDane, 200, 49, 50)





plt.plot(t, przefiltrowany2)
plt.plot(t, liczby)

plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [µmV]")
plt.title("Sygnał po filtracji pasmowozaporowej")
plt.show()
