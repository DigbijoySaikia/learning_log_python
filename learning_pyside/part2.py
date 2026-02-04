from PySide6.QtWidgets import QApplication, QWidget, QPushButton
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Button Example")

button = QPushButton("Click Me", window)
button.resize(100, 40)
button.move(150, 130)

window.resize(400, 300)
window.show()

sys.exit(app.exec())