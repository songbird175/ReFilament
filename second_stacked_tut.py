import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.stacked_widget = QtGui.QStackedWidget()
        self.button = QtGui.QPushButton("Next")

        self.button.clicked.connect(self.__next_page)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        layout.addWidget(self.button)

        widget = QtGui.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.stacked_widget.addWidget(QtGui.QLabel("Page 1"))
        self.stacked_widget.addWidget(QtGui.QLabel("Page 2"))
        self.stacked_widget.addWidget(QtGui.QLabel("Page 3"))

    def __next_page(self):
        idx = self.stacked_widget.currentIndex()
        if idx < self.stacked_widget.count() - 1:
            self.stacked_widget.setCurrentIndex(idx + 1)
        else:
            self.stacked_widget.setCurrentIndex(0)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())