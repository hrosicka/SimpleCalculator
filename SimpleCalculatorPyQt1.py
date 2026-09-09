import os
import sys
from typing import Any, List, Tuple

# Import the Calculator class from a separate module (Calculator.py)
from Calculator import Calculator
from config import (
    COLORS,
    DEFAULT_PRECISION,
    INITIAL_RESULT,
    MAX_HISTORY_SIZE,
    NUMBER_RANGE_MAX,
    NUMBER_RANGE_MIN,
    WINDOW_TITLE,
)

from styles import (
    get_button_style,
    get_window_style,
    get_label_style,
    get_textbox_style,
    get_textbox_error_style,
    get_history_style,
)

from PyQt5 import QtCore
from PyQt5.QtGui import QDoubleValidator, QFont, QIcon, QPixmap

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

# Set the locale to US English for formatting
locale: QtCore.QLocale = QtCore.QLocale(
    QtCore.QLocale.English, QtCore.QLocale.UnitedStates
)


class MainWindow(QWidget):
    """
    Main window class for the PyQt Calculator application.

    Provides a graphical interface for performing basic arithmetic operations
    with history tracking and file export capabilities.
    """

    BUTTON_STYLE: str = get_button_style()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initialize the MainWindow.

        Sets up the UI components, layout, styling, and event connections.
        """
        super().__init__(*args, **kwargs)

        # relative paths
        dirname: str = os.path.dirname(__file__)

        # Define paths for icon used in the application
        calc_icon: str = os.path.join(dirname, "calc_icon.png")

        # Set window title and icon
        self.setWindowTitle(WINDOW_TITLE)
        self.setWindowIcon(QIcon(calc_icon))
        self.setStyleSheet(get_window_style())

        self.calculator: Calculator = Calculator()

        # create a layout
        self.layout: QFormLayout = QFormLayout()
        self.setLayout(self.layout)

        self.label: QLabel = QLabel(INITIAL_RESULT)
        self.label.setFont(QFont("Arial", 14))
        self.label.setStyleSheet(get_label_style())

        self.label.setAlignment(QtCore.Qt.AlignRight)

        self.layout.addRow("Result:", self.label)

        # Create a validator to restrict input to numbers within a range
        validator: QDoubleValidator = QDoubleValidator(
            NUMBER_RANGE_MIN, NUMBER_RANGE_MAX, DEFAULT_PRECISION
        )

        # Set the validator's locale and notation for proper formatting
        locale: QtCore.QLocale = QtCore.QLocale(
            QtCore.QLocale.English, QtCore.QLocale.UnitedStates
        )

        validator.setLocale(locale)
        validator.setNotation(QDoubleValidator.StandardNotation)

        # Create text boxes for entering numbers
        self.textbox1: QLineEdit = QLineEdit(self)
        self.textbox1.setToolTip("<b>Please, enter Number 1!</b>")
        self.textbox1.setFont(QFont("Arial", 12))
        self.textbox1.setValidator(validator)
        self.textbox1.setAlignment(QtCore.Qt.AlignRight)
        self.textbox1.setStyleSheet(get_textbox_style())
        self.layout.addRow("Number 1:", self.textbox1)

        self.textbox2: QLineEdit = QLineEdit(self)
        self.textbox2.setToolTip("<b>Please, enter Number 2!</b>")
        self.textbox2.setFont(QFont("Arial", 12))
        self.textbox2.setValidator(validator)
        self.textbox2.setAlignment(QtCore.Qt.AlignRight)
        self.textbox2.setStyleSheet(get_textbox_style())
        self.layout.addRow("Number 2:", self.textbox2)

        # Create a text box for displaying calculation history
        self.history: QTextEdit = QTextEdit()
        self.history.setStyleSheet(get_history_style())
        self.layout.addRow("History:", self.history)

        # Create a grid layout for arranging buttons
        self.layout_button: QGridLayout = QGridLayout()
        self.layout.addRow(self.layout_button)

        # Define button titles and create buttons
        titles: List[str] = [
            "Sum",
            "Difference",
            "Product",
            "Quotient",
            "History Save",
            "Input Clear",
            "History Clear",
            "Exit",
        ]
        buttons: List[QPushButton] = [QPushButton(title) for title in titles]

        # Set stylesheet for buttons (background color and text color)
        for button in buttons:
            button.setStyleSheet(get_button_style())

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

    def save_history(self) -> None:
        """
        Save the calculator history to a text file.

        Opens a file dialog for selecting location and filename.
        Checks if history is empty and handles file write errors,
        permissions, and encoding issues.

        Raises:
            PermissionError: If the user doesn't have write permissions.
            FileNotFoundError: If the selected directory doesn't exist.
            OSError: For other system-level file errors.
            UnicodeEncodeError: If encoding issues occur.
        """
        dirname: str = os.path.dirname(__file__)
        warning: str = os.path.join(dirname, "warning.png")
        info: str = os.path.join(dirname, "info.png")
        error: str = os.path.join(dirname, "stop_writing.png")

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
        filepath: str
        _: str
        filepath, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "Text files (*.txt)"
        )

        # Check if the user selected a file (file path is not empty)
        if not filepath:
            return  # User cancelled the dialog

        try:
            history_text: str = self.history.toPlainText()

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

    def _show_message_box(
        self,
        message_type: QMessageBox.Icon,
        title: str,
        message: str,
        icon_path: str,
    ) -> None:
        """
        Display a styled message box to the user.

        Args:
            message_type: The type of message box (QMessageBox.Warning,
                         QMessageBox.Information, QMessageBox.Critical).
            title: The title of the message box dialog.
            message: The message text to display.
            icon_path: Path to the icon image file to display.
        """
        messagebox: QMessageBox = QMessageBox(
            message_type, title, message, buttons=QMessageBox.Ok, parent=self
        )
        messagebox.setIconPixmap(QPixmap(icon_path))

        ok_button: QPushButton | None = messagebox.findChild(QPushButton)
        if ok_button:
            ok_button.setStyleSheet(self.BUTTON_STYLE)

        messagebox.exec_()

    def clear_history(self) -> None:
        """
        Clear all history from the history text box.

        Removes all entries from the calculation history display.
        """
        self.history.clear()

    def clear_input(self) -> None:
        """
        Clear all input fields.

        Resets the result display to initial value and clears both
        number input fields.
        """
        self.label.setText(INITIAL_RESULT)
        self.textbox1.clear()
        self.textbox2.clear()

    def calculate(self, operation: str) -> None:
        """
        Perform a calculation based on the specified operation.

        Updates the result display and adds the calculation to history.
        Handles input validation and error cases appropriately.

        Args:
            operation: The type of calculation to perform:
                      "sum", "diff", "prod", or "quot".

        Raises:
            ValueError: If the input cannot be converted to a number.
            ZeroDivisionError: If division by zero is attempted.
        """

        dirname: str = os.path.dirname(__file__)
        stop_writing: str = os.path.join(dirname, "stop_writing.png")

        try:
            a: float = float(self.textbox1.text())
            b: float = float(self.textbox2.text())
            self.textbox1.setStyleSheet(get_textbox_style())
            self.textbox2.setStyleSheet(get_textbox_style())

            res: float | int
            ope: str
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
            self.textbox1.setStyleSheet(get_textbox_error_style())
            self.textbox2.setStyleSheet(get_textbox_error_style())
            messagebox: QMessageBox = QMessageBox(
                QMessageBox.Information,
                "Error",
                "Input can only be a number!",
                buttons=QMessageBox.Ok,
                parent=self,
            )
            messagebox.setIconPixmap(QPixmap(stop_writing))

            ok_button: QPushButton | None = messagebox.findChild(QPushButton)
            if ok_button:
                ok_button.setStyleSheet(self.BUTTON_STYLE)

            messagebox.exec_()

        except ZeroDivisionError:
            self.textbox2.setStyleSheet(get_textbox_error_style())
            messagebox: QMessageBox = QMessageBox(
                QMessageBox.Warning,
                "Error",
                "Division by zero is not allowed!",
                buttons=QMessageBox.Ok,
                parent=self,
            )
            messagebox.setIconPixmap(QPixmap(stop_writing))

            ok_button: QPushButton | None = messagebox.findChild(QPushButton)
            if ok_button:
                ok_button.setStyleSheet(self.BUTTON_STYLE)

            messagebox.exec_()


if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    window: MainWindow = MainWindow()
    sys.exit(app.exec())
