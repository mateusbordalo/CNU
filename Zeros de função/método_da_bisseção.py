import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

epsilon= 1e-10
a = 4
b = 0


m= (a+b)/2
y = np.sin(m)

n = 1
valores_parciais = [m]

while np.abs(y) > epsilon:
    if np.sin(a) * y < 0: 
        b = m
    else: 
        a = m

    n = n + 1
    m = (a + b) / 2
    valores_parciais.append(m)
    y = np.sin(m)

print('Iterações:', n)
print('Erro:', np.abs(y))
print('Erro de x:', np.abs(m - np.pi))
print('Resultado:', m)
print('Resultado esperado:', np.pi)

plt.title('Erro ')
plt.plot(np.arange(n), np.abs(np.array(valores_parciais) - np.pi))
plt.hlines(y=0, xmin=0, xmax=n-1, alpha=0.5)
plt.xlabel('Iterações')
plt.ylabel('Erro de x')
plt.show()
    