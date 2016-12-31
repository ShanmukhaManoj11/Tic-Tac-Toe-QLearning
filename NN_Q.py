from keras.models import Sequential
from keras.layers import Dense
import numpy
import time
import pickle
seed=7
numpy.random.seed(seed)
# load data
with open('Q_s','rb') as f:
    Q_data=pickle.load(f)
n=len(Q_data)
d=11
x_=Q_data.keys()
# split into input (X) and output (Y) variables
X=[]
for i in range(n):
    x=[]
    for j in range(9):
        x.append(x_[i][0][j])
    for j in range(2):
        x.append(x_[i][1][j])
    X.append(x)
Y=Q_data.values()
# create model
model=Sequential()
model.add(Dense(20,input_dim=d,init='uniform',activation='relu'))
model.add(Dense(20,init='uniform',activation='relu'))
model.add(Dense(20,init='uniform',activation='relu'))
model.add(Dense(1,init='uniform',activation='sigmoid'))
# Compile model
model.compile(loss='mean_squared_error',optimizer='adam',metrics=['accuracy'])
# Fit the model
model.fit(X,Y,nb_epoch=50000,batch_size=100,verbose=0)
time.sleep(0.1)
# evaluate the model
scores=model.evaluate(X,Y)
print("%s: %.2f%%" % (model.metrics_names[1],scores[1]*100))
with open('NN_keras','wb') as f:
    pickle.dump(model,f,protocol=pickle.HIGHEST_PROTOCOL)