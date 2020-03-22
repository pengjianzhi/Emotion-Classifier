import cv2
import imutils
from PyQt5 import QtGui, QtWidgets
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import numpy as np
import time, datetime


class recog_run:
    def __init__(self, model_path=None):

        self.img_save_path = None

        if model_path == None:
            classifier_path = 'Test_model.hdf5'  ##test model
        else:
            classifier_path = model_path

        self.face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        self.emotion_classifier = load_model(classifier_path, compile=False)
        self.EMOTIONS = ["angry", "disgust", "scared", "happy", "sad", "surprised", "neutral"]

    def face_recog(self, backgroundImg, frame_in, face_output, result_output, button_control):

        result_preb = []
        result = None
        frame = imutils.resize(frame_in, width=600)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(48, 48))

        if len(faces) > 0:
            faces = sorted(faces, reverse=True, key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]

            (x, y, w, h) = faces
            roi = gray[y:y + h, x:x + w]
            roi = cv2.resize(roi, (48, 48))

            if button_control == 1:
                timeNow = time.strftime("%Y-%b-%d %H-%M-%S")
                self.img_save_path = "photo\selfPhoto_" + timeNow + ".png"
                print(self.img_save_path)
                cv2.imshow("Roi", roi)
                cv2.imwrite(self.img_save_path, roi)
                button_control == 0

            roi = roi.astype("float")
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)

            result_preb = self.emotion_classifier.predict(roi)[0]
            result = self.EMOTIONS[result_preb.argmax()]

            cv2.putText(frame, result, (x, y - 10), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 0), 1)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2, 8, 0)

        for (i, (emotion, per)) in enumerate(zip(self.EMOTIONS, result_preb)):
            text = "{}: {:.2f}%".format(emotion, per * 100)
            lenth = int(per * 300)
            cv2.rectangle(backgroundImg, (0, (i * 39) + 3), (lenth, (i * 39) + 35), (150, 180, 90), -1)
            cv2.putText(backgroundImg, text, (10, (i * 39) + 29), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 0), 1)

        frame = cv2.resize(frame, (600, 600))
        show = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        face_output.setPixmap(QtGui.QPixmap.fromImage(showImage))

        show = cv2.cvtColor(backgroundImg, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], show.shape[1] * show.shape[2],
                                 QtGui.QImage.Format_RGB888)
        result_output.setPixmap(QtGui.QPixmap.fromImage(showImage))

        QtWidgets.QApplication.processEvents()

        return result
