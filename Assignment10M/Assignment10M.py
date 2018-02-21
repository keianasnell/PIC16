from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QVBoxLayout, QTextEdit
from PyQt5.QtCore import Qt, QTimer, QCoreApplication
import socket
import sys
import threading

class ChatApp(QWidget):
    def __init__(self):
        super(ChatApp,self).__init__()
        self.initUi()
        self.networking = threading.Thread(target = self.initNetwork)
        self.networking.start()
#        self.initNetwork()
        self.initChat()
        
        
    
    def initChat(self): 
        rec = threading.Thread(target = self.receiveMessage)     
        send = threading.Thread(target = self.sendMessage)
        rec.start()
        send.start()
        self.history = []
        self.qt = QTimer(self)
        self.qt.timeout.connect(self.addHistory)
        self.qt.start(100)
        
        
    def receiveMessage(self):
        while self.continueIter:
            if self.clientCreatedAndConnected == True:
                    try:
                        message = self.s.recv(1024)
                        if not message:
                            self.qt.stop()
#                            self.stopTimer = True
                            message = "<connection closed>"
                            self.t1.setEnabled(False)
                            self.l1.setText(str(message))
#                            break
                        self.history.append("Received: " + str(message))
                    except:
                        pass
        self.s.close()
            
    def closeEvent(self,e):
#        if(self.stopTimer == True):
#            self.qt.stop()
        self.continueIter = False
        self.s.close()
    
    def initNetwork(self):
        try:
            self.l1.setText("<attempting to connect>")
            self.beClient()
            self.clientCreatedAndConnected = True
            
        except:
            self.l1.setText("<waiting for connection>")
            self.beServer()
        self.s.settimeout(0.25)

    def beServer(self):
        self.ss = socket.socket()
#        self.ss = socket.socket()
        self.ss.bind(("localhost",5000))
        self.ss.listen(1)
        
        self.s,add = self.ss.accept()
        self.ss.close()
        self.clientCreatedAndConnected = True
        self.l1.setText("<connected>")
        self.t1.setEnabled(True)
        print "the server"
#        self.isServer = True
    
    def beClient(self):
        self.s = socket.socket()
        self.s.connect(("localhost",5000))
        self.l1.setText("<connected>")
        self.t1.setEnabled(True)
        print "the client"
#        self.d = socket.socket()
#        self.d.connect(("localhost",5101))
#        self.isServer = False
        
    def initUi(self):
        self.setGeometry(100,100,300,300)
        title = "Chat App"
        self.clientCreatedAndConnected = False
        self.continueIter = True
#        self.stopTimer = False
#        if self.isServer:
#            title = "Chat App - Server"
#        else:
#            title = "Chat App - Client"
            
        self.setWindowTitle(title)
        self.layout = QVBoxLayout()
        
        self.te= QTextEdit(self) 
        self.te.setReadOnly(True)
        self.te.resize(200,250)
        #self.te.setAlignment(Qt.AlignVCenter)
        
        self.t1 = QLineEdit(self)
        self.t1.setEnabled(False)
        self.t1.returnPressed.connect(self.sendMessage)
        #self.t1.setAlignment(Qt.AlignVCenter)
        
        self.l1 = QLabel("",self)
        
        self.layout.addWidget(self.te)
        self.layout.addWidget(self.t1)
        self.layout.addWidget(self.l1)
        
        self.setLayout(self.layout)
        self.show()
        
    def addHistory(self):
        for x in self.history:
            self.te.append(x)
        self.history = []
    
    def sendMessage(self):
        message = self.t1.text()
        if message != "":
            self.s.send(message)
            self.history.append("Send: "+ message)
        self.t1.clear()
        
def main():
    
    app = QApplication([])
    w = ChatApp()
    app.exec_()
    
if __name__=="__main_":
    main()