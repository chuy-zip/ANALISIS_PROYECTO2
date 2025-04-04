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
    print(f"\nOriginal: {a}")
    print(f"Cambiar a: {b}")

    # Dictionary for saving subproblems results
    memo = {}

    def dist(i, j):
        # The subproblem was already calculated
        if (i, j) in memo:
            return memo[(i, j)]

        # Base case
        if i == 0:
            return j
        if j == 0:
            return i

        if a[i - 1] == b[j - 1]:
            cost = dist(i - 1, j - 1)
        else:
            insert_op = 1 + dist(i, j - 1) # Insert character
            delete_op = 1 + dist(i - 1, j) # Delete character
            replace_op = 1 + dist(i - 1, j - 1) # Replace character
            cost = min(insert_op, delete_op, replace_op)

        memo[(i, j)] = cost  # Save cost in dictionary
        return cost

    result = dist(len(a), len(b))
    print("Levenshtein Distance:", result)
    return result

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
