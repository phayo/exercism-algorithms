

class School(object):
    def __init__(self):
        self.grades =   {
                "1": [],
                "2": [],
                "3": [],
                "4": [],
                "5": [],
                "6": [],
                "7": [],
                "8": [],
                "9": [],
                "10": [],
                "11": [],
                "12": []
            }

    def add_student(self, name, grade):
        grd = str(grade)
        self.grades[grd].append(name)

    def roster(self):
        roster = [student for i in range(1, 13) for student in sorted(self.grades[str(i)])]
        return roster

    def grade(self, grade_number):
        return sorted(self.grades[str(grade_number)])

