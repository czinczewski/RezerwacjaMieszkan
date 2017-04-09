# Aplikacja pozwalająca Użytkownikowi na rezerwacje mieszkania bez znajomości struktury bazy danych
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QTableWidget, QComboBox, QMessageBox, QTableWidgetItem
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


# --------------------------------------------------------
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.table = QTableWidget(self)
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)
        self.button1 = QPushButton("Search", self)
        self.list = QComboBox(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("User Panel")
        self.move(10, 10)
        self.resize(300, 500)

        self.db.setDatabaseName("./DataBase/database.db")

        self.table.close()

        self.set_labels()
        self.set_buttons()
        self.choose_city()


    def set_labels(self):
        self.label1.move(10, 10)
        self.label1.setText("Choose city: ")

        self.label2.move(10, 30)
        self.label2.setText("Start date: ")

        self.label3.move(10, 50)
        self.label3.setText("End date: ")

    def set_buttons(self):
        self.button1.move(10, 80)
        self.button1.clicked.connect(self.show_results)

    def choose_city(self):
        ok = self.db.open()
        self.list.move(90, 6)
        city_list =[]
        question = "SELECT name FROM city"
        query = QSqlQuery(question)
        while query.next():
                city_list.append(str(query.value(0)))

        print("City List", city_list)
        self.list.addItems(city_list)

    def show_results(self):
        self.table.move(10, 120)
        self.table.resize(280, 300)
        self.table.show()


# --------------------------------------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
