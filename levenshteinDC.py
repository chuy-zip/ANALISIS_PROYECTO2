import json
import time
import matplotlib.pyplot as plt

def load_test_cases(filename):

    with open(filename, 'r') as file:
        test_cases = json.load(file)

    return test_cases

def levenshtein_distance_DC(str1, str2):
    print()

json_data = load_test_cases("strings.json")

test_cases = json_data["test_cases"]

#print(test_cases)

print("\nEvaluando Levenshtein Distance con Divide and Conquer:")

indexes = []
execution_times = []

for index, strings in enumerate(test_cases, start=1):

    str1 = strings["str1"]
    str2 = strings["str2"]

    print(f"Caso: {index } con cadenas: '{str1}' y '{str2}' ")

    start_time = time.perf_counter()
    levenshtein_distance_DC(str1, str2)
    end_time = time.perf_counter()

    exec_time = end_time - start_time

    execution_times.append(exec_time)
    indexes.append(index)

plt.plot(indexes, execution_times, marker='o')  #
plt.xlabel('Caso de Prueba')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.title('Rendimiento de Levenshtein Distance (Divide and Conquer)')
plt.grid(True) 
plt.show()
