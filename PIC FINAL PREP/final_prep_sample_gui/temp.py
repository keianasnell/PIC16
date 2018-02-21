from PyQt5.QtWidgets import QApplication, QWidget, QColorDialog
from PyQt5.QtGui import QIcon, QPainter, QColor
from design3 import Ui_Form

class Example(QWidget, Ui_Form):
    
    def __init__(self):
        super(Example, self).__init__()
        self.setupUi(self)
     #   self.graphicsView.clicked.connect(self.PaintEvent)
        self.pushButton_2.clicked.connect(self.clear)
        self.pushButton.clicked.connect(self.selectColor)
    
    def PaintEvent(self, e):
        self.qp = QPainter(self)
        self.qp.begin(self)
        self.qp.setBrush(self.color)
        self.qp.drawRect(self.x,self.y,100,100)
    
    def clear(self):
        print "cleared"
    
    def selectColor(self, e):
        self.c = QColorDialog(self)
        self.c.setVisible(True)
        self.color = self.c.getColor()
        self.update()
        
        
if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    ex.show()
    app.exec_()