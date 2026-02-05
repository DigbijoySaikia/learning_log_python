from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Layouts")

layout = QVBoxLayout()

layout.addWidget(QPushButton("Button 1"))
layout.addWidget(QPushButton("Button 2"))
layout.addWidget(QPushButton("Button 3"))

window.setLayout(layout)
window.resize(300, 200)
window.show()

sys.exit(app.exec())