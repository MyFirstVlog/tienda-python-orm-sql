from flask import Flask #Como lo que importamos viene con la letra F mayuscula es porque es una clase
from flask import render_template #Para renderizar archivos html

from database import db # Si importo y no sale ningun error es porque la conexion se hizo de manera exitosa

app = Flask(__name__) # Flask necesita un contexto, por eso adicionamios el __name__

@app.route('/') # decorador para adicionar el metodo como retorno al hacer request a la ruta
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')



#Para ejecutar el server en modo 'watcher'
if(__name__) == '__main__': #los archivos .py es un modulo, siempre al ejecutar el modulo, python adhiere un atributo __name__ que por defecto pone __main__
    app.run(debug=True)