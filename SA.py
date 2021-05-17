import copy
import random
import math

bn=0

class Value:
    def calc_Objective(board):
        global bn
        hc = 0
        dc = 0
        n = bn
        for i in range(n):
          for j in range(n):
            if board[i][j] == 1:
              hc -= 2
              for k in range(n):
                if board[i][k] == 1:
                  hc += 1
                if board[k][j] == 1:
                  hc += 1
              k, l = i+1, j+1
              while k < n and l < n:
                if board[k][l] == 1:
                  dc += 1
                k +=1
                l +=1
              k, l = i+1, j-1
              while k < n and l >= 0:
                if board[k][l] == 1:
                  dc += 1
                k +=1
                l -=1
              k, l = i-1, j+1
              while k >= 0 and l < n:
                if board[k][l] == 1:
                  dc += 1
                k -=1
                l +=1
              k, l = i-1, j-1
              while k >= 0 and l >= 0:
                if board[k][l] == 1:
                  dc += 1
                k -=1
                l -=1
                
        heuristic = int((hc + dc)/2)
        th = int((bn*(bn-1))/2)
        objective = th - heuristic
        return objective
        #print('Heuristic Value: ',heuristic)

class Board:    
    def boardSize(self,n):
        self.n=n
        self.matrix = []
        for i in range(n):
            l=[]
            for j in range(n):
                l.append(0)
            self.matrix.append(l)
            
        #Board.printBoard(self.matrix)
        
    def printBoard(m):
        for i in m:
            print(i)
    def setQueenBoard(self,pos):
        for i in range(self.n):
            self.matrix[i][pos[i]-1]=1
            
        Board.printBoard(self.matrix)
        #print(Value.calc_Objective(self.matrix))
        ChildNodes.getChild(self.matrix,self.n)
            
class ChildNodes:
    def getChild(mat,n):
        nboard = copy.deepcopy(mat)
        bcn = copy.deepcopy(mat)
        allChild = []
        for i in range(n):
            a,b=0,0
            flag=0
            for j in range(n):
                if nboard[i][j] == 1:
                    a,b=i,j
                    nboard[i][j]=0
                    for l in range(n):
                        if nboard[i][l] != 1:
                            tmp = copy.deepcopy(nboard)
                            tmp[i][j] = 0
                            tmp[i][l] = 1
                            x = copy.deepcopy(tmp)
                            if x != bcn:
                                allChild.append(x)
                            tmp[i][l]=0
                    if flag==1:
                        break
            if flag==1:
                        break
            nboard[a][b]=1
        
        for i in allChild:
            print('C')
            Board.printBoard(i)
        Board.printBoard(SA.getSA(allChild))
        
class SA:
    def getSA(childs):
        global bn
        it = int(input('Initial Temparature: '))
        dr = float(input('Enter Decay Rate: '))
        stv = float(input('Enter Stopping Value: '))
        Temp = it
        currentState = childs[0]
        tt = int((bn*(bn-1))/2)
        if Value.calc_Objective(currentState) == tt:
            return currentState
        
        while True:
            if Temp <= 0:
                return currentState
            nextState = childs[random.randint(0,len(childs)-1)]
            diff = Value.calc_Objective(nextState) - Value.calc_Objective(currentState)
            if diff>0:
                currentState = nextState
            else:
                probabilty = math.exp(diff/Temp)
                if probabilty>stv and probabilty<1: 
                    currentState = nextState
                    #print('P: ',probabilty)
            Temp -= dr
            if Value.calc_Objective(nextState) == tt:
                return nextState
            #Board.printBoard(nextState)       
        
                
b = Board()
nn = int(input('Board Size: '))
bn = nn
b.boardSize(nn)
x = print('Enter Initial Queens Position: ')
l=[]
for i in range(nn):
    l.append(int(input()))
b.setQueenBoard(l)

