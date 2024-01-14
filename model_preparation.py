import joblib
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from joblib import dump, load
from sklearn.pipeline import Pipeline #импортирую бибилотеку трубы

X_train = pd.read_csv('/home/data1/lab1/X_train.csv', index_col='index')
y_train_pd = pd.read_csv('/home/data1/lab1/y_train.csv', index_col='index')

y_train = y_train_pd['churn']

pipe = Pipeline([ 
    ('KNeighborsClassifier', KNeighborsClassifier(n_neighbors=2)) #назначаем в качестве модел>
])

pipe = pipe.fit(X_train, y_train)

with open('/home/data1/lab1/knn.joblib', 'wb') as f:
    joblib.dump(pipe, f)

# pipe_knn = load('/home/data1/lab1/knn.joblib')
print('model_preparation исполнен')
