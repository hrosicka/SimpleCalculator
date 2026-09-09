"""
Stylesheet module for the PyQt Calculator application.

This module centralizes all CSS/QSS stylesheets used throughout the application,
making it easy to maintain, update, and switch between themes.
"""

from typing import Dict
from config import COLORS


def get_button_style() -> str:
    """
    Get the stylesheet for push buttons.

    Returns:
        str: QSS stylesheet for QPushButton with hover effect.

    Example:
        >>> button = QPushButton("Click me")
        >>> button.setStyleSheet(get_button_style())
    """
    return f"""QPushButton {{
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


def get_window_style() -> str:
    """
    Get the stylesheet for the main application window.

    Returns:
        str: QSS stylesheet for QWidget (main window) and tooltips.

    Example:
        >>> window = QWidget()
        >>> window.setStyleSheet(get_window_style())
    """
    return f"""QWidget{{background-color: {COLORS['background']};}}
    QToolTip {{ 
    border: 1px solid darkgrey;
    background-color: {COLORS['primary']};
    border-radius: 10px; 
    color: white; }}"""


def get_label_style() -> str:
    """
    Get the stylesheet for the result display label.

    Returns:
        str: QSS stylesheet for QLabel displaying calculation results.

    Example:
        >>> label = QLabel("0.0")
        >>> label.setStyleSheet(get_label_style())
    """
    return f"""background-color : white; 
    color: {COLORS['text']}; 
    border-radius: 10px; 
    border: 1px solid {COLORS['accent']};
    min-height: 40px;"""


def get_textbox_style() -> str:
    """
    Get the stylesheet for input textboxes in normal state.

    Returns:
        str: QSS stylesheet for QLineEdit in normal state.

    Example:
        >>> textbox = QLineEdit()
        >>> textbox.setStyleSheet(get_textbox_style())
    """
    return f"""background-color : white; 
    color: {COLORS['text']}; 
    border-radius: 10px; 
    border: 1px solid {COLORS['accent']};
    min-height: 40px;"""


def get_textbox_error_style() -> str:
    """
    Get the stylesheet for input textboxes in error state.

    Used when input validation fails to highlight the problematic field.

    Returns:
        str: QSS stylesheet for QLineEdit with error highlighting.

    Example:
        >>> textbox = QLineEdit()
        >>> textbox.setStyleSheet(get_textbox_error_style())
    """
    return f"""background-color : white; 
    color: {COLORS['text']}; 
    border-radius: 10px; 
    border: 4px solid {COLORS['error']};
    min-height: 40px;"""


def get_history_style() -> str:
    """
    Get the stylesheet for the calculation history text box.

    Returns:
        str: QSS stylesheet for QTextEdit displaying history.

    Example:
        >>> history = QTextEdit()
        >>> history.setStyleSheet(get_history_style())
    """
    return f"""background-color : white;
    color: {COLORS['text']};
    border-radius: 10px;
    border: 1px solid {COLORS['accent']};
    min-height: 40px;"""
