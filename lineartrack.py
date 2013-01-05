# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:09:03 2013

@author: <Ronny Eichler> ronny.eichler@gmail.com
"""

#!/usr/bin/python -d

import sys
from PyQt4 import QtCore, QtGui
from lineartrackUI import Ui_LinearTrackUI

class MyForm(QtGui.QMainWindow):
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
        if self.ui.cb_trigger.isChecked():
            print "TRIGGER!!!"
        else:
            print "NO TRIGGER!!!"

            

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())