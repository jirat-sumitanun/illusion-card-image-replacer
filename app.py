#! src/Scripts/python
import sys
from os import path as osPath ,getcwd as osGetcwd
from shutil import copy as shutilCopy
from PyQt5 import QtCore, QtGui, QtWidgets
from main import Ui_Form
from qImageLabel import ImageLabel

class MyApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        # init main window
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # init default data
        self.current_card = ''
        self.current_replace_image = ''
        self.saveFilename = ''
        self.savePath = ''
        # init button event
        self.ui.selectCard.clicked.connect(self.select_card_event)
        self.ui.selectReplaceImage.clicked.connect(self.select_replace_image_event)
        self.ui.saveBtn.clicked.connect(self.save_file)
        self.ui.saveAsBtn.clicked.connect(self.save_file_as)
        self.ui.clearBtn.clicked.connect(self.clear_button_event)

    def select_card_event(self):
        self.current_card,filters = QtWidgets.QFileDialog.getOpenFileName(None, 'Select card', filter="*png")
        if self.current_card != "":
            self.ui.saveLabel.setText("")
            self.saveFilename = 'new_{}'.format(self.current_card.split('/')[-1])
            self.ui.filename.setText(self.saveFilename)
            self.ui.card.setPixmap(
                QtGui.QPixmap(
                    "{}".format(self.current_card)
                    ).scaled(self.ui.card.width(), self.ui.card.height(), QtCore.Qt.KeepAspectRatio)
                )
        else:
            self.current_card = ""
            self.ui.filename.setText("")
            self.ui.card.setText("card")
            self.ui.saveLabel.setText("")

    def select_replace_image_event(self):
        self.current_replace_image,filters =  QtWidgets.QFileDialog.getOpenFileName(None, 'Select replace image', filter="*png")
        if self.current_replace_image != "":
            self.ui.saveLabel.setText("")
            self.ui.replaceImage.setPixmap(
                QtGui.QPixmap(
                    "{}".format(self.current_replace_image)
                    ).scaled(self.ui.replaceImage.width(), self.ui.replaceImage.height(), QtCore.Qt.KeepAspectRatioByExpanding)
                )
        else:
            self.current_replace_image = ""
            self.ui.replaceImage.setText("replace image")
            self.ui.saveLabel.setText("")
    
    def save_file(self):
        if self.errorHandler():
            self.saveFilename = self.ui.filename.text()
            self.savePath = osPath.join(osGetcwd(), self.saveFilename)
            self.create_new_card()
            self.save_success_message()
    
    def save_file_as(self):
        if self.errorHandler():
            self.saveFilename = self.ui.filename.text()
            dirs,filters = QtWidgets.QFileDialog.getSaveFileName(None, 'Save new card',self.saveFilename, filter="*png")
            if dirs != "":
                self.savePath = dirs
                self.create_new_card()
                self.save_success_message()

    def create_new_card(self):
        try:
            with open (self.current_card, 'rb') as f:
                s = f.read()
                text = b"IEND\xaeB`\x82"
                temp = s.split(text)
                shutilCopy(self.current_replace_image ,self.savePath)
                with open (self.savePath, 'ab') as newCard:
                    for i in range(1,len(temp)):
                        newCard.write(temp[i])
                        newCard.write(text)
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", "capture this and report to dev\n{}".format(e))

    def save_success_message(self):
        self.ui.saveLabel.setText("saved!")

    def clear_button_event(self):
        self.ui.saveLabel.setText("")
        self.current_card = ""
        self.ui.filename.setText("")
        self.ui.card.setText("card")
        self.current_replace_image = ""
        self.ui.replaceImage.setText("replace image")

    def errorHandler(self):
        if self.current_card == "":
            QtWidgets.QMessageBox.warning(self, "Error", "import card")
            return False
        if self.current_replace_image == "":
            QtWidgets.QMessageBox.warning(self, "Error", "import replace image")
            return False
        if self.ui.filename.text() == "":
            QtWidgets.QMessageBox.warning(self, "Error", "fill filename")
            return False
        return True

def main():
    try:
        app = QtWidgets.QApplication(sys.argv)
        myapp = MyApp()
        myapp.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
if __name__== "__main__" :
    main()