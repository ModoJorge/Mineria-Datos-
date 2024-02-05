"""
Este módulo proporciona una herramienta para convertir números enteros
de un archivo de texto a sus representaciones binarias y hexadecimales.
"""

import sys
import time

def convert_to_binary(number):
    """Convierte un número entero a su representación binaria sin usar funciones incorporadas."""
    if number == 0:
        return "0"
    binary_digits = []
    while number > 0:
        remainder = number % 2
        binary_digits.insert(0, str(remainder))
        number = number // 2
    return ''.join(binary_digits)

def convert_to_hexadecimal(number):
    """Convierte un número entero a su representación hexadecimal sin usar funciones incorporadas."""
    if number == 0:
        return "0"
    hex_digits = []
    hex_representation = "0123456789ABCDEF"
    while number > 0:
        remainder = number % 16
        hex_digits.insert(0, hex_representation[remainder])
        number = number // 16
    return ''.join(hex_digits)

def read_numbers_from_file(file_path):
    """Lee líneas de un archivo y las devuelve como generador de cadenas."""
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()

def write_results_to_file(file_path, results):
    """Escribe una lista de cadenas en un archivo de texto, una cadena por línea."""
    with open(file_path, 'w', encoding='utf-8') as file:
        for result in results:
            file.write(f"{result}\n")

def process_file(file_name):
    """Procesa un archivo dado, convirtiendo cada número a binario y hexadecimal."""
    results = []
    for number_str in read_numbers_from_file(file_name):
        try:
            number = int(number_str)
            binary = convert_to_binary(number)
            hexadecimal = convert_to_hexadecimal(number)
            result = f"Number: {number}, Binary: {binary}, Hex: {hexadecimal}"
            print(result)
            results.append(result)
        except ValueError:
            print(f"Invalid data: {number_str} is not a valid integer.")
    return results

def main(file_names):
    """Procesa múltiples archivos de números y escribe los resultados en un archivo de salida."""
    start_time = time.time()
    all_results = []
    
    for file_name in file_names:
        print(f"Processing file: {file_name}")
        file_results = process_file(file_name)
        all_results.extend(file_results)
        all_results.append("\n")  # Separate the results for different files
    
    write_results_to_file('conversion_results.txt', all_results)
    elapsed_time = time.time() - start_time
    print(f"Execution time: {elapsed_time} seconds")
    all_results.append(f"Execution time: {elapsed_time} seconds")
    write_results_to_file('conversion_results.txt', all_results)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_numbers.py file_with_data1.txt [file_with_data2.txt ...]")
    else:
        main(sys.argv[1:])
