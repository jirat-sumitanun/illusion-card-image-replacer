# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\workingSpace\python\card_image_replacer\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from module.qImageLabel import ImageLabel
from module.qImageLabel2 import ImageLabel as ImageLabel2

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(922, 520)
        Form.setMinimumSize(QtCore.QSize(922, 520))
        Form.setMaximumSize(QtCore.QSize(922, 520))
        Form.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("formidable01.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.saveBtn = QtWidgets.QPushButton(Form)
        self.saveBtn.setGeometry(QtCore.QRect(590, 450, 100, 31))
        font = QtGui.QFont()
        font.setFamily("FreesiaUPC")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.saveBtn.setFont(font)
        self.saveBtn.setObjectName("saveBtn")
        self.saveAsBtn = QtWidgets.QPushButton(Form)
        self.saveAsBtn.setGeometry(QtCore.QRect(710, 450, 100, 31))
        font = QtGui.QFont()
        font.setFamily("FreesiaUPC")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.saveAsBtn.setFont(font)
        self.saveAsBtn.setObjectName("saveAsBtn")
        self.filename = QtWidgets.QLineEdit(Form)
        self.filename.setGeometry(QtCore.QRect(590, 400, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filename.setFont(font)
        self.filename.setStyleSheet("padding-left:7%;")
        self.filename.setObjectName("filename")
        self.selectReplaceImage = QtWidgets.QPushButton(Form)
        self.selectReplaceImage.setGeometry(QtCore.QRect(190, 410, 121, 71))
        font = QtGui.QFont()
        font.setFamily("FreesiaUPC")
        font.setPointSize(20)
        self.selectReplaceImage.setFont(font)
        self.selectReplaceImage.setObjectName("selectReplaceImage")
        self.selectCard = QtWidgets.QPushButton(Form)
        self.selectCard.setGeometry(QtCore.QRect(50, 410, 101, 71))
        font = QtGui.QFont()
        font.setFamily("FreesiaUPC")
        font.setPointSize(20)
        self.selectCard.setFont(font)
        self.selectCard.setObjectName("selectCard")
        self.clearBtn = QtWidgets.QPushButton(Form)
        self.clearBtn.setGeometry(QtCore.QRect(350, 410, 121, 71))
        font = QtGui.QFont()
        font.setFamily("FreesiaUPC")
        font.setPointSize(25)
        self.clearBtn.setFont(font)
        self.clearBtn.setObjectName("clearBtn")
        self.saveLabel = QtWidgets.QLabel(Form)
        self.saveLabel.setGeometry(QtCore.QRect(640, 490, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.saveLabel.setFont(font)
        self.saveLabel.setStyleSheet("color: rgb(69, 207, 0);")
        self.saveLabel.setText("")
        self.saveLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.saveLabel.setObjectName("saveLabel")
        self.creditLabel = QtWidgets.QLabel(Form)
        self.creditLabel.setGeometry(QtCore.QRect(830, 500, 91, 16))
        self.creditLabel.setObjectName("creditLabel")
        self.card = ImageLabel(Form)
        self.replaceImage = ImageLabel2(Form)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 30, 831, 361))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.addWidget(self.card,0,0)
        self.gridLayout.addWidget(self.replaceImage,0,1)
        self.refreshFilenameBtn = QtWidgets.QPushButton(Form)
        self.refreshFilenameBtn.setGeometry(QtCore.QRect(510, 400, 75, 31))
        self.refreshFilenameBtn.setObjectName("refreshFilenameBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Card image replacer v1.1"))
        self.saveBtn.setText(_translate("Form", "save"))
        self.saveAsBtn.setText(_translate("Form", "save as"))
        self.filename.setPlaceholderText(_translate("Form", "filename"))
        self.selectReplaceImage.setText(_translate("Form", "select replace\n"
"image"))
        self.selectCard.setText(_translate("Form", "select card"))
        self.clearBtn.setText(_translate("Form", "Clear"))
        self.creditLabel.setText(_translate("Form", "created by Jirat.S"))
        self.refreshFilenameBtn.setText(_translate("Form", "refresh\n"
"filename"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
