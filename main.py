import sqlite3 as sql
print("sqllite3 version: ", sql.version)


# import sys
# from PyQt5 import QtCore, QtGui

# --------------------------------------------------------
db = sql.connect('./database/database.db')
coursor = db.cursor()

import sys
from PyQt5 import QtGui

app = QtGui.QGuiApplication(sys.argv)

window = QtGui.QWidget()
window.setGeometry(0, 0, 500, 300)
window.setWindowTitle("PyQT Tuts!")

window.show()

# --------------------------------------------------------

