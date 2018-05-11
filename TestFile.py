import json
import traceback

#import numby as nb
import pandas as pd

pd.set_option("display.expand_frame_repr", False)

try:
    df = pd.read_csv('logs_lp2_9_05_clean.csv')
    #print(df)


