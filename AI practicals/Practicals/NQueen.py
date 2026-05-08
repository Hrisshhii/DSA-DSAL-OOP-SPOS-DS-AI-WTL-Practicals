class NQueen:
    def __init__(self,n):
        self.N=n
        self.board=[[0]*n for _ in range(n)]
    
    def is_safe(self,row,col):
        for i in range(col):
            if self.board[row][i]==1:
                return False
        i=row
        j=col
        while i>=0 and j>=0:
            if self.board[i][j]==1:
                return False
            i-=1
            j-=1
        
        i=row
        j=col
        while i<self.N and j>=0:
            if self.board[i][j]==1:
                return False
            i+=1
            j-=1
        return True
    
    def solve_nq(self,col):
        if col>=self.N:
            return True
        for i in range(self.N):
            if self.is_safe(i,col):
                self.board[i][col]=1
                if self.solve_nq(col+1):
                    return True
                self.board[i][col]=0
        return False
        
    def print_result(self):
        for row in self.board:
            for cell in row:
                if(cell==1):
                    print("Q",end=" ")
                else:
                    print("-",end=" ")
            print()

def main():
    n=4
    q=NQueen(n)
    if q.solve_nq(0):
        print("\nSolution found!")
        q.print_result()
    else:
        print("No Solution")
main()
