import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *


class AddUserDialog(QDialog):
    add_user_success_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(AddUserDialog, self).__init__(parent)

        self.initUI()

    def initUI(self):
        self.layout = QFormLayout()
        self.setLayout(self.layout)
        self.layout.setVerticalSpacing(10)

        font = QFont()
        font.setPixelSize(20)
        title_label_font = QFont()
        title_label_font.setPixelSize(20)

        self.title_label = QLabel(' 添加读者')
        self.title_label.setFont(title_label_font)
        self.title_label.setMargin(8)

        self.user_id_label = QLabel("学   号:")
        self.user_id_label.setFont(font)
        self.user_id_edit = QLineEdit()
        self.user_id_edit.setFont(font)
        self.user_id_edit.setFixedWidth(180)
        self.user_id_edit.setFixedHeight(28)

        self.user_name_label = QLabel('姓   名:')
        self.user_name_label.setFont(font)
        self.user_name_edit = QLineEdit()
        self.user_name_edit.setFont(font)

        self.user_sex_label = QLabel('性   别:')
        self.user_sex_label.setFont(font)
        self.user_sex_edit = QLineEdit()
        self.user_sex_edit.setFont(font)

        self.user_department_label = QLabel('  系  :')
        self.user_department_label.setFont(font)
        self.user_department_edit = QLineEdit()
        self.user_department_edit.setFont(font)

        self.user_grade_label = QLabel('年  级:')
        self.user_grade_label.setFont(font)
        self.user_grade_edit = QLineEdit()
        self.user_grade_edit.setFont(font)

        self.user_password_label = QLabel('密   码:')
        self.user_password_label.setFont(font)
        self.user_password_edit = QLineEdit()
        self.user_password_edit.setFont(font)
        self.user_password_edit.setContextMenuPolicy(Qt.NoContextMenu)  # 不允许出现复制粘贴菜单
        self.user_password_edit.setEchoMode(QLineEdit.Password)  # 输入方式为密码输入，不看直接看见

        # 创建确认密码菜单
        self.password_confirm_label = QLabel('确认密码:')
        self.password_confirm_label.setFont(font)
        self.password_confirm_line_edit = QLineEdit()
        self.password_confirm_line_edit.setFont(font)
        self.password_confirm_line_edit.setContextMenuPolicy(Qt.NoContextMenu)  # 不允许出现复制粘贴菜单
        self.password_confirm_line_edit.setEchoMode(QLineEdit.Password)

        self.add_user_button = QPushButton('添加读者')
        button_font = QFont()
        button_font.setPixelSize(16)
        self.add_user_button.setFont(button_font)
        self.add_user_button.setFixedHeight(32)
        self.add_user_button.setFixedWidth(140)

        self.close_button = QPushButton('关闭')
        self.close_button.setFont(button_font)
        self.close_button.setFixedHeight(32)
        self.close_button.setFixedWidth(140)

        self.layout.addRow('', self.title_label)
        self.layout.addRow(self.user_id_label, self.user_id_edit)
        self.layout.addRow(self.user_name_label, self.user_name_edit)
        self.layout.addRow(self.user_sex_label, self.user_sex_edit)
        self.layout.addRow(self.user_department_label, self.user_department_edit)
        self.layout.addRow(self.user_grade_label, self.user_grade_edit)
        self.layout.addRow(self.user_password_label, self.user_password_edit)
        self.layout.addRow(self.password_confirm_label, self.password_confirm_line_edit)
        self.layout.addRow('', self.add_user_button)
        self.layout.addRow('', self.close_button)
        self.layout.setSpacing(10)

        # 设置验证
        id_reg = QRegExp("[0-9]{13}")
        id_validator = QRegExpValidator(id_reg, self)
        self.user_id_edit.setValidator(id_validator)

        self.password_reg = QRegExp("[a-zA-z0-9]+$")
        self.password_validator = QRegExpValidator(self.password_reg, self)
        self.user_password_edit.setValidator(self.password_validator)
        self.password_confirm_line_edit.setValidator(self.password_validator)

        self.add_user_button.clicked.connect(self.add_user_button_clicked)
        self.close_button.clicked.connect(self.close)

        self.setWindowTitle('添加用户')
        self.setGeometry(400, 250, 300, 500)
        self.setWindowIcon(QIcon("./imagesSourse/book_icon2.png"))
        self.setWindowModality(Qt.WindowModal)
        self.show()

    def add_user_button_clicked(self):
        id = self.user_id_edit.text()
        name = self.user_name_edit.text()
        sex = self.user_sex_edit.text()
        department = self.user_department_edit.text()
        grade = self.user_grade_edit.text()
        password = self.user_password_edit.text()
        confirm_password = self.password_confirm_line_edit.text()

        # 判断是否存在空值
        if id == '' or name == '' or sex == '' or department == '' or grade == '' or password == '' or confirm_password == '':
            print(QMessageBox.warning(self, '警告', '请填写完整', QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            # 检测两次密码是否一致
            if confirm_password != password:
                print(QMessageBox.warning(self, '警告', '两次密码不一致，请重新输入', QMessageBox.Yes, QMessageBox.Yes))
                return
            elif confirm_password == password:
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

                # 检测数据库中是否存在相同账号
                sql = "select * from user WHERE StudentId = '%s'" % id
                query.exec_(sql)  # 执行SQL语句
                if query.first():  # query.next()判断是否存在记录
                    print(QMessageBox.warning(self, '警告', '账号已经存在，请重新输入', QMessageBox.Yes, QMessageBox.Yes))
                    self.clear_edit()
                else:  # 插入数据
                    sql = "INSERT INTO user VALUES('%s','%s','%s','%s','%s', '%s')" % (id, name, sex, department, grade, password)
                    query.exec_(sql)
                    db.commit()
                    # print(db.lastError().text())
                    print(QMessageBox.information(self, '提醒', '注册成功！', QMessageBox.Yes, QMessageBox.Yes))
                    self.add_user_success_signal.emit()
                    self.close()
                    self.clear_edit()

    def clear_edit(self):
        self.user_id_edit.clear()
        self.user_name_edit.clear()
        self.user_sex_edit.clear()
        self.user_department_edit.clear()
        self.user_grade_edit.clear()
        self.user_password_edit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AddUserDialog()
    sys.exit(app.exec_())
