# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EmotionRecongnition.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt
from input_classifier import recog_run
import numpy as np
import cv2
import time
from os import getcwd
from base64 import b64decode
from background_png import img as bgImg
from os import remove

class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        self.dir_path = getcwd()
        self.timer_camera = QtCore.QTimer()
        self.cap = cv2.VideoCapture(0)
        self.setupUi(MainWindow)
        self.retranslateUi(MainWindow)
        self.slot_init()
        #self.backgroundimg = 255 * np.zeros((300, 250, 3), np.uint8)
        self.model_path = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(940, 620)
        MainWindow.setMinimumSize(QtCore.QSize(940, 620))
        MainWindow.setMaximumSize(QtCore.QSize(940, 620))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.face_output = QtWidgets.QLabel(self.centralwidget)
        self.face_output.setGeometry(QtCore.QRect(10, 10, 600, 600))
        self.face_output.setMinimumSize(QtCore.QSize(600, 600))
        self.face_output.setMaximumSize(QtCore.QSize(600, 600))
        self.face_output.setMouseTracking(False)
        self.face_output.setStyleSheet("color: rgb(0, 0, 0);\n"
                                       "background-color: rgb(255, 255, 255);")
        self.face_output.setFrameShadow(QtWidgets.QFrame.Plain)
        self.face_output.setText("")
        self.face_output.setObjectName("face_output")
        self.result_output = QtWidgets.QLabel(self.centralwidget)
        self.result_output.setGeometry(QtCore.QRect(630, 360, 300, 250))
        self.result_output.setMinimumSize(QtCore.QSize(300, 250))
        self.result_output.setMaximumSize(QtCore.QSize(300, 250))
        self.result_output.setStyleSheet("color: rgb(0, 0, 0);\n"
                                         "background-color: rgb(255, 255, 255);")
        self.result_output.setText("")
        self.result_output.setObjectName("result_output")
        self.button_camera = QtWidgets.QPushButton(self.centralwidget)
        self.button_camera.setGeometry(QtCore.QRect(630, 80, 150, 40))
        self.button_camera.setMinimumSize(QtCore.QSize(150, 40))
        self.button_camera.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_camera.setFont(font)
        self.button_camera.setObjectName("button_camera")
        self.button_takephoto = QtWidgets.QPushButton(self.centralwidget)
        self.button_takephoto.setGeometry(QtCore.QRect(780, 80, 150, 40))
        self.button_takephoto.setMinimumSize(QtCore.QSize(150, 40))
        self.button_takephoto.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_takephoto.setFont(font)
        self.button_takephoto.setObjectName("button_takephoto")
        self.button_model = QtWidgets.QPushButton(self.centralwidget)
        self.button_model.setGeometry(QtCore.QRect(630, 130, 70, 40))
        self.button_model.setMinimumSize(QtCore.QSize(40, 40))
        self.button_model.setMaximumSize(QtCore.QSize(70, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_model.setFont(font)
        self.button_model.setObjectName("button_model")
        self.textEdit_modelpath = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_modelpath.setGeometry(QtCore.QRect(700, 130, 230, 40))
        self.textEdit_modelpath.setMinimumSize(QtCore.QSize(230, 40))
        self.textEdit_modelpath.setMaximumSize(QtCore.QSize(230, 40))
        self.textEdit_modelpath.setStyleSheet("background-color: transparent;\n"
                                              "border-color: rgb(255, 255, 255);\n"
                                              "color: rgb(255, 255, 255);")
        self.textEdit_modelpath.setObjectName("textEdit_modelpath")
        self.textEdit_imagepath = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_imagepath.setGeometry(QtCore.QRect(700, 30, 230, 40))
        self.textEdit_imagepath.setMinimumSize(QtCore.QSize(230, 40))
        self.textEdit_imagepath.setMaximumSize(QtCore.QSize(230, 40))
        self.textEdit_imagepath.setStyleSheet("background-color: transparent;\n"
                                              "border-color: rgb(255, 255, 255);\n"
                                              "color: rgb(255, 255, 255);")
        self.textEdit_imagepath.setObjectName("textEdit_imagepath")
        self.button_image = QtWidgets.QPushButton(self.centralwidget)
        self.button_image.setGeometry(QtCore.QRect(630, 30, 70, 40))
        self.button_image.setMinimumSize(QtCore.QSize(70, 40))
        self.button_image.setMaximumSize(QtCore.QSize(70, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_image.setFont(font)
        self.button_image.setObjectName("button_image")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(609, 10, 21, 601))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(630, 165, 301, 31))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(630, 340, 301, 31))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(630, 240, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_result.setFont(font)
        self.label_result.setObjectName("label_result")
        self.label_resultoutput = QtWidgets.QLabel(self.centralwidget)
        self.label_resultoutput.setGeometry(QtCore.QRect(769, 240, 160, 50))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_resultoutput.setFont(font)
        self.label_resultoutput.setText("")
        self.label_resultoutput.setObjectName("label_resultoutput")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Emotion Recongnition"))
        self.button_camera.setText(_translate("MainWindow", "Open Camera"))
        self.button_takephoto.setText(_translate("MainWindow", "Take Photo"))
        self.button_model.setText(_translate("MainWindow", "Model"))
        self.textEdit_modelpath.setHtml(_translate("MainWindow",
                                                   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#828282;\">Model Path</span></p></body></html>"))
        self.textEdit_imagepath.setHtml(_translate("MainWindow",
                                                   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#828282;\">Image Path</span></p></body></html>"))
        self.button_image.setText(_translate("MainWindow", "Image"))
        self.label_result.setText(_translate("MainWindow", "Result:"))

    def slot_init(self):
        self.button_image.clicked.connect(self.choose_img)
        self.button_model.clicked.connect(self.choose_model)
        self.button_camera.clicked.connect(self.show_camera)
        self.button_takephoto.clicked.connect(self.take_photo)
        self.timer_camera.timeout.connect(self.display_result)

    def reset_frame(self):
        self.timer_camera.stop()
        self.cap.release()
        self.face_output.clear()
        self.label_resultoutput.clear()

    def choose_img(self):

        self.reset_frame()
        picChoose, filetype = QFileDialog.getOpenFileName(self.centralwidget,"Choose an Image", self.dir_path, "All Files(*)")
        if picChoose != '':
            self.button_image.setText('Done')
            self.textEdit_imagepath.setText(picChoose)
            self.textEdit_imagepath.setStyleSheet("background-color: transparent;\n""border-color: rgb(0, 0, 0);\n""color: rgb(0, 0, 0);")
            QtWidgets.QApplication.processEvents()

            self.emotion_model = recog_run(self.model_path)
            tmp = open('background.png', 'wb')
            tmp.write(b64decode(bgImg))
            tmp.close()
            backgroundImg = cv2.imread('background.png')
            remove('background.png')

            img = cv2.imdecode(np.fromfile(picChoose, dtype=np.uint8), -1)
            QtWidgets.QApplication.processEvents()
            return_label = self.emotion_model.face_recog(backgroundImg, img, self.face_output, self.result_output)
            self.label_resultoutput.setText(return_label)
            self.button_image.setText('Image')
        else:
            self.reset_frame()
        print("Img_button")

    def choose_model(self):
        self.reset_frame()
        modelChoose, filetype = QFileDialog.getOpenFileName(self.centralwidget, "Choose an Model", self.dir_path, "All Files(*)")
        if modelChoose != '':
            self.model_path = modelChoose
            self.textEdit_modelpath.setText(modelChoose)
            self.textEdit_modelpath.setStyleSheet("background-color: transparent;\n""border-color: rgb(0, 0, 0);\n""color: rgb(0, 0, 0);")
        else:
            self.reset_frame()
        print("modle_button")

    def show_camera(self):
        if self.timer_camera.isActive() == False:
            flag = self.cap.open(0)
            if flag == False:
                msg = QtWidgets.QMessageBox.warning(self,'warning', "can not open", buttons=QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QApplication.processEvents()
                self.button_camera.setText('Running')
                self.emotion_model = recog_run(self.model_path)
                QtWidgets.QApplication.processEvents()
                self.timer_camera.start(30)
        else:
            self.button_camera.setText('Open Camera')
            self.timer_camera.stop()
            self.cap.release()
            self.face_output.clear()
        print("Camera_button")

    def take_photo(self):
        print("takephoto_button")

    def display_result(self):
        ret, self.frame = self.cap.read()
        self.frame = cv2.flip(self.frame, 1)

        tmp = open('background.png', 'wb')
        tmp.write(b64decode(bgImg))
        tmp.close()
        backgroundImg = cv2.imread('background.png')
        remove('background.png')

        return_label = self.emotion_model.face_recog(backgroundImg, self.frame, self.face_output, self.result_output)

        self.label_resultoutput.setText(return_label)