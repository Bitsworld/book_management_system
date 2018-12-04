import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *

class UserStorageView(QWidget):
    def __init__(self):
        super(UserStorageView, self).__init__()

        # 初始化变量
        self.query_model = None  # 查询模型
        self.tablet_view = None  # 数据表
        self.cur_page = 0  # 当前页数
        self.total_page = 0  # 总页数
        self.total_record = 0  # 总记录数
        self.page_record = 10  # 每页数据数

        self.drop_user_id = ''



        self.layout = QVBoxLayout()
        self.h_layout1 = QHBoxLayout()
        self.h_layout2 = QHBoxLayout()

        self.font = QFont()
        self.font.setPixelSize(15)

        self.initUI()

    def initUI(self):
        # 内容输入框
        self.search_edit = QLineEdit()
        self.search_edit.setFixedHeight(32)
        self.search_edit.setFont(self.font)

        # 查询按钮
        self.search_button = QPushButton('查询')
        self.search_button.setFont(self.font)
        self.search_button.setFixedHeight(32)

        # 查询条件选择按钮
        self.condision_combobox = QComboBox()
        search_condision = ['按证号查询', '按姓名查询', '按性别查询', '按系名查询', '按年级查询']
        self.condision_combobox.addItems(search_condision)
        self.condision_combobox.setFixedHeight(32)
        self.condision_combobox.setFont(self.font)

        # 将按钮添加到布局中
        self.h_layout1.addWidget(self.search_edit)
        self.h_layout1.addWidget(self.search_button)
        self.h_layout1.addWidget(self.condision_combobox)

        # 跳转按钮及翻页按钮设置
        self.jump_to_label = QLabel('跳转到第')
        self.page_edit = QLineEdit()
        self.page_edit.setFixedWidth(30)
        s = '/' + str(self.total_page) + '页'
        self.pageLabel = QLabel(s)
        self.jump_button = QPushButton('跳转')
        self.pre_button = QPushButton('前一页')
        self.pre_button.setFixedWidth(60)
        self.back_button = QPushButton('下一页')
        self.back_button.setFixedWidth(60)

        # 将组件添加到布局中
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.jump_button)
        h_layout.addWidget(self.page_edit)
        h_layout.addWidget(self.pageLabel)
        h_layout.addWidget(self.pre_button)
        h_layout.addWidget(self.back_button)
        widget = QWidget()
        widget.setLayout(h_layout)
        widget.setFixedWidth(300)
        self.h_layout2.addWidget(widget)

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

        self.drop_user_query = QSqlQuery()
        self.user_book_query = QSqlQuery()

        # 表格布局设置
        self.tablet_view = QTableView()
        self.tablet_view.horizontalHeader().setStretchLastSection(True)
        self.tablet_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tablet_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.query_model = QSqlQueryModel()
        self.search_button_clicked()
        self.tablet_view.setModel(self.query_model)
        self.tablet_view.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.query_model.setHeaderData(0, Qt.Horizontal, '证号')
        self.query_model.setHeaderData(1, Qt.Horizontal, '姓名')
        self.query_model.setHeaderData(2, Qt.Horizontal, '性别')
        self.query_model.setHeaderData(3, Qt.Horizontal, '系名')
        self.query_model.setHeaderData(4, Qt.Horizontal, '年级')

        # 将所有布局添加到总体布局中去
        self.layout.addLayout(self.h_layout1)
        self.layout.addWidget(self.tablet_view)
        self.layout.addLayout(self.h_layout2)
        self.setLayout(self.layout)

        self.search_button.clicked.connect(self.search_button_clicked)
        self.pre_button.clicked.connect(self.pre_button_clicked)
        self.back_button.clicked.connect(self.back_button_clicked)
        self.jump_button.clicked.connect(self.jump_button_clicked)
        self.search_edit.returnPressed.connect(self.search_button_clicked)

        # 初始化界面
        self.setWindowTitle('图书管理系统')
        self.setGeometry(100, 100, 700, 500)
        self.setWindowIcon(QIcon("user_icon2.png"))
        self.show()

    # 设置前进后退按钮是否可点击
    def set_button_status(self):
        if self.cur_page == self.total_page:
            self.pre_button.setEnabled(True)
            self.back_button.setEnabled(False)

        if self.cur_page == 1:
            self.pre_button.setEnabled(False)
            self.back_button.setEnabled(True)

        if 1 < self.cur_page < self.total_page:
            self.pre_button.setEnabled(True)
            self.back_button.setEnabled(True)

    # 获取总的记录数
    def get_total_record_count(self):
        self.query_model.setQuery(
            'SELECT StudentId , Name, Sex, Department,Grade FROM user')
        self.total_record = self.query_model.rowCount()
        return

    # 获得页码数
    def get_page_count(self):
        self.get_total_record_count()
        self.total_page = int((self.total_record + self.page_record - 1) / self.page_record)
        return

    # 分页记录查询
    def record_query(self, index):
        query_condition = ''
        condition_choice = self.condision_combobox.currentText()
        if condition_choice == '按证号查询':
            condition_choice = 'StudentId'
        elif condition_choice == '按姓名查询':
            condition_choice = 'Name'
        elif condition_choice == '按性别查询':
            condition_choice = 'Sex'
        elif condition_choice == '按系名查询':
            condition_choice = 'Department'
        else:
            condition_choice = 'Grade'

        if self.search_edit.text() == '':
            query_condition = 'SELECT StudentId , Name, Sex, Department,Grade FROM user'
            self.query_model.setQuery(query_condition)
            self.total_record = self.query_model.rowCount()
            self.total_page = int((self.total_record + self.page_record - 1) / self.page_record)
            label = '/' + str(int(self.total_page)) + '页'
            self.pageLabel.setText(label)
            query_condition = "SELECT StudentId , Name, Sex, Department,Grade FROM user ORDER BY %s LIMIT %d, %d" % (
            condition_choice, index, self.page_record)
            self.query_model.setQuery(query_condition)
            self.drop_user_query.exec_(query_condition)
            self.set_button_status()
            return

        # 查询内容不为空
        temp = self.search_edit.text()
        s = '%'
        for i in range(0, len(temp)):
            s = s + temp[i] + '%'
        print('执行到query_condtion前面' + s)
        query_condition = "SELECT StudentId , Name, Sex, Department,Grade FROM user WHERE %s LIKE '%s' ORDER BY %s " % (
        condition_choice, s, condition_choice)
        print('执行到query_condition后面')
        self.query_model.setQuery(query_condition)
        self.drop_user_query.exec_(query_condition)
        print('执行到query_model.setQuery后面')
        self.total_record = self.query_model.rowCount()
        print(self.total_record)

        # 如果没有查询到内容
        if self.total_record == 0:
            print('执行到if')
            print(QMessageBox.information(self, '提醒', '无记录', QMessageBox.Yes, QMessageBox.Yes))
            print('执行到messagebox')
            query_condition = 'SELECT StudentId , Name, Sex, Department,Grade FROM user'
            self.query_model.setQuery(query_condition)
            self.drop_user_query.exec_(query_condition)
            self.total_record = self.query_model.rowCount()
            self.total_page = int((self.total_record + self.page_record - 1) / self.page_record)
            label = '/' + str(int(self.total_page)) + '页'
            self.pageLabel.setText(label)
            query_condition = "SELECT StudentId , Name, Sex, Department,Grade FROM user ORDER BY %s LIMIT %d, %d" % (
            condition_choice, index, self.page_record)
            print('执行到query_condition后面，limit')
            self.query_model.setQuery(query_condition)
            self.drop_user_query.exec_(query_condition)
            self.set_button_status()
            return

        # 如果查询到了内容
        self.total_page = int(
            (self.total_record + self.page_record - 1) / self.page_record)  # LIMIT %d,%d  , index, self.pageRecord
        label = '/' + str(int(self.total_page)) + '页'
        self.pageLabel.setText(label)
        print('执行到limit前面')
        query_condition = "SELECT StudentId , Name, Sex, Department,Grade FROM user WHERE %s LIKE '%s' ORDER BY %s LIMIT %d,%d " % (
        condition_choice, s, condition_choice, index, self.page_record)
        print('执行到limit后面')

        self.query_model.setQuery(query_condition)
        self.drop_user_query.exec_(query_condition)
        self.set_button_status()
        return

    # 点击查询按钮
    def search_button_clicked(self):
        self.cur_page = 1
        self.page_edit.setText(str(self.cur_page))
        self.get_page_count()
        s = '/' + str(int(self.total_page)) + '页'
        self.pageLabel.setText(s)
        index = (self.cur_page - 1) * self.page_record
        self.record_query(index)
        return

    # 向前翻页
    def pre_button_clicked(self):
        self.cur_page -= 1
        if self.cur_page <= 1:
            self.cur_page = 1
        self.page_edit.setText(str(self.cur_page))
        index = (self.cur_page - 1) * self.page_record
        self.record_query(index)
        return

    # 向后翻页
    def back_button_clicked(self):
        self.cur_page += 1
        if (self.cur_page >= int(self.total_page)):
            self.cur_page = int(self.total_page)
        self.page_edit.setText(str(self.cur_page))
        index = (self.cur_page - 1) * self.page_record
        self.record_query(index)
        return

    # 跳转至固定页数
    def jump_button_clicked(self):
        if self.page_edit.text().isdigit():
            self.cur_page = int(self.page_edit.text())
            if self.cur_page > self.total_page:
                self.cur_page = self.total_page
            if self.cur_page <= 1:
                self.cur_page = 1
        else:
            self.cur_page = 1
        index = (self.cur_page - 1) * self.page_record
        self.page_edit.setText(str(self.cur_page))
        self.record_query(index)
        return

    # 删除用户
    def drop_user(self):
        indexs = self.tablet_view.selectionModel().selectedRows()
        indexs_array = []
        for index in sorted(indexs):
            indexs_array.append(index.row()+1)
            print('row %d is selected' % index.row())
        # print(indexs_array)
        i = 1
        if not indexs_array:
            print(QMessageBox.information(self, '提示', '请选择要删除的用户', QMessageBox.Yes, QMessageBox.Yes))
        else:
            self.drop_user_query.first()
            while i != indexs_array[0] and self.drop_user_query.next():
               i = i + 1
            print(self.drop_user_query.value('StudentId'))
            print(self.drop_user_query.value('Name'))
            print(self.drop_user_query.value('Sex'))
            print(self.drop_user_query.value('Department'))
            print(self.drop_user_query.value('Grade'))
            student_id = self.drop_user_query.value('StudentId')
            student_name = self.drop_user_query.value('Name')
            student_sex = self.drop_user_query.value('Sex')
            student_department = self.drop_user_query.value('Department')
            student_grade = self.drop_user_query.value('Grade')
            user_book_sql = "SELECT * FROM user_book WHERE StudenrId = '%s" % (student_id)
            self.user_book_query.exec_(user_book_sql)
            if self.user_book_query.first():
                print(QMessageBox.warning(self, '警告', '你选择的读者有图书未归还，无法删除！', QMessageBox.Yes, QMessageBox.Yes))
                return
            else:
                drop_user_sql = "DELETE FROM user WHERE StudentId = '%s'" % student_id
                if (QMessageBox.warning(self, "提醒","删除用户:\n学号：%s\n姓名：%s\n性别：%s\n系别：%s\n年级：%s\n用户一经删除将无法恢复，是否继续?" % (student_id, student_name, student_sex, student_department, student_grade), QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.No):
                    return

                self.drop_user_query.exec_(drop_user_sql)
                self.search_button_clicked()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserStorageView()
    sys.exit(app.exec_())