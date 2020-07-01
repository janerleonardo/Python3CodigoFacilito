import requests
import json

if __name__ == '__main__':


    url = 'http://httpbin.org/post'
    #payload es el nombre del diccionario donde vamos a enviar los datos que se almacenaran en el metodo post
    payload = { 'name' : 'Janer', 'curso': 'Python'}
    #para el envio del encvambezado para en este enviar el token solo es necesario  crear el direccionario y enviarlo
    headers = {'Content-Type': 'application/json', 'access-token': '1234565'}
    # si lo enviamos los datos  en json, post se encarg de serializarlo
    response = requests.post(url, json=payload, headers=headers)
    print(response)
    # si lo enviamos los datos en data nosotros debemos serializarlo ejemplo
    response = requests.post(url=url, data=json.dumps(payload), headers= headers)
    print(response)


    if response.status_code == 200:

        response_json = response.json()
        print(response_json)

        #Para leer el encabezado del servidor utilizamos
        headers_response = response.headers # Es un diccionario, se obtiene los dats por su key
        print(headers_response)