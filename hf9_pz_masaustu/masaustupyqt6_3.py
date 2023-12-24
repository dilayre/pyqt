from PyQt6.QtWidgets import *
app = QApplication([])
def tiklama():
    alert = QMessageBox()
    alert.setText('Tıkladın!')
    alert.exec()
window = QWidget()

# icerik = QHBoxLayout() 

icerik = QVBoxLayout()

icerik.addWidget(QPushButton('dene!'))
buton1 = QPushButton('Tıkla')
buton1.clicked.connect(tiklama)

icerik.addWidget(buton1)
icerik.addWidget(QLabel('Bilgi!'))

window.setLayout(icerik)

window.show()
app.exec()


# icerik.addWidget(QLabel('OTOMASYON(ne old. bilmiom)'))
# icerik.addWidget(QLineEdit('Adınız:'))
# icerik.addWidget(QLineEdit('Soyadınız:'))
# icerik.addWidget(QLineEdit('TC No:'))
# icerik.addWidget(QLineEdit('Şifre:'))