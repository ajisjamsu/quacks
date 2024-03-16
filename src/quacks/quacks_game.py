import matplotlib.pyplot as plt
import numpy as np
import random
import logging
import click
import sys
from quacks import quacks_pieces as qp
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton

logger = logging.getLogger(__name__)

def quacks_gui():
    p1 = qp.QuacksPlayer("p1")

    app = QApplication([])

    window = QWidget()
    window.setWindowTitle("Signals and slots")
    layout = QVBoxLayout()

    button = QPushButton("Draw")
    button.clicked.connect(p1.drawChip)

    layout.addWidget(button)
    msgLabel = QLabel("")
    layout.addWidget(msgLabel)
    window.setLayout(layout)

    window.show()
    sys.exit(app.exec())

def main():
    logging.basicConfig(level=logging.INFO)
    logger.info(" Welcome to Quacks of Quedlinburg!")
    quacks_gui()

if __name__ == "__main__":
    main()
