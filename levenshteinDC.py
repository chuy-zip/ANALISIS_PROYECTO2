import json
import time
import matplotlib.pyplot as plt

def load_test_cases(filename):

    with open(filename, 'r') as file:
        test_cases = json.load(file)

    return test_cases

def levenshtein_distance_DC(str1, str2):
    # caso baso 1, si la primera cadena esta vacia, el costo/operaciones
    # que se tendran que hacer para convertir la cadena str1 a str2
    # es el largo de la cadena 2
    if len(str1) == 0:
        return len(str2)
    
    # caso base 2, lo mismo que el caso anterior, pero ahora la cadena 2 es vacia, 
    # entonces la cantidad de operaciones a realizar es el largo de la cadena 1
    if len(str2) == 0:
        return len(str1)
    
    # si los primeros char son iguales se continua con los demas
    if str1[0] == str2[0]:
        return levenshtein_distance_DC(str1[1:], str2[1:])
    else:
        # calculo de las 3 opciones posibles recursivamente
        deletion = levenshtein_distance_DC(str1[1:], str2) + 1
        insertion = levenshtein_distance_DC(str1, str2[1:]) + 1
        substitution = levenshtein_distance_DC(str1[1:], str2[1:]) + 1
        
        # minimo de las tres opciones
        return min(deletion, insertion, substitution)

json_data = load_test_cases("strings.json")

test_cases = json_data["test_cases"]

#print(test_cases)

print("\nEvaluando Levenshtein Distance con Divide and Conquer:")

indexes = []
execution_times = []

for index, strings in enumerate(test_cases, start=1):

    str1 = strings["str1"]
    str2 = strings["str2"]

    print(f"\nCaso: {index } con cadenas: '{str1}' y '{str2}' ")

    start_time = time.perf_counter()
    ld = levenshtein_distance_DC(str1, str2)
    end_time = time.perf_counter()

    exec_time = end_time - start_time

    print(f"Resultado: {ld} con tiempo {exec_time}")
    execution_times.append(exec_time)
    indexes.append(index)

plt.plot(indexes, execution_times, marker='o')  #
plt.xlabel('Caso de Prueba')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.title('Rendimiento de Levenshtein Distance (Divide and Conquer)')
plt.grid(True) 
plt.show()
