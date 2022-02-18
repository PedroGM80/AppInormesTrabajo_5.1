from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QAction, QCursor, QFont, QIcon)
from PySide6.QtWidgets import (QComboBox, QFormLayout, QGridLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy, QStatusBar,
                               QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
                               QToolBar, QVBoxLayout, QWidget)


import rc_icons
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(804, 648)
        MainWindow.setStyleSheet(u"background:#d3d3d3;")
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        icon = QIcon()
        icon.addFile(u":/icons/icons8-copiar-30.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.actionCopy.setIcon(icon)
        self.actionCut = QAction(MainWindow)
        self.actionCut.setObjectName(u"actionCut")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons8-cortar-24.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.actionCut.setIcon(icon1)
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons8-pegar-26.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.actionPaste.setIcon(icon2)
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setEnabled(True)#####

        self.actionHelp.setObjectName(u"actionHelp")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons8-acerca-de-32.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.actionHelp.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(30, 10, 741, 561))
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"background:grey;\n"
                                     "border:solid;\n"
                                     "border-width: 1px;border-radius: 20px; \n"
                                     "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.layoutWidget = QWidget(self.tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 681, 481))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.label_field1 = QLabel(self.layoutWidget)
        self.label_field1.setObjectName(u"label_field1")
        self.label_field1.setStyleSheet(u"    border-width: 0px;")
        self.label_field1.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_field1.setMargin(2)
        self.gridLayout.addWidget(self.label_field1, 0, 0, 1, 1)
        self.lineEdit_1 = QLineEdit(self.layoutWidget)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setStyleSheet(u"background:white;\n"
                                      "border-width: 2px;\n"
                                      "border-radius: 10px;\n"
                                      "")

        self.gridLayout.addWidget(self.lineEdit_1, 0, 1, 1, 1)
        self.label_field2 = QLabel(self.layoutWidget)
        self.label_field2.setObjectName(u"label_field2")
        self.label_field2.setStyleSheet(u"    border-width: 0px;")
        self.label_field2.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_field2.setMargin(2)
        self.gridLayout.addWidget(self.label_field2, 1, 0, 1, 1)
        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"background:white;\n"
                                      "border-width: 2px;\n"
                                      "border-radius: 10px;\n"
                                      "")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_field3 = QLabel(self.layoutWidget)
        self.label_field3.setObjectName(u"label_field3")
        self.label_field3.setStyleSheet(u"    border-width: 0px;")
        self.label_field3.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_field3.setMargin(2)
        self.gridLayout.addWidget(self.label_field3, 2, 0, 1, 1)
        self.lineEdit_3 = QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"background:white;\n"
                                      "border-width: 2px;\n"
                                      "border-radius: 10px;\n"
                                      "")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.label_field4 = QLabel(self.layoutWidget)
        self.label_field4.setObjectName(u"label_field4")
        self.label_field4.setStyleSheet(u"    border-width: 0px;")
        self.label_field4.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_field4.setMargin(2)

        self.gridLayout.addWidget(self.label_field4, 3, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"background:white;\n"
                                      "border-width: 2px;\n"
                                      "border-radius: 10px;\n"
                                      "")

        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.ButtonInsert = QPushButton(self.layoutWidget)
        self.ButtonInsert.setObjectName(u"ButtonInsert")
        self.ButtonInsert.setCursor(QCursor(Qt.PointingHandCursor))
        self.ButtonInsert.setStyleSheet(u"QPushButton {\n"
                                        "    background-color: grey;\n"
                                        "    border-style: outset;\n"
                                        "    border-width: 2px;\n"
                                        "    border-radius: 10px;\n"
                                        "    border-color: beige;\n"
                                        "    font: bold 14px;\n"
                                        "    padding: 6px;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: darkGreen;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    border-color: green;\n"
                                        "\n"
                                        "}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons8-m\u00e1s-24.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.ButtonInsert.setIcon(icon4)

        self.verticalLayout.addWidget(self.ButtonInsert)

        self.ButtonReplace = QPushButton(self.layoutWidget)
        self.ButtonReplace.setObjectName(u"ButtonReplace")
        self.ButtonReplace.setCursor(QCursor(Qt.PointingHandCursor))
        self.ButtonReplace.setStyleSheet(u"QPushButton {\n"
                                         "    background-color: grey;\n"
                                         "    border-style: outset;\n"
                                         "    border-width: 2px;\n"
                                         "    border-radius: 10px;\n"
                                         "    border-color: beige;\n"
                                         "    font: bold 14px;\n"
                                         "    padding: 6px;\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: darkGreen;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    border-color: green;\n"
                                         "\n"
                                         "}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons8-editar-24.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.ButtonReplace.setIcon(icon5)

        self.verticalLayout.addWidget(self.ButtonReplace)

        self.ButtonRemove = QPushButton(self.layoutWidget)
        self.ButtonRemove.setObjectName(u"ButtonRemove")
        self.ButtonRemove.setCursor(QCursor(Qt.PointingHandCursor))
        self.ButtonRemove.setStyleSheet(u"QPushButton {\n"
                                        "    background-color: grey;\n"
                                        "    border-style: outset;\n"
                                        "    border-width: 2px;\n"
                                        "    border-radius: 10px;\n"
                                        "    border-color: beige;\n"
                                        "    font: bold 14px;\n"
                                        "    padding: 6px;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: darkRed;\n"
                                        "    border-style: inset;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    border-color: red;\n"
                                        "    border-style: inset;\n"
                                        "}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons8-delete-24.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.ButtonRemove.setIcon(icon6)

        self.verticalLayout.addWidget(self.ButtonRemove)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.tableEdit = QTableWidget(self.layoutWidget)
        if (self.tableEdit.columnCount() < 4):
            self.tableEdit.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableEdit.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableEdit.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableEdit.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableEdit.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableEdit.setObjectName(u"tableEdit")
        self.tableEdit.setStyleSheet(u"QTableWidget{color:#DCDCDC;background:#444444;border:solid;\n"
                                     "border-width: 2px;border-radius: 10px; }\n"
                                     "QTableWidget::item:hover{ background:#5B5B5B;}\n"
                                     "")
        self.tableEdit.horizontalHeader().setVisible(True)
        self.tableEdit.horizontalHeader().setCascadingSectionResizes(True)
        self.tableEdit.horizontalHeader().setDefaultSectionSize(150)
        self.tableEdit.horizontalHeader().setHighlightSections(True)
        self.tableEdit.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableEdit.horizontalHeader().setStretchLastSection(True)
        self.tableEdit.verticalHeader().setVisible(False)
        self.tableEdit.verticalHeader().setCascadingSectionResizes(False)
        self.tableEdit.verticalHeader().setHighlightSections(True)
        self.tableEdit.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_4.addWidget(self.tableEdit)

        self.tabWidget.addTab(self.tab, icon5, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.layoutWidget1 = QWidget(self.tab_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 20, 691, 481))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.comboBoxFilter = QComboBox(self.layoutWidget1)
        self.comboBoxFilter.addItem("")
        self.comboBoxFilter.addItem("")
        self.comboBoxFilter.addItem("")
        self.comboBoxFilter.addItem("")
        self.comboBoxFilter.setObjectName(u"comboBoxFilter")
        self.comboBoxFilter.setStyleSheet(u"background:white;\n"
                                          "border-width: 2px;\n"
                                          "border-radius: 10px;")

        self.gridLayout_2.addWidget(self.comboBoxFilter, 0, 0, 1, 1)

        self.lineEditFilter = QLineEdit(self.layoutWidget1)
        self.lineEditFilter.setObjectName(u"lineEditFilter")
        self.lineEditFilter.setEnabled(True)
        self.lineEditFilter.setMinimumSize(QSize(36, 0))
        self.lineEditFilter.setStyleSheet(u"background:white;\n"
                                          "border-width: 2px;\n"
                                          "border-radius: 10px;")

        self.gridLayout_2.addWidget(self.lineEditFilter, 0, 1, 1, 1)

        self.ButtonFilterInfo = QPushButton(self.layoutWidget1)
        self.ButtonFilterInfo.setObjectName(u"ButtonFilterInfo")
        self.ButtonFilterInfo.setCursor(QCursor(Qt.PointingHandCursor))
        self.ButtonFilterInfo.setStyleSheet(u"QPushButton {\n"
                                            "    background-color: grey;\n"
                                            "    border-style: outset;\n"
                                            "    border-width: 2px;\n"
                                            "    border-radius: 10px;\n"
                                            "    border-color: beige;\n"
                                            "    font: bold 14px;\n"
                                            "    padding: 6px;\n"
                                            "}\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color: darkGreen;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    border-color: green;\n"
                                            "\n"
                                            "}")
        icon7 = QIcon()
        icon7.addFile(u"img/icons8-filter-32.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.ButtonFilterInfo.setIcon(icon7)

        self.gridLayout_2.addWidget(self.ButtonFilterInfo, 0, 2, 1, 1)

        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.tableFilter = QTableWidget(self.layoutWidget1)
        if (self.tableFilter.columnCount() < 4):
            self.tableFilter.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableFilter.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableFilter.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableFilter.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableFilter.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.tableFilter.setObjectName(u"tableFilter")
        self.tableFilter.setStyleSheet(u"QTableWidget{color:#DCDCDC;background:#444444;border:solid;\n"
                                       "border-width: 2px;border-radius: 10px; }\n"
                                       "QTableWidget::item:hover{ background:#5B5B5B;}\n"
                                       "")
        self.tableFilter.setInputMethodHints(Qt.ImhNoEditMenu)
        self.tableFilter.horizontalHeader().setCascadingSectionResizes(True)
        self.tableFilter.horizontalHeader().setDefaultSectionSize(150)
        self.tableFilter.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableFilter.horizontalHeader().setStretchLastSection(True)
        self.tableFilter.verticalHeader().setVisible(False)
        self.tableFilter.verticalHeader().setCascadingSectionResizes(True)
        self.tableFilter.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_3.addWidget(self.tableFilter)

        self.tabWidget.addTab(self.tab_3, icon7, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.buttoMakeInfo = QPushButton(self.tab_2)
        self.buttoMakeInfo.setObjectName(u"buttoMakeInfo")
        self.buttoMakeInfo.setEnabled(True)
        self.buttoMakeInfo.setGeometry(QRect(520, 460, 186, 36))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.buttoMakeInfo.sizePolicy().hasHeightForWidth())
        self.buttoMakeInfo.setSizePolicy(sizePolicy)
        self.buttoMakeInfo.setMaximumSize(QSize(10777211, 16777215))
        self.buttoMakeInfo.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttoMakeInfo.setStyleSheet(u"QPushButton {\n"
                                         "    background-color: grey;\n"
                                         "    border-style: outset;\n"
                                         "    border-width: 2px;\n"
                                         "    border-radius: 10px;\n"
                                         "    border-color: beige;\n"
                                         "    font: bold 14px;\n"
                                         "    padding: 6px;\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: darkGreen;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    border-color: green;\n"
                                         "\n"
                                         "}")
        icon8 = QIcon()
        icon8.addFile(u"img/icons8-archivo-nuevo-24.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.buttoMakeInfo.setIcon(icon8)
        self.layoutWidget2 = QWidget(self.tab_2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(40, 20, 661, 421))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.labelInffo1 = QLabel(self.layoutWidget2)
        self.labelInffo1.setObjectName(u"labelInffo1")
        self.labelInffo1.setStyleSheet(u"    border-width: 0px;")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelInffo1)

        self.lineEditInfo1 = QLineEdit(self.layoutWidget2)
        self.lineEditInfo1.setObjectName(u"lineEditInfo1")
        self.lineEditInfo1.setStyleSheet(u"background:white;\n"
                                         "border-width: 2px;\n"
                                         "border-radius: 10px;")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditInfo1)

        self.labelInfo2 = QLabel(self.layoutWidget2)
        self.labelInfo2.setObjectName(u"labelInfo2")
        self.labelInfo2.setStyleSheet(u"    border-width: 0px;")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelInfo2)

        self.lineEditInfo2 = QLineEdit(self.layoutWidget2)
        self.lineEditInfo2.setObjectName(u"lineEditInfo2")
        self.lineEditInfo2.setStyleSheet(u"background:white;\n"
                                         "border-width: 2px;\n"
                                         "border-radius: 10px;")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditInfo2)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.labelNotes = QLabel(self.layoutWidget2)
        self.labelNotes.setObjectName(u"labelNotes")
        font = QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setUnderline(True)
        self.labelNotes.setFont(font)
        self.labelNotes.setStyleSheet(u"    border-width: 0px;")
        self.labelNotes.setAlignment(Qt.AlignCenter)
        self.verticalLayout_2.addWidget(self.labelNotes)
        self.textEdit = QTextEdit(self.layoutWidget2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"background:white;\n"
                                    "border-width: 2px;\n"
                                    "border-radius: 10px;")

        self.verticalLayout_2.addWidget(self.textEdit)
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons8-archivo-nuevo-24.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon9, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addAction(self.actionHelp)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"Chemical tools", None))
        MainWindow.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Edici\u00f3n", None))
        self.actionCopy.setText(
            QCoreApplication.translate("MainWindow", u"Copy", None))
        self.actionCopy.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Copy text", None))
        self.actionCopy.setShortcut(
            QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
        self.actionCut.setText(
            QCoreApplication.translate("MainWindow", u"Cut", None))
        self.actionCut.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Cut text", None))
        self.actionCut.setShortcut(
            QCoreApplication.translate("MainWindow", u"Ctrl+X", None))
        self.actionPaste.setText(
            QCoreApplication.translate("MainWindow", u"Paste", None))
        self.actionPaste.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Paste text", None))
        self.actionPaste.setShortcut(
            QCoreApplication.translate("MainWindow", u"Ctrl+V", None))
        self.actionHelp.setText(
            QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionHelp.setToolTip(
            QCoreApplication.translate("MainWindow", u"Help", None))

        self.actionHelp.setShortcut(
            QCoreApplication.translate("MainWindow", u"Ctrl+H", None))

        self.tabWidget.setToolTip("")
        self.label_field1.setText(QCoreApplication.translate(
            "MainWindow", u"F\u00f3rmula qu\u00edmica:", None))
        self.lineEdit_1.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Campo para la f\u00f3rmula qu\u00edmica", None))
        self.label_field2.setText(
            QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.lineEdit_2.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Campo para el nombre de la f\u00f3rmula qu\u00edmica", None))
        self.label_field3.setText(QCoreApplication.translate(
            "MainWindow", u"Punto de ebullici\u00f3n:", None))
        self.lineEdit_3.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Campo para la punto de ebullici\u00f3n de la f\u00f3rmula qu\u00edmica", None))
        self.label_field4.setText(
            QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.lineEdit_4.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Campo para el tipo de la f\u00f3rmula qu\u00edmica", None))
        self.ButtonInsert.setStatusTip(QCoreApplication.translate(
            "MainWindow", u"Insertar valor", None))
        self.ButtonInsert.setText(QCoreApplication.translate(
            "MainWindow", u"Insertar", None))
        self.ButtonReplace.setStatusTip(QCoreApplication.translate(
            "MainWindow", u"Modificar valor", None))
        self.ButtonReplace.setText(QCoreApplication.translate(
            "MainWindow", u"Modificar", None))
        self.ButtonRemove.setStatusTip(QCoreApplication.translate(
            "MainWindow", u"Eliminar valor", None))
        self.ButtonRemove.setText(QCoreApplication.translate(
            "MainWindow", u"Eliminar", None))
        ___qtablewidgetitem = self.tableEdit.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", u"Nombre", None))
        ___qtablewidgetitem1 = self.tableEdit.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate(
            "MainWindow", u"F\u00f3rmula qu\u00edmica", None))
        ___qtablewidgetitem2 = self.tableEdit.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", u"Punto de ebullici\u00f3n", None))
        ___qtablewidgetitem3 = self.tableEdit.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("MainWindow", u"Tipo", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate(
            "MainWindow", u"Editar Informaci\u00f3n", None))
        self.comboBoxFilter.setItemText(
            0, QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.comboBoxFilter.setItemText(1, QCoreApplication.translate(
            "MainWindow", u"F\u00f3rmula qu\u00edmica", None))
        self.comboBoxFilter.setItemText(2, QCoreApplication.translate(
            "MainWindow", u"Punto de ebullici\u00f3n", None))
        self.comboBoxFilter.setItemText(
            3, QCoreApplication.translate("MainWindow", u"Tipo", None))

        self.lineEditFilter.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Campo de valor para el filtrado", None))
        self.ButtonFilterInfo.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Filtarr Informaci\u00f3n", None))
        self.ButtonFilterInfo.setStatusTip(QCoreApplication.translate(
            "MainWindow", u"Filtarr Informaci\u00f3n", None))
        self.ButtonFilterInfo.setText(
            QCoreApplication.translate("MainWindow", u"Filtrar", None))
        ___qtablewidgetitem4 = self.tableFilter.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("MainWindow", u"Nombre", None))
        ___qtablewidgetitem5 = self.tableFilter.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate(
            "MainWindow", u"F\u00f3rmula qu\u00edmica", None))
        ___qtablewidgetitem6 = self.tableFilter.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(
            QCoreApplication.translate("MainWindow", u"Punto de ebullici\u00f3n", None))
        ___qtablewidgetitem7 = self.tableFilter.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(
            QCoreApplication.translate("MainWindow", u"Tipo", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate(
            "MainWindow", u"Filtrar informaci\u00f3n", None))
        self.buttoMakeInfo.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Generar Informe", None))
        self.buttoMakeInfo.setStatusTip(QCoreApplication.translate(
            "MainWindow", u"Generar Informe", None))
        self.buttoMakeInfo.setText(QCoreApplication.translate(
            "MainWindow", u"Generar Informe", None))
        self.labelInffo1.setText(QCoreApplication.translate(
            "MainWindow", u"Formula A:", None))
        self.lineEditInfo1.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Campo para la f\u00f3rmula qu\u00edmica", None))
        self.labelInfo2.setText(QCoreApplication.translate(
            "MainWindow", u"Formula B:", None))
        self.lineEditInfo2.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Campo para la f\u00f3rmula qu\u00edmica", None))
        self.labelNotes.setText(QCoreApplication.translate(
            "MainWindow", u"Anotaciones", None))
        self.textEdit.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Entrada de texto paraa anotaciones", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), QCoreApplication.translate("MainWindow", u"Generar Informe", None))
        self.toolBar.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"toolBar", None))
