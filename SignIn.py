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
        self.student_line_edit.setMaxLength(13)

        # 密码及输入框设置
        self.password_label = QLabel('密 码： ')
        self.password_label.setFont(self.password_label_font)
        self.password_line_edit = QLineEdit()
        self.password_line_edit.setFont(self.password_line_edit_font)
        self.password_line_edit.setFixedWidth(180)
        self.password_line_edit.setFixedHeight(32)
        self.password_line_edit.setMaxLength(16)
        self.password_line_edit.setEchoMode(QLineEdit.Password)

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

        # 为输入内容设置验证
        id_reg = QRegExp('[0-9]{15}')
        id_validator = QRegExpValidator(id_reg, self)
        self.student_line_edit.setValidator(id_validator)

        password_reg = QRegExp("[a-zA-z0-9]+$")
        password_validator = QRegExpValidator(self)
        password_validator.setRegExp(password_reg)
        self.password_line_edit.setValidator(password_validator)

        # 初始化界面
        self.setWindowTitle('图书管理系统')
        self.setGeometry(100, 100, 900, 600)
        self.setWindowIcon(QIcon("book_icon2.png"))
        self.show()

        self.sign_button.clicked.connect(self.sign_in_check)
        self.student_line_edit.returnPressed.connect(self.sign_in_check)
        self.password_line_edit.returnPressed.connect(self.sign_in_check)

    def sign_in_check(self):
        # 获取输入值
        student_id = self.student_line_edit.text()
        password = self.password_line_edit.text()

        # 判断是否存在空值
        if (student_id=='' or password==''):
            print(QMessageBox.warning(self, '提醒', '学号和密码不能为空！', QMessageBox.Yes, QMessageBox.Yes))
            return

        # 打开数据库，建立连接
        db = QSqlDatabase.addDatabase("QMYSQL")
        db.setHostName('localhost')
        db.setDatabaseName('book_management_system')
        db.setUserName('root')
        db.setPassword('wadden@mysql')
        db.open()
        if db.isOpen():
            print('成功连接到数据库')
        else:
            print('数据库连接失败')

        query_student = QSqlQuery()
        query_admin = QSqlQuery()

        student_sql = "SELECT BookId ,BookName,Author,Publisher,PublishTime,NumStorage, NumStorage-NumBorrowed FROM user WHERE StudentId='%s'" % (student_id)
        admin_sql = "SELECT BookId ,BookName,Author,Publisher,PublishTime,NumStorage, NumStorage-NumBorrowed FROM admin WHERE id='%s'" % (student_id)
        # student_sql = "SELECT BookId ,BookName,Author,Publisher,PublishTime,NumStorage, NumStorage-NumBorrowed FROM user WHERE StudentId= '2016141462228'"

        # 开始查找
        query_student.exec_(student_sql)
        query_admin.exec_(admin_sql)

        query_student.next()
        print(query_student.value('StudentId'))
        print(query_student.value('Password'))
        print(query_student.isValid())
        query_admin.next()
        print(query_admin.value('id'))
        print(query_admin.value('password'))
        print(query_admin.isValid())
        query_admin_isValid = query_admin.isValid()
        query_student_isValid = query_student.isValid()


        # print(query_admin.lastError())
        '''
        print(student_id)
        print(query_student.next())
        print(query_student.value(5))
        '''
        db.close()

        if (not query_admin.first()) and (not query_student.first()):
            print(QMessageBox.information(self, '提示', '账号不存在，请重新输入！', QMessageBox.Yes, QMessageBox.Yes))
        elif query_admin.first():
            if student_id == str(query_admin.value('id')):
                if password == query_admin.value('password'):
                    print(QMessageBox.information(self, '提示', '登陆成功！', QMessageBox.Yes, QMessageBox.Yes))
                    self.is_admin_signal.emit()
                else:
                    print(QMessageBox.information(self, '提示', '密码错误', QMessageBox.Yes, QMessageBox.Yes))
            else:
                print(QMessageBox.information(self, '提示', '管理员这里存在错误', QMessageBox.Yes, QMessageBox.Yes))
        elif query_student.first():
            if student_id == query_student.value('StudentId'):
                if password == query_student.value('Password'):
                    print(QMessageBox.information(self, '提示', '登陆成功！', QMessageBox.Yes, QMessageBox.Yes))
                    self.is_student_signal.emit(student_id)
                else:
                    print(QMessageBox.information(self, '提示', '密码错误', QMessageBox.Yes, QMessageBox.Yes))
        else:
            print(QMessageBox.information(self, '提示', '有问题存在', QMessageBox.Yes, QMessageBox.Yes))
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SignIn()
    sys.exit(app.exec_())