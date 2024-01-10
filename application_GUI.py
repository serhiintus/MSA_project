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
        self.form_layout = QFormLayout()
        #Add rows with labels, line edits, and buttons
        self.add_row_with_button("TOP side data:", "enter path")
        self.add_row_with_button("TOP designators:", "list the designators")
        self.add_row_with_button("BOP side data:", "enter path")
        self.add_row_with_button("BOP designators:", "list the designators")

        self.main_layout.addLayout(self.form_layout)

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

    def add_row_with_button(self, label_text, placeholder_text):
        label = label_text
        line_edit = QLineEdit()
        line_edit.setPlaceholderText(placeholder_text)

        button = QPushButton("Action")
        button.clicked.connect(lambda: self.on_button_clicked(line_edit))

        self.form_layout.addRow(label, line_edit)
        self.form_layout.addWidget(button)

    def on_button_clicked(self, line_edit):
        text = line_edit.text()
        print(f"Button clicked! Text in the line edit: {text}")

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