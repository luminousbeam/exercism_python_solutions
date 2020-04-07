class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string=matrix_string

    def row(self, index):
        x=self.matrix_string.split("\n")
        returnArr=x[index-1].split(' ')
        for i in range(len(returnArr)):
            returnArr[i]=int(returnArr[i])
        return returnArr
    def column(self, index):
        return_arr=[]
        x=self.matrix_string.split("\n")
        for i in range(len(x)):
            x[i]=x[i].split(' ')
        for i in range(len(x)):
            return_arr.append(int(x[i][index-1]))
        return return_arr
