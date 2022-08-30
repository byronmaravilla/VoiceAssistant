from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys

  
  

def __init__(self):

    # setting title
    self.setWindowTitle("Voice Assistant")

    # setting geometry
    self.setGeometry(100, 100, 600, 400)

    # calling method
    self.UiComponents()

    # showing all the widgets
    self.show()

# method for widgets
def UiComponents(self):

    # creating a push button
    button = QPushButton("Run", self)

    # setting geometry of button
    button.setGeometry(100, 200, 100, 20)

    # adding action to a button
    button.clicked.connect(clickme)

def clickme(self):
    print("pressed")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    UiComponents(w)

    w.resize(300,300)
    w.setWindowTitle("Voice Assistant")
    w.show()
    sys.exit(app.exec_())

