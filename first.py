import csv
import sys
import io
import random

from PyQt6 import uic
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class gitAndYellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.draw_circle)

    def draw_circle(self):
        self.update()

    def paintEvent(self,event):
        x = random.randint(0, self.width())
        y = random.randint(0, self.height())
        diameter = random.uniform(10, self.width() / 2)
        color = QColor(255,255,0)

        painter = QPainter(self)
        painter.setBrush(color)
        painter.drawEllipse(QPointF(x, y), diameter / 2, diameter / 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = gitAndYellowCircles()
    ex.show()
    sys.exit(app.exec())
