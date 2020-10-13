from flask import Flask, render_template,request
app = Flask(__name__)

# Con el Callback befare_request puedes ejecutar cosas antes de la peticion, se usa para conectarse a una PAI, Base de datos, etc
@app.before_request
def before_request():
    print('Antes de la peticiones')

# Se ejecuat despues de cada peticion revise como parametro la repuesta de cada peticion, esa repues la debemos retornar
# y las accciones la ponemos antes del return
@app.after_request
def after_requests(response):
    print('Despues')
    return response

@app.route('/')
def index():
    name = 'Janer'
    course= 'Codigo Facilito'
    is_premium = False
    courses = ['Python', 'Ruby', 'C#', 'Java', 'Go', 'JavaScripts']
    return render_template('index.html', name=name, course=course,is_premium=is_premium,courses=courses)

@app.route('/about')
def about():
    print('En about')
    return render_template('about.html')

#Para defini un parametro se utiliza <> (signo de mayor y menor )
@app.route('/usuario/<username>')
def usuario(username):
    return f'Hola {username}'

@app.route('/usuario/<lastname>/<name>')
def user_last_name(lastname, name):
    return f'Hola {lastname} {name}, '

# por defecto los parametos son string si necesitamos que sea otro tipo de dato sera algo asi
@app.route('/usuario/<lastname>/<name>/<int:age>')
def user_last_name_age(lastname, name, age):
    return f'Hola {lastname} {name}, mi edad es {age} '

#Enviar informacion a flask por query string que es poner en la url los valores ejemplo url?name=janer
@app.route('/datos')
def datos():
    name = request.args.get('name','')
    return f'Listado de datos {name}'

if __name__ == '__main__':
    #Aqui estamos cambiando el puerto por defecto con el parametro port=9000
    #Tambien estamos cambiando el parametro debug = True, para que muestre los errores en la pagina
    app.run(port=9000, debug=True)