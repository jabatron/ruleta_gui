# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QThreadPool,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

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
import copy

rojo = "#b61827"
verde = "#5af466"
amarillo = "#fffecb"
azul = "#84b6f4"
fondo = "#abffff"

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
        self.radioExcel.toggled.connect(self.update_radio_excel)
        self.radioExcel.setEnabled(False)

        self.radioGS = QRadioButton(self.widget_fuente)
        self.radioGS.setObjectName(u"radioGS")
        self.radioGS.setGeometry(QRect(0, 63, 124, 20))
        self.radioGS.toggled.connect(self.update_radio_gs)
        self.label_url_gs = QLabel(self.widget_fuente)
        self.label_url_gs.setObjectName(u"label_url_gs")
        self.label_url_gs.setGeometry(QRect(0, 89, 651, 16))
        self.bt_sel_excel = QPushButton(self.widget_fuente)
        self.bt_sel_excel.setObjectName(u"bt_sel_excel")
        self.bt_sel_excel.setGeometry(QRect(79, 11, 75, 24))
        self.bt_sel_excel.setEnabled(False)

        self.label_file_excel = QLabel(self.widget_fuente)
        self.label_file_excel.setObjectName(u"label_file_excel")
        self.label_file_excel.setGeometry(QRect(0, 41, 321, 16))

        self.widget_tipo = QWidget(self.centralwidget)
        self.widget_tipo.setObjectName(u"widget_tipo")
        self.widget_tipo.setGeometry(QRect(350, 20, 241, 80))
        self.layoutWidget = QWidget(self.widget_tipo)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(13, 10, 221, 48))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.cb_enviar_mensaje = QCheckBox(self.layoutWidget)
        self.cb_enviar_mensaje.setObjectName(u"cb_enviar_mensaje")
        self.cb_enviar_mensaje.stateChanged.connect(self.enviar_mensaje)

        self.verticalLayout.addWidget(self.cb_enviar_mensaje)

        self.cb_enviar_fichero = QCheckBox(self.layoutWidget)
        self.cb_enviar_fichero.setObjectName(u"cb_enviar_fichero")
        self.cb_enviar_fichero.stateChanged.connect(self.enviar_fichero)

        self.verticalLayout.addWidget(self.cb_enviar_fichero)

        self.enviar_mensajes = QPushButton(self.centralwidget)
        self.enviar_mensajes.setObjectName(u"enviar_mensajes")
        self.enviar_mensajes.setGeometry(QRect(30, 150, 75, 24))
        self.enviar_mensajes.setEnabled(False)
        self.enviar_mensajes.clicked.connect(self.enviar_mensajes_clicked_thread)

        self.dryrun = QCheckBox(self.centralwidget)
        self.dryrun.setObjectName(u"dryrun")
        self.dryrun.setGeometry(QRect(120, 150, 151, 21))
        self.dryrun.setChecked(True)
        self.dryrun.stateChanged.connect(self.marcar_dryrun)

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

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 20):
            self.tableWidget.setRowCount(20)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 190, 661, 381))
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(155)
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Telefono", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Mensaje", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Fichero", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Estado", None));
   

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.setWindowTitle(QCoreApplication.translate("Enviator", u"Enviator", None))
        self.radioExcel.setText(QCoreApplication.translate("Enviator", u"Usar Excel", None))
        self.radioGS.setText(QCoreApplication.translate("Enviator", u"Usar Google Sheets", None))
        self.label_url_gs.setText(QCoreApplication.translate("Enviator", u"", None))
        self.bt_sel_excel.setText(QCoreApplication.translate("Enviator", u"Seleccionar", None))
        self.label_file_excel.setText(QCoreApplication.translate("Enviator", u"", None))
        self.cb_enviar_mensaje.setText(QCoreApplication.translate("Enviator", u"Enviar mensaje", None))
        self.cb_enviar_fichero.setText(QCoreApplication.translate("Enviator", u"Enviar imagen/video/fichero", None))
        self.enviar_mensajes.setText(QCoreApplication.translate("Enviator", u"Enviar", None))
        self.dryrun.setText(QCoreApplication.translate("Enviator", u"Solo probar/ NO enviar", None))
        self.label_qsoy.setText(QCoreApplication.translate("Enviator", u"Quien Soy:", None))


        self.excel_file = ''
        self.gs_key = ''
        self.type = ''
        self.mensaje = False
        self.fichero = False
        self.dryrun = True
        self.quiensoy = ''
        self.show()
        self.thread_manager = QThreadPool()

    def marcar_dryrun(self):
        if self.sender().isChecked():
            self.dryrun = True
        else:
            self.dryrun = False

    def enviar_mensaje(self):
        if self.sender().isChecked():
            self.mensaje = True
        else:
            self.mensaje = False
        self.check_enviar()

    def enviar_fichero(self):
        if self.sender().isChecked():
            self.fichero = True
        else:
            self.fichero = False
        self.check_enviar()

    def check_enviar(self):
        """ Activa o desactia el botón de enviar mensajes dependiendo de las opciones que hay activas """
        if self.type and (self.mensaje or self.fichero):
            self.enviar_mensajes.setEnabled(True)
        else:
            self.enviar_mensajes.setEnabled(False)


    def update_radio_excel(self):
        if self.sender().isChecked():
            self.label_file_excel.setText('abriendo fichero ...')
            self.type='Excel'
            self.check_enviar()
        else:
            self.label_file_excel.setText('')
            self.label_url_gs.setText('Espere ...')

    def leer_id_gs(self):
        self.statusbar.showMessage("Abriendo fichero ...")
        QCoreApplication.processEvents()
        self.gs_gc = gspread.service_account(filename="credentials/ruleta-gui-credentials.json")
        self.gs_key = open("credentials/key-mobiles.txt").read()
        try:
            self.worksheet = self.gs_gc.open_by_key(self.gs_key)
            self.sheet= self.worksheet.sheet1
        except:
            print ('Error con el fichero de Google Sheet')
            sys.exit()
        self.urlLink=f"<a href=\"{self.worksheet.url}\">{self.worksheet.url}</a>"
        # self.label_url_gs.setText(self.urlLink)
        self.label_url_gs.setOpenExternalLinks(True)

    def update_radio_gs(self):
        if self.sender().isChecked():
            if not self.gs_key:
                self.leer_id_gs()
                self.statusbar.clearMessage()
            self.label_url_gs.setText(self.urlLink)
            self.check_enviar()
            self.type="GS"
        else:
            self.label_url_gs.setText("")
    
    def enviar_google(self, messenger):
        self.enviar_mensajes.setEnabled(False)
        
        self.data = self.sheet.get_all_values()
        #Leer cabeceras que no necesitamos para nada 
        self.cabeceras = self.data.pop(0)

        self.llenar_tabla()

        font = QFont()

        for i, d in enumerate(self.data_to_table):
            numero, mensaje, fichero, qsoy, *_, gs_cell = d
            numero = '34' + numero
            pattern = re.compile("^34[67]\d{8}")
    
            if pattern.fullmatch(numero):    
                __qtablewidgetitem = QTableWidgetItem()
                __qtablewidgetitem.setFont(font)
                __qtablewidgetitem.setFlags(Qt.NoItemFlags)
                __qtablewidgetitem.setText(f"Enviando ...")
                self.tableWidget.setItem(i, 3, __qtablewidgetitem)
                self.tableWidget.item(i, 3).setBackground(QColor(amarillo))
                self.tableWidget.item(i, 3).setForeground(QColor(azul))
                QCoreApplication.processEvents()

                if self.mensaje:
                    #el mensaje va a enviarse
                    print (f'Enviando mensaje: -{mensaje}- al numero {numero}')
                 
                    if not self.dryrun:
                        messenger.find_user(numero)
                        messenger.send_message(mensaje)
                        self.tableWidget.item(i, 1).setForeground(QColor(verde))
                        QCoreApplication.processEvents()
                        self.sheet.update('G' + str(gs_cell), 'Mensaje Enviado')
                        self.sheet.format('G' + str(gs_cell), {"textFormat": {"foregroundColor": {"red": 0.0, "green": 75.0, "blue": 0.0}}})

                if self.fichero:
                    # comprobar si ha fichero para enviar y existe
                    # sacar tipo de fichero
                    # enviar segun tipo de fichero
                    if fichero and os.path.isfile(fichero): 
                        name, ext = os.path.splitext(fichero)
                        
                        if not self.dryrun:
                            messenger.find_user(numero)
                        
                        if ext.lower() in [".tiff", ".pjp", ".jfif", ".gif", ".svg", ".bmp", ".png", ".jpeg", ".svgz", ".jpg", ".webp", ".ico", ".xbm", ".dib", ".tif", ".pjpeg", ".avif", ".m4v", ".mp4", ".3gpp", ".mov"]:
                            if not self.dryrun:
                                messenger.send_picture(fichero)
                                self.sheet.update('H' + str(gs_cell), 'Imagen/Video Enviado')
                                self.sheet.format('H' + str(gs_cell), {"textFormat": {"foregroundColor": {"red": 0.0, "green": 75.0, "blue": 0.0}}})
                                self.tableWidget.item(i, 2).setForeground(QColor(verde))
                                QCoreApplication.processEvents()
                            print (f'Enviando imagen/video {fichero} al número: {numero}')
                        else:
                            if not self.dryrun:
                                messenger.send_file(fichero)
                                self.sheet.update('H' + str(gs_cell), 'Fichero Enviado')
                                self.sheet.format('H' + str(gs_cell), {"textFormat": {"foregroundColor": {"red": 0.0, "green": 75.0, "blue": 0.0}}})
                                self.tableWidget.item(i, 2).setForeground(QColor(verde))
                                QCoreApplication.processEvents()
                            print (f'Enviando fichero {fichero} al número: {numero}')
                    else:
                        if not self.dryrun:
                                self.tableWidget.item(i, 2).setForeground(QColor(rojo))
                                QCoreApplication.processEvents()
                        print (f'No hay fichero para enviar al numero {numero}')

                __qtablewidgetitem = QTableWidgetItem()
                __qtablewidgetitem.setFont(font)
                __qtablewidgetitem.setFlags(Qt.NoItemFlags)
                __qtablewidgetitem.setText(f"Enviado.")
                self.tableWidget.setItem(i, 3, __qtablewidgetitem)
                self.tableWidget.item(i, 3).setBackground(QColor(amarillo))
                self.tableWidget.item(i, 3).setForeground(QColor(verde))
                QCoreApplication.processEvents()
            else:
                if not self.dryrun and self.mensaje:
                    self.sheet.update('H' + str(gs_cell), 'No Enviado')
                    self.sheet.format('H' + str(gs_cell), {"textFormat": {"foregroundColor": {"red": 50.0, "green": 0.0, "blue": 0.0}}})
                    self.tableWidget.item(i, 1).setForeground(QColor(rojo))
                if not self.dryrun and self.fichero:
                    self.sheet.update('G' + str(gs_cell), 'No Enviado')
                    self.sheet.format('G' + str(gs_cell), {"textFormat": {"foregroundColor": {"red": 50.0, "green": 0.0, "blue": 0.0}}})
                    self.tableWidget.item(i, 2).setForeground(QColor(rojo))
                QCoreApplication.processEvents()
                print (f'el numero {numero} es incorrecto')


        self.enviar_mensajes.setEnabled(True)

    def enviar_excel(self):
        pass

    def enviar_mensajes_clicked(self):
        
        self.quiensoy = self.line_quien_soy.text()
        texto = f"El proceso {self.quiensoy} esta enviando mensajes"
        self.statusbar.showMessage(texto)
        QCoreApplication.processEvents()
        print (f"yo soy {self.quiensoy}")

        # leer datos del fichero
        self.data = self.sheet.get_all_values()
        #Leer cabeceras que no necesitamos para nada 
        self.cabeceras = self.data.pop(0)
        # print (self.cabeceras)
        # print (self.data)

        messenger = w.WhatsApp()
        t1 = time()
        print (f"Tipo: {self.type}")
        # Compruebo si leo los datos de Excel o de google.
        if self.type=="GS":
            self.enviar_google(messenger)
        else:
            self.enviar_xls(messenger)
        # Añado un delay para asegurarme que ee han enviado todos los mensajes    
        sleep(3)
        t2 = time()

        self.statusbar.showMessage(f'Envio finalizado. El proceso ha durado {t2-t1} segundos.')
        QCoreApplication.processEvents()
        print (f'El proceso ha durado {t2-t1} segundos.')
    
    def enviar_mensajes_clicked_thread(self):
        self.thread_manager.start(self.enviar_mensajes_clicked)

    def llenar_tabla(self):
        # duplico la tabla para poderla modificar
        rawdata = copy.deepcopy(self.data)

        # self.data_to_table = filter(lambda r: r[3] == self.quiensoy, self.rawdata)
        
        for i in range(len(rawdata)):
            rawdata[i].append(i+2)

        # Calcular tamaño de la tabla
        if self.quiensoy:
            self.data_to_table =[r for r in rawdata if r[3] == self.quiensoy]            
        else:
            self.data_to_table = rawdata

        items_tabla = len(self.data_to_table)

        self.tableWidget.setRowCount(items_tabla)

        for i in range (items_tabla):
            for j in range  (3):
                __qtablewidgetitem = QTableWidgetItem()
                # __qtablewidgetitem.setFont(font);
                __qtablewidgetitem.setFlags(Qt.NoItemFlags)
                __qtablewidgetitem.setText(self.data_to_table[i][j])
                self.tableWidget.setItem(i, j, __qtablewidgetitem)
            __qtablewidgetitem = QTableWidgetItem()
            # __qtablewidgetitem.setFont(font);
            __qtablewidgetitem.setFlags(Qt.NoItemFlags)
            __qtablewidgetitem.setText("Pendiente")
            self.tableWidget.setItem(i, 3, __qtablewidgetitem)
            
        
        header = self.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        QCoreApplication.processEvents()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    #app.setStyle('Fusion')

    windowes = MainWindow()


    app.exec()