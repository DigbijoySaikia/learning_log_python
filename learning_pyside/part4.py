from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout
)
import sys

def hello():
    print("Hello from PySide!")

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Signals & Slots")


button = QPushButton("Click Me")
button.clicked.connect(hello)


layout = QVBoxLayout()


layout.addWidget(button)


window.setLayout(layout)

window.resize(400, 300)
window.show()

sys.exit(app.exec())