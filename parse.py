# importacion de pandas y numpy
import pandas as pd
import numpy as np

# obtener el nombre del archivo
file_name = input("Enter the name of the file: ")

# verificar si el archivo existe
import os
if not os.path.exists(file_name):
    print(f"Error: El archivo '{file_name}' no existe.")
    print("Archivos CSV disponibles en el directorio actual:")
    csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]
    for csv_file in csv_files:
        print(f"  - {csv_file}")
    exit(1)

# leer el archivo
try:
    df = pd.read_csv(file_name)
    print(f"Archivo '{file_name}' leído exitosamente.")
    print(f"Dimensiones del dataset: {df.shape}")
except Exception as e:
    print(f"Error al leer el archivo: {e}")
    exit(1)

# mostrar las columnas del archivo
print(df.columns)

# calcular el promedio de las columnas
def calculate_average(column):
    return np.mean(column)

# calcular la mediana de las columnas
def calculate_median(column):
    return np.median(column)

# calcular la moda de las columnas
def calculate_mode(column):
    from scipy import stats
    mode_result = stats.mode(column, keepdims=True)
    return mode_result.mode[0] if len(mode_result.mode) > 0 else "No mode found"

# calcular la desviacion estandar de las columnas
def calculate_standard_deviation(column):
    return np.std(column)

# calcular la varianza de las columnas
def calculate_variance(column):
    return np.var(column)

# calcular el minimo de las columnas
def calculate_min(column):
    return np.min(column)

# calcular el maximo de las columnas
def calculate_max(column):
    return np.max(column)

# mostrar estadísticas para cada columna numérica
print("\n" + "="*50)
print("ESTADÍSTICAS DESCRIPTIVAS")
print("="*50)

# obtener solo las columnas numéricas
numeric_columns = df.select_dtypes(include=[np.number]).columns

if len(numeric_columns) == 0:
    print("No se encontraron columnas numéricas en el dataset.")
else:
    for column in numeric_columns:
        print(f"\n--- Columna: {column} ---")
        try:
            print(f"Promedio: {calculate_average(df[column]):.2f}")
            print(f"Mediana: {calculate_median(df[column]):.2f}")
            print(f"Moda: {calculate_mode(df[column])}")
            print(f"Desviación estándar: {calculate_standard_deviation(df[column]):.2f}")
            print(f"Varianza: {calculate_variance(df[column]):.2f}")
            print(f"Mínimo: {calculate_min(df[column]):.2f}")
            print(f"Máximo: {calculate_max(df[column]):.2f}")
        except Exception as e:
            print(f"Error al calcular estadísticas para {column}: {e}")