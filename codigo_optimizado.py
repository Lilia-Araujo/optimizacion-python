import time
import math
import numpy as np

inicio = time.time()

primos = []

for num in range(2, 100000):

    es_primo = True

    limite = int(math.sqrt(num)) + 1

    for i in range(2, limite):
        if num % i == 0:
            es_primo = False
            break

    if es_primo:
        primos.append(num)

primos_array = np.array(primos)

fin = time.time()

print("Cantidad de números primos:", len(primos_array))
print("Tiempo optimizado:", fin - inicio, "segundos")