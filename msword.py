import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
class BSWord(QMainWindow):
    def __init__(self):
        super(BSWord, self).__init__()
        self.editor = QTextEdit()
        self.editor.setFontPointSize(10)
        self.setCentralWidget(self.editor)
        self.font_size_box = QSpinBox()
        self.showMaximized()
        self.setWindowTitle("RanzEditor")
        self.setWindowIcon(QtGui.QIcon("Letter-R-Logo-Vector (1).png"))
        self.create_tool_bar()
    def create_tool_bar(self):
        tool_bar = QToolBar()
        undo_action = QAction('undo', self)
        undo_action.triggered.connect(self.editor.undo)
        tool_bar.addAction(undo_action)
        self.addToolBar(tool_bar)
        tool_bar = QToolBar()
        redo_action = QAction('redo', self)
        redo_action.triggered.connect(self.editor.redo)
        tool_bar.addAction(redo_action)
        cut_action = QAction('cut', self)
        cut_action.triggered.connect(self.editor.cut)
        tool_bar.addAction(cut_action)
        copy_action = QAction('copy', self)
        copy_action.triggered.connect(self.editor.copy)
        tool_bar.addAction(copy_action)
        paste_action = QAction('paste', self)
        paste_action.triggered.connect(self.editor.paste)
        tool_bar.addAction(paste_action)
        self.font_size_box.setValue(10)
        self.font_size_box.valueChanged.connect(self.set_font_size)
        tool_bar.addWidget(self.font_size_box)
        self.addToolBar(tool_bar)
    def set_font_size(self):
        value = self.font_size_box.value()
        self.editor.setFontPointSize(value)
app = QApplication(sys.argv)
window = BSWord()
window.show()
sys.exit(app.exec_())