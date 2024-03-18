import sys
import os

# PyQt5 imports for building the graphical user interface (GUI)
from PyQt5.QtWidgets import (
    QApplication,
    QFormLayout,
    QGridLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QWidget,
    )

from PyQt5.QtGui import (
    QFont,
    QDoubleValidator,
    QIcon,
    QPixmap,
    )

from PyQt5 import QtCore

# Import the Calculator class from a separate module (Calculator.py)
from Calculator import Calculator

# Set the locale to US English for formatting 
locale = QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates)


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # relative paths
        dirname = os.path.dirname(__file__)

        # Define paths for icons used in the application
        calc_icon = os.path.join(dirname, 'calc_icon.png')
        stop_writing = os.path.join(dirname, 'stop_writing.png')

        # Set window title and icon
        self.setWindowTitle('PyQt Calculator')
        self.setWindowIcon(QIcon(calc_icon))

        self.calculator = Calculator()

        # create a layout
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        self.label = QLabel('0.0')
        self.label.setFont(QFont('Arial', 14))
        self.label.setStyleSheet("background-color : white; color : darkblue")

        self.label.setAlignment(QtCore.Qt.AlignRight)
      
        self.layout.addRow('Result:', self.label)

        # Create a validator to restrict input to numbers within a range
        validator = QDoubleValidator(-10000000,10000000,5)

        # Set the validator's locale and notation for proper formatting
        locale = QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates)

        validator.setLocale(locale)
        validator.setNotation(QDoubleValidator.StandardNotation)
  
        # Create text boxes for entering numbers
        self.textbox1 = QLineEdit(self)
        self.textbox1.setToolTip("<b>Please, enter Number 1!</b>")
        self.textbox1.setFont(QFont('Arial', 12))
        self.textbox1.setValidator(validator)
        self.textbox1.setAlignment(QtCore.Qt.AlignRight)
        self.layout.addRow('Number 1:', self.textbox1)

        self.textbox2 = QLineEdit(self)
        self.textbox2.setToolTip("<b>Please, enter Number 2!</b>")
        self.textbox2.setFont(QFont('Arial', 12))
        self.textbox2.setValidator(validator)
        self.textbox2.setAlignment(QtCore.Qt.AlignRight)
        self.layout.addRow('Number 2:', self.textbox2)

        # Create a text box for displaying calculation history
        self.history = QTextEdit()
        self.layout.addRow('History:', self.history)

        # Create a grid layout for arranging buttons
        self.layout_button = QGridLayout()
        self.layout.addRow(self.layout_button)

        # Define button titles and create buttons
        titles = ['Sum', 'Difference', 'Product', 'Quotient', 'History Save', 'Input Clear',
                  'History Clear', 'Exit']
        buttons = [QPushButton(title) for title in titles]

        # Set stylesheet for buttons (background color and text color)
        for button in buttons:
            button.setStyleSheet("background-color: darkblue; color: white")
        
        # Set tooltips and functionality for each button:
        # Sum button calculates the sum and updates display and history
        buttons[0].setToolTip("<b>Sum = Number 1 + Number 2</b>")
        buttons[0].clicked.connect(lambda: self.calculate('sum'))
        self.layout_button.addWidget(buttons[0],0,0)

        # Difference button calculates the difference and updates display and history
        buttons[1].setToolTip("<b>Difference = Number 1 - Number 2</b>")
        buttons[1].clicked.connect(lambda: self.calculate('diff'))
        self.layout_button.addWidget(buttons[1],0,1)

        # Product button calculates the product and updates display and history
        buttons[2].setToolTip("<b>Product = Number 1 * Number 2</b>")
        buttons[2].clicked.connect(lambda: self.calculate('prod'))
        self.layout_button.addWidget(buttons[2],1,0)

        # Quotient button calculates the quotient and updates display and history
        buttons[3].setToolTip("<b>Quotient = Number 1 / Number 2</b>")
        buttons[3].clicked.connect(lambda: self.calculate('quot'))
        self.layout_button.addWidget(buttons[3],1,1)

        # Save History button saves the history to a text file
        buttons[4].setToolTip("<b>Press button for save history as file: history_calc.txt</b>")
        buttons[4].clicked.connect(lambda: self.save_history())
        self.layout_button.addWidget(buttons[4],2,0)

        # Clear Input button clears the input fields
        buttons[5].setToolTip("<b>Press button for clear input!</b>")
        buttons[5].clicked.connect(lambda: self.clear_input())
        self.layout_button.addWidget(buttons[5],2,1)
        
        # Clear History button clears the history text box
        buttons[6].setToolTip("<b>Press button for clear history!</b>")
        buttons[6].clicked.connect(lambda: self.clear_history())
        self.layout_button.addWidget(buttons[6],3,0)

        # Exit button closes the application
        buttons[7].setToolTip("<b>Press button for closing app!</b>")
        buttons[7].clicked.connect(app.exit)
        self.layout_button.addWidget(buttons[7],3,1)

        self.setStyleSheet('QToolTip { border: 3px solid darkgrey;}')
        
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

        dirname = os.path.dirname(__file__)
        stop_writing = os.path.join(dirname, 'stop_writing.png')

        a = self.textbox1.text()
        b = self.textbox2.text()

        if operation != 'quot':
            try:
                a = float(a)
                b = float(b)

                self.textbox1.setStyleSheet("background-color : white; color : black")
                self.textbox2.setStyleSheet("background-color : white; color : black")

                if operation == 'sum':
                    res = self.calculator.add(a, b)
                    ope = ' + '

                elif operation == 'diff':
                    res = self.calculator.subtract(a, b)
                    ope = ' - '

                elif operation == 'prod':
                    res = self.calculator.multiply(a, b)
                    ope = ' * '
    
            except Exception:

                self.textbox1.setStyleSheet("background-color : pink; color : black")
                self.textbox2.setStyleSheet("background-color : pink; color : black")
                messagebox = QMessageBox(QMessageBox.Warning, "Error", "Input can only be a number!", buttons = QMessageBox.Ok, parent=self)
                messagebox.setIconPixmap(QPixmap(stop_writing))
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
                messagebox = QMessageBox(QMessageBox.Warning, "Error", "Input can only be a number!", buttons = QMessageBox.Ok, parent=self)
                messagebox.setIconPixmap(QPixmap(stop_writing))
                messagebox.findChild(QPushButton).setStyleSheet("background-color : darkblue; color : white")
                messagebox.exec_()
                    
            else:

                try:
                    res = self.calculator.divide(a, b)
                    ope = ' / '

                    self.textbox1.setStyleSheet("background-color : white; color : black")
                    self.textbox2.setStyleSheet("background-color : white; color : black")

                except Exception:
                    self.textbox2.setStyleSheet("background-color : pink; color : black")
                    messagebox = QMessageBox(QMessageBox.Warning, "Error", "Cannot be divided by zero!", buttons = QMessageBox.Ok, parent=self)
                    messagebox.setIconPixmap(QPixmap(stop_writing))
                    messagebox.findChild(QPushButton).setStyleSheet("background-color : darkblue; color : white")
                    messagebox.exec_()

                else:

                    self.label.setText(str(res))
                    self.history.setText(str(a) + ope + str(b) + " = " + str(res) + "\n"
                                            + self.history.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())