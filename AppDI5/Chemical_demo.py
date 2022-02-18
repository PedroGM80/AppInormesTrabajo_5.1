import sys
from ast import Lambda
from datetime import date
from pickle import TRUE
from tkinter import Button, Spinbox
from pathlib import Path
import sys, os
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings
import numpy as np
import pyperclip
import pyqtgraph as pg
import pyqtgraph.exporters
from mongita import MongitaClientDisk
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from pyqtgraph.Qt import QtGui
from PySide6.QtGui import QPixmap,QIcon
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox,
                               QComboBox, QHBoxLayout, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QSpinBox,
                               QTableWidgetItem, QVBoxLayout, QWizard,
                               QWizardPage)
from reportlab.pdfgen.canvas import Canvas
from Chemical import Ui_MainWindow

basedir = os.path.dirname(__file__)
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Dato1f1 = ''
        self.Dato4f1 = ''
        self.Dato5f1 = ''
        self.Dato1f2 = ''
        self.Dato4f2 = ''
        self.Dato5f2 = ''
        client = MongitaClientDisk()
        my_db = client.b_db
        self.a_collection = my_db.new_collection
        self.actionPaste.triggered.connect(self.pasteClipboard)
        self.actionCopy.triggered.connect(self.copyClipboard)
        self.actionCut.triggered.connect(self.cutClipboard)
        self.actionHelp.triggered.connect(self.showHelp)
        self.ButtonInsert.clicked.connect(self.insertData)
        self.ButtonRemove.clicked.connect(self.removeData)
        self.ButtonRemove.enterEvent = lambda event: self.otherHide()
        self.ButtonRemove.leaveEvent = lambda event: self.otherShow()
        self.ButtonReplace.clicked.connect(self.updateData)
        self.ButtonFilterInfo.clicked.connect(self.filterTable)
        self.tableEdit.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Wizar
        self.wizard = QWizard()
        next = self.wizard.button(QWizard.NextButton)
        self.buttoMakeInfo.clicked.connect(self.newWizard)
        self.wizard.setWizardStyle(QWizard.ModernStyle)
        self.wizard.setPixmap(QWizard.WatermarkPixmap, QPixmap('Watermark.png'))
        self.wizard.setPixmap(QWizard.LogoPixmap, QPixmap('Logo.png'))
        self.wizard.setPixmap(QWizard.BannerPixmap, QPixmap('Banner.png'))
        page1 = QWizardPage()
        page1.setTitle('Identificación del usuario')
        page1.setSubTitle('Introduzaca su nombre completo')
        lineEdit = QLineEdit()
        label = QLabel()
        label.setText('Nombre completo:')
        hLayout1 = QHBoxLayout(page1)
        hLayout1.addWidget(label)
        hLayout1.addWidget(lineEdit)
        page1.registerField('nombre*', lineEdit, lineEdit.text(), 'textChanged')
        self.wizard.addPage(page1)

        page2 = QWizardPage()
        page2.setTitle('Generación del identificador')
        page2.setSubTitle('Genere su identificador')
        next.clicked.connect(lambda: page2.setSubTitle(page1.field('nombre') + ' genere su identificador'))
        next.clicked.connect(lambda: self.asignaNombre(page1.field('nombre')))

        self.spin = QSpinBox()
        self.check_box = QCheckBox()
        self.combo = QComboBox()
        self.combo.addItem('A')
        self.combo.addItem('B')
        self.combo.addItem('C')
        self.spin.setMaximum(9)
        self.spin.setMinimum(0)
        label1 = QLabel()
        label2 = QLabel()
        label1.setText('Letra de id: ')
        label2.setText('Número de id: ')
        hLayout2 = QHBoxLayout(page2)
        hLayout2.addWidget(label1)
        hLayout2.addWidget(self.spin)
        hLayout2.addWidget(label2)
        hLayout2.addWidget(self.combo)
        self.wizard.addPage(page2)

        page3 = QWizardPage()
        page3.setTitle('Verificación del idntificador')
        page3.setSubTitle('Verifique su id')
        label3 = QLabel()
        next.clicked.connect(lambda: label3.setText(' Su Id generada es: ' + self.combo.currentText() + '-' + str(
            self.spin.value()) + '   ¿Valores correctos?'))
        next.clicked.connect(lambda: self.setID())
        dateTimeObj = date.today()
        timestampStr = dateTimeObj.strftime('%d-%b-%Y')
        self.fechaFin = timestampStr
        hLayout3 = QHBoxLayout(page3)
        hLayout3.addWidget(label3)
        hLayout3.addWidget(self.check_box)
        self.check_box.mousePressEvent = lambda event: self.conectar()
        self.lineEdit_check = QLineEdit()
        hLayout3.addWidget(self.lineEdit_check)
        self.lineEdit_check.hide()
        page3.registerField('campo_check*', self.lineEdit_check)
        self.wizard.addPage(page3)

        page4 = QWizardPage()
        page4.setTitle('Generar informe')
        page4.setSubTitle('Terminando el proceso')
        label4 = QLabel()
        self.label5 = QLabel()
        button4 = QPushButton('Generar Informe')
        label4.setText('Muchas gracias por su colaboración')
        self.label5.setText('')
        hLayout4 = QVBoxLayout(page4)
        hLayout4.addWidget(label4)
        hLayout4.addWidget(self.label5)
        hLayout4.addWidget(button4)
        page4.setFinalPage(True)
        button4.mousePressEvent = lambda event: self.generaInforme()
        finish = self.wizard.button(QWizard.FinishButton)
        self.wizard.addPage(page4)

        self.updateTable()

    def setID(self):
        item_select = self.combo.currentText()
        spin_selected = self.spin.value()
        self.idFin = item_select + '-' + str(spin_selected)

    def asignaNombre(self, nombre):
        self.nombreFin = nombre

    def generaInforme(self):
        outfile = 'informe.pdf'
        template = PdfReader('template.pdf', decompress=False).pages[0]
        template_obj = pagexobj(template)
        canvas = Canvas(outfile)
        xobj_name = makerl(canvas, template_obj)
        canvas.doForm(xobj_name)
        # A4 595 x 842 px
        self.formula_filtradaA = self.lineEditInfo1.text()
        self.formula_filtradaB = self.lineEditInfo2.text()
        numCF1 = self.count_char(self.formula_filtradaA, 'C')
        numHF1 = self.count_char(self.formula_filtradaA, 'H')
        numCF2 = self.count_char(self.formula_filtradaB, 'C')
        numHF2 = self.count_char(self.formula_filtradaB, 'H')
        self.y1 = [numCF1]
        self.y2 = [numHF1]
        self.y1B = [numCF2]
        self.y2B = [numHF2]
        self.masa_molar_f1 = (numCF1 * 4) + numHF1
        self.masa_molar_f2 = (numCF2 * 4) + numHF2

        canvas.drawString(318, 660, self.idFin)
        canvas.drawString(170, 603, self.nombreFin)
        canvas.drawString(110, 632, self.fechaFin)
        canvas.drawString(50, 520, self.textEdit.toPlainText())

        canvas.drawString(355, 418, self.Dato1f1)
        canvas.drawString(400, 391, self.lineEditInfo1.text())
        canvas.drawString(375, 364, str(self.masa_molar_f1))
        canvas.drawString(340, 336, self.Dato4f1)
        canvas.drawString(410, 310, self.Dato5f1)

        canvas.drawString(355, 273, self.Dato1f2)
        canvas.drawString(400, 245, self.lineEditInfo2.text())
        canvas.drawString(375, 218, str(self.masa_molar_f2))
        canvas.drawString(340, 192, self.Dato4f2)
        canvas.drawString(410, 164, self.Dato5f2)
        canvas.save()
        # GRAFICAS###############################################
        win = pg.plot()
        win2 = pg.plot()
        win.setWindowTitle('Azul Hidrogeno Rojo Carbono')
        win2.setWindowTitle('Azul Hidrogeno Rojo Carbono')

        fn = QtGui.QFont()
        fn.setPointSize(15)
        win.getAxis('bottom').setTickFont(fn)
        win.getAxis('left').setTickFont(fn)
        win2.getAxis('bottom').setTickFont(fn)
        win2.getAxis('left').setTickFont(fn)
        x = np.arange(1)
        bg1 = pg.BarGraphItem(x=x, height=self.y1, width=0.6, brush='r')
        bg2 = pg.BarGraphItem(x=x + 2, height=self.y2, width=0.6, brush='b')
        win.addItem(bg1)
        win.addItem(bg2)
        bg1B = pg.BarGraphItem(x=x, height=self.y1B, width=0.6, brush='r')
        bg2B = pg.BarGraphItem(x=x + 2, height=self.y2B, width=0.6, brush='b')
        win2.addItem(bg1B)
        win2.addItem(bg2B)
        plt = win
        pltB = win2

        exporter = pg.exporters.ImageExporter(plt.plotItem)
        exporterB = pg.exporters.ImageExporter(pltB.plotItem)

        exporter.parameters()['width'] = 170
        exporterB.parameters()['width'] = 170
        exporter.export('graphic.png')
        exporterB.export('graphicB.png')
        outfile = 'informe.pdf'
        template = PdfReader('informe.pdf', decompress=False).pages[0]
        template_obj = pagexobj(template)
        canvas = Canvas(outfile)
        xobj_name = makerl(canvas, template_obj)
        canvas.doForm(xobj_name)
        canvas.drawImage('graphic.png', 50, 300, width=None, height=None, mask=None)
        canvas.drawImage('graphicB.png', 50, 160, width=None, height=None, mask=None)

        canvas.save()
        self.label5.setText('Informe generado con éxito')
        win.close()
        win2.close()

        self.setWindowTitle('Mi informe')
        self.web = QWebEngineView()
        self.web.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.setWindowTitle('Informe')
        self.web = QWebEngineView()
        self.web.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        ruta = Path('informe.pdf')
        ruta.absolute().as_uri()
        self.web.load(QUrl(ruta.absolute().as_uri()))
        self.setCentralWidget(self.web)
        self.setCentralWidget(self.web)
        self.showMaximized()
    def count_char(self, formula, char):
        longitud = len(formula)
        count = 0
        for i in range(longitud):
            if (formula[i] == char):
                if (formula[i + 1].isdigit() and (i + 1) != longitud):
                    count = count + int(formula[i + 1])
                else:
                    count = count + 1
        return count

    def conectar(self):
        if (self.check_box.checkState() == False):
            self.check_box.setChecked(True)
            self.lineEdit_check.setText('ok')
        else:
            self.check_box.setChecked(False)
            self.lineEdit_check.setText('')

    def otherHide(self):
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.lineEdit_4.hide()
        self.label_field2.hide()
        self.label_field3.hide()
        self.label_field4.setText('')

    def otherShow(self):
        self.lineEdit_2.show()
        self.label_field2.show()
        self.lineEdit_3.show()
        self.label_field3.show()
        self.lineEdit_4.show()
        self.label_field4.setText('Tipo: ')

    def getFocus(self):
        if (self.lineEdit_1.hasFocus() == True):
            return self.lineEdit_1
        if (self.lineEdit_2.hasFocus() == True):
            return self.lineEdit_2
        if (self.lineEdit_3.hasFocus() == True):
            return self.lineEdit_3
        if (self.lineEdit_4.hasFocus() == True):
            return self.lineEdit_4
        if (self.lineEditFilter.hasFocus() == True):
            return self.lineEditFilter
        if (self.lineEditInfo1.hasFocus() == True):
            return self.lineEditInfo1
        if (self.lineEditInfo2.hasFocus() == True):
            return self.lineEditInfo2

    def copyClipboard(self):
        lineEditFocus = self.getFocus()
        text = lineEditFocus.text()
        textCopyOK = pyperclip.copy(text)

    def cutClipboard(self):
        lineEditFocus = self.getFocus()
        text = lineEditFocus.text()
        textCopyOK = pyperclip.copy(text)
        lineEditFocus.setText('')

    def pasteClipboard(self):
        lineEditFocus = self.getFocus()
        lineEditFocus.setText(pyperclip.paste())

    def removeData(self):
        self.a_collection.delete_one({'_id': self.lineEdit_1.text()})
        self.updateTable()

    def newWizard(self):
        campo = str('Fórmula química')
        valor = self.lineEditInfo1.text()
        query = {campo: valor}
        valor2 = self.lineEditInfo2.text()
        query2 = {campo: valor2}
        try:
            for x in self.a_collection.find(query):
                for key, value in x.items():
                    if (key != '_id'):
                        if (key == 'Nombre'):
                            self.Dato1f1 = value
                        if (key == 'Tipo'):
                            self.Dato4f1 = value
                        if (key == 'Punto de ebullición'):
                            self.Dato5f1 = value
                for x in self.a_collection.find(query2):
                    for key, value in x.items():
                        if (key != '_id'):
                            if (key == 'Nombre'):
                                self.Dato1f2 = value
                            if (key == 'Tipo'):
                                self.Dato4f2 = value
                            if (key == 'Punto de ebullición'):
                                self.Dato5f2 = value
        except Exception as e:
            raise e

        self.wizard.activateWindow()
        self.wizard.raise_()
        self.wizard.show()
        self.showMinimized()

    def insertData(self):
        try:
            self.data_demo = {'_id': self.lineEdit_1.text(), 'Nombre': self.lineEdit_2.text(
            ), 'Fórmula química': self.lineEdit_1.text(), 'Punto de ebullición': self.lineEdit_3.text(),
                              'Tipo': self.lineEdit_4.text()}
            self.a_collection.insert_one(self.data_demo)
            self.updateTable()
        except:
            print('An exception occurred')

    def updateData(self):
        self.a_collection.update_one({'_id': self.lineEdit_1.text()}, {
            '$set': {'Nombre': self.lineEdit_2.text(), 'Fórmula química': self.lineEdit_1.text(),
                     'Punto de ebullición': self.lineEdit_3.text(), 'Tipo': self.lineEdit_4.text()}})
        self.updateTable()

    def updateTable(self):
        self.tableFilter.clearContents()
        self.tableEdit.clearContents()
        try:
            iter_length = len([i for i in self.a_collection.find()])
            self.tableEdit.setRowCount(iter_length)
            self.tableFilter.setRowCount(iter_length)
            fila = 0
            columna = 0
            for x in self.a_collection.find():
                for key, value in x.items():
                    if (key != '_id'):
                        self.tableEdit.setItem(
                            fila - 1, columna, QTableWidgetItem(value))
                        self.tableFilter.setItem(
                            fila - 1, columna, QTableWidgetItem(value))
                        columna += 1
                fila += 1
                columna = 0
        except Exception as e:
            raise e
    def showHelp(self):
        self.web = QWebEngineView()
        self.web.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        url = "https://pedrogm80.github.io/AppInormesTrabajo_5.1/"
        self.web.load(url)
        self.setCentralWidget(self.web)
    def filterTable(self):
        self.tableFilter.clearContents()
        fila = 0
        columna = 0
        campo = str(self.comboBoxFilter.currentText())
        valor = self.lineEditFilter.text()
        query = {campo: valor}
        try:
            iter_length = len([i for i in self.a_collection.find()])
            self.tableEdit.setRowCount(iter_length)
            self.tableFilter.setRowCount(iter_length)
            for x in self.a_collection.find(query):
                for key, value in x.items():
                    if (key != '_id'):
                        self.tableFilter.setItem(
                            fila, columna, QTableWidgetItem(value))
                        columna += 1
                fila += 1
                columna = 0
        except Exception as e:
            raise e


app = QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon('logo.ico'))
w = MainWindow()
w.show()
app.exec()
