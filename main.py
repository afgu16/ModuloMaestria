import sqlite3
from flask import Flask, render_template, request, redirect, url_for, render_template_string

app = Flask(__name__) #crear app de flask

def get_db_connection():
  conn = sqlite3.connect('censo.db')
  conn.row_factory = sqlite3.Row
  return conn

#ruta para la pagina de inicio
@app.route('/')

def index():
  return render_template_string('''
    <h1>Busqueda en el Censo</h1>
    <form action= "\buscar" method="post">
      <label for="tipo">Buscar por:</label>
      <select name="tipo" id="tipo">
        <option value="numero">Numero</option>
        <option value="nombre">Nombre</option>
      <\select>
      <label for="valor">Valor:</label>
      <input type="text" name="valor" id="valor" required>
      <button type="submit">Buscar</button>
    </form>
    ''')

#Ruta para realizar la busqueda
@app.route('/buscar', methods=['POST'])
def buscar():
  tipo=request.form['tipo']
  valor=request.form['valor']
  conn=get_db_connection()
  registro = None
  if tipo == 'numero':
    registro = conn.execute('SELECT * FROM censo WHERE numero = ?', (valor,)).fetchone()
  elif tipo == 'nombre':
    registro = conn.execute('SELECT * FROM censo WHERE nombre = ?', (valor,)).fetchone()

  conn.close()

  if registro:
    return render_template_string('''
    <p>Número: {{ registro['numero'] }}</p>
    <p>Nombre: {{ registro['nombre'] }}</p>
    <p>Edad: {{ registro['edad'] }}</p>
    <p>Impuestos: {{ registro['impuestos'] }}</p>
    <a href="/">Volver</a>
    ''')
  else:
    return 'Registro no encontrado. <a href="/">Volver</a>'
#Ruta para la pagina de registro    
if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5001)