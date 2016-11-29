import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def window():
   app = QApplication(sys.argv)
   win = QWidget()
   win.resize(800, 480)
	
   prompt = QLabel()
   prompt.setText("So you want to recycle filament...")
   prompt.setAlignment(Qt.AlignCenter)
	
   vbox = QVBoxLayout()
   vbox.addWidget(prompt)
   # vbox.addStretch()
	
   prompt.setOpenExternalLinks(True)
   win.setLayout(vbox)
	
   win.setWindowTitle("ReFilament")
   win.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   window()