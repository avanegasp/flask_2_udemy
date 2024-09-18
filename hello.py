from flask import Flask
# from markupsafe import escape

#en la instancia app se le dice que hello.py es el archivo principal
app = Flask(__name__)

#decorador
@app.route('/')
@app.route('/index')
def index():
    return "<h1>Página de Inicio</h1>"

@app.route('/hello')
@app.route('/hello/<string:name>')
@app.route('/hello/<string:name>/<int:age>')
def hello(name = None, age=None):
    if name == None and age == None:
        return f'<h1>Hola desde Index!</h1>'
    elif age == None:
        return f'<h1>Hola {name}!</h1>'
    else:
        return f'<h1>Hola {name}, sé que tienes {age} años!</h1>'
    
# #Para prevenir de ataques maliciosos

# @app.route('/code/<path:code>')
# def code(code):
#     return f'<code>{escape(code)}</code>'
    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')