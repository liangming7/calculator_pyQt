import math
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import Qt
from PyQt5 import uic
from PyQt5 import QtCore
import sys


class CalcForm(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        Form, Base = uic.loadUiType('calc.ui')
        self.form = Form()
        self.form.setupUi(self)
        self.number_one = 0
        self.number_two = 0
        self.operation = ''
        self.text_number_one = ''
        self.text_number_two = ''
        self.form.pushButton.clicked.connect(self.handler)
        self.form.pushButton_2.clicked.connect(self.handler)
        self.form.pushButton_3.clicked.connect(self.handler)
        self.form.pushButton_4.clicked.connect(self.handler)
        self.form.pushButton_5.clicked.connect(self.handler)
        self.form.pushButton_6.clicked.connect(self.handler)
        self.form.pushButton_7.clicked.connect(self.handler)
        self.form.pushButton_8.clicked.connect(self.handler)
        self.form.pushButton_9.clicked.connect(self.handler)
        self.form.pushButton_10.clicked.connect(self.handler)
        self.form.pushButton_11.clicked.connect(self.handler)
        self.form.pushButton_12.clicked.connect(self.handler)
        self.form.pushButton_13.clicked.connect(self.handler)
        self.form.pushButton_14.clicked.connect(self.handler)
        self.form.pushButton_15.clicked.connect(self.handler)
        self.form.pushButton_16.clicked.connect(self.handler)
        self.form.pushButton_17.clicked.connect(self.handler)
        self.form.pushButton_18.clicked.connect(self.handler)
        self.form.lcdNumber.setNumDigits(10)

    def handler(self):
        button = self.sender()
        text_button = button.text()
        if text_button in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'):
            if self.operation == '':
                self.text_number_one += text_button
                self.form.lcdNumber.display(self.text_number_one)
            else:
                self.text_number_two += text_button
                self.form.lcdNumber.display(self.text_number_two)
        elif text_button in ('+', '-', 'x', '/'):
            self.operation = text_button
            self.form.lcdNumber.display('0')
        elif text_button == 'sqrt':
            self.number_one = int(self.text_number_one)
            res = math.sqrt(self.number_one)
            self.form.lcdNumber.display(str(res))
        elif text_button == '=':
            self.number_one = int(self.text_number_one)
            self.number_two = int(self.text_number_two)
            res = 0
            if self.operation == '+':
                res = self.number_one + self.number_two
            if self.operation == '-':
                res = self.number_one - self.number_two
            if self.operation == 'x':
                res = self.number_one * self.number_two
            if self.operation == '/':
                res = self.number_one / self.number_two
            self.form.lcdNumber.display(str(res))
        elif text_button == 'C':
            self.form.lcdNumber.display('0')
            self.number_one = 0
            self.text_number_one = ''
            self.number_two = 0
            self.text_number_two = ''
            self.operation = ''


def main():
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = CalcForm()
        window.show()
        sys.exit(app.exec_())

main()
