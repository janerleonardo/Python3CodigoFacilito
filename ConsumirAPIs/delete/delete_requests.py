import requests
import json

if __name__ == '__main__':


    url = 'http://httpbin.org/delete'
    payload = { 'name' : 'Janer', 'curso': 'Python'}
    headers = {'Content-Type': 'application/json', 'access-token': '1234565'}
    response = requests.delete(url, json=payload, headers=headers)
    print(response)


    if response.status_code == 200:

        response_json = response.json()
        print(response_json)

        #Para leer el encabezado del servidor utilizamos
        headers_response = response.headers # Es un diccionario, se obtiene los dats por su key
        print(headers_response)