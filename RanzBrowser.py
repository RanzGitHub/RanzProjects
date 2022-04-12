import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtWebEngineWidgets import *
class  MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        #Icon
        self.setWindowIcon(QtGui.QIcon('Letter-R-Logo-Vector (1).png'))
        #Background
        self.setStyleSheet("background-color: orange;")
        #Buttons
        navbar = QToolBar()
        self.addToolBar(navbar)
        back_btn = QAction('<', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        forward_btn = QAction('>', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)
        refresh_btn = QAction('⟳', self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com'))
app = QApplication(sys.argv)
#Name of Browser
QApplication.setApplicationName('                                                                                                                                                                                RanzBrowser')
window = MainWindow()
app.exec_()