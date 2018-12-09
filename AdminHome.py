import sys
import time
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class AdminHome(QWidget):
    def __init__(self, admin_name):
        super().__init__()

        self.admin_name = admin_name
        self.initUI()

    def initUI(self):
        self.h_layout = QHBoxLayout()
        self.h1_layout = QHBoxLayout()
        self.h2_layout = QHBoxLayout()
        self.layout = QVBoxLayout()

        self.label_font = QFont()
        self.label_font.setPixelSize(30)
        self.button_font = QFont()
        self.button_font.setPixelSize(22)

        welcome_label = QLabel('       %s,欢迎使用图书管理系统' % self.admin_name)
        welcome_label.setFont(self.label_font)
        welcome_label.setFixedWidth(600)
        welcome_label.setFixedHeight(200)
        book_manage = QPushButton('书籍管理')
        book_manage.setFixedWidth(100)
        # book_manage.setFixedHeight()
        book_manage.setFont(self.button_font)
        user_manage = QPushButton('读者管理')
        user_manage.setFixedWidth(100)
        user_manage.setFont(self.button_font)

        self.h_layout.addWidget(welcome_label, Qt.AlignCenter)
        # welcome_label.setStyleSheet('background:#adae12')
        self.h1_layout.addWidget(book_manage, Qt.AlignCenter)
        self.h2_layout.addWidget(user_manage, Qt.AlignCenter)

        widget1 = QWidget()
        widget1.setLayout(self.h_layout)
        widget2 = QWidget()
        widget2.setLayout(self.h1_layout)
        widget3 = QWidget()
        widget3.setLayout(self.h2_layout)

        self.layout.addWidget(widget1)
        self.layout.addWidget(widget2)
        self.layout.addWidget(widget3)
        self.layout.addStretch(1)

        self.setLayout(self.layout)

        # 初始化界面
        self.setWindowTitle('书籍管理')
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.resize(600, 400)
        self.move((screen.width() - size.width()) / 2 - 100, (screen.height() - size.height()) / 2 - 100)
        self.setWindowIcon(QIcon("./imagesSourse/user_icon2.png"))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdminHome('王正文')
    sys.exit(app.exec_())