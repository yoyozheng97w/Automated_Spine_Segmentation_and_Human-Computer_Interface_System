# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addPtWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(307, 162)
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.name_line_ed = QtWidgets.QLineEdit(Dialog)
        self.name_line_ed.setObjectName("name_line_ed")
        self.horizontalLayout.addWidget(self.name_line_ed)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.birthday = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.birthday.setFont(font)
        self.birthday.setObjectName("birthday")
        self.horizontalLayout_2.addWidget(self.birthday)
        spacerItem1 = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.bd_day_edt = QtWidgets.QDateEdit(Dialog)
        self.bd_day_edt.setMinimumSize(QtCore.QSize(155, 0))
        self.bd_day_edt.setObjectName("bd_day_edt")
        self.horizontalLayout_2.addWidget(self.bd_day_edt)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.no = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.no.setFont(font)
        self.no.setObjectName("no")
        self.horizontalLayout_3.addWidget(self.no)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.no_line_edt = QtWidgets.QLineEdit(Dialog)
        self.no_line_edt.setObjectName("no_line_edt")
        self.horizontalLayout_3.addWidget(self.no_line_edt)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.submit = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        self.horizontalLayout_4.addWidget(self.submit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.name.setText(_translate("Dialog", "Name"))
        self.birthday.setText(_translate("Dialog", "Birthday"))
        self.no.setText(_translate("Dialog", "No."))
        self.submit.setText(_translate("Dialog", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
