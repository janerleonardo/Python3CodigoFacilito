from flask import Flask,request,make_response,redirect

app = Flask(__name__)

@app.route('/') # Decorador para definir la ruta de la apliacion
def index():
    user_ip =request.remote_addr
    reponse = make_response(redirect('/hello'))
    reponse.set_cookie('user_ip', user_ip)

    return reponse

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    return f'Esta es la Ip del usuario que ingreso {user_ip}'

if __name__ == '__main__':
    app.run(debug=True)