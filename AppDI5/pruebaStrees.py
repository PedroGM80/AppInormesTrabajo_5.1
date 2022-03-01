
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
            result_b.lineEditFilter.setText("Test nombre insert "+str(i))
            result_b.filterTable
        print("1000 query ok")
if __name__ == '__main__':
    unittest.main()