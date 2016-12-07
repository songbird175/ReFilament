import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#defining a class for the QMainWindow of the app. This window will always exist while the app is open
class Main(QMainWindow):
	def __init__(self, parent = None):
		super(Main, self).__init__()
		#establish the layout and geometry for the window. QWidgets will stretch to fit the window geometry, but not the other way around
		self.mainLayout = QVBoxLayout()
		self.setGeometry(0, 0, 800, 480)
		self.setWindowTitle("ReFilament")

		#instantiate a central widget, which will be the focus of the window
		#using a QStackedWidget so we can change the view in the window from one QWidget to another
		self.centralWidget = QStackedWidget()
		self.setCentralWidget(self.centralWidget)

		#create calls to each QWidget so each one can be accessed from the QMainWindow
		self.home_widget = HomePage(self)
		#add each widget to the QStackedWidget
		self.centralWidget.addWidget(self.home_widget)
		#add functionality to any applicable widgets that may be within the QWidgets
		self.home_widget.next_button.clicked.connect(self.form_page)
		# self.home_widget.log_button.clicked.connect(self.log_page)

		self.form_widget = FormPage(self)
		self.centralWidget.addWidget(self.form_widget)
		self.form_widget.back_button.clicked.connect(self.go_home)
		self.form_widget.preheat_button.clicked.connect(self.preheat)

		self.preheat_widget = PreheatPage(self)
		self.centralWidget.addWidget(self.preheat_widget)
		self.preheat_widget.stop_button.clicked.connect(self.support_page)
		self.preheat_widget.start_button.clicked.connect(self.start)

		self.start_widget = StartPage(self)
		self.centralWidget.addWidget(self.start_widget)
		self.start_widget.added_button.clicked.connect(self.status)
		self.start_widget.stop_button.clicked.connect(self.support_page)

		self.status_widget = StatusPage(self)
		self.centralWidget.addWidget(self.status_widget)
		self.status_widget.no_more_button.clicked.connect(self.watch_page)
		self.status_widget.stop_button.clicked.connect(self.support_page)

		self.support_widget = SupportPage(self)
		self.centralWidget.addWidget(self.support_widget)
		# self.support_widget.submit_button.clicked.connect(self.log_and_add)
		self.support_widget.submit_button.clicked.connect(self.watch_page) #just until we can switch using data

		self.watch_widget = WatchPage(self)
		self.centralWidget.addWidget(self.watch_widget)
		self.watch_widget.done_button.clicked.connect(self.cool)

		self.cool_widget = CoolPage(self)
		self.centralWidget.addWidget(self.cool_widget)
		self.cool_widget.done_button.clicked.connect(self.done)

		self.done_widget = DonePage(self)
		self.centralWidget.addWidget(self.done_widget)
		# self.done_widget.log_button.clicked.connect(self.log_and_add)

		#set the home page QWidget as the current widget so the home page appears upon app startup
		self.centralWidget.setCurrentWidget(self.home_widget)

	def form_page(self):
		self.centralWidget.setCurrentWidget(self.form_widget)

	def go_home(self):
		self.centralWidget.setCurrentWidget(self.home_widget)

	def preheat(self):
		self.centralWidget.setCurrentWidget(self.preheat_widget)

	def start(self):
		self.centralWidget.setCurrentWidget(self.start_widget)

	def status(self):
		self.centralWidget.setCurrentWidget(self.status_widget)

	def support_page(self):
		self.centralWidget.setCurrentWidget(self.support_widget)

	def watch_page(self):
		self.centralWidget.setCurrentWidget(self.watch_widget)

	def cool(self):
		self.centralWidget.setCurrentWidget(self.cool_widget)

	def done(self):
		self.centralWidget.setCurrentWidget(self.done_widget)

	# def log_page(self):
	# 	self.centralWidget.setCurrentWidget(self.log_widget)

	# def log_and_add(self):
	# 	#add info to the log somehow
	# 	self.centralWidget.setCurrentWidget(self.log_widget)


class HomePage(QWidget):
	def __init__(self, parent = None):
		QWidget.__init__(self, parent)

		prompt = QLabel()
		prompt.setText("So you want to recycle filament...")

		#make sure buttons are properties of the class so that they can be referenced from the QMainWindow
		self.next_button = QPushButton("Let's get started!")
		self.log_button = QPushButton("Check the log")

		grid = QGridLayout(self)
		grid.setSpacing(10) #sets the number of columns/rows you'll have
		grid.setColumnStretch(1, 1) #stretches a column horizontally by a given amount (column, amount)
		grid.setColumnStretch(10, 1)
		grid.addWidget(self.log_button, 2, 10) #(y, x)
		grid.addWidget(prompt, 5, 5)
		grid.addWidget(self.next_button, 7, 5)
		#honestly not sure why these are necessary, but without them the next_button gets put on the very bottom of the screen & log_button on the very top
		grid.setRowStretch(0, 1)
		grid.setRowStretch(10, 2)
		grid.setRowStretch(3, 2)
		grid.setRowStretch(6, 1)

class FormPage(QWidget):
	def __init__(self, parent = None):
		QWidget.__init__(self, parent)

		name_title = QLabel("Name")
		name_title.setAlignment(Qt.AlignCenter)
		date_title = QLabel("Date")
		date_title.setAlignment(Qt.AlignCenter)
		amount_title = QLabel("How much filament are you recycling? (grams)")
		amount_title.setAlignment(Qt.AlignCenter)
		status_title = QLabel("Is your filament ground up?")
		status_title.setAlignment(Qt.AlignCenter)

		nameEdit = QLineEdit()
		dateEdit = QLineEdit()
		amountEdit = QLineEdit()
		statusEdit = QLineEdit()

		self.back_button = QPushButton("Back")
		self.preheat_button = QPushButton("Preheat")

		grid = QGridLayout(self)
		grid.setSpacing(10)
		grid.setColumnStretch(2, 1)
		grid.addWidget(name_title, 1, 0)
		grid.addWidget(nameEdit, 1, 2)
		grid.addWidget(date_title, 2, 0)
		grid.addWidget(dateEdit, 2, 2)
		grid.addWidget(amount_title, 3, 0)
		grid.addWidget(amountEdit, 3, 2)
		grid.addWidget(status_title, 4, 0)
		grid.addWidget(statusEdit, 4, 2)
		grid.addWidget(self.back_button, 8, 0)
		grid.addWidget(self.preheat_button, 8, 10)

class PreheatPage(QWidget):
	def __init__(self, parent = None):
		QWidget.__init__(self, parent) 

		message = QLabel("Preheating...")
		message.setAlignment(Qt.AlignCenter)

		self.stop_button = QPushButton("Stop")

		#adding a button to get to the start page since we don't currently have the setup to have data switch it over
		self.start_button = QPushButton("Start page")

		grid = QGridLayout(self)
		grid.setSpacing(10)
		grid.addWidget(message, 5, 5)
		grid.addWidget(self.stop_button, 7, 5)
		grid.addWidget(self.start_button, 8, 5) #this will go away once we connect the GUI to the thermistor

class StartPage(QWidget):
	def __init__(self, parent = None):
		QWidget.__init__(self, parent) 

		message = QLabel("Start adding filament!")
		message.setAlignment(Qt.AlignCenter)

		self.added_button = QPushButton("Ok, I've added some!")
		self.stop_button = QPushButton("Stop")

		grid = QGridLayout(self)
		grid.setSpacing(10)
		grid.addWidget(message, 3, 5)
		grid.addWidget(self.added_button, 5, 5)
		grid.addWidget(self.stop_button, 7, 5)

class StatusPage(QWidget):
	def __init__(self, parent = None):
		QWidget.__init__(self, parent) 

		temp = QLabel("Current temperature: ")
		temp.setAlignment(Qt.AlignCenter)
		time = QLabel("Time elapsed: ")
		time.setAlignment(Qt.AlignCenter)
		diameter = QLabel("Filament diameter: ")
		diameter.setAlignment(Qt.AlignCenter)

		self.no_more_button = QPushButton("No more filament!")
		self.stop_button = QPushButton("Stop")

		grid = QGridLayout(self)
		grid.setSpacing(10)
		grid.addWidget(temp, 3, 2)
		grid.addWidget(time, 4, 2)
		grid.addWidget(diameter, 5, 2)
		grid.addWidget(self.no_more_button, 6, 5)
		grid.addWidget(self.stop_button, 7, 5)

class SupportPage(QWidget):
	def __init__(self, parent = None):
		QWidget.__init__(self, parent) 

		stop_question = QLabel("What made you stop the recycling process?")
		stop_question.setAlignment(Qt.AlignCenter)
		stop_answer = QLineEdit()

		self.submit_button = QPushButton("Submit")

		grid = QGridLayout(self)
		grid.setSpacing(10)
		grid.addWidget(stop_question, 5, 3)
		grid.addWidget(stop_answer, 5, 7)
		grid.addWidget(self.submit_button, 7, 5)

class WatchPage(QWidget):
	def __init__(self, parent = None):
		QWidget.__init__(self, parent) 

		message = QLabel("Keep watching to make sure all of the filament is extruded!")
		message.setAlignment(Qt.AlignCenter)

		self.done_button = QPushButton("It's done!")

		grid = QGridLayout(self)
		grid.setSpacing(10)
		grid.addWidget(message, 5, 5)
		grid.addWidget(self.done_button, 7, 5)
		
class CoolPage(QWidget):
	def __init__(self, parent = None):
		QWidget.__init__(self, parent) 

		message = QLabel("Stick around while the system cools down.")
		message.setAlignment(Qt.AlignCenter)
		temp = QLabel("Current temperature:")
		temp.setAlignment(Qt.AlignCenter)

		self.done_button = QPushButton("It's done!") #just until we can switch using data

		grid = QGridLayout(self)
		grid.setSpacing(10)
		grid.addWidget(message, 3, 5)
		grid.addWidget(temp, 5, 3)
		grid.addWidget(self.done_button, 7, 5)

class DonePage(QWidget):
	def __init__(self, parent = None):
		QWidget.__init__(self, parent) 

		message = QLabel("All done! Enjoy your new filament!")
		message.setAlignment(Qt.AlignCenter)

		self.log_button = QPushButton("Check the log")

		grid = QGridLayout(self)
		grid.setSpacing(10)
		grid.addWidget(message, 5, 5)
		grid.addWidget(self.log_button, 7, 5)


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())