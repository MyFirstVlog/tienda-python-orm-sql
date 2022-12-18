from flask import Flask #Como lo que importamos viene con la letra F mayuscula es porque es una clase
from flask import request
from flask import session #DICT
from flask import render_template #Para renderizar archivos html

#from database import db # Si importo y no sale ningun error es porque la conexion se hizo de manera exitosa
from database import User #Ahora solo importo la clase User

app = Flask(__name__) # Flask necesita un contexto, por eso adicionamios el __name__
app.secret_key = 'bootcamp_codigofacilito' #pfuscar, evita que los textos queden en texto plano  aun texto irreconocible por el texto humano -> necesario para generar la sesion

@app.route('/') # decorador para adicionar el metodo como retorno al hacer request a la ruta
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        _email = request.form.get('email')  #if value does not exist, return none, if it's done by casting ['email'], it may cause an error
        _password = request.form.get('password')

        if _email and _password:
            user = User.create_user(_email, _password) # inserta usuarios en la base de datos, no es necesario crear una instancia porque es un metodo de clase no de instancia
            print('user', user.id)
            session['user'] = user.id #para mirar que usuarios estan activo, evitar estar pidiendo credenciales en la navegacion
                       
        print(_email, _password)
        
    return render_template('register.html')


#Para ejecutar el server en modo 'watcher'
if(__name__) == '__main__': #los archivos .py es un modulo, siempre al ejecutar el modulo, python adhiere un atributo __name__ que por defecto pone __main__
    app.run(debug=True)