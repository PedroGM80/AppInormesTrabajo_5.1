
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
    


    def test_injection(self):
        result_b =MainWindow()
        result_b.lineEdit_1.setText("$collection=find(array('username' = $_GET['username'],'passwd' = $_GET['passwd']));")
        result_b.lineEdit_2.setText("Test nombre insert ")
        result_b.lineEdit_3.setText("Test punto de ebullición insert ")
        result_b.lineEdit_4.setText("Test tipo insert ")
        result_b.insertData()
        
if __name__ == '__main__':
    unittest.main()