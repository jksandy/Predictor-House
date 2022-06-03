import numpy as np
import pandas as pd
import sklearn
from sklearn import datasets
from sklearn.linear_model import LinearRegression,LogisticRegression

def house_rate(medinc):
    x,y = sklearn.datasets.fetch_california_housing(as_frame = True, return_X_y=True )
    x=np.array(x['MedInc']).reshape(-1, 1)
    model = LinearRegression().fit(x,y)
    test = np.array(medinc,dtype='float32').reshape(1,-1)
    return model.predict(test)
