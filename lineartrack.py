# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:09:03 2013

@author: <Ronny Eichler> ronny.eichler@gmail.com
"""

#!/usr/bin/python -d

import sys
import time
from PyQt4 import QtCore, QtGui
from lineartrackUI import Ui_LinearTrackUI
import arduino

class MyForm(QtGui.QMainWindow):

    running = False
    t_start = None    
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_LinearTrackUI()
        self.ui.setupUi(self)
#        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.ui.textEdit.clear)
#        QtCore.QObject.connect(self.ui.lineEdit, QtCore.SIGNAL("returnPressed()"), self.add_entry)

        QtCore.QObject.connect(self.ui.cb_trigger, QtCore.SIGNAL("clicked()"), self.toggleTrigger)
        
        # Status bar
        self.statusBar().showMessage("Ready")
        
        # Actions
        exit = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit Spotter')
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        
        self.arduino = arduino.Arduino('COM3')
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.checkPhysState)
        self.timer.start(5)
        
        
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 
                                          'Exit confirmation',
                                          'Are you sure?',
                                          QtGui.QMessageBox.Yes,
                                          QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
    def toggleTrigger(self):
        """ Flag to enable/disable trigger of any kind. """
        if self.ui.cb_trigger.isChecked():
            print "Trigger ON"
        else:
            print "Trigger OFF"
            
    def checkPhysState(self):
        byte = ord(self.arduino.sp.read(1))
        if byte > 0:
            if not self.running:
                self.running = True
                t_start = time.clock()
#            self.ui.lbl_runtime.startTimer()
                
        if byte == 1 or byte == 3:
            self.ui.gfx_sensor_left.setStyleSheet("background-color: rgba(255, 0, 0, 255);")
        else:
            self.ui.gfx_sensor_left.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
            
        if byte == 2 or byte == 3:
            self.ui.gfx_sensor_right.setStyleSheet("background-color: rgba(255, 0, 0, 255);")
        else:
            self.ui.gfx_sensor_right.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
        self.arduino.sp.flushInput()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())