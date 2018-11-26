import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *


class SignIn(QWidget):
    is_admin_signal = pyqtSignal()
    is_student_signal = pyqtSignal(str)

    def __init__(self):
        super(SignIn, self).__init__()
        #  初始布局变量设置
        self.v_layout = QVBoxLayout()
        self.form_layout = QFormLayout()
        self.h_layout1 = QHBoxLayout()
        self.h_layout2 = QHBoxLayout()
        self.h_layout3 = QHBoxLayout()

        #  字体设置
        self.welcome_label_font = QFont()
        self.welcome_label_font.setPixelSize(30)
        self.label_font = QFont()
        self.label_font.setPixelSize(18)
        self.line_edit_font = QFont()
        self.line_edit_font.setPixelSize(16)
        self.password_label_font = QFont()
        self.password_label_font.setPixelSize(18)
        self.password_line_edit_font = QFont()
        self.password_line_edit_font.setPixelSize(15)
        self.sign_button_font = QFont()
        self.sign_button_font.setPixelSize(18)
        self.init_ui()

    def init_ui(self):
        #  欢迎标签
        self.welcome_label = QLabel('欢迎登陆图书管理系统')
        self.welcome_label.setFont(self.welcome_label_font)
        self.welcome_label.setFixedWidth(300)

        #  学号及输入框设置
        self.student_id_label = QLabel("学 号： ")
        self.student_id_label.setFont(self.label_font)
        self.student_line_edit = QLineEdit()
        self.student_line_edit.setFixedHeight(32)
        self.student_line_edit.setFixedWidth(180)
        self.student_line_edit.setFont(self.line_edit_font)
        self.student_line_edit.setMaxLength(12)

        # 密码及输入框设置
        self.password_label = QLabel('密 码： ')
        self.password_label.setFont(self.password_label_font)
        self.password_line_edit = QLineEdit()
        self.password_line_edit.setFont(self.password_line_edit_font)
        self.password_line_edit.setFixedWidth(180)
        self.password_line_edit.setFixedHeight(32)
        self.password_line_edit.setMaxLength(16)

        # 登陆按钮设置
        self.sign_button = QPushButton('登陆')
        self.sign_button.setFixedWidth(75)
        self.sign_button.setFixedHeight(40)
        self.sign_button.setFont(self.sign_button_font)

        # 将布局或者组件添加到布局中去
        self.form_layout.addRow(self.student_id_label, self.student_line_edit)
        self.form_layout.addRow(self.password_label, self.password_line_edit)
        self.h_layout1.addWidget(self.welcome_label, Qt.AlignCenter)
        self.widget1= QWidget()
        self.widget1.setLayout(self.h_layout1)
        self.widget2 = QWidget()
        self.widget2.setFixedHeight(100)
        self.widget2.setFixedWidth(300)
        self.widget2.setLayout(self.form_layout)
        self.h_layout2.addWidget(self.widget2, Qt.AlignCenter)
        self.widget3 = QWidget()
        self.widget3.setLayout(self.h_layout2)
        self.widget4 = QWidget()
        self.h_layout3.addWidget(self.sign_button, Qt.AlignCenter)
        self.widget4.setLayout(self.h_layout3)

        self.v_layout.addWidget(self.widget1, Qt.AlignCenter)
        self.v_layout.addWidget(self.widget3, Qt.AlignCenter)
        self.v_layout.addWidget(self.widget4, Qt.AlignCenter)
        self.setLayout(self.v_layout)

        # 初始化界面
        self.setWindowTitle('图书管理系统')
        self.setGeometry(100, 100, 900, 600)
        self.setWindowIcon(QIcon("book_icon2.png"))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SignIn()
    sys.exit(app.exec_())