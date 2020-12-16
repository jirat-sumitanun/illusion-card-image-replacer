import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets

class ImageLabel(QtWidgets.QLabel):
    def __init__(self,parent):
        super().__init__(parent)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.setFont(font)
        self.setText('Replace image')
        self.setGeometry(QtCore.QRect(500, 20, 361, 361))
        self.setFixedSize(361,361)
        self.setAcceptDrops(True)
        self.setFrameShape(QtWidgets.QFrame.Box)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setObjectName("replaceImage")
        self.path = ''
        self.setStyleSheet('''
            QLabel{
                background-color: #d9ffff;
                border: 4px dashed #aaa;
            }
        ''')


    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(QtCore.Qt.CopyAction)
            self.path = event.mimeData().urls()[0].toLocalFile()
            self.set_image(self.path)
            #self.path = file_path
            event.accept()
        else:
            event.ignore()

    def set_image(self, file_path):
        self.setPixmap(QtGui.QPixmap(file_path).scaled(self.width(), self.height(), QtCore.Qt.KeepAspectRatioByExpanding))
        
    def reset_data(self):
        self.setText('Replace image')
        self.path = ""
    # def setPixmap(self, image):
    #     print(image)
    #     super().setPixmap(image.scaled(self.width(), self.height(), QtCore.Qt.KeepAspectRatioByExpanding))