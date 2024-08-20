# Partie 1 : Premier exemple avec la librairie PyQt6

# importer la librairie

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout
from PyQt6.QtCore import Qt
# Créer un objet QApplication
app = QApplication([])
# Créer un objet QWidget
fen = QWidget()
# Modifier les paramètres de l'objet
fen.setGeometry(100, 100, 700, 700)
fen.setWindowTitle('Application' )


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


# --------------- fenêtre en Gridlayout ---------------

fen2 = QWidget()
fen2.setGeometry(500, 500, 500, 500)
fen2.setWindowTitle("Grid Layout")

qlabl2 = QLabel("Buttons démo")
qlabl2.setStyleSheet("""
    background-color: white;
    color: black;
""")

grid_layout = QGridLayout()
fen2.setLayout(grid_layout)

# --------------- To Work On ---------------

# Définir Action
def action():
    print("Réaction")

def reaction():
    print("Action!")

# QPushButton
qbtn1 = QPushButton(fen2)
qbtn2 = QPushButton(fen2)

qbtn1.setText("Action")
qbtn1.clicked.connect(action)

qbtn2.setText("Réaction")
qbtn2.clicked.connect(reaction)

# --------------- To Work On ---------------

grid_layout.addWidget(qlabl2, 0, 1)
grid_layout.addWidget(qbtn1, 3, 0)
grid_layout.addWidget(qbtn2, 3, 2)

# --------------- fenêtre en Gridlayout ---------------








# Appler la methode show() de l'objet de type QWidget
#fen.show()
fen2.show()
# Executer l'application : object QApplication
app.exec()

