# import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class HomePage(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.setGeometry(800, 480, 800, 480)

		self.prompt = QLabel()
		self.prompt.setText("So you want to recycle filament...")
		self.prompt.setAlignment(Qt.AlignCenter)
		self.prompt.setOpenExternalLinks(True)

		self.next_button = QPushButton("Let's get started!")
		self.next_button.setCheckable(True)

		self.log_button = QPushButton("Check the log")
		self.log_button.setCheckable(True)

		hbox = QHBoxLayout(self)
		hbox.addStretch(1)
		hbox.addWidget(self.log_button)

		vbox = QVBoxLayout(self)
		vbox.addLayout(hbox)
		vbox.addStretch()
		vbox.addWidget(self.prompt)
		vbox.addWidget(self.next_button)
		vbox.addStretch()

		self.setWindowTitle("ReFilament")

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = HomePage()
    window.show()
    sys.exit(app.exec_())