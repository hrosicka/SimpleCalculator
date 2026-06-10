import sys
import os
from config import (
    COLORS,
    WINDOW_TITLE,
    DEFAULT_PRECISION,
    NUMBER_RANGE_MIN,
    NUMBER_RANGE_MAX,
    INITIAL_RESULT,
    MAX_HISTORY_SIZE,
)

# PyQt5 imports for building the graphical user interface (GUI)
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
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

    BUTTON_STYLE = f"""QPushButton {{
        background-color: {COLORS["primary"]}; 
        color: white; 
        border-radius: 10px; 
        padding: 10px 15px; 
        margin-top: 0px; 
        outline: 0px;
        min-width: 100px;
    }}
    QPushButton:hover {{
        background-color: {COLORS["accent"]}; 
    }}"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # relative paths
        dirname = os.path.dirname(__file__)

        # Define paths for icon used in the application
        calc_icon = os.path.join(dirname, "calc_icon.png")

        # Set window title and icon
        self.setWindowTitle(WINDOW_TITLE)
        self.setWindowIcon(QIcon(calc_icon))
        self.setStyleSheet(f"""QWidget{{background-color: {COLORS['background']};}}
                            QToolTip {{ 
                            border: 1px solid darkgrey;
                            background-color: {COLORS['primary']};
                            border-radius: 10px; 
                            color: white; }}""")

        self.calculator = Calculator()

        # create a layout
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        self.label = QLabel(INITIAL_RESULT)
        self.label.setFont(QFont("Arial", 14))
        self.label.setStyleSheet(f"""background-color : white; 
                                 color: {COLORS['text']}; 
                                 border-radius: 10px; 
                                 border: 1px solid {COLORS['accent']};
                                 min-height: 40px;
                                 """)

        self.label.setAlignment(QtCore.Qt.AlignRight)

        self.layout.addRow("Result:", self.label)

        # Create a validator to restrict input to numbers within a range
        validator = QDoubleValidator(
            NUMBER_RANGE_MIN, NUMBER_RANGE_MAX, DEFAULT_PRECISION
        )

        # Set the validator's locale and notation for proper formatting
        locale = QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates)

        validator.setLocale(locale)
        validator.setNotation(QDoubleValidator.StandardNotation)

        # Create text boxes for entering numbers
        self.textbox1 = QLineEdit(self)
        self.textbox1.setToolTip("<b>Please, enter Number 1!</b>")
        self.textbox1.setFont(QFont("Arial", 12))
        self.textbox1.setValidator(validator)
        self.textbox1.setAlignment(QtCore.Qt.AlignRight)
        self.textbox1.setStyleSheet(f"""background-color : white; 
                                    color: {COLORS['text']}; 
                                    border-radius: 10px; 
                                    border: 1px solid {COLORS['accent']};
                                    min-height: 40px;
                                    """)
        self.layout.addRow("Number 1:", self.textbox1)

        self.textbox2 = QLineEdit(self)
        self.textbox2.setToolTip("<b>Please, enter Number 2!</b>")
        self.textbox2.setFont(QFont("Arial", 12))
        self.textbox2.setValidator(validator)
        self.textbox2.setAlignment(QtCore.Qt.AlignRight)
        self.textbox2.setStyleSheet(f"""background-color : white; 
                                    color: {COLORS['text']}; 
                                    border-radius: 10px; 
                                    border: 1px solid {COLORS['accent']};
                                    min-height: 40px;
                                    """)
        self.layout.addRow("Number 2:", self.textbox2)

        # Create a text box for displaying calculation history
        self.history = QTextEdit()
        self.history.setStyleSheet(f"""background-color : white;
                                   color: {COLORS['text']};
                                   border-radius: 10px;
                                   border: 1px solid {COLORS['accent']};
                                   min-height: 40px;
                                   """)
        self.layout.addRow("History:", self.history)

        # Create a grid layout for arranging buttons
        self.layout_button = QGridLayout()
        self.layout.addRow(self.layout_button)

        # Define button titles and create buttons
        titles = [
            "Sum",
            "Difference",
            "Product",
            "Quotient",
            "History Save",
            "Input Clear",
            "History Clear",
            "Exit",
        ]
        buttons = [QPushButton(title) for title in titles]

        # Set stylesheet for buttons (background color and text color)
        for button in buttons:
            button.setStyleSheet(f"""QPushButton {{
                                 background-color: {COLORS['primary']}; 
                                 color: white; 
                                 border-radius: 10px; 
                                 padding: 10px 15px; 
                                 margin-top: 0px; 
                                 outline: 0px;
                                 }}
                                 QPushButton:hover {{
                                 background-color: {COLORS['accent']};
                                 }}
                                 """)

        # Set tooltips and functionality for each button:
        # Sum button calculates the sum and updates display and history
        buttons[0].setToolTip("<b>Sum = Number 1 + Number 2</b>")
        buttons[0].clicked.connect(lambda: self.calculate("sum"))
        self.layout_button.addWidget(buttons[0], 0, 0)

        # Difference button calculates the difference and updates display and history
        buttons[1].setToolTip("<b>Difference = Number 1 - Number 2</b>")
        buttons[1].clicked.connect(lambda: self.calculate("diff"))
        self.layout_button.addWidget(buttons[1], 0, 1)

        # Product button calculates the product and updates display and history
        buttons[2].setToolTip("<b>Product = Number 1 * Number 2</b>")
        buttons[2].clicked.connect(lambda: self.calculate("prod"))
        self.layout_button.addWidget(buttons[2], 1, 0)

        # Quotient button calculates the quotient and updates display and history
        buttons[3].setToolTip("<b>Quotient = Number 1 / Number 2</b>")
        buttons[3].clicked.connect(lambda: self.calculate("quot"))
        self.layout_button.addWidget(buttons[3], 1, 1)

        # Save History button saves the history to a text file
        buttons[4].setToolTip(
            "<b>Press button for save history as file: history_calc.txt</b>"
        )
        buttons[4].clicked.connect(lambda: self.save_history())
        self.layout_button.addWidget(buttons[4], 2, 0)

        # Clear Input button clears the input fields
        buttons[5].setToolTip("<b>Press button for clear input!</b>")
        buttons[5].clicked.connect(lambda: self.clear_input())
        self.layout_button.addWidget(buttons[5], 2, 1)

        # Clear History button clears the history text box
        buttons[6].setToolTip("<b>Press button for clear history!</b>")
        buttons[6].clicked.connect(lambda: self.clear_history())
        self.layout_button.addWidget(buttons[6], 3, 0)

        # Exit button closes the application
        buttons[7].setToolTip("<b>Press button for closing app!</b>")
        buttons[7].clicked.connect(app.exit)
        self.layout_button.addWidget(buttons[7], 3, 1)

        self.show()

    def save_history(self):
        """
        Saves the calculator history to a text file with a dialog for selecting location and name.

        Checks if the history is empty and displays a message box if so.
        Handles file write errors, permissions, and encoding issues.
        """
        dirname = os.path.dirname(__file__)
        warning = os.path.join(dirname, "warning.png")
        info = os.path.join(dirname, "info.png")
        error = os.path.join(dirname, "stop_writing.png")

        # Check if history is empty
        if not self.history.toPlainText():
            self._show_message_box(
                QMessageBox.Warning,
                "Save History",
                "History is empty! Cannot save an empty file.",
                warning,
            )
            return

        # Get the selected file path
        filepath, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "Text files (*.txt)"
        )

        # Check if the user selected a file (file path is not empty)
        if not filepath:
            return  # User cancelled the dialog

        try:
            history_text = self.history.toPlainText()

            # Check if history is not too large (limit to MAX_HISTORY_SIZE)
            if len(history_text.encode("utf-8")) > MAX_HISTORY_SIZE:
                self._show_message_box(
                    QMessageBox.Warning,
                    "Save History",
                    f"History is too large (> {MAX_HISTORY_SIZE // (1024 * 1024)}MB)! Please clear some history before saving.",
                    warning,
                )
                return

            # Try to write the file
            with open(filepath, mode="w", encoding="utf-8") as history_file:
                history_file.write(history_text)

            # Show success message
            self._show_message_box(
                QMessageBox.Information,
                "Save History",
                f"History successfully saved to:\n{filepath}",
                info,
            )

        except PermissionError:
            self._show_message_box(
                QMessageBox.Critical,
                "Save History - Error",
                f"Permission denied! Cannot write to:\n{filepath}\n\nTry saving to a different location.",
                error,
            )

        except FileNotFoundError:
            self._show_message_box(
                QMessageBox.Critical,
                "Save History - Error",
                f"Path not found:\n{filepath}\n\nMake sure the directory exists.",
                error,
            )

        except OSError as e:
            self._show_message_box(
                QMessageBox.Critical,
                "Save History - Error",
                f"System error while saving:\n{str(e)}\n\nTry again later.",
                error,
            )

        except UnicodeEncodeError:
            self._show_message_box(
                QMessageBox.Critical,
                "Save History - Error",
                "Encoding error! Some characters cannot be saved.\n\nTry using a different filename.",
                error,
            )

        except Exception as e:
            self._show_message_box(
                QMessageBox.Critical,
                "Save History - Error",
                f"Unexpected error:\n{str(e)}\n\nPlease try again.",
                error,
            )

    def _show_message_box(self, message_type, title, message, icon_path):
        """
        Helper method to display styled message boxes.

        Args:
            message_type: Type of message (QMessageBox.Warning, Information, Critical)
            title: Title of the message box
            message: Message text
            icon_path: Path to the icon image
        """
        messagebox = QMessageBox(
            message_type, title, message, buttons=QMessageBox.Ok, parent=self
        )
        messagebox.setIconPixmap(QPixmap(icon_path))
        messagebox.findChild(QPushButton).setStyleSheet(self.BUTTON_STYLE)
        messagebox.exec_()

    def clear_history(self):
        self.history.clear()

    def clear_input(self):
        self.label.setText(INITIAL_RESULT)
        self.textbox1.clear()
        self.textbox2.clear()

    def calculate(self, operation):
        """
        Performs the calculation based on the operation and updates the display and history.

        Args:
            operation: The type of calculation to perform (e.g., "sum", "diff", "prod", "quot").

        Raises:
            ValueError: If no input is provided.
            ZeroDivisionError: If division by zero is attempted.
        """

        dirname = os.path.dirname(__file__)
        stop_writing = os.path.join(dirname, "stop_writing.png")

        try:
            a = float(self.textbox1.text())
            b = float(self.textbox2.text())
            self.textbox1.setStyleSheet(f"""background-color : white; 
                                        color: {COLORS['text']}; 
                                        border-radius: 10px; 
                                        border: 1px solid {COLORS['accent']};
                                        min-height: 40px;
                                        """)
            self.textbox2.setStyleSheet(f"""background-color : white; 
                                        color: {COLORS['text']}; 
                                        border-radius: 10px; 
                                        border: 1px solid {COLORS['accent']};
                                        min-height: 40px;
                                        """)

            if operation == "sum":
                res = self.calculator.add(a, b)
                ope = " + "
            elif operation == "diff":
                res = self.calculator.subtract(a, b)
                ope = " - "
            elif operation == "prod":
                res = self.calculator.multiply(a, b)
                ope = " * "
            elif operation == "quot":
                res = self.calculator.divide(a, b)
                ope = " / "
            else:
                raise ValueError("Invalid operation")  # Handle invalid operation

            self.label.setText(str(res))
            self.history.setText(
                str(a)
                + ope
                + str(b)
                + " = "
                + str(res)
                + "\n"
                + self.history.toPlainText()
            )

        except ValueError:
            self.textbox1.setStyleSheet(f"""background-color : white; 
                                        color: {COLORS['text']}; 
                                        border-radius: 10px; 
                                        border: 4px solid {COLORS['error']};
                                        min-height: 40px;
                                 """)
            self.textbox2.setStyleSheet(f"""background-color : white; 
                                        color: {COLORS['text']}; 
                                        border-radius: 10px; 
                                        border: 4px solid {COLORS['error']};
                                        min-height: 40px;
                                        """)
            messagebox = QMessageBox(
                QMessageBox.Information,
                "Error",
                "Input can only be a number!",
                buttons=QMessageBox.Ok,
                parent=self,
            )
            messagebox.setIconPixmap(QPixmap(stop_writing))
            messagebox.findChild(QPushButton).setStyleSheet(self.BUTTON_STYLE)
            messagebox.exec_()

        except ZeroDivisionError:
            self.textbox2.setStyleSheet("""background-color : white; 
                                        color: {COLORS['text']}; 
                                        border-radius: 10px; 
                                        border: 4px solid {COLORS['error']};
                                        min-height: 40px;
                                 """)
            messagebox = QMessageBox(
                QMessageBox.Warning,
                "Error",
                "Division by zero is not allowed!",
                buttons=QMessageBox.Ok,
                parent=self,
            )
            messagebox.setIconPixmap(QPixmap(stop_writing))
            messagebox.findChild(QPushButton).setStyleSheet(self.BUTTON_STYLE)
            messagebox.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
