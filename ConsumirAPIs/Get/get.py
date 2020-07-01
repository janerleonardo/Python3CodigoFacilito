import requests
import json

if __name__ == '__main__':

    url_params = 'http://httpbin.org/get?name=Janer&curso=Python' # Url con Parametros

    url = 'http://httpbin.org/get'
    args = { 'name' : 'Janer', 'curso': 'Python'}
    response = requests.get(url, params=args) # el metodo get recibe un parametro que es la URL, puedeir sin  la palabra params
    print(response)
    if response.status_code == 200:

        response_json = response.json() # Retornado un Diccionario
        print(response_json)


        response_json = json.loads(response.text) # Utilizando la libreria Json
        print(response_json)