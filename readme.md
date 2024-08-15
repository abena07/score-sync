
---

# `score-sync`

`score-sync` is a simple Python script that merges IA scores and Exam scores from two sheets within an Excel workbook based on a common `Student Id` field.

## Installation

Ensure you have Python 3.x installed, and then install the required libraries:

```bash
pip install pandas openpyxl
```

## Usage

Place your Excel file in the same directory as the script, then run the script to merge the data:

```bash
python mergescores.py
```

1. **Basic Usage:**
    Replace 'path_to_your_file.xlsx' with the actual file path.

   Merge IA and Exam scores using `Student Id` as the common identifier:

   ```bash
   python merge_scores.py
   ```

2. **Custom Save Location:**
   Modify the script to save the merged file to a specified path.

## License

This project is licensed under the MIT License.

---

