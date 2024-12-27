import os 
from flask import Flask, render_template, request, redirect, url_for, session,jsonify
from flask_socketio import SocketIO, emit
import subprocess
from config import PATH_CONFIG_INI, complement_ini, USERNAME_INI, PASSWORD_INI, PORT_WEB_INI, HOST_WEB_INI, DEBUG_INI,NAME_APP,get_config
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('APP_SECRET_KEY')

@app.route('/execute', methods=['POST','GET'])
def execute():
    try:
        if request.method == 'GET':
            return jsonify({'status':'pong'})
        command = request.json.get('command')
        subprocess.Popen(command, shell=True)
        return {"status": "success", "message": "Programa executado!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500

# Função para iniciar o Flask em uma thread separada
def start_flask():
    app.run(port=get_config()['Settings']['port_local'])
    
if __name__=='__main__'    :
    start_flask()