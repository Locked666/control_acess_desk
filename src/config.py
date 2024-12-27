import os 
import configparser
from pathlib import Path


global PATH_DATABASE
global PATH_CONFIG_INI 
global USERNAME_INI
global PASSWORD_INI
global PORT_WEB_INI
global HOST_WEB_INI
global DEBUG_INI
global NAME_APP


__version__= '1.0.0.0'

PATH_CONFIG_INI = 'config.ini'
NAME_APP = 'System Tray - Controle de Acesso.'
MODE_DEBUG = False

config = configparser.ConfigParser()

settings_sec =  {
    'username':'',
    'password':'',
    'port_web': '5000',
    'host_web': '',
    'debug': 'False', 
    'port_local': '00000'
}

app_path_sec = {
    'teamviewer' : r'C:\Program Files (x86)\TeamViewer\TeamViewer.exe',
    'anydesk' : r'C:\Program Files (x86)\AnyDesk\AnyDesk.exe',
    'qsconnect' : r''
}


def exist_config():
    if not os.path.exists(PATH_CONFIG_INI):
        try:
            config['Settings'] = settings_sec
            config['AppPath'] = app_path_sec
            with open(PATH_CONFIG_INI, 'w') as configfile:
                config.write(configfile)
                return True
        except Exception as e:
            raise f"Ocorreu um erro ao criar arquivo de configuração: {e}"    

def get_config():
    config.read(PATH_CONFIG_INI)
    return config

def complement_ini(session:str = '', line:str = '', new_info = ''):
    # Modifica os valores desejados

    try:
        config[session][line] = new_info 
    # Salva as alterações de volta no arquivo
        with open(PATH_CONFIG_INI, 'w') as configfile:
            config.write(configfile)

        return f"Sessão {session} linha {line} informação {new_info}"    
    
    except ValueError as e:
        return f'Ocorreu ao executar a função\n {e}'


# print('Configurações do sistema')
exist_config()
p_variavel = get_config()
USERNAME_INI = p_variavel['Settings']['username']
PASSWORD_INI = p_variavel['Settings']['password']
PORT_WEB_INI = p_variavel['Settings']['port_web']
HOST_WEB_INI = p_variavel['Settings']['host_web']
DEBUG_INI = p_variavel['Settings']['debug']


   