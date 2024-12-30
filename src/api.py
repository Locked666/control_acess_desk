import os 
from flask import Flask, render_template, request, redirect, url_for, session,jsonify
# from flask_socketio import SocketIO, emit
import subprocess
from config import PATH_CONFIG_INI, complement_ini, USERNAME_INI, PASSWORD_INI, PORT_WEB_INI, HOST_WEB_INI, DEBUG_INI,NAME_APP,get_config
from datetime import datetime
from utils.encrypt import encrypt,decrypt

app = Flask(__name__)
app.secret_key = os.environ.get('APP_SECRET_KEY')

@app.route('/execute', methods=['POST','GET'])
def execute():
    data =  request.json
    username = data['username']
    password = data['password']
    passw = decrypt(get_config()['Settings']['password'],os.environ.get('APP_SECRET_KEY'),os.environ.get('APP_SECRET_SALT'))
    type_acess = data['type_acess']
    id_acess = data['id_acess']
    user_acess = data['user_acess']
    password_acess =  data['password_acess']
    d_password_acess = decrypt(password_acess,os.environ.get('APP_SECRET_KEY'),os.environ.get('APP_SECRET_SALT'))


    try:
        if request.method == 'POST':
            if username == get_config()['Settings']['username'] and password == passw:
                if type_acess == 'teamviewer':
                    subprocess.Popen(get_config()['AppPath']['teamviewer'], shell=True)
                    return {"status": "success", "message": "Programa executado!"}
                elif type_acess == 'anydesk':
                    subprocess.Popen(get_config()['AppPath']['anydesk'], shell=True)
                    return {"status": "success", "message": "Programa executado!"}
                elif type_acess == 'qsconnect':
                    subprocess.Popen(get_config()['AppPath']['qsconnect'], shell=True)
                    return {"status": "success", "message": "Programa executado!"}
                else:
                    return {"status": "error", "message": "Tipo de acesso inválido!"}
            else:
                return {"status": "error", "message": "Usuário ou senha inválidos!"}
    # try:
    #     if request.method == 'GET':
    #         return jsonify({'status':'pong'})
    #     else : 
    #         command = request.args.get('command')
    #         subprocess.Popen(command, shell=True)
    #         return {"status": "success", "message": "Programa executado!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500
    

@app.errorhandler(404)
def not_found(e):
    return ("pong"), 404

# Função para iniciar o Flask em uma thread separada
def start_flask():
    app.run(port=get_config()['Settings']['port_local'])
    
if __name__=='__main__'    :
    start_flask()