import pandas as pd

# Load the IA scores from an Excel sheet
ia_scores = pd.read_excel('path_to_your_file.xlsx', sheet_name='IA Scores')

# Load the Exam scores from another Excel sheet
exam_scores = pd.read_excel('path_to_your_file.xlsx', sheet_name='Exam Scores')

# Merge the two DataFrames based on the 'Student ID'
merged_scores = pd.merge(ia_scores, exam_scores[['Student ID', 'Exam Score']], on='Student ID', how='left')

# Save the merged data to a new Excel file or overwrite the existing one
merged_scores.to_excel('path_to_your_merged_file.xlsx', index=False)

print("Data merged successfully!")
