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
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(722, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget_fuente = QWidget(self.centralwidget)
        self.widget_fuente.setObjectName(u"widget_fuente")
        self.widget_fuente.setGeometry(QRect(30, 20, 321, 111))
        self.radioExcel = QRadioButton(self.widget_fuente)
        self.radioExcel.setObjectName(u"radioExcel")
        self.radioExcel.setGeometry(QRect(0, 13, 76, 20))
        self.radioGS = QRadioButton(self.widget_fuente)
        self.radioGS.setObjectName(u"radioGS")
        self.radioGS.setGeometry(QRect(0, 63, 124, 20))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.radioExcel.setText(QCoreApplication.translate("MainWindow", u"Usar Excel", None))
        self.radioGS.setText(QCoreApplication.translate("MainWindow", u"Usar Google Sheets", None))
        self.label_url_gs.setText(QCoreApplication.translate("MainWindow", u"URL_GS", None))
        self.bt_sel_excel.setText(QCoreApplication.translate("MainWindow", u"Seleccionar", None))
        self.label_file_excel.setText(QCoreApplication.translate("MainWindow", u"ExcelFile", None))
        self.cb_enviar_mensaje.setText(QCoreApplication.translate("MainWindow", u"Enviar mensaje", None))
        self.cb_enviar_fichero.setText(QCoreApplication.translate("MainWindow", u"Enviar fichero", None))
        self.enviar_mensajes.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.dryrun.setText(QCoreApplication.translate("MainWindow", u"Solo probar/ NO enviar", None))
        self.label_qsoy.setText(QCoreApplication.translate("MainWindow", u"Quien Soy:", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Telefono", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Mensaje", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Fichero", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Estado", None));
    # retranslateUi

