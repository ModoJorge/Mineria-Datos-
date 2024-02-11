#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Este módulo contiene funciones para calcular el costo total de las ventas."""

import json
import time
import sys


def load_data(file_path):
    """Carga datos desde un archivo JSON."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Advertencia: El archivo {file_path} no existe. "
              "Se utilizarán valores predeterminados.")
        return {}  # Devolver un diccionario vacío en caso de que el archivo no exista
    except json.JSONDecodeError:
        print(f"Error: No se decodifica el archivo {file_path}. "
              " Asegúrate de que sea un archivo JSON válido.")
        sys.exit(1)


def compute_total_cost(catalog, sales):
    """Calcula el costo total de las ventas."""
    total_cost = 0
    for sale in sales:
        product_name = sale['Product']
        quantity = sale['Quantity']

        # Buscar el producto en el catálogo por nombre
        matching_products = [product for product in catalog
                             if product['title'] == product_name]

        if matching_products:
            product = matching_products[0]
            total_cost += product['price'] * quantity
        else:
            print(f"Advertencia: El producto {product_name} "
                  "no se encuentra en el catálogo.")

    return total_cost


def main():
    """Función principal que calcula el costo total de las ventas."""
    # Asignar nombres de archivo directamente
    catalog_file = 'TC1/priceCatalogue_default.json'
    sales_file = 'TC1/salesRecord_default.json'

    start_time = time.time()

    catalog = load_data(catalog_file)
    sales = load_data(sales_file)

    total_cost = compute_total_cost(catalog, sales)

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Imprimir resultados en pantalla
    print(f"Costo total de las ventas: {total_cost}")
    print(f"Tiempo transcurrido: {elapsed_time} segundos")

    # Guardar resultados en SalesResults.txt
    with open('SalesResults.txt', 'w') as result_file:
        result_file.write(f"Costo total de las ventas: {total_cost}\n")
        result_file.write(f"Tiempo transcurrido: {elapsed_time} segundos\n")


if __name__ == "__main__":
    main()

