from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtCore import Qt, QTimer

class Bounce(QWidget):
    def __init__(self):
        super(Bounce, self).__init__()
    
        self.x = 1
        self.y = 1
        self.diameter = 30
        self.xVel = 1 
        self.yVel = 1
        
        self.setup()
        self.show()
        
        
    def animate(self):
        self.checkCollision()
        self.x = self.x + self.xVel
        self.y = self.y + self.yVel
        self.update()

    def checkCollision(self):
        if self.x == self.geometry().width()-30 or self.x == 0:
            self.xVel = self.xVel*-1
        if self.y == self.geometry().height()-30 or self.y == 0:
            self.yVel = self.yVel*-1
    
    def setup(self):
        self.setGeometry(0,0,600,400)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

    def paintEvent(self, event): 
        self.qp = QPainter(self)
        self.qp.begin(self)
        self.qp.setBrush(QColor(255,0,0))
        self.qp.drawEllipse(self.x,self.y,self.diameter,self.diameter)
        self.qp.end()
    
       
def main():
    app = QApplication([])
    b = Bounce()
    
    q = QTimer()
    q.timeout.connect(b.animate)
    q.start(10)
    
    app.exec_()

if __name__ == '__main__':
    main()
        
