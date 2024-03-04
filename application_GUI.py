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


WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
LINE_HEIGHT = 50

class AppGUI(QMainWindow):
    """Application's GUI"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MSA data processing")
        #self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.main_layout = QHBoxLayout()
        central_widget = QWidget(self)
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)

        self.create_input_boxes()
        self.main_layout.addSpacing(20)
        self.create_image()
        #self.main_layout.setSpacing(20)

    def create_input_boxes(self):
        # Create grid layout
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(10)
        
        # Add Input Boxes in the first column
        label1 = QLabel("Input data for the TOP side:")
        self.input_box1 = QLineEdit(self)

        label2 = QLabel("Input list of the designators for the TOP side:")
        self.input_box2 = QLineEdit(self)

        label3 = QLabel("Input data for the BOT side:")
        self.input_box3 = QLineEdit(self)

        label4 = QLabel("Input list of the designators for the BOT side:")
        self.input_box4 = QLineEdit(self)

        self.grid_layout.addWidget(label1, 0, 0)
        self.grid_layout.addWidget(self.input_box1, 0, 1)

        self.grid_layout.addWidget(label2, 1, 0)
        self.grid_layout.addWidget(self.input_box2, 1, 1, 1, 2)

        self.grid_layout.addWidget(label3, 2, 0)
        self.grid_layout.addWidget(self.input_box3, 2, 1)

        self.grid_layout.addWidget(label4, 3, 0)
        self.grid_layout.addWidget(self.input_box4, 3, 1, 1, 2)

        # Add Buttons in the second column
        self.button1 = QPushButton("SEARCH", self)
        self.button2 = QPushButton("SEARCH", self)
        button3 = QPushButton("CREATE", self)
        button4 = QPushButton("CLEAR", self)

        self.grid_layout.addWidget(self.button1, 0, 2)
        self.grid_layout.addWidget(self.button2, 2, 2)
        self.grid_layout.addWidget(button3, 4, 1)
        self.grid_layout.addWidget(button4, 4, 2)

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

    def select_file(self):
        #Get the button that triggered the event
        sender_button = self.sender()
        options = QFileDialog.Options()
        #Show the file dialog to select a file
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("CSV Files (*.csv)")
        file_dialog.setViewMode(QFileDialog.ViewMode.Detail)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                file_path = selected_files[0]
                if sender_button == self.search_top_csv:
                    self.csv_top_path.setText(file_path)
                elif sender_button == self.search_bot_csv:
                    self.csv_bot_path.setText(file_path)

def main():
    app = QApplication([])
    appGui = AppGUI()
    appGui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()