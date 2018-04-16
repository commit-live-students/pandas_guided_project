import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from q06_sub_total.build import q06_sub_total
import matplotlib.pyplot as plt
plt.switch_backend('agg')

def q09_pie_chart_jan(path1,path2):

    'write your solution here'
    df_sub =q06_sub_total(path1,path2)

    return df_sub['Jan'].plot(kind='pie')



