#! src/Scripts/python
import sys
from os import path as osPath ,getcwd as osGetcwd
from shutil import copy as shutilCopy
from PyQt5 import QtCore, QtGui, QtWidgets
from module.appUi import Ui_Form

class MyApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        # init main window
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # init default data
        self.saveFilename = ''
        self.savePath = ''
        # init button event
        self.ui.selectCard.clicked.connect(self.select_card_event)
        self.ui.selectReplaceImage.clicked.connect(self.select_replace_image_event)
        self.ui.saveBtn.clicked.connect(self.save_file)
        self.ui.saveAsBtn.clicked.connect(self.save_file_as)
        self.ui.clearBtn.clicked.connect(self.clear_button_event)
        self.ui.refreshFilenameBtn.clicked.connect(self.refreshFilename)

    def select_card_event(self):
        self.ui.card.path,filters = QtWidgets.QFileDialog.getOpenFileName(None, 'Select card', filter="*png")
        if self.ui.card.path != "":
            self.ui.saveLabel.setText("")
            self.ui.filename.setText('new_{}'.format(self.ui.card.path.split('/')[-1]))
            self.ui.card.set_image(self.ui.card.path)
        else:
            self.ui.filename.setText("")
            self.ui.saveLabel.setText("")
            self.ui.card.path = ""

    def select_replace_image_event(self):
        self.ui.replaceImage.path,filters =  QtWidgets.QFileDialog.getOpenFileName(None, 'Select replace image', filter="*png")
        if self.ui.replaceImage.path != "":
            self.ui.saveLabel.setText("")
            self.ui.replaceImage.set_image(self.ui.replaceImage.path)
        else:
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
            if not self.savePath.endswith(".png"):
                self.savePath += ".png"
            with open (self.ui.card.path, 'rb') as f:
                s = f.read()
                text = b"IEND\xaeB`\x82"
                temp = s.split(text)
                shutilCopy(self.ui.replaceImage.path ,self.savePath)
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
        self.ui.filename.setText("")
        self.ui.card.reset_data()
        self.ui.replaceImage.reset_data()

    def refreshFilename(self):
        self.ui.filename.setText('new_{}'.format(self.ui.card.path.split('/')[-1]))

    def errorHandler(self):
        if self.ui.card.path == "":
            QtWidgets.QMessageBox.warning(self, "Error", "import card")
            return False
        if self.ui.replaceImage.path == "":
            QtWidgets.QMessageBox.warning(self, "Error", "import replace image")
            return False
        if self.ui.filename.text() == "":
            self.refreshFilename()
            if self.ui.card.path == "":
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