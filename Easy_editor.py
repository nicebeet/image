from PyQt5.QtWidgets import (
    QApplication,QWidget,QFileDialog,QLabel,QPushButton,QListWidget,QHBoxLayout,QVBoxLayout
)
import os 

app = QApplication([])
win = QWidget()
win.resize(700,500)
win.setWindowTitle("Ешкереееееееее")

but_folder = QPushButton("Folder")
but_left  = QPushButton("Left")
but_right = QPushButton("rigth")
but_mirros = QPushButton("mirror")
but_bv = QPushButton("b/w")
but_blur = QPushButton("blure")

list = QListWidget()
lable_image = QLabel("Picture")

lineH = QHBoxLayout()
lineH2 = QHBoxLayout()

lineV = QVBoxLayout()
lineV2 = QVBoxLayout()

lineV.addWidget(but_folder)
lineV.addWidget(list)

lineH2.addWidget(but_left)
lineH2.addWidget(but_right)
lineH2.addWidget(but_mirros)
lineH2.addWidget(but_blur)
lineH2.addWidget(but_bv)

lineV2.addWidget(lable_image)
lineV2.addLayout(lineH2)

lineH.addLayout(lineV,25)
lineH.addLayout(lineV2,75)

win.setLayout(lineH)

win.show()

def filter(files,image_show):
    result = []
    for filename in files:
        for e in image_show:
            if filename.endswith(e):
                result.append(filename)
    return result

workdir = ""

def showDir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def showfile():
    image_show = [".png",".jpg",".jpeg",".gif",".bmp"]
    showDir()
    filenames = filter(os.listdir(workdir),image_show)
    list.clear()
    for filename in filenames:
        list.addItem(filename)

but_folder.clicked.connect(showfile)

app.exec_()