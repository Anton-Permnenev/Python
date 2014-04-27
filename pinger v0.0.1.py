import sys
import threading
import os
from PySide import QtGui

import  queue

def ping(hostname,q):
    #print("hostname "+str(hostname))
    response = os.system(' '.join(["ping", str(hostname)]))
    if response == 0:
        q.put("passed")
    else: q.put("failed")



def pinglist(s):
    result=""
    q=queue.Queue()
    for i in s.split("\n"):
        threading.Thread(target=ping, args=(i, q)).start()
        result=q.get()
        return(result)





class Pinger(QtGui.QWidget):
    def __init__(self):
        super(Pinger, self).__init__()
        
        self.initUI()
        
    def initUI(self):

        self.btn=QtGui.QPushButton('Check',self)
        self.btn.move(70,210)
        self.btn.clicked.connect(self.pingbtn)
        self.clrbtn=QtGui.QPushButton('Clear',self)
        self.clrbtn.move(150,210)
        self.clrbtn.clicked.connect(self.clear)

        self.lbl=QtGui.QLabel('            ',self)
        self.lbl.move(230,15)


        self.listin = QtGui.QLineEdit(self)
        self.listin.move(10, 10)


        self.setGeometry(300, 300, 310, 250)
        self.setWindowTitle('Pinger v0.1')
        self.center()
        self.show()
    def pingbtn(self):
        self.lbl.setText(pinglist(self.listin.text()))
    def clear(self):
            self.lbl.clear()
            self.listin.clear()
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Pinger()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()



#pinging and checking response

