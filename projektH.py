# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#wczytywanie pliku csv:
data = pd.read_csv('titanic.csv')

data["Sex_cleaned"]=np.where(data["Sex"]=="male",0,1)
#data["Embarked_cleaned"]=np.where(data["Embarked"]=="S",0,1)


#czyszczenie wierszy, w których brakuje danych
data_cleaned=data[[ 
 "Survived",
 "Pclass",
 "Sex_cleaned",
 "Age",
 "SibSp",
 "Parch",
 "Fare",
]].dropna(axis=0, how='any')

print(data_cleaned)

data_surv = data_cleaned.loc[data_cleaned.Survived == 1]
print(data_surv)

data_not_surv = data_cleaned.loc[data_cleaned.Survived == 0]
print(data_not_surv)

#zielony = przeżyli
#czerwony = nie przeżyli
plt.hist([data_surv['Age'], data_not_surv['Age']], color=['green', 'red'])
plt.title('wiek vs przeżywalnosć')
plt.xlabel('wiek')
plt.ylabel('ilosc osob')
plt.show()

#szary - przeżyli
#czarny - nie przeżyli
plt.hist([data_surv['Age'], data_not_surv['Fare']], color=['grey', 'black'])
plt.title('cena blietu vs przeżywalnosć')
plt.xlabel('cena biletu')
plt.ylabel('ilosc osob')
plt.show()
