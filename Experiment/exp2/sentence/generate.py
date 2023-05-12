import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget, QApplication, QGroupBox, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, \
    QGridLayout, QFormLayout, QLineEdit, QTextEdit
from PyQt5.QtGui import QIcon
import prepare


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        title = QLabel('输入首词')
        title2 = QLabel('输入词数')
        button = QPushButton('start', self)

        self.titleEdit = QLineEdit("")
        self.titleEdit2 = QLineEdit("")
        self.reviewEdit = QTextEdit("")

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(self.titleEdit, 1, 1)
        grid.addWidget(title2, 2, 0)
        grid.addWidget(self.titleEdit2, 2, 1)

        grid.addWidget(button, 3, 0)
        grid.addWidget(self.reviewEdit, 3, 1, 6, 1)

        self.setLayout(grid)
        self.setGeometry(300, 300, 450, 400)
        self.setWindowTitle('自动生成句子')
        button.clicked.connect(self.action)
        self.show()

    def action(self):
        name = self.titleEdit.text()
        num = self.titleEdit2.text()
        if num == '':
            num = '20'
        if name == '':
            name = '<BOS>'
        self.reviewEdit.setText(prepare.makesen(name, int(num)))


if __name__ == '__main__':
    prepare.loading()
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
