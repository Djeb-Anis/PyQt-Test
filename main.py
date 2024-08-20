# Partie 1 : Premier exemple avec la librairie PyQt6

# importer la librairie

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtCore import Qt
# Créer un objet QApplication
app = QApplication([])
# Créer un objet QWidget
fen = QWidget()
# Modifier les paramètres de l'objet
fen.setGeometry(100, 100, 700, 700)
fen.setWindowTitle('Application' )

# Définir Action
def action():
    print("Réaction")

# Qlabel
qlabl1 = QLabel(fen)
qlabl1.setText('Mon projet est un Qt')
qlabl1.setStyleSheet("""
    background-color: black;
    font-size: 2.5em;
    font-weight: bold;
    color: white;
    text-align: center;    
    text-transform: uppercase;
    letter-spacing: 2px;
""")
qlabl1.setAlignment(Qt.AlignmentFlag.AlignCenter)
qlabl1.setGeometry(0, 0, fen.width(), fen.height()) # Center the text


# QPushButton
qbtn1 = QPushButton(fen)
qbtn1.setText("Action")
qbtn1.clicked.connect(action)


# Appler la methode show() de l'objet de type QWidget
fen.show()
# Executer l'application : object QApplication
app.exec()