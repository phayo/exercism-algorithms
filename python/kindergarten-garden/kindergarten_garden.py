defaultStudents = [
    "Alice", "Bob", "Charlie", "David",
    "Eve", "Fred", "Ginny", "Harriet",
    "Ileana", "Joseph", "Kincaid", "Larry"
]

plants = {
    "G": "Grass",
    "V": "Violets",
    "R": "Radishes",
    "C": "Clover"
}

class Garden(object):
    def __init__(self, diagram, students=defaultStudents):
        rows = diagram.split("\n")
        self.diagram = [[x[i] + x[i+1] for i in range(0, len(x), 2)] for x in rows]
        self.students = sorted(students)

    # def __init__(self, diagram):
    #     rows = diagram.split("\n")
    #     self.diagram = [[x[i] + x[i+1] for i in range(0, len(x), 2)] for x in rows]

    def plants(self, name):
        try:
            ind = self.students.index(name)
        except ValueError:
            raise ValueError("".join(name, " is not a valid student"))
        
        student_plant = "".join([x[ind] for x in self.diagram])

        return [plants[x] for x in student_plant]

garden = Garden(
    "VCRRGVRG\nRVGCCGCV", students=["Samantha", "Patricia", "Xander", "Roger"]
)
print(garden.plants("Patricia"))