from flask import Flask,request,make_response,redirect,render_template

app = Flask(__name__)

everyone = ['Programar Tareas con Python y Flask', 'Curso de Platzi de Flask Python', 'Curso de Codigo facilito Flask Python']

@app.route('/') # Decorador para definir la ruta de la apliacion
def index():
    user_ip =request.remote_addr
    reponse = make_response(redirect('/hello'))
    reponse.set_cookie('user_ip', user_ip)

    return reponse

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    # Se crea un diccionario de contexto en donde cada key seria cada una de las variable
    # que se utilizaran y se pasa con el doble aterisco (**) para no tener que utilizar la
    # la variable.key(contexto.user_ip).
    context = {'user_ip' : user_ip,
               'everyone': everyone}
    #return render_template('hello.html', user_ip=user_ip, everyone=everyone) Esto es igual a

    return render_template('hello.html', **context)

if __name__ == '__main__':
    app.run(debug=True)