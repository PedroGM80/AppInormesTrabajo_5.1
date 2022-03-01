
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
        for i in range(11):
            result_b.lineEdit_1.setText("CH"+str(i))
            result_b.lineEdit_2.setText("Test nombre insert "+str(i))
            result_b.lineEdit_3.setText("Test punto de ebullición insert "+str(i))
            result_b.lineEdit_4.setText("Test tipo insert "+str(i))
            result_b.insertData()
        print("1000 insert ok")
if __name__ == '__main__':
    unittest.main()