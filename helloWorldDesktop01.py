from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class HelloWorld(QDialog):
    def __init__(self): #Overwrite base class Qdialog
        QDialog.__init__(self)

        layout = QVBoxLayout()
        label = QLabel("Hello World")
        line_edit = QLineEdit()
        button = QPushButton("Click Me")

        layout.addWidget(label)
        layout.addWidget(line_edit)
        layout.addWidget(button)

        self.setLayout(layout)

        button.clicked.connect(self.close) #do not pass arguments
        line_edit.textChanged.connect(label.setText)

app = QApplication(sys.argv)
dialog = HelloWorld()
dialog.show()
app.exec_()