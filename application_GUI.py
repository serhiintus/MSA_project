import sys
import os
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLineEdit,
    QHBoxLayout,
    QGridLayout,
    QVBoxLayout,
    QFormLayout,
    QPushButton,
    QLabel,
    QFileDialog,
)
from PyQt6.QtGui import QPixmap


WINDOW_WIDTH = 750
WINDOW_HEIGHT = 500
LINE_HEIGHT = 50
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 25

class AppGUI(QMainWindow):
    """Application's GUI"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MSA data processing")
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.main_layout = QVBoxLayout()
        central_widget = QWidget(self)
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)

        self.create_input_boxes()
        self.main_layout.addSpacing(20)
        self.create_image()
        self.main_layout.setSpacing(20)

    def create_input_boxes(self):
        #create list of label texts
        texts = [
            "Select CSV file for the TOP side:", 
            "Enter designators for the TOP side separated by a comma:", 
            "Select CSV file for the BOT side:", 
            "Enter designators for the BOT side separated by a comma:"
            ]

        #define the number of input boxes
        self.input_boxes_names = [[f"label{i + 1}", f"input{i + 1}"]for i in range(len(texts))]

        #create a grid layout
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(20)

        #define the input boxes and place them in the layout
        self.input_boxes = {}
        for row, input_box in enumerate(self.input_boxes_names):
            for column, element in enumerate(input_box):
                if column == 0:
                    self.input_boxes[element] = QLabel(texts[row])
                    self.grid_layout.addWidget(self.input_boxes[element], row, column)
                else:
                    self.input_boxes[element] = QLineEdit(self)
                    self.grid_layout.addWidget(self.input_boxes[element], row, column)

        #create and place the buttons in the layout
        self.button1 = QPushButton("SEARCH", self)
        self.button1.setFixedSize(BUTTON_WIDTH, BUTTON_HEIGHT)
        self.button2 = QPushButton("SEARCH", self)
        self.button2.setFixedSize(BUTTON_WIDTH, BUTTON_HEIGHT)
        self.button3 = QPushButton("CREATE EXCEL", self)
        self.button3.setFixedSize(BUTTON_WIDTH, BUTTON_HEIGHT)
        self.button4 = QPushButton("CLEAR DATA", self)
        self.button4.setFixedSize(BUTTON_WIDTH, BUTTON_HEIGHT)

        containerWidget = QWidget()
        containerLayout = QHBoxLayout()
        containerLayout.addWidget(self.button3)
        containerLayout.addWidget(self.button4)
        containerWidget.setLayout(containerLayout)

        self.grid_layout.addWidget(self.button1, 0, 2)
        self.grid_layout.addWidget(self.button2, 2, 2)
        self.grid_layout.addWidget(containerWidget, 4, 1)

        self.main_layout.addLayout(self.grid_layout)

    def create_image(self):
        self.pattern_image = QLabel()
        #Get the current working directory
        current_dir = os.path.dirname(os.path.realpath(__file__))
        #Construct the file path using the current directory and the file name
        image_path = os.path.join(current_dir, "component_pattern.png")
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(450, 250)
        self.pattern_image.setPixmap(pixmap)
        self.main_layout.addWidget(self.pattern_image)


class AppController:
    def __init__(self, view):
        self.view = view
        self.connect_signals_and_slots()

    def select_file(self):
        #Get the button that triggered the event
        sender_button = self.view.sender()
        options = QFileDialog.Option(0)
        #Show the file dialog to select a file
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("CSV Files (*.csv)")
        file_dialog.setViewMode(QFileDialog.ViewMode.Detail)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                file_path = selected_files[0]
                if sender_button == self.view.button1:
                    self.view.input_boxes["input1"].setText(file_path)
                elif sender_button == self.view.button2:
                    self.view.input_boxes["input3"].setText(file_path)

    def clear_data(self):
        #clear data in the input boxes
        for key in self.view.input_boxes:
            if key.find("input") != -1:
                self.view.input_boxes[key].clear()

    def connect_signals_and_slots(self):
        self.view.button1.clicked.connect(self.select_file)
        self.view.button2.clicked.connect(self.select_file)
        self.view.button4.clicked.connect(self.clear_data)

def main():
    app = QApplication([])
    appGui = AppGUI()
    appGui.show()
    appController = AppController(
        view=appGui
    )
    sys.exit(app.exec())

if __name__ == "__main__":
    main()