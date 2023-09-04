import os, csv
import pandas as pd
from typing import Union


def leer_csv(path_input: str) -> Union[list, None]:
    """
    Lee un archivo CSV en la ruta especificada y lo retorna como un objeto DataFrame de Pandas.

    Argumentos:
    - path_input: ruta relativa o absoluta donde se encuentra el archivo CSV.

    Retorna:
    - data: DataFrame de Pandas con los datos del archivo CSV o None.
    """
    # Abrir el archivo de entrada
    data_list = None
    with open(path_input, 'r') as archivo_input:
        # Leer el archivo csv
        data = csv.reader(archivo_input)
        data_list = [row for row in data]
    return data_list


def return_dataframe(data_list:list) -> Union[pd.DataFrame, None]:
    try:
        data = pd.DataFrame(data_list[1:], columns=data_list[0])
    except:
        data = None
    return data

def convert_path_to_dataframe(path_input:str) -> Union[pd.DataFrame, None]:
    # Obtener el path absoluto del archivo de entrada
    path_input = os.path.abspath(path_input)
    data_list = leer_csv(path_input=path_input)
    dataframe = return_dataframe(data_list=data_list)
    return dataframe