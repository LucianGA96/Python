"""Acest modul contine testul 2 la disciplina

Limbaje de programare 2, Saptamana 11, subiectul 2
de Bogdan Dragulescu
https://www.cm.upt.ro/cursuri/licenta/lp2/

Cerinta:

"""
import pandas as pd
import numpy as np
import os
import traceback
import csv
pd.set_option('display.expand_frame_repr', False)
try:
    df=pd.read_csv('logs_lp2_9_05_clean.csv')
    #print(df)
    """
    Incarcati fisierul logs_lp2_9_05_clean.csv. (1P)
    """
    """
    Returnati intr-o variabila noua doar inregistrarile din luna mai. (2P)
    """
    df['Time'] = pd.to_datetime(df['Time'], format='%d/%m/%y, %H:%M')
    df['Time'] = df['Time'].apply(lambda x: x.strftime('%Y-%m-%d'))
    mai = df[df['Time'].between('2018-05-01','2018-05-31')].reset_index()
    #print(mai)
    """
    Aplicati o functie lambda asupra coloanei IP_intern care sa returneze numarul de accesari externe. (2P)
    """
    ip = list(df["IP_intern"])
    # x= lambda  x:x=='0' if x=='no' else x=='1', val
    val = 0
    x = filter(lambda val: val.count('no'), ip)

    print(len(list(filter(lambda x:x=='no',ip))))
    #print(grup)
    """
    Salvati unul din rezultatele precedente in format CSV in folderul date. (2P)
    Tratati toate exceptiile. (2P)
    """
    import csv


    mai.to_csv('Test22.csv')

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
"""
import pandas as pd
import numpy as np
import os
import traceback
pd.set_option('display.expand_frame_repr', False)
df=pd.read_csv('logs_lp2_9_05_clean.csv')
print(df)
df['Time'] = pd.to_datetime(df['Time'], format='%d/%m/%y, %H:%M')
df['Time'] = df['Time'].apply(lambda x: x.strftime('%Y-%m-%d'))
mai = df[df['Time'].between('2018-05-01','2018-05-31')].reset_index()
print(mai)
a=len(list(filter(lambda x:x.startswith('no'),df )))
print(a)
if not os.path.exists('date'):
    os.mkdir('date')
mai.to_csv('date/results.csv')
try:
    fhand = open('logs_lp2_9_05_clean.csv')
except FileNotFoundError as e:
    print(e)
except NameError as e:
    print(e)
    traceback.print_exc()
except Exception as e:
    print(e)
finally:
    try:
        fhand.close()
        print(fhand.close)
    except:
        pass

"""





