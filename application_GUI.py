import sys
from tkinter import Widget
from turtle import window_height
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLineEdit,
    QHBoxLayout,
    QGridLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
)
from PyQt6.QtGui import QPixmap


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
LINE_HEIGHT = 50

class AppGUI(QMainWindow):
    """Application's GUI"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MSA data processing")
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.main_layout = QHBoxLayout()
        central_widget = QWidget(self)
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

        self.create_datataker()
        self.create_image()
    
    def create_datataker(self):
        pass

    def create_image(self):
        self.pattern_image = QLabel()
        pixmap = QPixmap("C:\Users\K90006169\MSA_project\component_pattern.png")
        #pixmap = pixmap.scaled(450, 250)
        self.pattern_image.setPixmap(pixmap)
        self.main_layout.add(Widget(self.pattern_image))