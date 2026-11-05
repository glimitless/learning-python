file_list = [
    "report.csv",
    "data.xlsx",
    "summary.docx",
    "report.csv",
    "data.csv"
]
stored_file_names = []
duplicate_file_names = False

for file in file_list:
    if file in stored_file_names:
        print(f"{file} is a duplicate.")
        if not duplicate_file_names:
            duplicate_file_names = True
        continue
    stored_file_names.append(file)

    if file == file_list[len(file_list) - 1] and duplicate_file_names:
        print("Duplicate file names exist in this data")
        break
else:
    print("No duplicate file names exist in this data.")
