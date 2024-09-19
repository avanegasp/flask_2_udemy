from flask import Flask, render_template, url_for
from markupsafe import escape
from datetime import datetime

#en la instancia app se le dice que hello.py es el archivo principal
app = Flask(__name__)

#Filtro
@app.add_template_filter
def today(date):
    return date.strftime('%d-%m-%Y')

# app.add_template_filter(today, 'today')

# Función personalizada

@app.add_template_global
def repeat(s, n):
    return s * n

# app.add_template_global(repeat, 'repeat')
#decorador
@app.route('/')
def index():
    print(url_for('index'))
    print(url_for('hello', name = "Angie"))
    print(url_for('code', code = 'print("Hola")'))
    name = "Angie"
    friends = ["Caro", "Oliva", "Diana"]
    date = datetime.now()
    return render_template('index.html',
                            name=name, 
                            friends=friends, 
                            date=date,
                            # repeat=repeat 
                            )

@app.route('/hello')
@app.route('/hello/<string:name>')
@app.route('/hello/<string:name>/<int:age>')
@app.route('/hello/<string:name>/<int:age>/<email>')
def hello(name = None, age=None, email=None):
    my_data = {
        'name':name,
        'age':age,
        'email':email
    }

    return render_template('hello.html',data=my_data)
    
# #Para prevenir de ataques maliciosos

@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'
    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')