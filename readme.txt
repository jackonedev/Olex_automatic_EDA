# Olex automatic-EDA

inicio: 24 de Agosto de 2023

objetivo: crear un generador de reportes EDA automático que convierta archivos .csv en .html, cuyo resultado sea la salida de de aplicar el framework ydata-profiling, y que esté disponibilizado al público por medio de un endpoint de FastAPI

motivación: crear web apis que puedan interactuar con objetos tipo bytes (archivos)

producto final: que sea abierto al público

Features:
1- modo explorativo: para realizar un análisis más superficial y velóz

[deeper profiling](https://ydata-profiling.ydata.ai/docs/master/pages/getting_started/quickstart.html)

2- minimal mode: para anular los cálculos más complejos. Util a la hora de introducir grandes datasets.

[minimal mode](https://ydata-profiling.ydata.ai/docs/master/pages/use_cases/big_data.html)

3- sample mode: ejecuta todos los cálculos sobre una muestra aleatoria que representa una proporcion fija del tamaño total del dataset

[sample the dataset](https://ydata-profiling.ydata.ai/docs/master/pages/use_cases/big_data.html)

4- sensitive mode: para que el reporte no exponga datos que no son publicos. Utiles para datasets de servicios médicos.

[senstitive data](https://ydata-profiling.ydata.ai/docs/master/pages/use_cases/sensitive_data.html)

5- comparacion de dataset: se utiliza para comparar dos dataset que contengan las mismas variables. Util para series temporales, o para validar train and test sets for machine learning

[dataset comparison](https://ydata-profiling.ydata.ai/docs/master/pages/use_cases/comparing_datasets.html)
