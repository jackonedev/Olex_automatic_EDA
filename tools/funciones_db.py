##  original path: Olex\actividad_2\funciones_db.py

import os
import pandas as pd
import zipfile, tarfile

def data_info(data):
    "Funcion que devuelve informacion de las columnas de un dataframe"
    df = pd.DataFrame(pd.Series(data.columns))
    df.columns = ["columna"]
    df["Nan"] = data.isna().sum().values
    df["pct_nan"] = round(df["Nan"] / data.shape[0] * 100, 2)
    df["dtype"] = data.dtypes.values
    df["count"] = data.count().values
    df["pct_reg"] = (data.notna().sum().values / data.shape[0] * 100).round(2)
    df["count_unique"] = [
        len(data[elemento].value_counts()) for elemento in data.columns
    ]
    df = df.reset_index(drop=False)
    df = df.sort_values(by=["dtype", "count_unique"])
    df = df.reset_index(drop=True)
    return df


def leer_csv(path_input: str) -> pd.DataFrame:
    """
    Lee un archivo CSV en la ruta especificada y lo retorna como un objeto DataFrame de Pandas.

    Argumentos:
    - path_input: ruta relativa o absoluta donde se encuentra el archivo CSV.

    Retorna:
    - data: DataFrame de Pandas con los datos del archivo CSV.

    """
    # Obtener el path absoluto del archivo de entrada
    path_absoluto_input = os.path.abspath(path_input)
    print('Leyendo ubicación:')
    print(path_absoluto_input)
    # Abrir el archivo de entrada
    data = None
    with open(path_absoluto_input, 'r') as archivo_input:
        # Leer el archivo csv
        data = pd.read_csv(archivo_input)
    # Retornar la data
    if not isinstance(data, type(None)):
        return data


def guardar_csv(path_output, data):
    # Obtener el path absoluto del archivo de salida
    path_absoluto_output = os.path.abspath(path_output)
    print('Guardando en ubicación:')
    print(path_absoluto_output)
    # Abrir el archivo de salida
    with open(path_absoluto_output, 'w') as archivo_output:
        # Guardar el archivo csv
        data.to_csv(archivo_output, index=False)


def crear_directorio(path_output):
    # Obtener el path absoluto del directorio de salida
    path_absoluto_output = os.path.abspath(path_output)
    # Crear el directorio de salida si no existe
    if not os.path.exists(path_absoluto_output):
        print(f'Se crea el directorio {path_output} en ubicación:')
        print(path_absoluto_output)
        os.makedirs(path_absoluto_output)
    else:
        print(f'Directorio {path_absoluto_output} ya existe')


# Ejercicio 4.1
def read_book(path_input):
    # crear un path absoluto a partir de path_input
    path_abs = os.path.abspath(path_input)
    # abrir el archivo en modo lectura utilizando with
    with open(path_abs, 'r', encoding='utf-8-sig') as f:
        text = f.read()
    chapters = []
    current_chapter = ""
    for line in text.split("\n"):
        if line.isupper():
            # Si la línea está completamente en mayúsculas, empezamos un nuevo capítulo
            if current_chapter:
                chapters.append(current_chapter.strip())
            current_chapter = line + "\n"
        else:
            # Si la línea no está en mayúsculas, agregamos la línea al capítulo actual
            current_chapter += line + "\n"
    # Agregamos el último capítulo a la lista de capítulos
    if current_chapter:
        chapters.append(current_chapter.strip())
    # Creamos un DataFrame con los capítulos
    splitted_chapters = [chapter.split("\n") for chapter in chapters]
    text_df = pd.DataFrame(splitted_chapters).transpose()
    text_df.columns = ["chapter_{:02d}".format(i) for i in range(1, len(text_df.columns) + 1)]
    return text_df

# Ejercicio 4.2
def split_chapters_into_files(book, path_output):
    crear_directorio(path_output)
    chapter_series = book.apply(lambda serie: '\n'.join(serie.dropna().tolist()))
    for i in range(len(chapter_series)):
        path = os.path.abspath(path_output)
        path = os.path.join(path, chapter_series.index[i]+'.txt')
        with open(path, 'w') as f:
            f.write(chapter_series.values[i])

# Ejercicio 4.3
def compress_files(input_path, output_path, type='zip'):
    """Comprime el archivo de entrada en el formato especificado (zip o tar)

    Args:
        input_path (str): Ruta del archivo a comprimir.
        output_path (str): Ruta donde se guardará el archivo comprimido.
        type (str, optional): Formato de compresión ('zip' o 'tar'). Por defecto 'zip'.
    """
    crear_directorio(output_path)
    if type == 'zip':
        compress_path = os.path.join(output_path, output_path + '.zip')
        with zipfile.ZipFile(compress_path, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(input_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, arcname=os.path.relpath(file_path, input_path))
    elif type == 'tar':
        compress_path = os.path.join(output_path, output_path + '.tar')
        with tarfile.open(compress_path, 'w') as tar:
            tar.add(input_path, arcname=os.path.basename(input_path))
    else:
        print ('Didn\'t recognized the compression type name')

# Ejercicio 4.4
def get_folder_size(folder_path):
    "Devuelve el tamaño de la carpeta en bytes'"
    total_size = 0
    for path, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(path, file)
            total_size += os.path.getsize(file_path)
    return total_size

def bytes_to_kilobytes(bytes):
    return bytes / 1024

def get_file_size(file_path):
    """Obtiene el tamaño de un archivo en bytes"""
    return os.path.getsize(file_path)

def get_size(path):
    full_path = os.path.abspath(path)
    if os.path.isfile(full_path):
        file = 'fichero'
        size = get_file_size(path)
    elif os.path.isdir(full_path):
        file = 'directorio'
        size = get_folder_size(path)
    else:
        print('No existe el archivo o carpeta')
        return
    msg = """\
    Tamaño del {} "{}":
    >>  {} [KB]
    """
    print(msg.format(file, path, round(bytes_to_kilobytes(size), 2)))
    return round(bytes_to_kilobytes(size), 2)