import requests
import json
"""
Descargar desde un APi un archivo muy pesado 
"""
if __name__ == '__main__':
    url = 'https://image.shutterstock.com/image-photo/3d-rendered-guitar-isolated-realistic-260nw-564905389.jpg'
    response = requests.get(url=url,stream=True) # Realiza la peticion sin descargar el contenido
    with open('image.jpg', 'wb') as file:
        for chunk in response.iter_content(): #Descarga el contenido poco a poco
            file.write(chunk)
    response.close()