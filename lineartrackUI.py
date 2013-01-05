# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lineartrack.ui'
#
# Created: Sat Jan  5 16:25:07 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_LinearTrackUI(object):
    def setupUi(self, LinearTrackUI):
        LinearTrackUI.setObjectName(_fromUtf8("LinearTrackUI"))
        LinearTrackUI.setEnabled(True)
        LinearTrackUI.resize(400, 230)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LinearTrackUI.sizePolicy().hasHeightForWidth())
        LinearTrackUI.setSizePolicy(sizePolicy)
        self.gfx_track = QtGui.QLabel(LinearTrackUI)
        self.gfx_track.setGeometry(QtCore.QRect(30, 60, 341, 20))
        self.gfx_track.setAutoFillBackground(True)
        self.gfx_track.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        self.gfx_track.setText(_fromUtf8(""))
        self.gfx_track.setObjectName(_fromUtf8("gfx_track"))
        self.gfx_sensor_left = QtGui.QLabel(LinearTrackUI)
        self.gfx_sensor_left.setGeometry(QtCore.QRect(50, 40, 8, 61))
        self.gfx_sensor_left.setToolTip(_fromUtf8(""))
        self.gfx_sensor_left.setAutoFillBackground(True)
        self.gfx_sensor_left.setStyleSheet(_fromUtf8("background-color: rgba(0, 0, 0, 100);"))
        self.gfx_sensor_left.setText(_fromUtf8(""))
        self.gfx_sensor_left.setObjectName(_fromUtf8("gfx_sensor_left"))
        self.gfx_sensor_right = QtGui.QLabel(LinearTrackUI)
        self.gfx_sensor_right.setGeometry(QtCore.QRect(330, 40, 8, 61))
        self.gfx_sensor_right.setAutoFillBackground(True)
        self.gfx_sensor_right.setStyleSheet(_fromUtf8("background-color: rgba(0, 0, 0, 100);"))
        self.gfx_sensor_right.setText(_fromUtf8(""))
        self.gfx_sensor_right.setObjectName(_fromUtf8("gfx_sensor_right"))
        self.gfx_sensor_center = QtGui.QLabel(LinearTrackUI)
        self.gfx_sensor_center.setEnabled(True)
        self.gfx_sensor_center.setGeometry(QtCore.QRect(200, 40, 8, 61))
        self.gfx_sensor_center.setToolTip(_fromUtf8(""))
        self.gfx_sensor_center.setAutoFillBackground(False)
        self.gfx_sensor_center.setStyleSheet(_fromUtf8("background-color: rgba(0, 0, 0, 100);"))
        self.gfx_sensor_center.setText(_fromUtf8(""))
        self.gfx_sensor_center.setProperty("setVisible", False)
        self.gfx_sensor_center.setObjectName(_fromUtf8("gfx_sensor_center"))
        self.cb_trigger = QtGui.QCheckBox(LinearTrackUI)
        self.cb_trigger.setGeometry(QtCore.QRect(160, 10, 71, 31))
        self.cb_trigger.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cb_trigger.setObjectName(_fromUtf8("cb_trigger"))
        self.lbl_runtime = QtGui.QTimeEdit(LinearTrackUI)
        self.lbl_runtime.setEnabled(True)
        self.lbl_runtime.setGeometry(QtCore.QRect(150, 130, 101, 27))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_runtime.setFont(font)
        self.lbl_runtime.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lbl_runtime.setToolTip(_fromUtf8(""))
        self.lbl_runtime.setAutoFillBackground(False)
        self.lbl_runtime.setFrame(False)
        self.lbl_runtime.setReadOnly(True)
        self.lbl_runtime.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.lbl_runtime.setKeyboardTracking(False)
        self.lbl_runtime.setObjectName(_fromUtf8("lbl_runtime"))
        self.widget = QtGui.QWidget(LinearTrackUI)
        self.widget.setGeometry(QtCore.QRect(290, 110, 92, 83))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.Group_Right = QtGui.QVBoxLayout(self.widget)
        self.Group_Right.setMargin(0)
        self.Group_Right.setObjectName(_fromUtf8("Group_Right"))
        self.lbl_right_water = QtGui.QLabel(self.widget)
        self.lbl_right_water.setObjectName(_fromUtf8("lbl_right_water"))
        self.Group_Right.addWidget(self.lbl_right_water)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.spin_right_waterreward = QtGui.QSpinBox(self.widget)
        self.spin_right_waterreward.setToolTip(_fromUtf8(""))
        self.spin_right_waterreward.setMaximum(10000)
        self.spin_right_waterreward.setProperty("value", 30)
        self.spin_right_waterreward.setObjectName(_fromUtf8("spin_right_waterreward"))
        self.horizontalLayout_2.addWidget(self.spin_right_waterreward)
        self.lbl_right_waterreward = QtGui.QLabel(self.widget)
        self.lbl_right_waterreward.setObjectName(_fromUtf8("lbl_right_waterreward"))
        self.horizontalLayout_2.addWidget(self.lbl_right_waterreward)
        self.Group_Right.addLayout(self.horizontalLayout_2)
        self.lcd_right_triggers = QtGui.QLCDNumber(self.widget)
        self.lcd_right_triggers.setObjectName(_fromUtf8("lcd_right_triggers"))
        self.Group_Right.addWidget(self.lcd_right_triggers)
        self.widget1 = QtGui.QWidget(LinearTrackUI)
        self.widget1.setGeometry(QtCore.QRect(30, 110, 92, 83))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.Group_Left = QtGui.QVBoxLayout(self.widget1)
        self.Group_Left.setMargin(0)
        self.Group_Left.setObjectName(_fromUtf8("Group_Left"))
        self.lbl_left_water = QtGui.QLabel(self.widget1)
        self.lbl_left_water.setObjectName(_fromUtf8("lbl_left_water"))
        self.Group_Left.addWidget(self.lbl_left_water)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.spin_left_waterreward = QtGui.QSpinBox(self.widget1)
        self.spin_left_waterreward.setEnabled(True)
        self.spin_left_waterreward.setToolTip(_fromUtf8(""))
        self.spin_left_waterreward.setMaximum(10000)
        self.spin_left_waterreward.setProperty("value", 30)
        self.spin_left_waterreward.setObjectName(_fromUtf8("spin_left_waterreward"))
        self.horizontalLayout.addWidget(self.spin_left_waterreward)
        self.lbl_left_waterreward = QtGui.QLabel(self.widget1)
        self.lbl_left_waterreward.setObjectName(_fromUtf8("lbl_left_waterreward"))
        self.horizontalLayout.addWidget(self.lbl_left_waterreward)
        self.Group_Left.addLayout(self.horizontalLayout)
        self.lcd_left_triggers = QtGui.QLCDNumber(self.widget1)
        self.lcd_left_triggers.setObjectName(_fromUtf8("lcd_left_triggers"))
        self.Group_Left.addWidget(self.lcd_left_triggers)

        self.retranslateUi(LinearTrackUI)
        QtCore.QMetaObject.connectSlotsByName(LinearTrackUI)
        LinearTrackUI.setTabOrder(self.spin_left_waterreward, self.spin_right_waterreward)
        LinearTrackUI.setTabOrder(self.spin_right_waterreward, self.cb_trigger)

    def retranslateUi(self, LinearTrackUI):
        LinearTrackUI.setWindowTitle(QtGui.QApplication.translate("LinearTrackUI", "Linear Track Control", None, QtGui.QApplication.UnicodeUTF8))
        LinearTrackUI.setToolTip(QtGui.QApplication.translate("LinearTrackUI", " ", None, QtGui.QApplication.UnicodeUTF8))
        self.gfx_sensor_left.setStatusTip(QtGui.QApplication.translate("LinearTrackUI", "Left sensor status", None, QtGui.QApplication.UnicodeUTF8))
        self.gfx_sensor_right.setStatusTip(QtGui.QApplication.translate("LinearTrackUI", "Right Sensor", None, QtGui.QApplication.UnicodeUTF8))
        self.gfx_sensor_center.setStatusTip(QtGui.QApplication.translate("LinearTrackUI", "Center sensor status", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_trigger.setStatusTip(QtGui.QApplication.translate("LinearTrackUI", "Trigger active/inactive", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_trigger.setText(QtGui.QApplication.translate("LinearTrackUI", "Trigger", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_runtime.setStatusTip(QtGui.QApplication.translate("LinearTrackUI", "Total runtime since first trigger", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_right_water.setText(QtGui.QApplication.translate("LinearTrackUI", "Right Water", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_right_waterreward.setStatusTip(QtGui.QApplication.translate("LinearTrackUI", "Right solenoid open time in [ms]", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_right_waterreward.setText(QtGui.QApplication.translate("LinearTrackUI", "ms", None, QtGui.QApplication.UnicodeUTF8))
        self.lcd_right_triggers.setStatusTip(QtGui.QApplication.translate("LinearTrackUI", "# right triggers", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_left_water.setText(QtGui.QApplication.translate("LinearTrackUI", "Left Water", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_left_waterreward.setStatusTip(QtGui.QApplication.translate("LinearTrackUI", "Left solenoid open time in [ms]", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_left_waterreward.setText(QtGui.QApplication.translate("LinearTrackUI", "ms", None, QtGui.QApplication.UnicodeUTF8))
        self.lcd_left_triggers.setStatusTip(QtGui.QApplication.translate("LinearTrackUI", "# left triggers", None, QtGui.QApplication.UnicodeUTF8))
