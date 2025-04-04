import json
import time
import matplotlib.pyplot as plt

def load_test_cases(filename):

    with open(filename, 'r') as file:
        test_cases = json.load(file)

    return test_cases

# Algorithm obtained from:
# https://how.dev/answers/the-levenshtein-distance-algorithm
def algh_levenshtein(a, b):
    # Declaring array 'D' with rows = len(a) + 1 and columns = len(b) + 1:
    D = [[0 for i in range(len(b) + 1)] for j in range(len(a) + 1)]

    # Initialising first row:
    for i in range(len(a) + 1):
        D[i][0] = i

    # Initialising first column:
    for j in range(len(b) + 1):
        D[0][j] = j

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                D[i][j] = D[i - 1][j - 1]
            else:
                # Adding 1 to account for the cost of operation
                insertion = 1 + D[i][j - 1]
                deletion = 1 + D[i - 1][j]
                replacement = 1 + D[i - 1][j - 1]

                # Choosing the best option:
                D[i][j] = min(insertion, deletion, replacement)

json_data = load_test_cases("strings.json")

test_cases = json_data["test_cases"]

print("Distancia de Levenshtein con Programación Dinámica:\n")

indexes = []
execution_times = []

for index, strings in enumerate(test_cases, start=1):

    str1 = strings["str1"]
    str2 = strings["str2"]

    print(f"\nCaso: {index }:")

    start_time = time.perf_counter()
    ld = algh_levenshtein(str1, str2)
    end_time = time.perf_counter()

    exec_time = end_time - start_time

    print(f"Resultado: {ld} con tiempo {exec_time}")
    execution_times.append(exec_time)
    indexes.append(index)

plt.plot(indexes, execution_times, marker='o')  #
plt.xlabel('Caso de Prueba')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.title('Rendimiento de Levenshtein Distance (Programación Dinámica)')
plt.grid(True) 
plt.show()
