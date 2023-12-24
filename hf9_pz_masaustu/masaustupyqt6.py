import sys
from PyQt6.QtWidgets import *
app = QApplication(sys.argv)

window = QWidget()
window.show()

window1 = QPushButton("tıkla")
window1.show()

window2 = QLabel("merhabaaa")
window2.show()
app.exec() #uygulamayı çalıştırmak için (adı app olmak zorunda değil)