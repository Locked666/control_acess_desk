# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mnConfig.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QToolButton, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_mnConfig(object):
    def setupUi(self, mnConfig):
        if not mnConfig.objectName():
            mnConfig.setObjectName(u"mnConfig")
        mnConfig.resize(495, 365)
        mnConfig.setMinimumSize(QSize(495, 365))
        mnConfig.setMaximumSize(QSize(1600, 1600))
        self.verticalLayout_3 = QVBoxLayout(mnConfig)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, -1, -1, -1)
        self.label = QLabel(mnConfig)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.tab_body = QTabWidget(mnConfig)
        self.tab_body.setObjectName(u"tab_body")
        self.tab_body.setEnabled(True)
        self.tab_body.setMaximumSize(QSize(1600, 1600))
        self.tab_first = QWidget()
        self.tab_first.setObjectName(u"tab_first")
        self.verticalLayout_9 = QVBoxLayout(self.tab_first)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frm_top = QFrame(self.tab_first)
        self.frm_top.setObjectName(u"frm_top")
        self.frm_top.setMinimumSize(QSize(0, 37))
        self.frm_top.setMaximumSize(QSize(16777215, 37))
        self.horizontalLayout_8 = QHBoxLayout(self.frm_top)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer = QSpacerItem(298, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frm_top)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.pushButton_4 = QPushButton(self.frm_top)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon = QIcon()
        icon.addFile(u":/icons/reload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(25, 25))
        self.pushButton_4.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_4)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_3)


        self.verticalLayout_9.addWidget(self.frm_top)

        self.frm_body = QFrame(self.tab_first)
        self.frm_body.setObjectName(u"frm_body")
        self.frm_body.setEnabled(False)
        self.frm_body.setFrameShape(QFrame.StyledPanel)
        self.frm_body.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frm_body)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 10, 401, 170))
        self.verticalLayout_12 = QVBoxLayout(self.widget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_10.addWidget(self.label_6)

        self.text_user = QLineEdit(self.widget)
        self.text_user.setObjectName(u"text_user")

        self.verticalLayout_10.addWidget(self.text_user)


        self.horizontalLayout_2.addLayout(self.verticalLayout_10)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_13.addWidget(self.label_8)

        self.text_password = QLineEdit(self.widget)
        self.text_password.setObjectName(u"text_password")
        self.text_password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_13.addWidget(self.text_password)


        self.horizontalLayout_2.addLayout(self.verticalLayout_13)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_11.addWidget(self.label_7)

        self.text_host = QLineEdit(self.widget)
        self.text_host.setObjectName(u"text_host")

        self.verticalLayout_11.addWidget(self.text_host)


        self.horizontalLayout_4.addLayout(self.verticalLayout_11)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_14.addWidget(self.label_9)

        self.text_port = QLineEdit(self.widget)
        self.text_port.setObjectName(u"text_port")

        self.verticalLayout_14.addWidget(self.text_port)


        self.horizontalLayout_4.addLayout(self.verticalLayout_14)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, -1, 0)
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_4.addWidget(self.label_10)

        self.text_port_local = QLineEdit(self.widget)
        self.text_port_local.setObjectName(u"text_port_local")
        self.text_port_local.setMaximumSize(QSize(1600, 20))
        self.text_port_local.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.text_port_local)


        self.horizontalLayout_9.addLayout(self.verticalLayout_4)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_19.addWidget(self.label_12)

        self.text_p = QLineEdit(self.widget)
        self.text_p.setObjectName(u"text_p")

        self.verticalLayout_19.addWidget(self.text_p)


        self.horizontalLayout_9.addLayout(self.verticalLayout_19)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)


        self.verticalLayout_12.addLayout(self.verticalLayout_5)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.checkbox_debug = QCheckBox(self.widget)
        self.checkbox_debug.setObjectName(u"checkbox_debug")

        self.horizontalLayout_10.addWidget(self.checkbox_debug)

        self.checkbox_grava_log = QCheckBox(self.widget)
        self.checkbox_grava_log.setObjectName(u"checkbox_grava_log")

        self.horizontalLayout_10.addWidget(self.checkbox_grava_log)


        self.verticalLayout_12.addLayout(self.horizontalLayout_10)


        self.verticalLayout_9.addWidget(self.frm_body)

        self.tab_body.addTab(self.tab_first, "")
        self.tab_path_app = QWidget()
        self.tab_path_app.setObjectName(u"tab_path_app")
        self.frm_path = QFrame(self.tab_path_app)
        self.frm_path.setObjectName(u"frm_path")
        self.frm_path.setEnabled(False)
        self.frm_path.setGeometry(QRect(9, 9, 441, 201))
        self.frm_path.setFrameShape(QFrame.StyledPanel)
        self.frm_path.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frm_path)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.frm_path)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.text_path_teamviewer = QLineEdit(self.frm_path)
        self.text_path_teamviewer.setObjectName(u"text_path_teamviewer")
        self.text_path_teamviewer.setClearButtonEnabled(True)

        self.horizontalLayout_5.addWidget(self.text_path_teamviewer)

        self.tool_path_teamviewer = QToolButton(self.frm_path)
        self.tool_path_teamviewer.setObjectName(u"tool_path_teamviewer")

        self.horizontalLayout_5.addWidget(self.tool_path_teamviewer)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout_15.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_4 = QLabel(self.frm_path)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_7.addWidget(self.label_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.text_path_qsconnect = QLineEdit(self.frm_path)
        self.text_path_qsconnect.setObjectName(u"text_path_qsconnect")
        self.text_path_qsconnect.setClearButtonEnabled(True)

        self.horizontalLayout_6.addWidget(self.text_path_qsconnect)

        self.tool_path_qsconnect = QToolButton(self.frm_path)
        self.tool_path_qsconnect.setObjectName(u"tool_path_qsconnect")

        self.horizontalLayout_6.addWidget(self.tool_path_qsconnect)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)


        self.verticalLayout_15.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_5 = QLabel(self.frm_path)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_8.addWidget(self.label_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.text_path_anydesk = QLineEdit(self.frm_path)
        self.text_path_anydesk.setObjectName(u"text_path_anydesk")
        self.text_path_anydesk.setClearButtonEnabled(True)

        self.horizontalLayout_7.addWidget(self.text_path_anydesk)

        self.tool_path_anydesk = QToolButton(self.frm_path)
        self.tool_path_anydesk.setObjectName(u"tool_path_anydesk")

        self.horizontalLayout_7.addWidget(self.tool_path_anydesk)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)


        self.verticalLayout_15.addLayout(self.verticalLayout_8)


        self.verticalLayout_17.addLayout(self.verticalLayout_15)

        self.tab_body.addTab(self.tab_path_app, "")

        self.verticalLayout_2.addWidget(self.tab_body)

        self.frame_2 = QFrame(mnConfig)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(1600, 45))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bnt_edit = QPushButton(self.frame_2)
        self.bnt_edit.setObjectName(u"bnt_edit")
        icon1 = QIcon()
        icon1.addFile(u":/icons/pencil.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_edit.setIcon(icon1)

        self.horizontalLayout.addWidget(self.bnt_edit)

        self.bnt_save = QPushButton(self.frame_2)
        self.bnt_save.setObjectName(u"bnt_save")
        self.bnt_save.setEnabled(False)
        icon2 = QIcon()
        icon2.addFile(u":/icons/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_save.setIcon(icon2)

        self.horizontalLayout.addWidget(self.bnt_save)

        self.bnt_cancel = QPushButton(self.frame_2)
        self.bnt_cancel.setObjectName(u"bnt_cancel")
        icon3 = QIcon()
        icon3.addFile(u":/icons/error.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_cancel.setIcon(icon3)

        self.horizontalLayout.addWidget(self.bnt_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

#if QT_CONFIG(shortcut)
        self.label_6.setBuddy(self.text_user)
        self.label_8.setBuddy(self.text_password)
        self.label_7.setBuddy(self.text_host)
        self.label_9.setBuddy(self.text_port)
        self.label_10.setBuddy(self.text_port_local)
        self.label_12.setBuddy(self.text_p)
        self.label_3.setBuddy(self.text_path_teamviewer)
        self.label_4.setBuddy(self.text_path_qsconnect)
        self.label_5.setBuddy(self.text_path_anydesk)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.text_user, self.text_password)
        QWidget.setTabOrder(self.text_password, self.text_host)
        QWidget.setTabOrder(self.text_host, self.text_port)
        QWidget.setTabOrder(self.text_port, self.text_port_local)
        QWidget.setTabOrder(self.text_port_local, self.text_p)
        QWidget.setTabOrder(self.text_p, self.checkbox_debug)
        QWidget.setTabOrder(self.checkbox_debug, self.bnt_edit)
        QWidget.setTabOrder(self.bnt_edit, self.bnt_save)
        QWidget.setTabOrder(self.bnt_save, self.bnt_cancel)
        QWidget.setTabOrder(self.bnt_cancel, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.text_path_teamviewer)
        QWidget.setTabOrder(self.text_path_teamviewer, self.tool_path_teamviewer)
        QWidget.setTabOrder(self.tool_path_teamviewer, self.text_path_qsconnect)
        QWidget.setTabOrder(self.text_path_qsconnect, self.tool_path_qsconnect)
        QWidget.setTabOrder(self.tool_path_qsconnect, self.text_path_anydesk)
        QWidget.setTabOrder(self.text_path_anydesk, self.tool_path_anydesk)
        QWidget.setTabOrder(self.tool_path_anydesk, self.tab_body)

        self.retranslateUi(mnConfig)

        self.tab_body.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mnConfig)
    # setupUi

    def retranslateUi(self, mnConfig):
        mnConfig.setWindowTitle(QCoreApplication.translate("mnConfig", u"Form", None))
        self.label.setText(QCoreApplication.translate("mnConfig", u".......................................Arquivo de Configura\u00e7\u00e3o................................................", None))
        self.label_2.setText(QCoreApplication.translate("mnConfig", u"Testar:", None))
        self.pushButton_4.setText("")
        self.label_6.setText(QCoreApplication.translate("mnConfig", u"Usu\u00e1rio :", None))
        self.label_8.setText(QCoreApplication.translate("mnConfig", u"Senha :", None))
        self.label_7.setText(QCoreApplication.translate("mnConfig", u"Host Web :", None))
        self.label_9.setText(QCoreApplication.translate("mnConfig", u"Porta Web :", None))
        self.label_10.setText(QCoreApplication.translate("mnConfig", u"Porta Local : ", None))
        self.label_12.setText(QCoreApplication.translate("mnConfig", u"Time Notifica\u00e7\u00e3o :", None))
        self.checkbox_debug.setText(QCoreApplication.translate("mnConfig", u"Mode Debug.", None))
        self.checkbox_grava_log.setText(QCoreApplication.translate("mnConfig", u"Gravar Log.", None))
        self.tab_body.setTabText(self.tab_body.indexOf(self.tab_first), QCoreApplication.translate("mnConfig", u"Principal", None))
        self.label_3.setText(QCoreApplication.translate("mnConfig", u"Team Viewer:", None))
        self.tool_path_teamviewer.setText(QCoreApplication.translate("mnConfig", u"...", None))
        self.label_4.setText(QCoreApplication.translate("mnConfig", u"QSConect :", None))
        self.tool_path_qsconnect.setText(QCoreApplication.translate("mnConfig", u"...", None))
        self.label_5.setText(QCoreApplication.translate("mnConfig", u"AnyDesk :", None))
        self.tool_path_anydesk.setText(QCoreApplication.translate("mnConfig", u"...", None))
        self.tab_body.setTabText(self.tab_body.indexOf(self.tab_path_app), QCoreApplication.translate("mnConfig", u"Caminho", None))
        self.bnt_edit.setText(QCoreApplication.translate("mnConfig", u"Alterar", None))
#if QT_CONFIG(shortcut)
        self.bnt_edit.setShortcut(QCoreApplication.translate("mnConfig", u"Alt+A", None))
#endif // QT_CONFIG(shortcut)
        self.bnt_save.setText(QCoreApplication.translate("mnConfig", u"Salvar", None))
#if QT_CONFIG(shortcut)
        self.bnt_save.setShortcut(QCoreApplication.translate("mnConfig", u"Alt+S", None))
#endif // QT_CONFIG(shortcut)
        self.bnt_cancel.setText(QCoreApplication.translate("mnConfig", u"Cancelar", None))
#if QT_CONFIG(shortcut)
        self.bnt_cancel.setShortcut(QCoreApplication.translate("mnConfig", u"Alt+C", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

