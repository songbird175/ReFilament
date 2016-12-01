#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
 
# Create an PyQT4 application object.
app = QApplication(sys.argv)
# The QWidget widget is the base class of all user interface objects in PyQt4.
win = QWidget()
# Set window size.
win.resize(800, 480)

label = QLabel()
label.setText("So you want to recycle filament...")
label.setAlignment(Qt.AlignCenter)

vbox = QVBoxLayout()
vbox.addWidget(label)

# Set window title
win.setWindowTitle("Hello World!")
# Show window
win.show()
sys.exit(app.exec_())