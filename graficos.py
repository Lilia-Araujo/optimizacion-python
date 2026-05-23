import matplotlib.pyplot as plt

# Datos
etiquetas = ["Código Original", "Código Optimizado"]
tiempos = [36.35, 0.23]

# Crear gráfico de barras
plt.figure(figsize=(8,5))
plt.bar(etiquetas, tiempos, color="pink")

# Títulos
plt.title("Comparación de Tiempos de Ejecución")
plt.ylabel("Tiempo en segundos")

# Mostrar valores
for i, valor in enumerate(tiempos):
    plt.text(i, valor + 0.5, str(valor), ha='center')

# Mostrar gráfico
plt.show()