class Matrix():
    def __init__(self, data):
        self.data = data
        self.det = self.determinant(data)

    def determinant(self, data):
        n=len(data)
        if n == 1:
            return n
        elif (n>2):
            i=1
            t=0
            sum=0
            while t<=n-1:
                d={}
                t1=1
                while t1<=n-1:
                    m=0
                    d[t1]=[]
                    while m<=n-1:
                        if (m!=t):
                            d[t1].append(data[t1][m])
                        m+=1
                    t1+=1
                l1=[d[x] for x in d]
                sum=sum+i*(data[0][t])*(self.determinant(l1))
                i=i*(-1)
                t+=1
            return sum
        else:
            return (data[0][0]*data[1][1]-data[0][1]*data[1][0])

matrix = [[1,-2,3],[0,-3,-4],[0,0,-3]]
matrix1 = [[0]]
test = Matrix(matrix)
print(test.determinant(test.data))