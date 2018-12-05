import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from BookStorageView import BookStorageView
from PyQt5.QtSql import *
from BorrowBookDialog import BorrowBookDialog


class BorrowAndReturnBook(QWidget):
    def __init__(self, user_id, parent=None):
        super(BorrowAndReturnBook, self).__init__(parent)
        self.student_id = user_id
        print('What happen?')
        self.initUI()

    def initUI(self):
        self.layout = QHBoxLayout()
        self.button_layout = QVBoxLayout()
        self.model_layout = QVBoxLayout()

        button_font = QFont()
        button_font.setPixelSize(18)

        label_font = QFont()
        label_font.setPixelSize(18)

        self.borrow_book_button = QPushButton('借书')
        self.borrow_book_button.setFixedWidth(100)
        self.borrow_book_button.setFixedHeight(40)
        self.borrow_book_button.setFont(button_font)

        self.return_book_button = QPushButton('还书')
        self.return_book_button.setFixedWidth(100)
        self.return_book_button.setFixedHeight(40)
        self.return_book_button.setFont(button_font)

        self.button_layout.addWidget(self.borrow_book_button)
        self.button_layout.addWidget(self.return_book_button)

        self.storage_view = BookStorageView()

        self.borrow_label = QLabel('未归还：')
        self.borrow_label.setFont(label_font)
        self.borrow_label.setFixedWidth(60)
        self.borrow_label.setFixedHeight(30)

        self.borrowed_table_view = QTableView()
        self.borrowed_table_view.horizontalHeader().setStretchLastSection(True)
        self.borrowed_table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.borrowed_table_view.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.borrowed_query_model = QSqlQueryModel()
        self.borrowed_table_view.setModel(self.borrowed_query_model)
        self.borrowed_query()

        self.borrowed_query_model.setHeaderData(0, Qt.Horizontal, '书号')
        self.borrowed_query_model.setHeaderData(1, Qt.Horizontal, '书名')
        self.borrowed_query_model.setHeaderData(2, Qt.Horizontal, '作者')
        self.borrowed_query_model.setHeaderData(3, Qt.Horizontal, '出版社')
        self.borrowed_query_model.setHeaderData(4, Qt.Horizontal, '出版时间')
        self.borrowed_query_model.setHeaderData(5, Qt.Horizontal, '借阅时间')
        self.borrowed_query_model.setHeaderData(6, Qt.Horizontal, '到期时间')

        self.model_layout.addWidget(self.storage_view)
        self.storage_view.setFixedHeight(400)
        self.model_layout.addWidget(self.borrow_label)
        self.model_layout.addWidget(self.borrowed_table_view)

        self.layout.addLayout(self.button_layout)
        self.layout.addLayout(self.model_layout)
        self.setLayout(self.layout)
        self.storage_view.search_button_clicked()

        self.borrow_book_button.clicked.connect(self.borrow_book_button_clicked)
        self.return_book_button.clicked.connect(self.return_book_button.clicked)

        # 初始化界面
        self.setWindowTitle('书籍管理')
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.resize(880, 600)
        self.move((screen.width() - size.width()) / 2-100,  (screen.height() - size.height()) / 2-100)
        self.setWindowIcon(QIcon("./imagesSourse/user_icon2.png"))
        self.show()

    def borrowed_query(self):
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

        query = QSqlQuery()

        sql = "SELECT b.BookId, b.BookName, b.Author, b.Publisher, b.PublishTime,  ub.BorrowTime, ub.ReturnTime FROM user_book AS ub, book AS b WHERE ub.StudentId = '%s' AND  ub.BookId = b.BookId" % self.student_id
        self.borrowed_query_model.setQuery(sql)

    def borrow_book_button_clicked(self):
        borrow_book_dialog = BorrowBookDialog(self.student_id, self)
        borrow_book_dialog.borrow_book_success_signal.connect(self.borrowed_query)
        borrow_book_dialog.borrow_book_success_signal.connect(self.storage_view.search_button_clicked)
        borrow_book_dialog.back_success_signal.connect(self.borrowed_query)
        borrow_book_dialog.back_success_signal.connect(self.storage_view.search_button_clicked)
        self.borrowed_query()
        self.storage_view.search_button_clicked()
        borrow_book_dialog.show()

    def return_book_button_clicked(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BorrowAndReturnBook('2016141462225')
    sys.exit(app.exec_())

