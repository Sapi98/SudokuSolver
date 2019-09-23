"""*********************************************ALL ABOUT SUDOKU**********************************************************
*The popular Japanese puzzle game Sudoku is based on the logical placement of numbers. Sudoku is one of the most popular *
*puzzle games of all time. The goal of Sudoku is to fill a 9×9 grid with numbers so that each row, column and 3×3 section*
*contain all of the digits between 1 and 9. As a logic puzzle, Sudoku is also an excellent brain game.                   *
**************************************************************************************************************************

***********************************************RULES FOR THE GAME*********************************************************
*The goal of Sudoku is to fill in a 9×9 grid with digits so that each column, row, and 3×3 section contain the numbers   *
*between 1 to 9. At the beginning of the game, the 9×9 grid will have some of the squares filled in. Your job is to use  *
*logic to fill in the missing digits and complete the grid. Do not forget, a move is incorrect if:                       *
*                                                                                                                        *
*1) Any row contains more than one of the same number from 1 to 9                                                        *
*                                                                                                                        *
*2) Any column contains more than one of the same number from 1 to 9                                                     *
*                                                                                                                        *
*3) Any 3×3 grid contains more than one of the same number from 1 to 9                                                   *
**************************************************************************************************************************

**************************************************ALGORITHM***************************************************************
*1) Find for unassigned number grid                                                                                      *
*2) If any unassigned block is found the row and column is set to that unassigned block                                  *
*3) A loop is iterated from 1 to 9 to check which number can be placed in that unassigned block                          *
*4) Check feasibility for each number held by the iteration variable (i.e. 1 to 9)                                       *
*5) If feasible place the assign the number to the position and make recursive call to the working function              *
*6) If not feasible let the iteration continue                                                                           *
*7) If none can be placed then backtrack to the previous position and reset the position with value 0                    *
*8) If no other position remains unassigned, produce a return condition to exhaust the recursive stack                   *
*9) Print the result                                                                                                     *
**************************************************************************************************************************

*****************************************BEHAVIOUR OF THE FUNCTIONS USED**************************************************
*solve() -> basic solution handling secondary function making call to the actual solution function                       *
*place() -> actual solution function which makes recursive calls to itself and assign numbers to the SUDOKU GRIDS        *
*isFeasible() -> function to check the feasibility of placing  particular number at particular position of SUDOKU matrix *
*findUnassigned() -> finds rows and columns of unassigned locations in the SUDOKU matrix                                 *
*printSolution() -> prints the whole solved matrix at an organized and well formatted way as output                      *
**************************************************************************************************************************

            NOTE : All non-zero elements are treated as assigned and '0' elements are treated as unassigned"""


def findUnassigned(arr, r, c):

    for i in range(maxBlock):
        for j in range(maxBlock):
            if arr[i][j] == 0:
                return (True, i, j)
    
    return (False, r, c)

def isInputFeasible(arr, r, c, num):

    for i in range(maxBlock):
        if (arr[r][i] == num and i != c) or (arr[i][c] == num and i != r):
            return False
    
    r1 = (r // 3) * 3  # sets the lower row index of a 3x3 sub matrix
    c1 = (c // 3) * 3  # sets the lower column index of a 3x3 sub matrix
    
    for i in range(r1, r1 + 3):
        for j in range(c1, c1 + 3):
            if arr[i][j] == num:
                if i == r and j == c:
                    continue
                
                return False
    
    return True

def isFeasible(arr, r, c, num):

    for i in range(maxBlock):
        if arr[r][i] == num or arr[i][c] == num:
            return False
    
    r = (r // 3) * 3  # sets the lower row index of a 3x3 sub matrix
    c = (c // 3) * 3  # sets the lower column index of a 3x3 sub matrix
    
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            if arr[i][j] == num:
                return False
    
    return True

def place(arr, r, c):

    flag, r, c = findUnassigned(arr, r, c) # Checks for any unassigned positions in the Sudoku matrix
    
    if not flag:
        return True
    
    for i in range(1, maxBlock+1):
        if isFeasible(arr, r, c, i): # Checks feasibility of position (r,c) for number i
            arr[r][c] = i
            if place(arr, r, c): # Recursive Call
                return True
            arr[r][c] = 0 # If recursive call fails to assign then the previous positions is made unassigned again by backtracking
    
    return False # Triggers Backtracking

maxBlock = 9

if __name__ == "__main__":
    def printSolution(arr):
    
        print(" -------------------------------\n")
        for i in range(maxBlock):
            for j in range(maxBlock):
                if j % 3 == 0:
                    print('|', end = '')
                print(' {0} '.format(arr[i][j]), end = '')
            print('|')
            if (i + 1) % 3 == 0:
                print(" -------------------------------\n")
            
    def solve():

        arr = [[0 for i in range(maxBlock)] for j in range(maxBlock)]
        print("Enter the given Nos. formatted as : position row,position column,no. n to be assigned\nEnter -1 in any to exit")
        while True: # Takes Input and assigns to the SUDOKU matrix for given numbers
            i, j, num = list(map(int, input('Enter Data : ').strip().split()))
            if num > maxBlock or i > maxBlock or j > maxBlock:
                print('Input Out Of Range')
                continue
            elif num == -1 or i == -1 or j == -1:
                break
            else:
                arr[i-1][j-1] = num
    
        if place(arr, 0, 0):
            print('\n -: SOLUTION :- \n\n')
            printSolution(arr)
        else:
            print('\n!!! Solution Not Possible !!!\n\n')
    
    solve()
