from urllib import request,parse



if __name__=='__main__':
    url = 'http://httpbin.org/put'
    # payload es el nombre del diccionario donde vamos a enviar los datos que se almacenaran en el metodo post
    data= {'name': 'Janer', 'curso': 'Python'}
    #Esta serializando los datos
    pyloads = parse.urlencode(data).encode()

    requests = request.Request(url=url, data=pyloads)
    request.get_method = 'PUT'
    response = request.urlopen(requests).read()

    print(response)
