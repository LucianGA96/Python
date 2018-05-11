"""Acest modul contine testul 2 la disciplina

Limbaje de programare 2, Saptamana 11, subiectul 1
de Bogdan Dragulescu
https://www.cm.upt.ro/cursuri/licenta/lp2/

Cerinta:

Incarcati fisierul logs_lp2_9_05_clean.csv. (1P)
"""
import json
import traceback

#import numby as nb
import pandas as pd

pd.set_option("display.expand_frame_repr", False)

try:
    df = pd.read_csv('logs_lp2_9_05_clean.csv')
    #print(df)

    """
    # TODO 1: incarca datele din csv
    Returnati intr-o variabila noua doar inregistrarile pentru cursul 8. (2P)
    """

    #print(list(df['Context'].unique()))
    linii=df[df['Context'].str.startswith('File: C8')].groupby('Context')
    #print(linii.count())

    #grup=df[df["Context"].str.startwith("File C8")]]..groupby("Context")

    """
    Aplicati o functie lambda asupra coloanei IP_intern care sa transforme NO in 0 si Yes in 1. (2P)
    """
    #lambda a,b: a if (a > b) else b
    #f = list[df["IP_intern"].apply(lambda x: 1 if x == "Yes" else 0)]
    ip=list(df["IP_intern"])
    #x= lambda  x:x=='0' if x=='no' else x=='1', val
    x = map(lambda val: 0 if val == 'no' else 1, ip)

    print(list(x))
    """
    Salvati unul din rezultatele precedente in format JSON in folderul rezultate. (2P)
    
    
    
    Tratati exceptiile generate de lucrul cu fisiere. (2P)
    """

    df.to_json('Test.json')

    with open("/rezultate/Test22.json", 'wb') as outfile:
        json.dump(x, outfile)

except IOError as e:
    print(e)
except NameError as e:
    print(e)
except Exception as e:
    print(e)


"""
OBS: Puctaj maxim doar daca folositi pandas, functional sau list comprehension.

Copyright 2018 Bogdan Dragulescu

Licenta: http://creativecommons.org/licenses/by/4.0/
"""
