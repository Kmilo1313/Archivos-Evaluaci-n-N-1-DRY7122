import json

# Ruta al archivo JSON en la máquina virtual (asegúrate de reemplazar '/ruta/a/myfile.json' con la ruta correcta)
ruta_archivo_json = '/home/devasc/labs/devnet-src/parsing/myfile.json'

try:
    # Abrir el archivo JSON y cargar su contenido en la variable json_file
    with open(ruta_archivo_json, 'r') as ourjson:
        json_file = json.load(ourjson)
        print("Archivo JSON cargado correctamente.")

    # Aquí puedes utilizar la variable json_file para acceder a los datos del archivo JSON
    print("Contenido del archivo JSON:")
    print(json_file)

except FileNotFoundError:
    print("El archivo JSON no se encontró en la ruta especificada.")
except json.JSONDecodeError:
    print("El archivo no es un archivo JSON válido.")
except Exception as e:
    print("Ocurrió un error:", str(e))
