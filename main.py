from csv_file_processor import CsvProcessor
from excel_file_processor import ExcelProcessor
from file_processor import FileProcessor

# Điểm khởi chạy của chương trình
if __name__ == "__main__":
    FileProcessor: FileProcessor = None
    print(f"Please enter student list file path:")
    file_path = input().strip()
    print(f"File path entered: {file_path}")
    if file_path.endswith('.csv'):
        file_processor = CsvProcessor()
    elif file_path.endswith('xlsx'):
        file_processor = ExcelProcessor()
    else:
        print(f"Unsupported file type. Please provide a .csv or .xlsx file.")
        exit(1)
    file_processor.read_file_to_get_student_list(file_path)
    file_processor.print_student_list()