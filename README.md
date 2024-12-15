# Prueba Técnica: Cálculo de Paneles y Optimización

## Descripción
Esta prueba técnica aborda dos problemas:

1. **Cálculo de la cantidad máxima de paneles solares que caben en un techo:**
   - Dados las dimensiones de un rectángulo grande (techo) y un rectángulo pequeño (panel solar), se busca determinar cuántos paneles pueden colocarse en el techo.

2. **Optimización de disposición de elementos mediante algoritmos de colonia de hormigas:**
   - Uso de un algoritmo avanzado para maximizar el valor de cajas dispuestas dentro de un pallet, considerando restricciones de espacio.

---

## Solución 1: Cálculo de Paneles

El siguiente código calcula cuántos paneles de dimensiones `a` y `b` caben dentro de un área rectangular de dimensiones `x` e `y`:

```python
def calcular_cantidad_paneles(largo_grande, ancho_grande, largo_pequeno, ancho_pequeno):
    cantidad_largo = largo_grande // largo_pequeno
    cantidad_ancho = ancho_grande // ancho_pequeno
    return cantidad_largo * cantidad_ancho

# Ejemplo interactivo
largo_grande = int(input("Introduce el largo del área grande: "))
ancho_grande = int(input("Introduce el ancho del área grande: "))
largo_pequeno = int(input("Introduce el largo del panel pequeño: "))
ancho_pequeno = int(input("Introduce el ancho del panel pequeño: "))

print(calcular_cantidad_paneles(largo_grande, ancho_grande, largo_pequeno, ancho_pequeno))
```

---

## Solución 2: Optimización con Algoritmo de Colonia de Hormigas

Este enfoque emplea un algoritmo de colonia de hormigas para maximizar la disposición de cajas en un pallet tridimensional, considerando el valor de cada caja.

### Código:

```python
import numpy as np
import random

class AntColonyKnapsack:
    def __init__(self, boxes, pallet_dims, alpha=1, beta=2, evaporation_rate=0.5, ant_count=10, iterations=100):
        self.boxes = boxes
        self.pallet_dims = pallet_dims
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.ant_count = ant_count
        self.iterations = iterations
        self.pheromones = np.ones(len(boxes))

    def run(self):
        best_solution = None
        best_value = 0

        for _ in range(self.iterations):
            solutions = []
            values = []

            for _ in range(self.ant_count):
                solution, value = self._build_solution()
                solutions.append(solution)
                values.append(value)

                if value > best_value:
                    best_solution = solution
                    best_value = value

            self._update_pheromones(solutions, values)

        return best_solution, best_value

    def _build_solution(self):
        solution = []
        total_value = 0
        remaining_area = self.pallet_dims[0] * self.pallet_dims[1]
        remaining_height = self.pallet_dims[2]

        available_boxes = list(range(len(self.boxes)))

        while available_boxes:
            probabilities = self._calculate_probabilities(available_boxes)
            selected_box = np.random.choice(available_boxes, p=probabilities)

            box = self.boxes[selected_box]
            box_area = box[0] * box[1]
            box_height = box[2]

            if box_area <= remaining_area and box_height <= remaining_height:
                solution.append(selected_box)
                total_value += box[3]
                remaining_area -= box_area
                remaining_height -= box_height

            available_boxes.remove(selected_box)

        return solution, total_value

    def _calculate_probabilities(self, available_boxes):
        pheromones = np.array([self.pheromones[i] for i in available_boxes])
        values = np.array([self.boxes[i][3] for i in available_boxes])

        attractiveness = (pheromones ** self.alpha) * (values ** self.beta)
        probabilities = attractiveness / attractiveness.sum()
        return probabilities

    def _update_pheromones(self, solutions, values):
        self.pheromones *= (1 - self.evaporation_rate)

        for solution, value in zip(solutions, values):
            for box_idx in solution:
                self.pheromones[box_idx] += value / sum(values)

if __name__ == "__main__":
    num_boxes = 20
    boxes = [(random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(10, 100)) for _ in range(num_boxes)]
    pallet_dims = (10, 10, 15)

    print("Datos de entrada:")
    print("Cajas (largo, ancho, alto, valor):")
    for i, box in enumerate(boxes):
        print(f"Caja {i+1}: {box}")
    print(f"Dimensiones del pallet: {pallet_dims}")

    colony = AntColonyKnapsack(boxes, pallet_dims, alpha=1, beta=2, evaporation_rate=0.5, ant_count=10, iterations=50)
    best_solution, best_value = colony.run()

    print("\nResultados:")
    print(f"Mejor valor total: {best_value}")
    print("Cajas seleccionadas:")
    for i in best_solution:
        print(f"Caja {i+1}: {boxes[i]}")
```

---

## Cómo Usar
1. **Ejecutar el script del cálculo de paneles**
   - Copia el código correspondiente y ejecuta en cualquier entorno de Python.
   - Ingresa las dimensiones requeridas cuando el programa lo solicite.

2. **Ejecutar el algoritmo de colonia de hormigas**
   - Asegúrate de tener instaladas las dependencias: `numpy`.
   - Ejecuta el script y observa los resultados en la consola.

---

## Notas
- La solución del cálculo de paneles no contempla la rotación de los paneles para maximizar el uso del espacio.
- El algoritmo de colonia de hormigas es un enfoque optimizado, ideal para problemas donde se busca maximizar valor bajo restricciones de espacio.
