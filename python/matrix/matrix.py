class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = matrix_string.split("\n")

    def row(self, index=-1):
        if index == -1:
            return [[int(a) for a in x.split()] for x in self.matrix]
        return [[int(a) for a in x.split()] for x in self.matrix][index-1]

    def column(self, index):
        row = self.row()
        res = []
        for i in range(len(row[0])):
            res.append([x[i] for x in row])
        return res[index - 1]
