import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1, 10, 100)
labels = ['Exponencial', 'Cubica', 'Quadratica', 'Logaritmica Linear', 'Constante', 'Logaritmico', 'Linear']
big_o = [2**n, n**3, n**2, n * np.log(n), np.ones(n.shape), np.log(n), n]

plt.figure(figsize=(100, 100))
plt.ylim(0, 10)

for i in range(len(big_o)):
    plt.plot(n, big_o[i], label = labels[i])

plt.legend()
plt.ylabel('Tempo de execucao')
plt.xlabel('n')
plt.show()