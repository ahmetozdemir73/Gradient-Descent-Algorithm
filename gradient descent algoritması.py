# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 17:42:19 2020

@author: Ahmet
"""


import numpy as np
import matplotlib.pyplot as plt

"""grafiğe yerleştirilecek rastgele değerler oluşturalım"""
x=np.arange(1,11)
y=np.array([1.1,3.2,4.5,5.7,10,11.5,12.8,15,16.5,20.1])



"""       H(x)=teta0+teta1*x    """

teta=np.ones((2,1)) #tetalara gecici olarak 1 verdik

egitimSayisi=len(x)  #eğitim sayımızı x'in uzunluğuna eşitledik



""" J(teta)=1/(2m) * SUM(h(x)-y)"""

plt.scatter(x,y)

errorFonk= 1/(2*egitimSayisi)*pow((teta[0]+teta[1]*x-y),2) #error fonksiyonumuz
epsilon=10e-9  #maximum hatamızı söyler
learningRate=0.0001  #öğrenme katsayımız
i=0
deneme=0
max_deneme=10000 #döngü sayısını sınırlandırmak için yaptık

while sum(errorFonk)>epsilon and  deneme<max_deneme:       
    while  i<egitimSayisi:
        temp0=teta[0]-learningRate*(1/egitimSayisi)*(teta[0]+teta[1]*x[i]-y[i])
        temp1=teta[1]-learningRate*(1/(egitimSayisi))*(teta[0]+teta[1]*x[i]-y[i])*x[i]
        teta[0]=temp0
        teta[1]=temp1
        errorFonk[i]= 1/(2*egitimSayisi)*pow((teta[0]+teta[1]*x[i]-y[i]),2)        
        i+=1
    deneme+=1    
    i=0
    
        
plt.plot(x,teta[0]+x*teta[1])
plt.show()