from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from modules.app import app


main_window = QMainWindow()
main_window.setWindowTitle("Weather")

WIDTH_WINDOW = 1100
HEIGHT_WINDOW = 780
primary_screen = app.primaryScreen()
screen_size = primary_screen.size()
main_window.setGeometry(
    (screen_size.width() - WIDTH_WINDOW) // 2,
    (screen_size.height() - HEIGHT_WINDOW) // 2,
    WIDTH_WINDOW,
    HEIGHT_WINDOW,
)

central_widget = QWidget(main_window)
central_widget.setStyleSheet("background-color: #303030;")
main_window.setCentralWidget(central_widget)

main_layout = QVBoxLayout(central_widget)
main_layout.setContentsMargins(18, 62, 18, 18)
main_layout.setSpacing(58)
main_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

press_button = QPushButton("Press", central_widget)
press_button.setFixedSize(100, 42)
press_button.setStyleSheet(
    "background-color: #4a4a4a; color: white; border: 1px solid #5c5c5c;"
)
main_layout.addWidget(press_button)

input_frame = QFrame(central_widget)
input_frame.setFixedSize(502, 502)
input_frame.setStyleSheet("background-color: #858585;")
main_layout.addWidget(input_frame)

frame_layout = QVBoxLayout(input_frame)
frame_layout.setContentsMargins(9, 9, 13, 9)
frame_layout.addStretch()

input_row = QHBoxLayout()
input_row.setSpacing(10)

options_combo = QComboBox(input_frame)
options_combo.addItems(["Опція 1", "Опція 2", "Опція 3"])
options_combo.setFixedWidth(78)
input_row.addWidget(options_combo)

text_input = QLineEdit(input_frame)
text_input.setPlaceholderText("Введи текст")
text_input.setStyleSheet("background-color: black; color: white;")
input_row.addWidget(text_input)

frame_layout.addLayout(input_row)
frame_layout.addStretch()
