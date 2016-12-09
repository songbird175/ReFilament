import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import csv
import serial

#defining a class for the QMainWindow of the app. This window will always exist while the app is open
class Main(QMainWindow):
	def __init__(self, parent = None):
		super(Main, self).__init__()
		"""The main window of our ReFilament app"""

		#establish the layout and geometry for the window. QWidgets will stretch to fit the window geometry, but not the other way around
		self.mainLayout = QVBoxLayout()
		self.setGeometry(0, 0, 800, 480)
		self.setWindowTitle("ReFilament")

		#we don't want the system getting too ridiculously hot. this gives it a cap temperature
		self.desired_temperature = 200
		#this value will establish the power status of the system. 0 is off, 1 is on
		self.heat_on_off = 0
		self.motor_on_off = 0
		#establish connection to the arduino upon app start
		self.ser = serial.Serial('/dev/ttyACM0', 115200)

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
		self.home_widget.log_button.clicked.connect(self.log_page)

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
		self.support_widget.submit_button.clicked.connect(self.log_and_add)
		self.support_widget.submit_button.clicked.connect(self.go_home)

		self.watch_widget = WatchPage(self)
		self.centralWidget.addWidget(self.watch_widget)
		self.watch_widget.done_button.clicked.connect(self.cool)

		self.cool_widget = CoolPage(self)
		self.centralWidget.addWidget(self.cool_widget)
		self.cool_widget.done_button.clicked.connect(self.done)

		self.done_widget = DonePage(self)
		self.centralWidget.addWidget(self.done_widget)
		self.done_widget.log_button.clicked.connect(self.log_and_add)

		self.log_widget = LogPage(self)
		self.centralWidget.addWidget(self.log_widget)
		self.log_widget.home_button.clicked.connect(self.go_home)

		#if you're on the Preheat Page and the temperature reaches desired value, switch to the Start Page
		if self.centralWidget.currentWidget == self.preheat_widget and self.temp_read == self.desired_temperature:
			self.centralWidget.setCurrentWidget(self.start_widget)
		#if you're on the Cool Page, once the system is cool enough, switch to the Done Page
		elif self.centralWidget.currentWidget == self.cool_widget and self.temp_read < 10:
			self.centralWidget.setCurrentWidget(self.done_widget)

		#set the home page QWidget as the current widget so the home page appears upon app startup
		self.centralWidget.setCurrentWidget(self.home_widget)

	def form_page(self):
		self.centralWidget.setCurrentWidget(self.form_widget)

	def go_home(self):
		self.centralWidget.setCurrentWidget(self.home_widget)

	def preheat(self):
		"""Pressing the preheat button turns on the system.
		It also initializes the temperature readout,
		and switches to the Preheat Page QWidget so we can see that readout."""
		self.heat_on_off = 1
		self.ser.write(bytearray([self.heat_on_off, self.motor_on_off]))
		self.centralWidget.setCurrentWidget(self.preheat_widget)
		while int(self.preheat_widget.current_temp.text()) < self.desired_temperature:
			self.bitsToNumberList()
			print self.preheat_widget.current_temp
			return self.preheat_widget.current_temp

	def start(self):
		self.motor_on_off = 1
		self.ser.write(bytearray([self.heat_on_off, self.motor_on_off]))
		self.centralWidget.setCurrentWidget(self.start_widget)

	def status(self):
		"""This function switches the view to the Status Page and
		populates it with data output."""
		while self.status_widget.no_more_button.clicked == False and self.status_widget.stop_button.clicked == False:
			self.bitsToNumberList()
			return self.start_widget.current_temp, self.status_widget.time_elapse, self.status_widget.fil_diameter
		self.centralWidget.setCurrentWidget(self.status_widget)

	def support_page(self):
		"""If someone is going to the Support Page,
		the system needs to turn off."""
		self.heat_on_off = 0
		self.motor_on_off = 0
		self.ser.write(bytearray([self.heat_on_off, self.motor_on_off]))
		self.centralWidget.setCurrentWidget(self.support_widget)

	def watch_page(self):
		self.centralWidget.setCurrentWidget(self.watch_widget)

	def cool(self):
		"""Once we reach the Cool Page,
		we want the system to turn off so it can actually cool."""
		self.heat_on_off = 0
		self.motor_on_off = 0
		self.ser.write(bytearray([self.heat_on_off, self.motor_on_off]))
		self.centralWidget.setCurrentWidget(self.cool_widget)

	def done(self):
		self.centralWidget.setCurrentWidget(self.done_widget)

	def log_page(self):
		self.centralWidget.setCurrentWidget(self.log_widget)

	def log_and_add(self):
		"""All text inputs are added to the log by this function,
		and the user is brought to the Log Page so they can view it."""
		name_text = self.form_widget.nameEdit.text()
		date_text = self.form_widget.dateEdit.text()
		amount_text = self.form_widget.amountEdit.text()
		status_text = self.form_widget.statusEdit.text()
		stop_explain = self.support_widget.stop_answer.text()
		if stop_explain == "":
			stop_explain = "None"
		
		with open('refilament_log.csv', 'a') as csvfile:
			gui_info = csv.writer(csvfile)
			gui_info.writerow([name_text, date_text, amount_text, status_text, stop_explain])

		self.centralWidget.setCurrentWidget(self.log_widget)

	def bitsToNumberList(self):
		"""This function parses out the raw arduino data
		and appropriately distributes the information."""
		#gather data from the arduino
		self.msg = self.ser.readline()
		
		msg = self.msg.rstrip(b'\r\n')
		msg = self.msg.rsplit(b',')

		return_numbers = []

		for number in msg:
			print number
			try:
				return_numbers.append(int(number))
			except:
				return_numbers.append(float(number))

		self.preheat_widget.current_temp = str(return_numbers[0])
		self.status_widget.current_temp = str(return_numbers[0])
		self.status_widget.fil_diameter = str(return_numbers[1])
		self.status_widget.time_elapse = str(return_numbers[2])
		self.cool_widget.cool_temp = str(return_numbers[0])



class HomePage(QWidget):
	def __init__(self, parent = None):
		QWidget.__init__(self, parent)
		"""The Home Page, which appears upon starting the app"""

		prompt = QLabel("So you want to recycle filament...")

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
		"""The Form Page, where the user inputs information about the job they're about to do"""

		name_title = QLabel("Name")
		name_title.setAlignment(Qt.AlignCenter)
		date_title = QLabel("Date")
		date_title.setAlignment(Qt.AlignCenter)
		amount_title = QLabel("How much filament are you recycling? (grams)")
		amount_title.setAlignment(Qt.AlignCenter)
		status_title = QLabel("Is your filament ground up?")
		status_title.setAlignment(Qt.AlignCenter)

		self.nameEdit = QLineEdit()
		self.dateEdit = QLineEdit()
		self.amountEdit = QLineEdit()
		self.statusEdit = QLineEdit()

		self.back_button = QPushButton("Back")
		self.preheat_button = QPushButton("Preheat")

		grid = QGridLayout(self)
		grid.setSpacing(10)
		grid.setColumnStretch(2, 1)
		grid.addWidget(name_title, 1, 0)
		grid.addWidget(self.nameEdit, 1, 2)
		grid.addWidget(date_title, 2, 0)
		grid.addWidget(self.dateEdit, 2, 2)
		grid.addWidget(amount_title, 3, 0)
		grid.addWidget(self.amountEdit, 3, 2)
		grid.addWidget(status_title, 4, 0)
		grid.addWidget(self.statusEdit, 4, 2)
		grid.addWidget(self.back_button, 8, 0)
		grid.addWidget(self.preheat_button, 8, 10)

class PreheatPage(QWidget):
	def __init__(self, parent = None):
		QWidget.__init__(self, parent)
		"""The Preheat Page, where a status bar appears to show the user how close the system is to being ready"""

		message = QLabel("Preheating...")
		message.setAlignment(Qt.AlignCenter)

		self.current_temp = QLabel("0")

		self.stop_button = QPushButton("Stop")

		#adding a button to get to the start page since we don't currently have the setup to have data switch it over
		self.start_button = QPushButton("Start page")

		grid = QGridLayout(self)
		grid.setSpacing(10)
		grid.addWidget(message, 5, 5)
		grid.addWidget(self.current_temp, 6, 5)
		grid.addWidget(self.stop_button, 7, 5)
		grid.addWidget(self.start_button, 8, 5) #this will go away once we connect the GUI to the thermistor

class StartPage(QWidget):
	def __init__(self, parent = None):
		QWidget.__init__(self, parent)
		"""The Start Page, where the user is brought once the system is ready.
		The recycling process begins here."""

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
		"""The Status Page, where the user can view data output regarding their recycling job"""

		temp = QLabel("Current temperature: ")
		temp.setAlignment(Qt.AlignCenter)
		time = QLabel("Time elapsed: ")
		time.setAlignment(Qt.AlignCenter)
		diameter = QLabel("Filament diameter: ")
		diameter.setAlignment(Qt.AlignCenter)

		self.current_temp = QLabel()
		self.time_elapse = QLabel()
		self.fil_diameter = QLabel()

		self.no_more_button = QPushButton("No more filament!")
		self.stop_button = QPushButton("Stop")

		grid = QGridLayout(self)
		grid.setSpacing(10)
		grid.addWidget(temp, 3, 2)
		grid.addWidget(self.current_temp, 3, 8)
		grid.addWidget(time, 4, 2)
		grid.addWidget(self.time_elapse, 4, 8)
		grid.addWidget(diameter, 5, 2)
		grid.addWidget(self.fil_diameter, 5, 8)
		grid.addWidget(self.no_more_button, 6, 5)
		grid.addWidget(self.stop_button, 7, 5)

class SupportPage(QWidget):
	def __init__(self, parent = None):
		QWidget.__init__(self, parent)
		"""The Support Page, where the user is brought if they prematurely end the recycling job"""

		stop_question = QLabel("What made you stop the recycling process?")
		stop_question.setAlignment(Qt.AlignCenter)
		self.stop_answer = QLineEdit()

		self.submit_button = QPushButton("Submit")

		grid = QGridLayout(self)
		grid.setSpacing(10)
		grid.addWidget(stop_question, 5, 3)
		grid.addWidget(self.stop_answer, 5, 7)
		grid.addWidget(self.submit_button, 7, 5)

class WatchPage(QWidget):
	def __init__(self, parent = None):
		QWidget.__init__(self, parent)
		"""The Watch Page, where the user is brought when the system is extruding the last of the filament"""

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
		"""The Cool Page, where the user is brought while the system is cooling down"""

		message = QLabel("Stick around while the system cools down.")
		message.setAlignment(Qt.AlignCenter)
		temp = QLabel("Current temperature:")
		temp.setAlignment(Qt.AlignCenter)

		self.cool_temp = QLabel()

		self.done_button = QPushButton("It's done!") #just until we can switch using data

		grid = QGridLayout(self)
		grid.setSpacing(10)
		grid.addWidget(message, 3, 5)
		grid.addWidget(temp, 5, 3)
		grid.addWidget(self.cool_temp, 5, 7)
		grid.addWidget(self.done_button, 7, 5)

class DonePage(QWidget):
	def __init__(self, parent = None):
		QWidget.__init__(self, parent)
		"""The Done Page, which tells the user that they're all done"""

		message = QLabel("All done! Enjoy your new filament!")
		message.setAlignment(Qt.AlignCenter)

		self.log_button = QPushButton("Check the log")

		grid = QGridLayout(self)
		grid.setSpacing(10)
		grid.addWidget(message, 5, 5)
		grid.addWidget(self.log_button, 7, 5)

class LogPage(QWidget):
	def __init__(self, parent = None):
		QWidget.__init__(self, parent)
		"""The Log Page, which displays information as logged for each job done on this system"""

		self.model = QStandardItemModel(self)

		table_layout = QTableView(self)
		table_layout.setModel(self.model)
		table_layout.horizontalHeader().setStretchLastSection(True)

		with open('refilament_log.csv', 'rb') as csvfile:
			log_reader = csv.reader(csvfile)
			for row in log_reader:
				items = [
                    QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)

		self.home_button = QPushButton("Home")

		grid = QGridLayout(self)
		grid.setSpacing(10)
		grid.addWidget(table_layout)
		grid.addWidget(self.home_button, 7, 5)


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())