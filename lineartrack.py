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

SENSOR_LEFT = chr(0x01)
SENSOR_RIGHT = chr(0x02)
SENSOR_ALL = chr(0x03)

class MyForm(QtGui.QMainWindow):

    running = False
    t_start = None    
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_LinearTrackUI()
        self.ui.setupUi(self)

        # Trigger checkbox
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
        
        self.t_elapsed = QtCore.QTime()
        self.t_elapsed.start()
        
        
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
        if not self.arduino.bytes_available():
            return
        
        bytestr = self.arduino.read_n_bytes(self.arduino.bytes_available())

#        if byte > 0:
#            if not self.running:
#                self.running = True
#                t_start = time.clock()
#        print self.t_elapsed.elapsed()
        self.ui.lbl_runtime.setTime(self.t_elapsed) #self.t_elapsed.elapsed()
                
        if (SENSOR_LEFT in bytestr) or (SENSOR_ALL in bytestr):
            self.ui.gfx_sensor_left.setStyleSheet("background-color: rgba(255, 0, 0, 255);")
        else:
            self.ui.gfx_sensor_left.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
            
        if (SENSOR_RIGHT in bytestr) or (SENSOR_ALL in bytestr):
            self.ui.gfx_sensor_right.setStyleSheet("background-color: rgba(255, 0, 0, 255);")
        else:
            self.ui.gfx_sensor_right.setStyleSheet("background-color: rgba(0, 0, 0, 100);")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())