import pandas as pd
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


class ExcelCreator:

    def __init__(self, df_columns = ["OffsetX", "OffsetY"], modules = 5, tests = 9) -> None:
        self.df_columns = df_columns
        self.modules = modules
        self.tests = tests

    def create_msa_df(self):
        self.columns_for_msa_data = {
            'Operator': [1 for i in range(self.modules*self.tests)],
            'Part': [i+1 for i in range(self.modules) for j in range(self.tests)]
        }
        self.msa_data = pd.DataFrame(self.columns_for_msa_data)

    def csv_reader(self, path):
        df = pd.read_csv(path)
        return df
    
    def data_filter(self, df, components, side):
        for i in components:
            #create a temporary dataframe
            filtered_data = pd.DataFrame(columns=self.df_columns)

            for j in range(self.modules):
                #create filter
                filt = (df["ModuleID"] == j + 1) & (df["Location Name"] == i)
                #filtered data from the .csv file and add it to the temporary dataframe
                filtered_data = pd.concat([filtered_data, df.loc[filt, self.df_columns].iloc[:9]], ignore_index=True)

            column_mapping = {
                self.df_columns[0]: f"{side}_{i}_X",
                self.df_columns[1]: f"{side}_{i}_Y"
            }
            #rename the columns and update the values of the temporary dataframe
            filtered_data = filtered_data.rename(columns=column_mapping).apply(lambda x: x/1000)
            #concatenate the MSA dataframe and the temporary dataframe with renaming columns of the temporary dataframe
            self.msa_data = pd.concat([self.msa_data, filtered_data], axis=1)

    def create_tolerance_df(self, components):
        n = len(components)
        columns_with_data = {
            'Desygnator': components,
            'Obudowa': ['none' for i in range(n)],
            'Tolerancja X': [0 for i in range(n)],
            'Tolerancja Y': [0 for i in range(n)]
        }
        self.tolerance_data = pd.DataFrame(columns_with_data)

    def export_data(self):
        #export MSA and tolerance dataframes to the Excel
        with pd.ExcelWriter('MSA_data.xlsx', engine='xlsxwriter') as writer:
            self.msa_data.to_excel(writer, sheet_name='Sheet1', startrow=0, startcol=0, index=False)
            self.tolerance_data.to_excel(writer, sheet_name='Sheet1', startrow=0, startcol=len(self.msa_data.columns) + 2, index=False)

    


class AppController:

    def __init__(self, view, exporter):
        self.view = view
        self.exporter = exporter
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

    def create_excel(self):
        top_csv = self.view.input_boxes["input1"].text()
        bot_csv = self.view.input_boxes["input3"].text()
        components_top = self.input_boxes["input2"].text().upper()
        components_bot = self.input_boxes["input4"].text().upper()

        self.exporter.create_msa_df()

        if top_csv and components_top:
            top_data = self.exporter.csv_reader(top_csv)
            self.exporter.data_filter(top_data, components_top, "TOP")
        if bot_csv and components_bot:
            bot_data = self.exporter.csv_reader(bot_csv)
            self.exporter.data_filter(bot_data, components_bot, "BOT")

        components = components_top + components_bot
        if components:
            self.exporter.create_tolerance_df()
            self.exporter.export_data()

    def connect_signals_and_slots(self):
        self.view.button1.clicked.connect(self.select_file)
        self.view.button2.clicked.connect(self.select_file)
        self.view.button3.clicked.connect(self.create_excel)
        self.view.button4.clicked.connect(self.clear_data)

def main():
    app = QApplication([])
    appGui = AppGUI()
    appGui.show()
    appLogic = ExcelCreator()
    appController = AppController(
        view=appGui,
        exporter = appLogic
    )
    sys.exit(app.exec())

if __name__ == "__main__":
    main()