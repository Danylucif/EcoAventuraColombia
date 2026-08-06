import pandas as pd
import os

RUTA_BD = "data/reportes_ciudadanos.csv"

def guardar_reporte_fauna(departamento, grupo, estado, detalles):
    """
    Guarda de forma permanente los reportes de los usuarios en una base de datos local CSV.
    """
    nuevo_registro = {
        "Departamento": [departamento],
        "Clase de Espécimen": [grupo],
        "Estado de Salud": [estado],
        "Descripción": [detalles]
    }
    df_nuevo = pd.DataFrame(nuevo_registro)
    
    # Si el archivo no existe, lo crea con encabezados. Si existe, añade la fila abajo.
    if not os.path.exists(RUTA_BD):
        df_nuevo.to_csv(RUTA_BD, index=False, encoding="utf-8")
    else:
        df_nuevo.to_csv(RUTA_BD, mode='a', header=False, index=False, encoding="utf-8")

def cargar_todos_los_reportes():
    """
    Lee y retorna la base de datos de reportes existentes para analítica interna.
    """
    if os.path.exists(RUTA_BD):
        return pd.read_csv(RUTA_BD, encoding="utf-8")
    return pd.DataFrame()

