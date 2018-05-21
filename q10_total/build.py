import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from q06_sub_total.build import q06_sub_total
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def q10_total(path1,path2):
    df = q06_sub_total(path1,path2)
    df.plot(x='Jan', kind='pie', subplots='True')
    plt.show()
