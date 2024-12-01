import sys
import random
import sys

from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget


class gitAndYellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.pushButton.clicked.connect(self.draw_circle)

    def initUI(self):
        self.pushButton = QPushButton("Рисуй!!!")
        self.pushButton.setFixedSize(50, 50)

        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setFixedSize(500, 500)

    def draw_circle(self):
        self.update()

    def paintEvent(self, event):
        x = random.randint(0, self.width())
        y = random.randint(0, self.height())
        diameter = random.uniform(10, self.width() / 2)
        color = self.random_color()

        painter = QPainter(self)
        painter.setBrush(color)
        painter.drawEllipse(QPointF(x, y), diameter / 2, diameter / 2)

    def random_color(self):
        return QColor(random.randint(0, 255),
                      random.randint(0, 255),
                      random.randint(0, 255))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = gitAndYellowCircles()
    ex.show()
    sys.exit(app.exec())
