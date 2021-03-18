# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Spine_Broken.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import addPtWidget

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1068, 743)
		MainWindow.setStyleSheet("")
		self.central_widget = QtWidgets.QWidget(MainWindow)
		self.central_widget.setObjectName("central_widget")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.central_widget)
		self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_2.setSpacing(0)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.header_frame = QtWidgets.QFrame(self.central_widget)
		self.header_frame.setMaximumSize(QtCore.QSize(16777215, 30))
		self.header_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.header_frame.setObjectName("header_frame")
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.header_frame)
		self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_3.setSpacing(0)
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.header_left_frame = QtWidgets.QFrame(self.header_frame)
		self.header_left_frame.setStyleSheet("background-color: rgb(0, 0, 0);")
		self.header_left_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.header_left_frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.header_left_frame.setObjectName("header_left_frame")
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.header_left_frame)
		self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_4.setSpacing(0)
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.header = QtWidgets.QLabel(self.header_left_frame)
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setPointSize(10)
		self.header.setFont(font)
		self.header.setStyleSheet("color: #fff;")
		self.header.setObjectName("header")
		self.horizontalLayout_4.addWidget(self.header)
		self.horizontalLayout_3.addWidget(self.header_left_frame)
		self.top_right_btns = QtWidgets.QFrame(self.header_frame)
		self.top_right_btns.setMaximumSize(QtCore.QSize(100, 16777215))
		self.top_right_btns.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: #76a5af;\n"
"}\n"
"\n"
"QFrame{\n"
"    background-color: #76a5af;\n"
"}")
		self.top_right_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.top_right_btns.setFrameShadow(QtWidgets.QFrame.Raised)
		self.top_right_btns.setObjectName("top_right_btns")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_right_btns)
		self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_2.setSpacing(7)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.minimize_button = QtWidgets.QPushButton(self.top_right_btns)
		self.minimize_button.setText("")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/icons/icons/cil-minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.minimize_button.setIcon(icon)
		self.minimize_button.setIconSize(QtCore.QSize(24, 24))
		self.minimize_button.setObjectName("minimize_button")
		self.horizontalLayout_2.addWidget(self.minimize_button)
		self.restore_button = QtWidgets.QPushButton(self.top_right_btns)
		self.restore_button.setText("")
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(":/icons/icons/cil-window-restore.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.restore_button.setIcon(icon1)
		self.restore_button.setIconSize(QtCore.QSize(24, 24))
		self.restore_button.setObjectName("restore_button")
		self.horizontalLayout_2.addWidget(self.restore_button)
		self.close_button = QtWidgets.QPushButton(self.top_right_btns)
		self.close_button.setText("")
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(":/icons/icons/cil-x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.close_button.setIcon(icon2)
		self.close_button.setIconSize(QtCore.QSize(24, 24))
		self.close_button.setObjectName("close_button")
		self.horizontalLayout_2.addWidget(self.close_button)
		self.horizontalLayout_3.addWidget(self.top_right_btns)
		self.verticalLayout_2.addWidget(self.header_frame)
		self.frame_mian_body = QtWidgets.QFrame(self.central_widget)
		self.frame_mian_body.setStyleSheet("QFrame{\n"
"    background-color: #4F4F4F\n"
"}")
		self.frame_mian_body.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.frame_mian_body.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_mian_body.setObjectName("frame_mian_body")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_mian_body)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setSpacing(0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.frame_left_menu = QtWidgets.QFrame(self.frame_mian_body)
		self.frame_left_menu.setMaximumSize(QtCore.QSize(200, 16777215))
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setPointSize(9)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(50)
		self.frame_left_menu.setFont(font)
		self.frame_left_menu.setStyleSheet("QFrame{\n"
"    font: 9pt \"Verdana\";\n"
"    background-color: #8E8E8E;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: #8E8E8E;\n"
"    color: #fff;\n"
"}\n"
"QLabel{\n"
"    color: #fff;\n"
"}\n"
"\n"
"\n"
"")
		self.frame_left_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_left_menu.setObjectName("frame_left_menu")
		self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.menu_toggle = QtWidgets.QPushButton(self.frame_left_menu)
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setPointSize(16)
		self.menu_toggle.setFont(font)
		self.menu_toggle.setStyleSheet("")
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap(":/icons/icons/cil-menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.menu_toggle.setIcon(icon3)
		self.menu_toggle.setIconSize(QtCore.QSize(36, 36))
		self.menu_toggle.setFlat(True)
		self.menu_toggle.setObjectName("menu_toggle")
		self.verticalLayout_3.addWidget(self.menu_toggle, 0, QtCore.Qt.AlignLeft)
		self.add_patient = QtWidgets.QPushButton(self.frame_left_menu)
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setPointSize(14)
		self.add_patient.setFont(font)
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap(":/icons/icons/cil-user-follow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.add_patient.setIcon(icon4)
		self.add_patient.setFlat(True)
		self.add_patient.setObjectName("add_patient")
		self.verticalLayout_3.addWidget(self.add_patient, 0, QtCore.Qt.AlignLeft)
		self.line_1 = QtWidgets.QFrame(self.frame_left_menu)
		self.line_1.setStyleSheet("color: #fff;")
		self.line_1.setFrameShadow(QtWidgets.QFrame.Plain)
		self.line_1.setLineWidth(1)
		self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_1.setObjectName("line_1")
		self.verticalLayout_3.addWidget(self.line_1)
		self.search = QtWidgets.QPushButton(self.frame_left_menu)
		self.search.setEnabled(True)
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setPointSize(14)
		self.search.setFont(font)
		icon5 = QtGui.QIcon()
		icon5.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-search-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.search.setIcon(icon5)
		self.search.setFlat(True)
		self.search.setObjectName("search")
		self.verticalLayout_3.addWidget(self.search, 0, QtCore.Qt.AlignLeft)
		self.line_2 = QtWidgets.QFrame(self.frame_left_menu)
		self.line_2.setStyleSheet("color: #fff;")
		self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
		self.line_2.setLineWidth(1)
		self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_2.setObjectName("line_2")
		self.verticalLayout_3.addWidget(self.line_2)
		self.patients = QtWidgets.QPushButton(self.frame_left_menu)
		self.patients.setEnabled(False)
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setPointSize(14)
		self.patients.setFont(font)
		icon6 = QtGui.QIcon()
		icon6.addPixmap(QtGui.QPixmap(":/icons/icons/cil-people.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.patients.setIcon(icon6)
		self.patients.setFlat(True)
		self.patients.setObjectName("patients")
		self.verticalLayout_3.addWidget(self.patients, 0, QtCore.Qt.AlignLeft)
		self.line_3 = QtWidgets.QFrame(self.frame_left_menu)
		self.line_3.setStyleSheet("color: #fff;")
		self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
		self.line_3.setLineWidth(1)
		self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_3.setObjectName("line_3")
		self.verticalLayout_3.addWidget(self.line_3)
		self.patient_list = QtWidgets.QListWidget(self.frame_left_menu)
		self.patient_list.setObjectName("patient_list")
		self.verticalLayout_3.addWidget(self.patient_list)
		self.horizontalLayout.addWidget(self.frame_left_menu)
		self.frame_right = QtWidgets.QFrame(self.frame_mian_body)
		self.frame_right.setMinimumSize(QtCore.QSize(0, 0))
		self.frame_right.setStyleSheet("QFrame{\n"
"    background-color: #4F4F4F\n"
"}")
		self.frame_right.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.frame_right.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_right.setObjectName("frame_right")
		self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_right)
		self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_4.setSpacing(0)
		self.verticalLayout_4.setObjectName("verticalLayout_4")
		self.recently_frame = QtWidgets.QFrame(self.frame_right)
		font = QtGui.QFont()
		font.setPointSize(14)
		self.recently_frame.setFont(font)
		self.recently_frame.setStyleSheet("QLabel{\n"
"    color: #fff;\n"
"}")
		self.recently_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.recently_frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.recently_frame.setObjectName("recently_frame")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.recently_frame)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.recently_viewed = QtWidgets.QLabel(self.recently_frame)
		self.recently_viewed.setMaximumSize(QtCore.QSize(16777215, 50))
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setPointSize(24)
		self.recently_viewed.setFont(font)
		self.recently_viewed.setObjectName("recently_viewed")
		self.verticalLayout.addWidget(self.recently_viewed, 0, QtCore.Qt.AlignHCenter)
		self.recently_list = QtWidgets.QListWidget(self.recently_frame)
		font = QtGui.QFont()
		font.setFamily("Verdana")
		font.setPointSize(10)
		self.recently_list.setFont(font)
		self.recently_list.setObjectName("recently_list")
		self.verticalLayout.addWidget(self.recently_list)
		self.verticalLayout_4.addWidget(self.recently_frame)
		self.tool_box = QtWidgets.QFrame(self.frame_right)
		self.tool_box.setMinimumSize(QtCore.QSize(0, 70))
		self.tool_box.setMaximumSize(QtCore.QSize(16777215, 70))
		self.tool_box.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(118, 165, 175);\n"
"}\n"
"")
		self.tool_box.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.tool_box.setFrameShadow(QtWidgets.QFrame.Raised)
		self.tool_box.setObjectName("tool_box")
		self.verticalLayout_4.addWidget(self.tool_box)
		self.horizontalLayout.addWidget(self.frame_right)
		self.verticalLayout_2.addWidget(self.frame_mian_body)
		MainWindow.setCentralWidget(self.central_widget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		self.backend()

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.header.setText(_translate("MainWindow", "脊椎檢測DICOM"))
		self.menu_toggle.setText(_translate("MainWindow", "MENU"))
		self.add_patient.setText(_translate("MainWindow", "Add Patient"))
		self.search.setText(_translate("MainWindow", "Search"))
		self.patients.setText(_translate("MainWindow", "Patients"))
		self.recently_viewed.setText(_translate("MainWindow", "Recently Viewed"))
	
	def backend(self):
		self.add_patient.clicked.connect(self.addPatient)

	def addPatient(self):
		self.Dialog = QtWidgets.QDialog()
		self.ui = addPtWidget.Ui_Dialog()
		self.ui.setupUi(self.Dialog)
		self.Dialog.show()

import nike_app_rc
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
