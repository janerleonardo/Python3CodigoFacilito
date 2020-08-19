from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Janer'
    course= 'Codigo Facilito'
    is_premium = False
    courses = ['Python', 'Ruby', 'C#', 'Java', 'Go', 'JavaScripts']
    return render_template('index.html', name=name, course=course,is_premium=is_premium,courses=courses)

@app.route('/usuario/<username>')
def usuario(username):
    return f'Hola {username}'

if __name__ == '__main__':
    #Aqui estamos cambiando el puerto por defecto con el parametro port=9000
    #Tambien estamos cambiando el parametro debug = True, para que muestre los errores en la pagina
    app.run(port=9000, debug=True)