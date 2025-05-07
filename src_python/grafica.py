import matplotlib
import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10]
y = [1, 3, 5, 7, 9]

nombre_linea = "Mi Linea"
plt.plot(x, y, label = nombre_linea, color ="blue")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Grafica de Linea")

plt.legend()
plt.show()