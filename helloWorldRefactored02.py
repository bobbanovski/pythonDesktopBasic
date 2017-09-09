from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class HelloWorld(QDialog):
    def __init__(self): #Overwrite base class Qdialog
        QDialog.__init__(self)

        layout = QVBoxLayout() #Vertical Layout
        #layout = QHBoxLayout() #Horizontal Layout
        #layout = QGridLayout() #Arrayed grid Layout
        #layout = QFormLayout() #2 columns only

        self.label = QLabel("Hello World")
        line_edit = QLineEdit()
        button = QPushButton("Click Me")

        layout.addWidget(self.label)
        layout.addWidget(line_edit)
        layout.addWidget(button)

        self.setLayout(layout)

        button.clicked.connect(self.close) #do not pass arguments
        line_edit.textChanged.connect(self.changeTextLabel)

    def changeTextLabel(self, text):
        self.label.setText(text)

app = QApplication(sys.argv)
dialog = HelloWorld()
dialog.show()
app.exec_()