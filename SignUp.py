import sys
import hashlib
import qdarkstyle
from PyQt5.QtWidgets import   *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *


# 注册界面类
class SignUpWidget(QWidget):
    student_signup_signal = pyqtSignal(str)  # 自定义信号和槽

    def __init__(self):
        super().__init__()

        self.initUI()

    #  注册界面初始化函数
    def initUI(self):
        # 设置标签字体大小
        font = QFont()
        font.setPixelSize(36)

        # 注册标签
        self.sign_up_label = QLabel('欢迎注册', self)
        self.sign_up_label.setAlignment(Qt.AlignCenter)  # 设置标签水平居中
        self.sign_up_label.setFont(font)
        self.sign_up_label.setFixedHeight(100)  # 设置标签高度

        # 设置输入框字体大小
        line_edit_font = QFont()
        line_edit_font.setPixelSize(20)

        # 设置盒布局的垂直布局方式
        self.box_layout = QVBoxLayout(self)
        self.box_layout.addWidget(self.sign_up_label)
        self.setLayout(self.box_layout)


        # 设置表格布局
        self.form_layout = QFormLayout(self)
        font.setPixelSize(16)

        # 创建学号表单
        self.id_label = QLabel('学  号:')
        self.id_label.setFont(font)
        self.id_line_edit = QLineEdit()
        self.id_line_edit.setFixedHeight(30)
        self.id_line_edit.setFixedWidth(200)
        self.id_line_edit.setFont(line_edit_font)

        # 创建姓名输入表单
        self.name_label = QLabel('姓  名:')
        self.name_label.setFont(font)
        self.name_line_edit = QLineEdit()
        self.name_line_edit.setFixedHeight(30)
        self.name_line_edit.setFixedWidth(200)
        self.name_line_edit.setFont(line_edit_font)

        # 创建性别输入表单
        self.sex_label = QLabel('姓  别:')
        self.sex_label.setFont(font)
        self.sex_line_edit = QLineEdit()
        self.sex_line_edit.setFixedHeight(30)
        self.sex_line_edit.setFixedWidth(200)
        self.sex_line_edit.setFont(line_edit_font)

        # 创建系输入表单
        self.deparment_label = QLabel('系  名:')
        self.deparment_label.setFont(font)
        self.deparment_line_edit = QLineEdit()
        self.deparment_line_edit.setFixedHeight(30)
        self.deparment_line_edit.setFixedWidth(200)
        self.deparment_line_edit.setFont(line_edit_font)

        # 创建系输入表单
        self.grade_label = QLabel('年  级:')
        self.grade_label.setFont(font)
        self.grade_line_edit = QLineEdit()
        self.grade_line_edit.setFixedHeight(30)
        self.grade_line_edit.setFixedWidth(200)
        self.grade_line_edit.setFont(line_edit_font)

        # 创建密码输入表单
        self.password_label = QLabel('密  码:')
        self.password_label.setFont(font)
        self.password_line_edit = QLineEdit()
        self.password_line_edit.setFixedHeight(30)
        self.password_line_edit.setFixedWidth(200)
        self.password_line_edit.setFont(line_edit_font)
        self.password_line_edit.setContextMenuPolicy(Qt.NoContextMenu)  # 不允许出现复制粘贴菜单
        self.password_line_edit.setEchoMode(QLineEdit.Password)  # 输入方式为密码输入，不看直接看见

        # 创建确认密码菜单
        self.password_confirm_label = QLabel('确认密码:')
        self.password_confirm_label.setFont(font)
        self.password_confirm_line_edit = QLineEdit()
        self.password_confirm_line_edit.setFixedHeight(30)
        self.password_confirm_line_edit.setFixedWidth(200)
        self.password_confirm_line_edit.setFont(line_edit_font)
        self.password_confirm_line_edit.setContextMenuPolicy(Qt.NoContextMenu)  # 不允许出现复制粘贴菜单
        self.password_confirm_line_edit.setEchoMode(QLineEdit.Password)

        # 设置注册按钮
        self.sign_up_button = QPushButton('注 册')
        self.sign_up_button.setFont(font)
        self.sign_up_button.setFixedWidth(130)
        self.sign_up_button.setFixedHeight(35)

        # 将所有表单组建添加到表单布局中
        self.form_layout.addRow(self.id_label, self.id_line_edit)
        self.form_layout.addRow(self.name_label, self.name_line_edit)
        self.form_layout.addRow(self.sex_label, self.sex_line_edit)
        self.form_layout.addRow(self.deparment_label, self.deparment_line_edit)
        self.form_layout.addRow(self.grade_label, self.grade_line_edit)
        self.form_layout.addRow(self.password_label, self.password_line_edit)
        self.form_layout.addRow(self.password_confirm_label, self.password_confirm_line_edit )
        self.form_layout.addRow('',  self.sign_up_button)
        #self.form_layout.addWidget(self.sign_up_button)

        # 将表单布局转化为组件添加到布局中
        form_widget = QWidget()
        form_widget.setLayout(self.form_layout)
        form_widget.setFixedHeight(380)
        form_widget.setFixedWidth(320)
        self.Hlayout = QHBoxLayout()
        self.Hlayout.addWidget(form_widget, Qt.AlignCenter)
        widget = QWidget()
        widget.setLayout(self.Hlayout)
        self.box_layout.addWidget(widget, Qt.AlignCenter)


        # 设置验证
        id_reg = QRegExp("[0-9]{13}")
        id_validator = QRegExpValidator(id_reg, self)
        self.id_line_edit.setValidator(id_validator)

        self.password_reg = QRegExp("[a-zA-z0-9]+$")
        self.password_validator = QRegExpValidator(self.password_reg, self)
        self.password_line_edit.setValidator(self.password_validator)
        self.password_confirm_line_edit.setValidator(self.password_validator)

        # 触发器
        self.sign_up_button.clicked.connect(self.sign_up)
        self.id_line_edit.returnPressed.connect(self.sign_up)
        self.name_line_edit.returnPressed.connect(self.sign_up)
        self.sex_line_edit.returnPressed.connect(self.sign_up)
        self.deparment_line_edit.returnPressed.connect(self.sign_up)
        self.grade_line_edit.returnPressed.connect(self.sign_up)
        self.password_line_edit.returnPressed.connect(self.sign_up)
        self.password_confirm_line_edit.returnPressed.connect(self.sign_up)

        self.setWindowTitle('欢迎注册图书管理系统')
        self.setGeometry(100, 100, 900, 600)
        self.setWindowIcon(QIcon("./imagesSourse/book_icon2.png"))
        self.show()

    def sign_up(self):
        # 获取学号，姓名，密码，确认密码文本值
        id = self.id_line_edit.text()
        name = self.name_line_edit.text()
        sex = self.sex_line_edit.text()
        department = self.deparment_line_edit.text()
        grade = self.grade_line_edit.text()
        password = self.password_line_edit.text()
        confirm_password = self.password_confirm_line_edit.text()

        #判断是否存在空值
        if (id == '' or name == '' or sex == '' or department == '' or grade == '' or password == '' or confirm_password==''):
            print(QMessageBox.warning(self, '警告', '请填写完整', QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            # 数据库连接
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

            query = QSqlQuery()  # 实例化查询对象，执行和操作SQL语句
            # print(query.exec_("select * from user"))

            # 检测两次密码是否一致
            if (confirm_password != password):
                print(QMessageBox.warning(self, '警告', '两次密码不一致，请重新输入', QMessageBox.Yes, QMessageBox.Yes))
                return
            elif(confirm_password == password):

                # 检测数据库中是否存在相同账号
                sql = "select * from user WHERE StudentId = '%s'" % (id)
                query.exec_(sql)  # 执行SQL语句
                if query.first():  # query.next()判断是否存在记录
                    print(QMessageBox.warning(self, '警告', '账号已经存在，请重新输入', QMessageBox.Yes, QMessageBox.Yes ))
                    return
                else:  # 插入数据
                    sql = "INSERT INTO user VALUES('%s','%s','%s','%s','%s', '%s')" % (id, name, sex, department, grade, password)
                    db.exec_(sql)
                    db.commit()

                    print(db.lastError().text())

                    print(QMessageBox.information(self, '提醒', '注册成功！', QMessageBox.Yes, QMessageBox.Yes))
                    self.student_signup_signal.emit(id)
                db.close()
                return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SignUpWidget()
    sys.exit(app.exec_())










