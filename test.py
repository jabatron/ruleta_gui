# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTableView, QVBoxLayout, QWidget)

import whatsapp as w
from datetime import datetime
from openpyxl import load_workbook
from openpyxl.styles import colors
from openpyxl.styles import Font, Color
from time import time
from time import sleep
import gspread
import re
import os.path
import sys



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # if not self.objectName():
        #     self.setObjectName(u"self")
        self.resize(722, 600)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")

        self.widget_fuente = QWidget(self.centralwidget)
        self.widget_fuente.setObjectName(u"widget_fuente")
        self.widget_fuente.setGeometry(QRect(30, 20, 621, 111))
        self.radioExcel = QRadioButton(self.widget_fuente)
        self.radioExcel.setObjectName(u"radioExcel")
        self.radioExcel.setGeometry(QRect(0, 13, 76, 20))
        self.radioExcel.toggled.connect(self.update_radio)

        self.radioGS = QRadioButton(self.widget_fuente)
        self.radioGS.setObjectName(u"radioGS")
        self.radioGS.setGeometry(QRect(0, 63, 124, 20))
        self.radioGS.toggled.connect(self.update_radio)
        self.label_url_gs = QLabel(self.widget_fuente)
        self.label_url_gs.setObjectName(u"label_url_gs")
        self.label_url_gs.setGeometry(QRect(0, 89, 651, 16))
        self.bt_sel_excel = QPushButton(self.widget_fuente)
        self.bt_sel_excel.setObjectName(u"bt_sel_excel")
        self.bt_sel_excel.setGeometry(QRect(79, 11, 75, 24))
        self.label_file_excel = QLabel(self.widget_fuente)
        self.label_file_excel.setObjectName(u"label_file_excel")
        self.label_file_excel.setGeometry(QRect(0, 41, 321, 16))

        self.widget_tipo = QWidget(self.centralwidget)
        self.widget_tipo.setObjectName(u"widget_tipo")
        self.widget_tipo.setGeometry(QRect(350, 20, 141, 80))
        self.layoutWidget = QWidget(self.widget_tipo)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(13, 10, 121, 48))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.cb_enviar_mensaje = QCheckBox(self.layoutWidget)
        self.cb_enviar_mensaje.setObjectName(u"cb_enviar_mensaje")

        self.verticalLayout.addWidget(self.cb_enviar_mensaje)

        self.cb_enviar_fichero = QCheckBox(self.layoutWidget)
        self.cb_enviar_fichero.setObjectName(u"cb_enviar_fichero")

        self.verticalLayout.addWidget(self.cb_enviar_fichero)

        self.enviar_mensajes = QPushButton(self.centralwidget)
        self.enviar_mensajes.setObjectName(u"enviar_mensajes")
        self.enviar_mensajes.setGeometry(QRect(30, 150, 75, 24))
        self.enviar_mensajes.setEnabled(False)
        self.dryrun = QCheckBox(self.centralwidget)
        self.dryrun.setObjectName(u"dryrun")
        self.dryrun.setGeometry(QRect(120, 150, 151, 21))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(490, 30, 191, 31))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget1 = QWidget(self.frame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 0, 181, 24))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_qsoy = QLabel(self.layoutWidget1)
        self.label_qsoy.setObjectName(u"label_qsoy")

        self.horizontalLayout.addWidget(self.label_qsoy)

        self.line_quien_soy = QLineEdit(self.layoutWidget1)
        self.line_quien_soy.setObjectName(u"line_quien_soy")

        self.horizontalLayout.addWidget(self.line_quien_soy)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(30, 190, 661, 371))
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.radioExcel.setText(QCoreApplication.translate("MainWindow", u"Usar Excel", None))
        self.radioGS.setText(QCoreApplication.translate("MainWindow", u"Usar Google Sheets", None))
        self.label_url_gs.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.bt_sel_excel.setText(QCoreApplication.translate("MainWindow", u"Seleccionar", None))
        self.label_file_excel.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.cb_enviar_mensaje.setText(QCoreApplication.translate("MainWindow", u"Enviar mensaje", None))
        self.cb_enviar_fichero.setText(QCoreApplication.translate("MainWindow", u"Enviar fichero", None))
        self.enviar_mensajes.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.dryrun.setText(QCoreApplication.translate("MainWindow", u"Solo probar/ NO enviar", None))
        self.label_qsoy.setText(QCoreApplication.translate("MainWindow", u"Quien Soy:", None))


        self.excel_file = ''
        self.gs_key = ''
        self.type = ''
        self.show()

    def update_radio(self):
        if self.sender().isChecked():
            print (self.sender().name())    






if __name__ == "__main__":

    app = QApplication(sys.argv)
    #app.setStyle('Fusion')

    windowes = MainWindow()


    app.exec()