# import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class HomePage(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.setGeometry(0, 0, 800, 480)

		self.prompt = QLabel()
		self.prompt.setText("So you want to recycle filament...")
		self.prompt.setAlignment(Qt.AlignCenter)
		self.prompt.setOpenExternalLinks(True)

		self.next_button = QPushButton("Let's get started!")
		self.next_button.setCheckable(True)

		self.log_button = QPushButton("Check the log")
		self.log_button.setCheckable(True)

		grid = QGridLayout(self)
		grid.setSpacing(10)
		grid.setColumnStretch(0, 1)
		grid.setColumnStretch(10, 1)
		grid.addWidget(self.log_button, 2, 10)
		grid.addWidget(self.prompt, 5, 5)
		grid.addWidget(self.next_button, 6, 5)

		self.setWindowTitle("ReFilament")

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = HomePage()
    window.show()
    sys.exit(app.exec_())