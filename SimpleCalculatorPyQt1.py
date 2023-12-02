import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QPushButton,
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
    QFormLayout,
    QTextEdit,
    QLineEdit,
    QMessageBox,
    )
from PyQt5.QtGui import (
    QFont,
    QDoubleValidator,
    QIcon,
    QPixmap,
    )
from PyQt5 import QtCore
import PyQt5.QtCore

locale = QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates)


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt Calculator')
        self.setWindowIcon(QIcon('D:\\Programovani\\Python\\naucse\\PyQtSimpleCalculator\\calc_icon.png'))

        # create a layout
        layout = QFormLayout()
        self.setLayout(layout)

        self.label = QLabel('0.0')
        self.label.setFont(QFont('Arial', 14))
        self.label.setStyleSheet("background-color : white; color : darkblue")
        self.label.setAlignment(QtCore.Qt.AlignRight)
      
        layout.addRow('Result:', self.label)

        validator = QDoubleValidator(-10000000,10000000,5)

        locale = QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates)

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

        self.layout_button = QGridLayout()

        layout.addRow(self.layout_button)

        titles = ['Sum', 'Difference', 'Product', 'Quotient', 'History Save', 'Input Clear',
                  'History Clear', 'Exit']
        buttons = [QPushButton(title) for title in titles]
        

        buttons[0].setToolTip("Sum = Number 1 + Number 2")
        buttons[0].setStyleSheet("background-color : darkblue; color : white")
        buttons[0].clicked.connect(lambda: self.calculate('sum'))
        self.layout_button.addWidget(buttons[0],0,0)

        buttons[1].setToolTip("Difference = Number 1 - Number 2")
        buttons[1].setStyleSheet("background-color : darkblue; color : white")
        buttons[1].clicked.connect(lambda: self.calculate('diff'))
        self.layout_button.addWidget(buttons[1],0,1)

        buttons[2].setToolTip("Product = Number 1 * Number 2")
        buttons[2].setStyleSheet("background-color : darkblue; color : white")
        buttons[2].clicked.connect(lambda: self.calculate('prod'))
        self.layout_button.addWidget(buttons[2],1,0)

        buttons[3].setToolTip("Quotient = Number 1 / Number 2")
        buttons[3].setStyleSheet("background-color : darkblue; color : white")
        buttons[3].clicked.connect(lambda: self.calculate('quot'))
        self.layout_button.addWidget(buttons[3],1,1)

        buttons[4].setToolTip("Press button for save history as file!!!")
        buttons[4].setStyleSheet("background-color : darkblue; color : white")
        buttons[4].clicked.connect(lambda: self.save_history())
        self.layout_button.addWidget(buttons[4],2,0)

        buttons[5].setToolTip("Press button for clear input!!!")
        buttons[5].setStyleSheet("background-color : darkblue; color : white")
        buttons[5].clicked.connect(lambda: self.clear_input())
        self.layout_button.addWidget(buttons[5],2,1)
        
        buttons[6].setToolTip("Press button for clear history!!!")
        buttons[6].setStyleSheet("background-color : darkblue; color : white")
        buttons[6].clicked.connect(lambda: self.clear_history())
        self.layout_button.addWidget(buttons[6],3,0)

        buttons[7].setToolTip("Press button for closing app!!!")
        buttons[7].setStyleSheet("background-color : darkblue; color : white")
        buttons[7].clicked.connect(app.exit)
        self.layout_button.addWidget(buttons[7],3,1)

        
        self.setStyleSheet('''QToolTip { 
                           background-color: darkblue; 
                           color: white; 
                           border: white solid 1px
                           }''')
        
        self.show()

    def save_history(self):
        with open('history_calc.txt', mode='w', encoding='utf-8') as history_file:
            print(self.history.toPlainText(), file=history_file)
        

    def clear_history(self):
        self.history.clear()

    def clear_input(self):
        self.label.setText('0.0')
        self.textbox1.clear()
        self.textbox2.clear()
        
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
                messagebox = QMessageBox(QMessageBox.Warning, "Error", "Input can only be a number!", buttons = QMessageBox.Ok, parent=self)
                messagebox.setIconPixmap(QPixmap('D:\\Programovani\\Python\\naucse\\PyQtSimpleCalculator\\stop_writing.png'))
                messagebox.findChild(QPushButton).setStyleSheet("background-color : darkblue; color : white")
                messagebox.exec_()


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