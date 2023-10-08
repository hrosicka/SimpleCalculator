import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
    QFormLayout,
    QTextEdit,
    QLineEdit,
    QMessageBox
    )
from PyQt5.QtGui import (
    QFont,
    QDoubleValidator
    )
from PyQt5 import QtCore
from PyQt5.QtCore import QLocale

locale = QLocale(QLocale.English, QLocale.UnitedStates)


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt Calculator')

        # create a layout
        layout = QFormLayout()
        self.setLayout(layout)


        self.label = QLabel('0.0')
        self.label.setFont(QFont('Arial', 14))
        self.label.setStyleSheet("background-color : white; color : darkblue")
        self.label.setAlignment(QtCore.Qt.AlignRight)
      
        layout.addRow('Result:', self.label)

        validator = QDoubleValidator(-10000000,10000000,5)

        locale = QLocale(QLocale.English, QLocale.UnitedStates)

        validator.setLocale(locale)
        validator.setNotation(QDoubleValidator.StandardNotation)
  
        self.textbox1 = QLineEdit(self)
        self.textbox1.setFont(QFont('Arial', 12))
        self.textbox1.setValidator(validator)
        self.textbox1.setAlignment(QtCore.Qt.AlignRight)
        layout.addRow('Number 1:', self.textbox1)

        self.textbox2 = QLineEdit(self)
        self.textbox2.setFont(QFont('Arial', 12))
        self.textbox2.setValidator(validator)
        self.textbox2.setAlignment(QtCore.Qt.AlignRight)
        layout.addRow('Number 2:', self.textbox2)

        self.history = QTextEdit()
        layout.addRow('History:', self.history)

        titles = ['Sum', 'Difference', 'Product', 'Quotient', 'History Clear', 'Exit']
        buttons = [QPushButton(title) for title in titles]
        for button in buttons:
            layout.addRow(button)

        buttons[0].setToolTip("Sum = Number 1 + Number 2")
        buttons[0].setStyleSheet("background-color : darkblue; color : white")
        buttons[0].clicked.connect(lambda: self.calculate('sum'))
        buttons[1].setToolTip("Difference = Number 1 - Number 2")
        buttons[1].setStyleSheet("background-color : darkblue; color : white")
        buttons[1].clicked.connect(lambda: self.calculate('diff'))

        buttons[2].setToolTip("Product = Number 1 * Number 2")
        buttons[2].setStyleSheet("background-color : darkblue; color : white")
        buttons[2].clicked.connect(lambda: self.calculate('prod'))

        buttons[3].setToolTip("Quotient = Number 1 / Number 2")
        buttons[3].setStyleSheet("background-color : darkblue; color : white")
        buttons[3].clicked.connect(lambda: self.calculate('quot'))

        buttons[4].setToolTip("Press button for clear history!!!")
        buttons[4].setStyleSheet("background-color : darkblue; color : white")
        buttons[4].clicked.connect(lambda: self.clear_history())

        buttons[5].setToolTip("Press button for closing app!!!")
        buttons[5].setStyleSheet("background-color : darkblue; color : white")
        buttons[5].clicked.connect(app.exit)

        
        self.setStyleSheet('''QToolTip { 
                           background-color: darkblue; 
                           color: white; 
                           border: white solid 1px
                           }''')
        
        self.show()

    def clear_history(self):
        self.history.clear()
        

    def calculate(self, operation):
        a = self.textbox1.text()
        b = self.textbox2.text()

        if operation != 'quot':
            try:
                a = float(a)
                b = float(b)

                self.textbox1.setStyleSheet("background-color : white; color : black")
                self.textbox2.setStyleSheet("background-color : white; color : black")

                if operation == 'sum':
                    res = a + b
                    ope = ' + '

                elif operation == 'diff':
                    res = a - b
                    ope = ' - '

                elif operation == 'prod':
                    res = a * b
                    ope = ' * '
    
            except Exception:
                self.textbox1.setStyleSheet("background-color : pink; color : black")
                self.textbox2.setStyleSheet("background-color : pink; color : black")
                QMessageBox.about(self, 'Error','Input can only be a number')

            else:

                self.label.setText(str(res))
                self.history.setText(str(a) + ope + str(b) + " = " + str(res) + "\n"
                                            + self.history.toPlainText())

        elif operation == 'quot':

            try:
                a = float(a)
                b = float(b)

                self.textbox1.setStyleSheet("background-color : white; color : black")
                self.textbox2.setStyleSheet("background-color : white; color : black")

            except Exception:
                self.textbox1.setStyleSheet("background-color : pink; color : black")
                self.textbox2.setStyleSheet("background-color : pink; color : black")
                QMessageBox.about(self, 'Error','Input can only be a number')
                    
            else:

                try:
                    res = a / b
                    ope = ' / '

                    self.textbox1.setStyleSheet("background-color : white; color : black")
                    self.textbox2.setStyleSheet("background-color : white; color : black")

                except Exception:
                    self.textbox2.setStyleSheet("background-color : pink; color : black")
                    QMessageBox.about(self, 'Error','Cannot be divided by zero')

                else:

                    self.label.setText(str(res))
                    self.history.setText(str(a) + ope + str(b) + " = " + str(res) + "\n"
                                            + self.history.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())