from file_processor import FileProcessor
import openpyxl
from student import Student

class ExcelProcessor(FileProcessor):
    def read_file_to_get_student_list(self, file_path):
        workbook = openpyxl.load_workbook(file_path, data_only = True)
        sheet = workbook.active

        for row in sheet.iter_row(min_row=2, values_only=True):
            if row[0] is None:
                continue

            student = Student (
                RollNumber = str(row[0]).strip(),
                FullName = str(row[1]).strip(),
                DateOfBirth = str(row[2]).strip()
            )

            print(f"{student.RollNumber} - {student.FullName}")
            self.student_list.append(student)