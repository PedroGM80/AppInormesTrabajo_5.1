

import sys
from tkinter import Widget
from types import NoneType
from typing import Any
from Chemical import Ui_MainWindow
import unittest
from PySide6.QtWidgets import QApplication, QWidget
from Animado import AnimatedButton
from PySide6.QtWidgets import QApplication
from Chemical_demo import MainWindow
from PySide6.QtWidgets import ( QApplication,QMainWindow)
class Testing(unittest.TestCase):
    

    def test_app(self):
        app = QApplication.instance()
        if app == None:
            app = QApplication([])
        result = MainWindow()
        self.assertTrue(result.make)

    def test_insert(self):
        result_b =MainWindow()
        result_b.lineEdit_1.setText("CH13")
        result_b.lineEdit_2.setText("Test nombre insert")
        result_b.lineEdit_3.setText("Test punto de ebullición insert")
        result_b.lineEdit_4.setText("Test tipo insert")
        #result_b.insertData()
        query={"_id": "CH13"}
        for x in result_b.a_collection.find(query):
                        for key, value in x.items():
                            if (key == '_id'):
                                campo1=value
                            if (key == 'Nombre'):
                                campo2 = value
                            if (key == 'Tipo'):
                                campo3= value
                            if (key == 'Punto de ebullición'):
                                campo4 = value
        #self.assertEqual("CH13"+"Test nombre insert"+"Test tipo insert"+"Test punto de ebullición insert",campo1+campo2+campo3+campo4)


    def test_update(self):
        result_c =MainWindow()
        result_c.lineEdit_1.setText("CH13")
        result_c.lineEdit_2.setText("Test nombre update")
        result_c.lineEdit_3.setText("Test punto de ebullición update")
        result_c.lineEdit_4.setText("Test tipo update")
        #result_c.updateData()
        query={"_id": "CH13"}
        for x in result_c.a_collection.find(query):
                        for key, value in x.items():
                            if (key == '_id'):
                                campo1=value
                            if (key == 'Nombre'):
                                campo2 = value
                            if (key == 'Tipo'):
                                campo3= value
                            if (key == 'Punto de ebullición'):
                                campo4 = value
        #self.assertEqual("CH13"+"Test nombre update"+"Test tipo update"+"Test punto de ebullición update",campo1+campo2+campo3+campo4)

    def test_del(self):
        result_d =MainWindow()
        result_d.lineEdit_1.setText("CH13")
        result_d.removeData()
        query={"_id": "CH13"}
        print(result_d.lineEdit_1.text())
        for x in result_d.a_collection.find(query):
                    for key, value in x.items():
                            if (key == '_id'):
                                campo1="empy"+value
                                self.assertEquals(campo1,"empy")
    def test_colorAnimacion(self):
       app=QApplication.instance()
       if app==None:
        app= QApplication([])
       window=QWidget()
       animado = AnimatedButton(color='blue')
       resultado = animado.pcolor
       self.assertEqual(resultado,'blue')

    def test_TextoBoton(self): 
        app=QApplication.instance()
        if app==None:
            app= QApplication([])
        window=QWidget()       
        animado = AnimatedButton(textoboton='Limpia')
        resultado= animado.ptexto
        self.assertEquals(resultado,'Limpia')
if __name__ == '__main__':
    unittest.main()