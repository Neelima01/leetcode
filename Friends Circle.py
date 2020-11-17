'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def circle(mat):
    mat1 = mat[0]
    mat2 = mat[1]
    mat3 = mat[2]
    a = []
    b = []
    if len(mat1)==len(mat2)==len(mat3):
        for i in range(len(mat1)):
            if(mat1[i] and mat2[i]==1):
                a.append([mat1[i],mat2[i]])
            if(mat2[i] and mat3[i]==1):
                b.append([mat2[i],mat3[i]])
        if len(a)==len(b):
            print("1")
        elif len(a)>len(b):
            print(len(a))
        else:
            print(len(b))
arr = [list(map(int,input().strip().split())) for i in range(3)]
print(arr)
circle(arr)
                
            

