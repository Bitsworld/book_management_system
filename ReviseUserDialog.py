import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *


class ReviseUserDialog(QDialog):
    revise_user_successful_signal = pyqtSignal()
    revise_user_back_signal = pyqtSignal()

    def __init__(self, user_id, parent=None):
        super(ReviseUserDialog, self).__init__(parent)
        self.user_id = user_id

        self.initUI()

    def initUI(self):
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()
        self.form_layout = QFormLayout()
        self.h_layout_revise_button = QHBoxLayout()
        self.h_layout_back_button = QHBoxLayout()
        self.fally_layout = QVBoxLayout()

        font = QFont()
        font.setPixelSize(20)
        title_label_font = QFont()
        title_label_font.setPixelSize(20)
        button_font = QFont()
        button_font.setPixelSize(18)

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

        self.query = QSqlQuery()
        sql = "SELECT StudentId , Name, Sex, Department,Grade, Password FROM user WHERE StudentId = '%s'" % self.user_id

        self.query.exec_(sql)
        self.query.first()

        self.title_label = QLabel(' 修改信息')
        self.title_label.setFont(title_label_font)
        self.title_label.setMargin(8)

        self.user_id_label = QLabel("学  号:")
        self.user_id_label.setFont(font)
        self.user_id_edit = QLineEdit()
        self.user_id_edit.setFont(font)
        self.user_id_edit.setFixedWidth(180)
        self.user_id_edit.setFixedHeight(28)
        self.user_id_edit.setStyleSheet("background:#F0F0F0")
        self.user_id_edit.setReadOnly(True)
        self.user_id_edit.setText(self.user_id)

        self.user_name_label = QLabel('姓  名:')
        self.user_name_label.setFont(font)
        self.user_name_edit = QLineEdit()
        self.user_name_edit.setFont(font)
        self.user_name_edit.setReadOnly(False)
        self.user_name_edit.setText(self.query.value('Name'))

        self.user_sex_label = QLabel('性  别:')
        self.user_sex_label.setFont(font)
        self.user_sex_edit = QLineEdit()
        self.user_sex_edit.setFont(font)
        # self.sex_edit.setStyleSheet("background:#F0F0F0")
        self.user_sex_edit.setReadOnly(False)
        self.user_sex_edit.setText(self.query.value('Sex'))

        self.user_department_label = QLabel('系  别:')
        self.user_department_label.setFont(font)
        self.user_department_edit = QLineEdit()
        self.user_department_edit.setFont(font)
        # self.department_edit.setStyleSheet("background:#F0F0F0")
        self.user_department_edit.setReadOnly(False)
        self.user_department_edit.setText(self.query.value('Department'))

        self.user_grade_label = QLabel('年  级:')
        self.user_grade_label.setFont(font)
        self.user_grade_edit = QLineEdit()
        self.user_grade_edit.setFont(font)
        # self.user_grade_edit.setStyleSheet("background:#F0F0F0")
        self.user_grade_edit.setReadOnly(False)
        self.user_grade_edit.setText(self.query.value('Grade'))

        self.user_password_label = QLabel('密  码:')
        self.user_password_label.setFont(font)
        self.user_password_edit = QLineEdit()
        self.user_password_edit.setFont(font)
        # self.password_edit.setStyleSheet("background:#F0F0F0")
        self.user_password_edit.setEchoMode(QLineEdit.Password)
        self.user_password_edit.setReadOnly(False)
        self.user_password_edit.setText(self.query.value('Password'))

        self.form_layout.addRow('', self.title_label)
        self.form_layout.addRow(self.user_id_label, self.user_id_edit)
        self.form_layout.addRow(self.user_name_label, self.user_name_edit)
        self.form_layout.addRow(self.user_sex_label, self.user_sex_edit)
        self.form_layout.addRow(self.user_department_label, self.user_department_edit)
        self.form_layout.addRow(self.user_grade_label, self.user_grade_edit)
        self.form_layout.addRow(self.user_password_label, self.user_password_edit)
        self.form_layout.setSpacing(10)

        self.revise_button = QPushButton('确认修改')
        self.revise_button.setFixedHeight(32)
        self.revise_button.setFixedWidth(120)
        self.revise_button.setFont(button_font)
        self.back_button = QPushButton('返  回')
        self.back_button.setFont(button_font)
        self.back_button.setFixedWidth(120)
        self.back_button.setFixedHeight(32)

        self.h_layout_revise_button.addWidget(self.revise_button, Qt.AlignCenter)
        self.h_layout_back_button.addWidget(self.back_button, Qt.AlignCenter)

        form_widget = QWidget()
        form_widget.setLayout(self.form_layout)

        h_revise_widget = QWidget()
        h_back_widget = QWidget()

        h_revise_widget.setLayout(self.h_layout_revise_button)
        h_back_widget.setLayout(self.h_layout_back_button)

        self.h_layout.addWidget(form_widget, 0, Qt.AlignLeft | Qt.AlignTop)

        widget = QWidget()
        widget.setLayout(self.h_layout)

        self.fally_layout.addWidget(widget)
        self.fally_layout.addWidget(h_revise_widget)
        self.fally_layout.addWidget(h_back_widget)

        self.setLayout(self.fally_layout)

        self.revise_button.clicked.connect(self.revise_button_clicked)
        self.back_button.clicked.connect(self.close)

        self.setWindowTitle('修 改 读 者')
        self.setGeometry(400, 250, 300, 500)
        self.setWindowIcon(QIcon("./imagesSourse/book_icon2.png"))
        self.setWindowModality(Qt.WindowModal)
        self.show()

    def revise_button_clicked(self):
        id = self.user_id_edit.text()
        name = self.user_name_edit.text()
        sex = self.user_sex_edit.text()
        department = self.user_department_edit.text()
        grade = self.user_grade_edit.text()
        password = self.user_password_edit.text()
        if id == '' or name == '' or sex == '' or department == '' or grade == '' or password == '':
            print(QMessageBox.warning(self, '警告', '请填写完整', QMessageBox.Yes, QMessageBox.Yes))
        else:
            sql = "UPDATE user SET Name = '%s', Sex = '%s', Department = '%s', Grade = '%s', Password = '%s' WHERE StudentId = '%s'" % (name, sex, department, grade, password, id)
            self.query.exec_(sql)
            print(QMessageBox.information(self, '提示', '数据更新成功', QMessageBox.Yes, QMessageBox.Yes))
            self.revise_user_successful_signal.emit()
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReviseUserDialog('2016141462225')
    sys.exit(app.exec_())