# Aplikacja pozwalająca Użytkownikowi na rezerwacje mieszkania bez znajomości struktury bazy danych
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
import sqlite3 as sql
# --------------------------------------------------------
db = sql.connect('./database/database.db')
print("Connected to DB")
coursor = db.cursor()


# --------------------------------------------------------
class App(QWidget()):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("User Panel")
        self.move(10, 10)
        self.resize(300, 500)
        self.show()


# --------------------------------------------------------
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
