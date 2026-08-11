# ⚙️ MSA Automation Tool

## 📌 Overview

MSA Automation Tool is a Python desktop application designed to automate processing of raw AOI (Automated Optical Inspection) data.

It transforms raw CSV measurement data into a structured Excel format ready for Measurement Systems Analysis (MSA), significantly reducing manual effort, minimizing human error, and improving data consistency.

---

## 🚀 Key Value

- ⏱ Reduced data preparation time by ~50%
- ❌ Eliminated manual filtering and sorting
- 📊 Standardized MSA input format for Minitab
- ⚡ One-click data transformation

---

## 🎯 Target Users

- Process Engineers and Technician working with AOI systems  

---

## ❗ Problem

In manufacturing environments using AOI (Automated Optical Inspection), raw measurement data:

- Comes in large CSV files
- Requires manual filtering by component (designators)
- Needs sorting by module and test iteration
- Must be converted to millimeters
- Must be formatted for MSA (ANOVA) in Minitab

👉 This process is repetitive, time-consuming, and error-prone.

---

## ✅ Solution

This application:

1. Loads raw AOI CSV data
2. Filters data by selected component designators
3. Extracts offset measurements (X, Y)
4. Converts values to millimeters
5. Structures data into MSA format
6. Exports a ready-to-use Excel file

---

## 🖼 Application Preview

![App Screenshot](screenshot.png)

---

## 🔄 Before vs After

**Before:**
- Manual data filtering in Excel  
- High risk of human error  
- Time-consuming repetitive work  

**After:**
- Automated data processing  
- Consistent and reliable output  
- Ready for MSA (ANOVA) in minutes  

---

## 📦 Download (No Python required)

👉 **[Download MSA-Automation-Tool.exe](https://github.com/serhiintus/msa-automation-tool/releases)**

---

## ⚡ Quick Start

```bash
git clone https://github.com/serhiintus/msa-automation-tool.git
cd msa-automation-tool
pip install -r requirements.txt
python main.py
```

---

## ⚙️ Virtual Environment (Recommended)

```bash
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
```

---

## 🧪 Tests

```bash
pytest
```

---

## ⚙️ How It Works

1. **Input data**
   - Raw AOI measurement data is stored in `.csv` files (TOP and/or BOT side)
   - User selects file paths or pastes them manually

2. **User input**
   - User provides component **designators** (e.g., R1, C5, U10)

3. **Processing**
   - Data is filtered, sorted, and converted to millimeters
   - Measurements are structured for MSA analysis

4. **Output**
   - Excel file (`MSA_data.xlsx`) with two tables

---

## 📊 Output Structure

### 1️⃣ MSA Data Table
- Contains processed measurement data
- Includes:
  - Operator
  - Part
  - X/Y offsets for each component

### 2️⃣ Tolerance Table
- Designator  
- Package (user-defined)  
- Tolerance X (user-defined)  
- Tolerance Y (user-defined)  

---

## 📈 Integration with Minitab

The generated Excel data can be directly copied into Minitab.

Workflow:
1. Copy processed data  
2. Paste into Minitab  
3. Run MSA using ANOVA  

---

## 📂 Project Structure

```text
msa-automation-tool/
│
├── data/
│   ├── sample_top.csv
│   └── sample_bot.csv
│
├── tests/
|   └── test_excel_creator.py
|
├── .gitignore
├── chip-intelligence-processor.png
├── controller.py
├── excel_creator.py
├── gui.py
├── main.py
├── README.md
├── requirements.txt
└── screenshot.png
```

---

## 🛠 Tech Stack

- Python
- pandas
- PyQt6
- pytest
- XlsxWriter

---

## 📊 Sample Data

The repository includes example datasets:

- `sample_top.csv`
- `sample_bot.csv`

These files can be used to test the application without requiring real AOI machine output.

---

## ⭐ Highlights

- Real-world engineering problem solved with Python
- Data processing pipeline using pandas
- GUI application with PyQt6
- Automated Excel report generation
- Clean and testable code structure

---

## 👨‍💻 Author

**Serhii Provotorov**

LinkedIn: https://www.linkedin.com/in/serhii-provotorov/