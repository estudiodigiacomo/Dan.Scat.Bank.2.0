from banks.nacion.nacion_position import nacion_report
from banks.credicoop.credicoop_position import credicoop
from banks.pampa.pampa_position import pampa_report
from banks.bbva.bbva_position import bbva
from banks.bbva.bbva_echeq import bbva as bbva_echeq_func
from banks.macro.macro_position import macro_report
from banks.macro.macro_prestam import macro
import sys
import os
import shutil
import datetime
from PyPDF2 import PdfMerger
from utils.folders import folders_report

def report_general(automation_var):
    try:
        banks_and_functions = [
            ('Banco Nacion', nacion_report),
            ('Banco Credicoop', credicoop),
            ('Banco de La Pampa', pampa_report),
            ('BBVA Frances', bbva),
            ('BBVA Frances', bbva_echeq_func),
            ('Banco Macro', macro_report),
            ('Banco Macro', macro),
        ]

        client_folder = 'Scattone Daniel Oscar'
        date_folder = folders_report(client_folder, automation_var)

        for bank_name, bank_function in banks_and_functions:
            bank_function(bank_name, automation_var)
            # Procesar PDFs inmediatamente después de cada función de banco
            procesar_pdfs(date_folder, bank_name)

        # Unificar todos los PDFs al final
        unificar_todos_los_pdfs(date_folder, client_folder)
    except Exception as e:
        print('Error al iniciar la automatizacion de reporte general: ', {str(e)})

def procesar_pdfs(directorio, bank_name):
    try:
        def obtener_ultimos_pdfs(directorio, n=1):
            archivos = [f for f in os.listdir(directorio) if f.endswith('.pdf')]
            archivos = sorted(archivos, key=lambda x: os.path.getctime(os.path.join(directorio, x)), reverse=True)
            return archivos[:n]

        def unificar_pdfs(rutas_pdfs, salida_pdf):
            merger = PdfMerger()
            for ruta_pdf in rutas_pdfs:
                merger.append(ruta_pdf)
            merger.write(salida_pdf)
            merger.close()

        # Añadir PDF de presentación
        pdfs_presentacion = []
        presentacion_path = fr'C:\Daniel Scattone - Automatizacion\src\report\pdf_presentacion\{bank_name}.pdf'
        if os.path.exists(presentacion_path):
            pdfs_presentacion.append(presentacion_path)

        # Obtener el último archivo PDF descargado
        ultimos_pdfs = obtener_ultimos_pdfs(directorio)
        rutas_pdfs = [os.path.join(directorio, pdf) for pdf in ultimos_pdfs]

        if not rutas_pdfs:
            print("No se encontraron archivos PDF para unificar.")
            return

        date = datetime.datetime.now()
        formatted_date = date.strftime("%d-%m-%Y %H.%M.%S")
        # Ruta del archivo PDF unificado
        salida_pdf = os.path.join(directorio, f'{bank_name} - Emisión {formatted_date}.pdf')

        # Unificar los archivos PDF (primero la presentación y luego el descargado)
        todas_las_rutas_pdfs = pdfs_presentacion + rutas_pdfs
        unificar_pdfs(todas_las_rutas_pdfs, salida_pdf)
        print(f"Archivos PDF unificados en {salida_pdf}")

        # Eliminar los archivos PDF originales
        for ruta_pdf in rutas_pdfs:
            os.remove(ruta_pdf)
            print(f"Archivo eliminado: {ruta_pdf}")
    except Exception as e:
        print('Error al procesar PDFs:', {str(e)})

def unificar_todos_los_pdfs(directorio, client_folder):
    try:
        def obtener_todos_los_pdfs(directorio):
            archivos = [f for f in os.listdir(directorio) if f.endswith('.pdf')]
            return sorted(archivos, key=lambda x: os.path.getctime(os.path.join(directorio, x)))

        def unificar_pdfs(rutas_pdfs, salida_pdf):
            merger = PdfMerger()
            for ruta_pdf in rutas_pdfs:
                merger.append(ruta_pdf)
            merger.write(salida_pdf)
            merger.close()

        todos_los_pdfs = obtener_todos_los_pdfs(directorio)
        rutas_pdfs = [os.path.join(directorio, pdf) for pdf in todos_los_pdfs]

        if not rutas_pdfs:
            print("No se encontraron archivos PDF para unificar.")
            return

        date = datetime.datetime.now()
        formatted_date = date.strftime("%d-%m-%Y %H.%M.%S")
        salida_pdf = os.path.join(directorio, f'Reporte general - Bancos - Emisión {formatted_date}.pdf')

        # Añadir el PDF de presentación general al inicio
        presentacion_general_path = fr'C:\Daniel Scattone - Automatizacion\src\report\pdf_presentacion\DanielScattone-Presentacion-Reporte-Bancos.pdf'
        if os.path.exists(presentacion_general_path):
            rutas_pdfs.insert(0, presentacion_general_path)
        
        unificar_pdfs(rutas_pdfs, salida_pdf)
        print(f"Todos los archivos PDF unificados en {salida_pdf}")

        # Crear carpeta con formato de fecha y hora
        nueva_carpeta = os.path.join(directorio, datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
        os.makedirs(nueva_carpeta)

        # Mover el archivo PDF unificado a la nueva carpeta
        nueva_ruta_pdf = os.path.join(nueva_carpeta, f'Reporte general - Bancos - Emisión {formatted_date}.pdf')
        shutil.move(salida_pdf, nueva_ruta_pdf)
        print(f"Archivo PDF unificado movido a {nueva_ruta_pdf}")
    except Exception as e:
        print('Error al unificar todos los PDFs:', {str(e)})
    finally:
        sys.exit()