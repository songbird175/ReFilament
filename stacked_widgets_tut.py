from PyQt4 import QtCore
from PyQt4.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(0, 0, 800, 480)

        self.setCentralWidget(HomePage())

        # login_widget = LoginWidget(self)
        # login_widget.button.clicked.connect(self.login)
        # self.central_widget.addWidget(login_widget)

    # def login(self):
    #     logged_in_widget = LoggedWidget(self)
    #     self.central_widget.addWidget(logged_in_widget)
    #     self.central_widget.setCurrentWidget(logged_in_widget)


# class LoginWidget(QtGui.QWidget):
#     def __init__(self, parent=None):
#         super(LoginWidget, self).__init__(parent)
#         layout = QtGui.QHBoxLayout()

#         self.button = QtGui.QPushButton('Login')
#         layout.addWidget(self.button)
#         self.setLayout(layout)


# class LoggedWidget(QtGui.QWidget):
#     def __init__(self, parent=None):
#         super(LoggedWidget, self).__init__(parent)
#         layout = QtGui.QHBoxLayout()

#         self.label = QtGui.QLabel('logged in!')
#         layout.addWidget(self.label)
#         self.setLayout(layout)

class HomePage(QStackedWidget):
    def __init__(self, parent=None):
        super(HomePage, self).__init__(parent)

        self.prompt = QLabel()
        self.prompt.setText("So you want to recycle filament...")

        self.next_button = QPushButton("Let's get started!")
        self.next_button.setCheckable(True)

        self.log_button = QPushButton("Check the log")
        self.log_button.setCheckable(True)

        # grid = QGridLayout(self)
        # grid.setSpacing(10)
        # grid.setColumnStretch(0, 1)
        # grid.setColumnStretch(10, 1)
        # grid.addWidget(self.log_button, 2, 10)
        # grid.addWidget(self.prompt, 5, 5)
        # grid.addWidget(self.next_button, 6, 5)

        self.addWidget(self.prompt)

        self.setWindowTitle("ReFilament")



if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()