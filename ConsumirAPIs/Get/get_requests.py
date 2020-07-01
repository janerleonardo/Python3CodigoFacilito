import requests

if __name__ == '__main__':
    url = 'https://www.google.com.co/'
    response = requests.get(url) # el metodo get recibe un parametro que es la URL
    print(response)
    if response.status_code == 200:
        print(response.content)
        #Sacamos la respuesta de la peticion y la guardamos en un archivo html
        content = response.content
        file = open('google_requests.html', 'wb')
        file.write(content)
        file.close()
#Todo los APis devuelven un valor esstutus 200 quiere decir qe todo salio bien

