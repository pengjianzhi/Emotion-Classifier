import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import EmotionRecongnition

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = EmotionRecongnition.Ui_MainWindow(MainWindow)  ##Main window object & attuibet
    MainWindow.show()
    sys.exit(app.exec_())

