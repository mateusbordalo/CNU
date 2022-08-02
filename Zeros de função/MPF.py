import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math


x0 = 1.5 #inicial
x=x0

epsilon = 1e-10 #erro
qsi = 2 #raiz
n=1 #iterações
valores_parciais = [x]

def f(x):
    return x**2+x-6

def fi(x):
    return np.sqrt(6-x)

i=0
while np.abs(f(x))>epsilon:
    a=fi(x)
    n= n + 1
    valores_parciais.append(a)
    x=a
    i+=1

print(valores_parciais)
print('\n')

print('Iterações:', +(n-1))
print('Erro:', +np.abs(f(x)))
print('Erro de x:', +(np.abs(x - qsi))/qsi)
print('Resultado:', +x)
print('Resultado esperado:', +qsi)

plt.title('Erro ')
plt.plot(np.arange(n), np.abs(np.array(valores_parciais) - qsi))
plt.hlines(y=0, xmin=0, xmax=n-1, alpha=0.5)
plt.xlabel('Iterações')
plt.ylabel('Erro de x')
plt.show()