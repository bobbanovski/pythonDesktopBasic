from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import urllib.request

class Qwidgetdemo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("QWidget Demo")

        label = QLabel()
        label.setText("<b>QWidget Demo</b>") #Recognises Html

        line_edit = QLineEdit()
        line_edit.setText("Hello To You")
        line_edit.setReadOnly(True)
        line_edit.selectAll()
        #line_edit.setPlaceholderText("Enter Username")
        text = line_edit.text()
        print(text)

        password_edit = QLineEdit()
        password_edit.setEchoMode(QLineEdit.Password)

        self.checkbox = QCheckBox()
        self.checkbox.setText("Click Here")
        self.checkbox.setChecked(True)

        self.combobox = QComboBox()
        # self.combobox.addItem("First")
        # self.combobox.addItem("Second")
        # self.combobox.addItem("Third")
        self.combobox.addItems(["First", "Second", "Third"])

        close_button = QPushButton("Close Program")
        close_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(line_edit)
        layout.addWidget(password_edit)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.combobox)
        layout.addWidget(close_button)

        self.setLayout(layout)
        self.setFocus()
        self.checkbox.stateChanged.connect(self.selected)
        self.combobox.currentIndexChanged.connect(self.comboselected)

    def selected(self):
        if self.checkbox.isChecked():
            print ("Hurrah")
        else:
            print (":<")

    def comboselected(self):
        current_text = self.combobox.currentText()
        current_index = str(self.combobox.currentIndex())
        print(current_text + " At Index " + current_index)

app = QApplication(sys.argv)
dialog = Qwidgetdemo()
dialog.show()

#set an exception hook
sys._excepthook = sys.excepthook
#Provides error reporting instead of "Python has stopped working"
def pyqtexceptionhook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)

sys.excepthook = pyqtexceptionhook

try:
    sys.exit(app.exec_())
except:
    print("Exiting")