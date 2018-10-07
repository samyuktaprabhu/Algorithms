def safe(board, row,col):
    i=0
    while(i<col): #check row-wise
        if(board[row][i]):                
            return False
        i+=1
    
    i,j=row,col
    while(i>=0 and j>=0): #check the upper left diagonal
        if(board[i][j]):
            return False
        i-=1
        j-=1

    i,j=row,col
    while(i<n and j>=0): #check the lower left diagonal
        if(board[i][j]):
            return False
        i+=1
        j-=1
    #if safe to place, return true else return false
    return True

def placed(board, col):
    # if column number is equal to or more than the dimension, exit
    if(col==n):
        return True
    for row in range(n):
        if(safe(board,row,col)): #check safety
            board[row][col]=1
            if(placed(board,col+1)): #recursive function
                return True            
            board[row][col]=0
    return False

n=input("Enter dimension : ")
print("The dimension is {}".format(n))

import numpy
board=numpy.zeros((n,n)) #in-built function of a zero matrix generator

print("The Board before Queen Placement : ")
print(board) #printing empty chess board

if(placed(board,0)):
    print("")
print("The Board after Queen Placement : ")    
print(board) #printing new chess board
#end of code
