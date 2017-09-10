from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import urllib.request

class Downloader(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        layout = QVBoxLayout()

        #Make QLineEdits Instance wide variable with self.url, self.save_location
        self.url = QLineEdit()
        self.save_location = QLineEdit()

        self.progress = QProgressBar()
        browse = QPushButton("Browse")
        download = QPushButton("Download")

        self.url.setPlaceholderText("Enter Url")
        self.save_location.setPlaceholderText("Set Save Location")

        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(browse)
        layout.addWidget(self.progress)
        layout.addWidget(download)

        self.setLayout(layout)
        self.setWindowTitle("PyDownloader")
        self.setFocus()

        download.clicked.connect(self.download)
        browse.clicked.connect(self.browse_files)

    def browse_files(self):
        save_file = QFileDialog.getSaveFileName(self, caption="Save File As", directory=".", filter="All Files (*.*)")
        self.save_location.setText(QDir.toNativeSeparators(save_file[0]))

    def download(self):
        #create local variable
        url = self.url.text()
        save_location = self.save_location.text()

        try:
            urllib.request.urlretrieve(url, save_location, self.report)
        except Exception:
            QMessageBox.warning(self, "Warning", "Download Failed")
            return

        QMessageBox.information(self, "Information", "Download was successful")

        self.progress.setValue(0)
        self.url.setText("")
        self.save_location.setText("")

    def report(self, blocknum, blocksize, totalsize):
        readProgress = blocknum * blocksize
        if totalsize > 0:
            percent = readProgress * 100 / totalsize
            self.progress.setValue(int(percent)) #type cast to int

app = QApplication(sys.argv)
dialog = Downloader()
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
