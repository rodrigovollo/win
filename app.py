from flask import Flask, request, render_template
import subprocess
import os


app = Flask(__name__)
@app.route('/')
def index():
    return 'Ola'

@app.route('/exec')
def exe():
    resultado = os.system("dir")
    print ('result= ')
    print  (resultado.stdout)
    return 'ok'

@app.route('/exec2')
def exe2():
    args = request.args
    comando = args['cmd']
    comando = comando.replace(',', ' ')
    comando = comando.replace(';', '&')
    print (comando)
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    return 'Content-type: text/html \n\n' + \
          resultado.stdout


app.run(host='0.0.0.0', port=5000)