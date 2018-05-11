"""Acest modul contine testul 2 la disciplina

Limbaje de programare 2, Saptamana 11, subiectul 4
de Bogdan Dragulescu
https://www.cm.upt.ro/cursuri/licenta/lp2/

Cerinta:

Incarcati fisierul logs_lp2_9_05_clean.csv. (1P)
Aplicand o functie lambda returnati intr-o variabila noua doar inregistrarile din 8 mai. (2P)
Returnati numarul total de accesari pe fisierele de curs C5-C8. (2P)
Salvati unul din rezultatele precedente in format CSV. (2P)
Tratati toate exceptiile. (2P)

OBS: Puctaj maxim doar daca folositi pandas, functional sau list comprehension.

Copyright 2018 Bogdan Dragulescu

Licenta: http://creativecommons.org/licenses/by/4.0/
"""
import pandas as pd
pd.set_option('display.expand_frame_repr', False)
df = pd.read_csv('logs_lp2_9_05_clean.csv')

df['Time'] = pd.to_datetime(df['Time'], format='%d/%m/%y, %H:%M')
df['Time'] = df['Time'].apply(lambda x: x.strftime('%Y-%m-%d'))
mai8 = df[df['Time'].apply(lambda x: x.endswith('05-08'))].reset_index()
print(mai8)
context = df[df['Context'].str.startswith('File: C')].reset_index()
cursu5_8 = context[context['Context'].str.contains('C[5-8]')].reset_index()
print(cursu5_8)
cursu5_8.to_csv('Crusuri5-8.csv')
