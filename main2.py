
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout, QLineEdit, QSizePolicy
from PyQt6.QtCore import Qt

# Créer un objet QApp
app = QApplication([])

# Créer un objet QWidget
fen = QWidget()

# Modifier les paramètres de l'objet
fen.setGeometry(100, 100, 700, 500)
fen.setWindowTitle('Calculatrice Primitive')

# Définir les actions

def multiplication():
    result.setText(str(int(number_input.text())*2))

def division():
    result.setText(str(int(number_input.text())/2))

def addition_un():
    result.setText(str(int(number_input.text())+1))

def soustraction_un():
    result.setText(str(int(number_input.text())-1))

def addition_dix():
    result.setText(str(int(number_input.text())+10))

def soustraction_dix():
    result.setText(str(int(number_input.text())-10))


# Création des boutons
multiplication_2 = QPushButton(fen)
multiplication_2.setText("X2")
multiplication_2.clicked.connect(multiplication)

division_2 = QPushButton(fen)
division_2.setText("/2")
division_2.clicked.connect(division)

addition_1 = QPushButton(fen)
addition_1.setText("+1")
addition_1.clicked.connect(addition_un)

soustraction_1 = QPushButton(fen)
soustraction_1.setText("-1")
soustraction_1.clicked.connect(soustraction_un)

addition_10 = QPushButton(fen)
addition_10.setText("+10")
addition_10.clicked.connect(addition_dix)

soustraction_10 = QPushButton(fen)
soustraction_10.setText("-10")
soustraction_10.clicked.connect(soustraction_dix)

# Input Field
number_input = QLineEdit(fen)
number_input.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
number_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

# Result field (Label)
result = QLabel(fen)
result.setAlignment(Qt.AlignmentFlag.AlignCenter)

# StyleSheet

fen.setStyleSheet("""
    QWidget {
        background-color: #2E2E2E;  /* Dark background for the calculator */
    }
    QPushButton {
        background-color: #4CAF50;  /* Green background for buttons */
        color: white;                /* White text */
        border: none;                /* No border */
        border-radius: 10px;        /* Rounded corners */
        padding: 15px;               /* Padding inside the button */
        font-size: 18px;             /* Font size */
        transition: background-color 0.3s, transform 0.2s; /* Smooth transition */
    }
    QPushButton:hover {
        background-color: #45a049;   /* Darker green on hover */
        transform: scale(1.05);      /* Slightly enlarge on hover */
    }
    QPushButton:pressed {
        background-color: #388E3C;   /* Even darker green when pressed */
        transform: scale(0.95);       /* Slightly shrink when pressed */
    }
""")

number_input.setStyleSheet("""
    background-color: #f0f0f0;  /* Light gray background */
    border: 5px solid #ccc;      /* Light gray border */
    border-radius: 5px;          /* Rounded corners */
    padding: 5px;                 /* Padding inside the line edit */
    
    font-size: 50px;              /* Font size */
    color: black;
""")

result.setStyleSheet("""
    background-color: #c5c5c5;    /* Darker gray background */
    border: 5px solid white;      /* Light gray border */
    border-radius: 10px;          /* Rounded corners */
    padding: 5px;                 /* Padding inside the line edit */
    
    font-size: 50px;              /* Font size */
    color: #123524;
""")

# Grid Layout
grid_layout = QGridLayout()
fen.setLayout(grid_layout)

grid_layout.addWidget(number_input, 0, 0, 1, 2)
grid_layout.addWidget(result, 1, 0, 1, 2)

grid_layout.addWidget(multiplication_2, 5, 0)
grid_layout.addWidget(division_2, 5, 1)
grid_layout.addWidget(addition_1, 3, 0)
grid_layout.addWidget(soustraction_1, 3, 1)
grid_layout.addWidget(addition_10, 4, 0)
grid_layout.addWidget(soustraction_10, 4, 1)


# Appeler la méthode show() de l'objet de type QWidget
fen.show()
# Executer l'application
app.exec()