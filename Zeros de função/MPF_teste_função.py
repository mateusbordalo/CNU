import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


x0 = 1.5 #inicial
x=x0
def fi(x):
    return np.sqrt(6-x) #local para botar a função teste

valores_parciais = [x]

i=0

while i <= 5:
    x = fi(x)
    valores_parciais.append(x)
    i = i+1

print (valores_parciais) #avaliar se está convergindo
