import pandas as pd
import math
import numpy as np
from math import sqrt
import statistics

#Verileri okuma
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)
pd.options.mode.chained_assignment = None

xl_file = pd.ExcelFile("Iris.xls")
dfs = pd.read_excel(xl_file)

#k değeri
k = int(input("k sayısını giriniz: "));

#Silinen veri ve indeksi
deleted_value = 5.4
deleted_value_index = 4
deleted_value_column = 'sepal length'

#Eğitim ve test veri setlerinin oluşturulması
test_dataset = dfs.iloc[0::4, :]
train_dataset = dfs.drop(test_dataset.index)

#Silinen değerin bulunduğu kolonun işleme katılmaması
train_dataset.drop(deleted_value_column, axis=1, inplace=True)
test_dataset.drop(deleted_value_column, axis=1, inplace=True)

#Sorgu örneğinin oluşturulması
query_example = []
for i in range(3):
    query_example.append(test_dataset.iloc[deleted_value_index][i])

#Eğitim veri seti boyutu kadar 0 içeren uzaklık dizisi
distances = []

#Sorgu örneği ile eğitim verisetindeki veriler arasındaki uzaklığın hesaplanması
sum = 0
for j in range(len(train_dataset)):
    for m in range(3):
        sum += (query_example[m]-train_dataset.iloc[j][m])**2

    distance = sqrt(sum)
    distances.append(distance)
    sum = 0
    distance = 0

#Uzaklıkların küçükten büyüğe sıralanması
distances.sort()

#En küçük k tane uzaklığın tutulduğu dizi
k_distances = [];
for l in range(k):
    k_distances.append(distances[l])

#Ağırlıklı ortalamaların hesaplanması
weighted_average = []
for n in range(k):
    weighted_average.append(1/k_distances[n])

#Verinin tahmin edilmesi
print("Tahmin Edilmesi Gereken Veri-->",deleted_value)
print("Tahmin Edilen Veri-->",statistics.mean(weighted_average))
