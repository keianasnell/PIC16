#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 12:41:55 2017

@author: keianarei
"""

from PyQt5.QtWidgets import QApplication, QWidget, QColorDialog
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QTimer

class Square(QWidget):
    def __init__(self):
        super(Square,self).__init__()
        
        self.setup()
        
        self.x = 0
        self.y = 0
        self.diffX = 0
        self.diffY = 0
        
        self.q = QTimer(self)
        self.q.timeout.connect(self.animate)
        self.q.start(10)
        
        self.color = QColor(255,0,0)
        self.drag = False
        self.show()
        
        
    def setup(self):
        self.setGeometry(0,0,600,400)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

    def paintEvent(self, event): 
        self.qp = QPainter(self)
        self.qp.begin(self)
        self.qp.setBrush(self.color)
        self.qp.drawRect(self.x,self.y,50,50)
        self.qp.end()
        
    def mouseMoveEvent(self, QMouseEvent):
        if self.drag == True:
            self.x = QMouseEvent.x()-self.diffX
            self.y = QMouseEvent.y()-self.diffY

    def mousePressEvent(self,e):
        self.pressed = True
        if e.x() >= self.x and e.x() <=self.x+50 \
        and e.y() >= self.y and e.y() <=self.y+50:
            self.drag = True
            self.diffX = e.x()-self.x
            self.diffY = e.y()-self.y
    
    def mouseReleaseEvent(self,QMouseEvent):
        self.pressed = False
        self.drag = False
    
    def mouseDoubleClickEvent(self, e):
        if e.x() >= self.x and e.x() <=self.x+50 \
        and e.y() >= self.y and e.y() <=self.y+50:
            self.c = QColorDialog(self)
            self.c.setVisible(True)
            self.color = self.c.getColor()
            self.update()

    def animate(self):
        if self.drag == True:
            self.update()

def main():
    app = QApplication([])
    s = Square()
    app.exec_()
    

if __name__ == "__main__":
    main()
        