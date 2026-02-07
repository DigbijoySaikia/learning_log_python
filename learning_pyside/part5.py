from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QLineEdit,
    QVBoxLayout
)
import sys

def greet():
    name = name_input.text()
    greeting_label.setText("Hello ,"+name)

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("User Input Example")


name_input = QLineEdit()
name_input.setPlaceholderText("Enter your name")

greeting_label = QLabel("")

greet_button = QPushButton("Greet Me")
greet_button.clicked.connect(greet)

layout = QVBoxLayout()
layout.addWidget(name_input)
layout.addWidget(greet_button)
layout.addWidget(greeting_label)

window.setLayout(layout)
window.resize(300, 150)
window.show()

sys.exit(app.exec())