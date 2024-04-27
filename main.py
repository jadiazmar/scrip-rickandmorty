# 1.primero se hace llamado al apy de rick and morty
import requests
import json
# URL de la API
url = "https://rickandmortyapi.com/api/character"

# Realizar la petición GET
response = requests.get(url)

lista_humanos = []

# Comprobar si la petición fue exitosa (código de estado 200)
if response.status_code == 200:
    # Convertir la respuesta a formato JSON
    data = response.json()
    # Imprimir la respuesta JSON

    # 2.luego se recorre la lista de personajes de la serie
    for item in data['results']:
        # 3.luego vamos hacer un condicional solo vamos a guardar los personajes que sean humanos
        especie = item['species']
        if especie == "Alien":

            print("------------------------------------")
            print(especie)
            # guar objeto en la lista
            lista_humanos.append(item)
    # 4. vamos aguardar esos personajes en json local
    nombre_archivo = "humanos.json"

# Abrir el archivo en modo de escritura
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        # Escribir la lista de objetos JSON en el archivo
        json.dump(lista_humanos, archivo)

    print("Datos guardados correctamente en", nombre_archivo)

else:
    print("Error al hacer la petición:", response.status_code)
