import joblib
import pandas as pd
import numpy as np
from sklearn.metrics import f1_score
from joblib import load

with open('/home/data1/lab1/knn.joblib', 'rb') as f:
    knn = joblib.load(f)

X_test = pd.read_csv('/home/data1/lab1/X_test.csv', index_col='index')
y_test_pd = pd.read_csv('/home/data1/lab1/y_test.csv', index_col='index')

y_test = y_test_pd['churn']

model = knn.predict(X_test)

print('Model test f1-score is: ',f1_score(y_test, model))
