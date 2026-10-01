class Student:
    def __init__(self, RollNumber, FullName, DateOfBirth):
        self.RollNumber = RollNumber
        self.FullName = FullName
        self.DateOfBirth = DateOfBirth

    #Hàm để thông tin in ra đẹp hơn
    def __str__(self):
        return (f"MSV: {self.RollNumber} | Name: {self.FullName} | DOB: {self.DateOfBirth}")