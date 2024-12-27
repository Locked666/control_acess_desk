# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mnConfig.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
    QVBoxLayout, QWidget)
import icons

class Ui_mnConfig(object):
    def setupUi(self, mnConfig):
        if not mnConfig.objectName():
            mnConfig.setObjectName(u"mnConfig")
        mnConfig.resize(372, 359)
        mnConfig.setMinimumSize(QSize(338, 279))
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

        self.frm_body = QFrame(mnConfig)
        self.frm_body.setObjectName(u"frm_body")
        self.frm_body.setEnabled(False)
        self.frm_body.setMaximumSize(QSize(301, 191))
        self.frm_body.setFrameShape(QFrame.StyledPanel)
        self.frm_body.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frm_body)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(200, 1, 80, 35))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.pushButton_4 = QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon = QIcon()
        icon.addFile(u":/icons/reload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(25, 25))
        self.pushButton_4.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.widget = QWidget(self.frm_body)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(11, 42, 284, 148))
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_10.addWidget(self.label_6)

        self.text_user = QLineEdit(self.widget)
        self.text_user.setObjectName(u"text_user")

        self.verticalLayout_10.addWidget(self.text_user)


        self.verticalLayout_9.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_11.addWidget(self.label_7)

        self.text_host = QLineEdit(self.widget)
        self.text_host.setObjectName(u"text_host")

        self.verticalLayout_11.addWidget(self.text_host)


        self.verticalLayout_9.addLayout(self.verticalLayout_11)


        self.horizontalLayout_4.addLayout(self.verticalLayout_9)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_13.addWidget(self.label_8)

        self.text_password = QLineEdit(self.widget)
        self.text_password.setObjectName(u"text_password")
        self.text_password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_13.addWidget(self.text_password)


        self.verticalLayout_12.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_14.addWidget(self.label_9)

        self.text_port = QLineEdit(self.widget)
        self.text_port.setObjectName(u"text_port")

        self.verticalLayout_14.addWidget(self.text_port)


        self.verticalLayout_12.addLayout(self.verticalLayout_14)


        self.horizontalLayout_4.addLayout(self.verticalLayout_12)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkbox_debug = QCheckBox(self.widget)
        self.checkbox_debug.setObjectName(u"checkbox_debug")

        self.horizontalLayout_2.addWidget(self.checkbox_debug)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, -1, -1, 6)
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_4.addWidget(self.label_10)

        self.text_port_local = QLineEdit(self.widget)
        self.text_port_local.setObjectName(u"text_port_local")
        self.text_port_local.setMaximumSize(QSize(133, 20))
        self.text_port_local.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.text_port_local)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.frm_body)

        self.frame_2 = QFrame(mnConfig)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(331, 45))
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
        self.label_2.setBuddy(self.pushButton_4)
        self.label_6.setBuddy(self.text_user)
        self.label_7.setBuddy(self.text_host)
        self.label_8.setBuddy(self.text_password)
        self.label_9.setBuddy(self.text_port)
        self.label_10.setBuddy(self.text_port)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.text_user, self.text_password)
        QWidget.setTabOrder(self.text_password, self.text_host)
        QWidget.setTabOrder(self.text_host, self.text_port)
        QWidget.setTabOrder(self.text_port, self.checkbox_debug)
        QWidget.setTabOrder(self.checkbox_debug, self.bnt_edit)
        QWidget.setTabOrder(self.bnt_edit, self.bnt_cancel)
        QWidget.setTabOrder(self.bnt_cancel, self.bnt_save)

        self.retranslateUi(mnConfig)
        self.text_user.returnPressed.connect(self.text_password.setFocus)
        self.text_password.returnPressed.connect(self.text_host.setFocus)
        self.text_host.returnPressed.connect(self.text_port.setFocus)
        self.text_port.returnPressed.connect(self.checkbox_debug.setFocus)

        QMetaObject.connectSlotsByName(mnConfig)
    # setupUi

    def retranslateUi(self, mnConfig):
        mnConfig.setWindowTitle(QCoreApplication.translate("mnConfig", u"Form", None))
        self.label.setText(QCoreApplication.translate("mnConfig", u"........................Arquivo de Configura\u00e7\u00e3o...............................", None))
        self.label_2.setText(QCoreApplication.translate("mnConfig", u"Testar:", None))
        self.pushButton_4.setText("")
        self.label_6.setText(QCoreApplication.translate("mnConfig", u"Usu\u00e1rio :", None))
        self.label_7.setText(QCoreApplication.translate("mnConfig", u"Host Web :", None))
        self.label_8.setText(QCoreApplication.translate("mnConfig", u"Senha :", None))
        self.label_9.setText(QCoreApplication.translate("mnConfig", u"Porta Web :", None))
        self.checkbox_debug.setText(QCoreApplication.translate("mnConfig", u"Mode Debug.", None))
        self.label_10.setText(QCoreApplication.translate("mnConfig", u"Porta Local : ", None))
        self.bnt_edit.setText(QCoreApplication.translate("mnConfig", u"Alterar", None))
#if QT_CONFIG(shortcut)
        self.bnt_edit.setShortcut(QCoreApplication.translate("mnConfig", u"Alt+E", None))
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

