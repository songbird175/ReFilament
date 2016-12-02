from PyQt4 import QtGui, QtCore
import sys
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure()
        FigureCanvas.__init__(self, self.fig)

        self.setParent(parent)
        self.fig.add_subplot(111).plot((1, 2, 3), (4, 3, 4))      

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

class ApplicationWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.main_widget = QtGui.QWidget(self)
        self.setGeometry(0, 0, 200, 200)

        # Plot object
        plot1=MyMplCanvas()

        # With this definition it would resize as expected
        l = QtGui.QGridLayout()
        l.setSpacing(10)
        l.addWidget(plot1, 5, 5)

        # Unfortunatly it is not resizing if I use QStackedWidget
        self.viewsStack = QtGui.QStackedWidget(self.main_widget)
        self.viewsStack.setSizePolicy(QtGui.QSizePolicy.Expanding,
                                      QtGui.QSizePolicy.Expanding)        
        self.viewsStack.addWidget(plot1)

        # General code
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

if __name__ == '__main__':
    qApp = QtGui.QApplication(sys.argv)
    aw = ApplicationWindow()
    aw.show()
    sys.exit(qApp.exec_())