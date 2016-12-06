import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Main(QMainWindow):
	def __init__(self, parent = None):
		super(Main, self).__init__()

        # main layout
		self.mainLayout = QVBoxLayout()
		self.setGeometry(0, 0, 800, 480)

		# central widget
		self.centralWidget = QStackedWidget()
		self.setCentralWidget(self.centralWidget)

		self.home_widget = HomePage(self)
		self.form_widget = FormPage(self)

		self.centralWidget.addWidget(self.home_widget)
		self.centralWidget.addWidget(self.form_widget)
		self.centralWidget.setCurrentWidget(self.home_widget)

		self.home_widget.next_button.clicked.connect(self.next)
		self.form_widget.back_button.clicked.connect(self.go_home)


	def next(self):
		self.centralWidget.setCurrentWidget(self.form_widget)

	def go_home(self, current_widget):
		self.centralWidget.setCurrentWidget(self.home_widget)


class HomePage(QWidget):
	def __init__(self, parent = None):
		QWidget.__init__(self, parent)
		self.setGeometry(0, 0, 800, 480)

		self.prompt = QLabel()
		self.prompt.setText("So you want to recycle filament...")

		self.next_button = QPushButton("Let's get started!")

		self.log_button = QPushButton("Check the log")

		grid = QGridLayout(self)
		grid.setSpacing(10)
		grid.setColumnStretch(0, 1)
		grid.setColumnStretch(10, 1)
		grid.addWidget(self.log_button, 2, 10)
		grid.addWidget(self.prompt, 5, 5)
		grid.addWidget(self.next_button, 6, 5)

		self.setWindowTitle("ReFilament")

class FormPage(QWidget):
	def __init__(self, parent = None):
		QWidget.__init__(self, parent)
		self.setGeometry(0, 0, 800, 480)

		self.name_title = QLabel("Name")
		self.name_title.setAlignment(Qt.AlignCenter)
		self.date_title = QLabel("Date")
		self.date_title.setAlignment(Qt.AlignCenter)
		self.amount_title = QLabel("How much filament are you recycling? (grams)")
		self.amount_title.setAlignment(Qt.AlignCenter)
		self.status_title = QLabel("Is your filament ground up?")
		self.status_title.setAlignment(Qt.AlignCenter)

		self.nameEdit = QLineEdit()
		self.dateEdit = QLineEdit()
		self.amountEdit = QLineEdit()
		self.statusEdit = QLineEdit()

		self.back_button = QPushButton("Back")
		self.back_button.setCheckable(True)

		self.preheat_button = QPushButton("Preheat")
		self.preheat_button.setCheckable(True)

		grid = QGridLayout(self)
		grid.setSpacing(10)
		grid.setColumnStretch(2, 1)
		grid.addWidget(self.name_title, 1, 0)
		grid.addWidget(self.nameEdit, 1, 2)
		grid.addWidget(self.date_title, 2, 0)
		grid.addWidget(self.dateEdit, 2, 2)
		grid.addWidget(self.amount_title, 3, 0)
		grid.addWidget(self.amountEdit, 3, 2)
		grid.addWidget(self.status_title, 4, 0)
		grid.addWidget(self.statusEdit, 4, 2)
		grid.addWidget(self.back_button, 8, 0)
		grid.addWidget(self.preheat_button, 8, 10)

		self.setWindowTitle("ReFilament")


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())