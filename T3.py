"""Acest modul contine testul 2 la disciplina

Limbaje de programare 2, Saptamana 11, subiectul 3
de Bogdan Dragulescu
https://www.cm.upt.ro/cursuri/licenta/lp2/

Cerinta:

Incarcati fisierul logs_lp2_9_05_clean.csv. (1P)
Returnati intr-o variabila noua doar inregistrarile in care Event contine 'viewed'. (2P)
Aplicati o functie lambda asupra coloanei Context astfel incat sa pastrati doar tipul resursei (ex: File, Folder, URL). (2P)
Salvati unul din rezultatele precedente in format Pickle in folderul export. (2P)
Tratati exceptiile generate de aplicarea functiei lambda. (2P)

OBS: Puctaj maxim doar daca folositi pandas, functional sau list comprehension.

Copyright 2018 Bogdan Dragulescu

Licenta: http://creativecommons.org/licenses/by/4.0/
"""
import pandas as pd
import numpy as np

pd.set_option('display.expand_frame_repr', False)

df = pd.read_csv('logs_lp2_9_05_clean.csv')

grup = df[df['Event'].str.contains('viewed')].reset_index()

print(grup)

df['Context'] = df['Context'].apply(lambda x: x.split()[0])

print(df)

df.to_pickle("daa.pkl")