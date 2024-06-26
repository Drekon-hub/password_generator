from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import pyperclip
import string
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(250, 300)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(250, 300))
        MainWindow.setMaximumSize(QtCore.QSize(250, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 10, 231, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setScaledContents(False)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setWordWrap(False)
        self.title.setObjectName("title")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 47, 231, 161))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textPasswordLength = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.textPasswordLength.setFont(font)
        self.textPasswordLength.setAlignment(QtCore.Qt.AlignCenter)
        self.textPasswordLength.setObjectName("textPasswordLength")
        self.verticalLayout.addWidget(self.textPasswordLength)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSlider = QtWidgets.QSlider(self.widget)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(50)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.spinBox = QtWidgets.QSpinBox(self.widget)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textIncluding = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.textIncluding.setFont(font)
        self.textIncluding.setAlignment(QtCore.Qt.AlignCenter)
        self.textIncluding.setObjectName("textIncluding")
        self.verticalLayout.addWidget(self.textIncluding)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_2.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_2.addWidget(self.checkBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buttonGenerate = QtWidgets.QPushButton(self.widget)
        self.buttonGenerate.setObjectName("buttonGenerate")
        self.verticalLayout.addWidget(self.buttonGenerate)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 210, 231, 21))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textEntry = QtWidgets.QTextEdit(self.widget1)
        self.textEntry.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEntry.setReadOnly(True)
        self.textEntry.setObjectName("textEntry")
        self.horizontalLayout_3.addWidget(self.textEntry)
        self.buttonCopy = QtWidgets.QPushButton(self.widget1)
        self.buttonCopy.setObjectName("buttonCopy")
        self.horizontalLayout_3.addWidget(self.buttonCopy)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 250, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.buttonCopy.clicked.connect(self.copy_to_clipboard)
        self.buttonGenerate.clicked.connect(self.generate_password)
        self.horizontalSlider.valueChanged.connect(self.conectSliderWithSpinBox)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "PASSWORD GENERATOR"))
        self.textPasswordLength.setText(_translate("MainWindow", "Password´s length"))
        self.textIncluding.setText(_translate("MainWindow", "Including"))
        self.checkBox.setText(_translate("MainWindow", "Letters"))
        self.checkBox_2.setText(_translate("MainWindow", "Numbers"))
        self.checkBox_3.setText(_translate("MainWindow", "Symbols"))
        self.buttonGenerate.setText(_translate("MainWindow", "Generate"))
        self.buttonCopy.setText(_translate("MainWindow", "Copy"))

    def conectSliderWithSpinBox(self):
        value = self.horizontalSlider.value()
        self.spinBox.setValue(value)

    def copy_to_clipboard(self):
        text_to_copy = self.textEntry.toPlainText()
        if text_to_copy:
            pyperclip.copy(text_to_copy)

    def insert_password(self, password):
        if self.textEntry.toPlainText() == "":
            self.textEntry.setReadOnly(False)
            self.textEntry.setText(f"{password}")
            self.textEntry.setReadOnly(True)
        elif self.textEntry.toPlainText() != "":
            self.textEntry.setReadOnly(False)
            self.textEntry.setText("")
            self.textEntry.setText(f"{password}")
            self.textEntry.setReadOnly(True)

    def generate_password(self):
        charsets = []
        if self.checkBox.isChecked():
            charsets.append(string.ascii_letters)
        if self.checkBox_2.isChecked():
            charsets.append(string.digits)
        if self.checkBox_3.isChecked():
            charsets.append(string.punctuation)
        if not charsets:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Select an option to generate the password")
            msg.setWindowTitle("Información")
            msg.exec_()
            return
        password_length = self.horizontalSlider.value()
        password = "".join(
            random.choice("".join(charsets)) for _ in range(password_length)
        )
        self.insert_password(password)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
