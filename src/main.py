from PySide6.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QMenu, \
    QMessageBox, QSizePolicy, QPushButton, QCheckBox, QVBoxLayout
from PySide6 import QtCore
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt,QCoreApplication,QFile,Slot,SLOT,Signal,QRect,QObject, QTime,QAbstractTableModel,QDateTime
from PySide6.QtGui import QIcon, QAction
from pathlib import Path
from PIL import Image, ImageDraw
import threading
from flask import Flask, request
import subprocess
import os
import asyncio
import requests
import sys
from config import PATH_CONFIG_INI, complement_ini, USERNAME_INI, PASSWORD_INI, PORT_WEB_INI, HOST_WEB_INI, DEBUG_INI,NAME_APP,get_config
from ui.mnConfig import Ui_mnConfig
from utils.encrypt import encrypt,decrypt

class Window(QWidget,Ui_mnConfig):
    def __init__(self, system_tray):
        super().__init__()
        self.setupUi(self)

        # Save system tray object
        self._system_tray = system_tray
        # Resize window
        self.resize(300, 150)
        # Set window title
        self.setWindowTitle(NAME_APP)

        # CREATE signal and slot for button
        self.bnt_save.clicked.connect(self.callback_save)
        self.bnt_cancel.clicked.connect(self.callback_cancel)
        self.bnt_edit.clicked.connect(self.callback_edit)
        self.pushButton_4.clicked.connect(self.on_sync_api)

        # Load config
        self.load_config()

    def on_sync_api(self):
               
        p = encrypt(self.text_password.text().strip(),os.environ.get('APP_SECRET_KEY'),os.environ.get('APP_SECRET_SALT'))
        url = f'http://{self.text_host.text().strip()}:{self.text_port.text().strip()}/CheckStatus' 
        params = { 'username': {self.text_user.text().strip()}, 
                  'password': {p} }
        try :  
            response = requests.get(url, params=params) 
            if response.status_code == 200: 
                QMessageBox.information(self, 'Informação', 'Conexão realizada com sucesso.')
            else: 
                if self.checkbox_debug.isChecked():
                    QMessageBox.warning(self,'Erro ao conectar', f'Ocorreu um erro ao conectar com o servidor\n {response.json()}')
                else :  
                    QMessageBox.warning(self,'Erro ao conectar', f'Ocorreu um erro ao conectar com o servidor\n Erro codigo: {response.status_code}')  
                
            
        
        except Exception as e: 
            if self.checkbox_debug.isChecked():
                QMessageBox.warning(self, 'Erro ao realizar operação',f"Ocorreu um erro ao conectar com o servidor\n {e}")
            else :     
                QMessageBox.warning(self, 'Erro ao realizar operação',f"Ocorreu um erro ao conectar com o servidor")
        
        
        pass

    def load_config(self):
        # Load config
        self.config = get_config()
        self.text_user.setText(get_config()['Settings']['username'])
        if get_config()['Settings']['password']:
            self.text_password.setText(decrypt(get_config()['Settings']['password'],os.environ.get('APP_SECRET_KEY'),os.environ.get('APP_SECRET_SALT')))    
        self.text_port.setText(get_config()['Settings']['port_web'])
        self.text_host.setText(get_config()['Settings']['host_web'])
        self.checkbox_debug.setChecked( True if get_config()['Settings']['debug'] == 'True' else False)



    @Slot()
    def callback_save(self):
        if not self.text_user.text().strip() or not self.text_password.text().strip() or not self.text_port.text().strip() or not self.text_host.text().strip():
            QMessageBox.warning(self, 'Aviso', 'Todos os campos são obrigatórios.')
            return
        try:
            complement_ini('Settings', 'username', self.text_user.text().strip())
            p = encrypt(self.text_password.text().strip(),os.environ.get('APP_SECRET_KEY'),os.environ.get('APP_SECRET_SALT'))
            complement_ini('Settings', 'password',p.decode() )
            complement_ini('Settings', 'port_web', self.text_port.text().strip())
            complement_ini('Settings', 'host_web', self.text_host.text().strip())
            complement_ini('Settings', 'debug', 'True' if self.checkbox_debug.isChecked() else 'False')
            QMessageBox.information(self, 'Informação', 'Configurações salvas com sucesso.')
            self.frm_body.setEnabled(False)
            self.control_button('viewer')
        except Exception as e:
            QMessageBox.critical(self, 'Erro', f'Ocorreu um erro ao salvar as configurações:\n {e}')
        pass
    
    @Slot()
    def callback_cancel(self):
        if not self.bnt_edit.isEnabled():
            reply = QMessageBox.question(self, 'Confirmar Saída',
                                     'A tela está em modo de edição, deseja realmente sair?\n Todas as alterações serão perdidas.',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.frm_body.setEnabled(False)
                self.control_button('viewer')
                self.load_config()

            else:
                return
           

        else:
            self.close()    


    @Slot()
    def callback_edit(self):
        self.frm_body.setEnabled(True)
        self.control_button('edit')


    @Slot()
    def control_button(self, args_1):
        """_description_

        Args:
            edit (str): buttons state for edition
            viewer (str): buttons state for viewer
        """
        match args_1:
            case 'edit':
                self.bnt_edit.setEnabled(False)
                self.bnt_save.setEnabled(True)
                self.bnt_cancel.setEnabled(True)
            case 'viewer':
                self.bnt_edit.setEnabled(True)
                self.bnt_save.setEnabled(False)
                self.bnt_cancel.setEnabled(True)

    @Slot()
    def closeEvent(self, event,t=None):
        if not self.bnt_edit.isEnabled():
            reply = QMessageBox.question(self, 'Confirmar Saída',
                                     'A tela está em modo de edição, deseja realmente sair?\n Todas as alterações serão perdidas.',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        else :
            reply = QMessageBox.question(self, 'Confirmar Saída',
                                        'Você realmente fechar o lançamento?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()  # Aceita o fechamento da janela
            self.destroy()

        else:
            event.ignore()                    

class Application(QApplication):
    def __init__(self, args):
        super().__init__(args)

        self._menu = None
        self._system_tray = None
        self._window = None

        self.btn_show_hide = None
        self.btn_minimize = None
        self.btn_hello = None
        self.chk_option = None
        self.btn_quit = None

        # Keep application running when all windows are closed
        self.setQuitOnLastWindowClosed(False)
        # Set window icon
        path = Path(__file__).resolve().parent
        self.setWindowIcon(QIcon(os.path.join(r"D:\desenvolvimento\python\control_acess_desk\image\web.png")))

        # Create tray menu
        self.create_menu()

        # Create system tray
        self.create_system_tray()

        # Create window widget
        self._window = Window(self._system_tray)

    def create_menu(self):
        # Create the menu
        # The system tray icon does not take ownership of the menu. You must ensure
        # that it is deleted at the appropriate time by, for example, creating the
        # menu with a suitable parent object.
        self._menu = QMenu()

        # Create hello button
        self.btn_show_hide = QAction('Show')
        self.btn_show_hide.triggered.connect(self.on_btn_show)

        # self.btn_minimize = QAction('Minimize')
        # self.btn_minimize.triggered.connect(self.on_btn_minimize)

        # self.btn_hello = QAction('Say hi!')
        # self.btn_hello.triggered.connect(self.on_btn_hello)

        # self.chk_option = QAction('Value')
        # self.chk_option.setCheckable(True)
        # self.chk_option.setChecked(True)
        # self.chk_option.triggered.connect(self.on_checkbox_change)

        # Create quit button
        self.btn_quit = QAction('Quit')
        self.btn_quit.triggered.connect(QApplication.quit)

        # Add buttons to menu
        self._menu.addAction(self.btn_show_hide)

        self._menu.addSeparator()
        self._menu.addAction(self.btn_quit)

    def create_system_tray(self):
        # Create system tray icon with menu
        # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QSystemTrayIcon.html
        self._system_tray = QSystemTrayIcon()

        # Set system tray icon
        path = Path(__file__).resolve().parent
        self._system_tray.setIcon(QIcon(os.path.join(r"D:\desenvolvimento\python\control_acess_desk\image\web.png")))

        # Make system tray icon with menu visible
        self._system_tray.setVisible(True)

        # Set system tray tooltip
        self._system_tray.setToolTip('PySide6 app')

        # Add the menu to the system tray
        self._system_tray.setContextMenu(self._menu)

        # Show system tray
        self._system_tray.show()


    def on_btn_show(self):
        # When the window is minimized on Ubuntu, it does not restore to normal
        # after calling show() or showNormal(). Workaround is to call hide()
        # first followed by showNormal().
        self._window.hide()
        self._window.showNormal()


def main():
    # Create application
    app = Application(sys.argv)

    # Application main loop
    sys.exit(app.exec())


if __name__ == '__main__':
    main()       





