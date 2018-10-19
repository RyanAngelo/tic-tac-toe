from tkinter import *
from tkinter import font

class Application(Frame):

    btnheight=5
    btnwidth=10
    gameboard = [[],[],[]]
    currentPlayer = 'x'
    

    def __init__(self,master=None):
        super().__init__(master)
        print("TicTacToe is starting!")
        self.createWidgets()

    def choseBlock(self, row, col):
        self.gameboard[row][col].config(text=self.currentPlayer)
        self.gameboard[row][col].config(state=DISABLED)
        self.analyzeAction(row, col)
        if self.currentPlayer == 'x':
            self.currentPlayer='o'
        else:
            self.currentPlayer='x'
    
    def analyzeAction(self, row, col):
        print("Analyzing move for win condition!")
        #Check the row for a win state
        rowwinstate=[]
        for square in self.gameboard[row]:
            if square["text"] == self.currentPlayer:
                rowwinstate.append(square)
                
        #Check the column for a win state
        colwinstate=[]
        rowindex=0
        for rowSquares in self.gameboard:
            square = rowSquares[col]
            if square["text"] == self.currentPlayer:
                colwinstate.append(square)

        #Check the diagonal win statea
        diagwinstate=[]
        print(row, col)
        if col+row == 2:
            print("Col+Row==2!")
            if self.currentPlayer == self.gameboard[0][2]["text"]\
             == self.gameboard[1][1]["text"] == self.gameboard[2][0]["text"]:
                diagwinstate = self.gameboard[0][2],self.gameboard[1][1],self.gameboard[2][0]
        if col==row:
            print("Col==Row!")
            if self.currentPlayer == self.gameboard[2][2]["text"]\
             == self.gameboard[1][1]["text"] == self.gameboard[0][0]["text"]:
                diagwinstate = self.gameboard[2][2],self.gameboard[1][1],self.gameboard[0][0]
        print(rowwinstate, colwinstate, diagwinstate)
        winstate = (winconditions for winconditions in [rowwinstate,colwinstate,diagwinstate] if len(winconditions) == 3)
        winner=False
        for state in winstate:
            winner=True
            for square in state:
                square.configure(bg = "green")
                square.update_idletasks()     
        if winner==True:
            print(self.currentPlayer+" won!")
            self.lockGameboard()

    def lockGameboard(self):
        for row in self.gameboard:
            for square in row:
                square.config(state=DISABLED)
                
    def resetGameboard(self):
        for row in self.gameboard:
            for square in row:
                square.config(state=NORMAL)
                square.config(text="")
                square.configure(bg = "white")
                square.update_idletasks()
                
    def configureSquares(self):
        for row in self.gameboard:
            for square in row:
                square.config( height=self.btnheight, width=self.btnwidth )
                square.config(state=NORMAL)
                square['font']=self.customFont
                square.configure(bg = "white")
                square.update_idletasks()
        

    def createWidgets(self):
        self.customFont = font.Font(family="Helvetica", size=18, weight='bold')

        frame = Frame(root, bg='black')
        frame.grid(row=0, column=0, padx=(5,5), pady=(5,5))
        button0 = Button(frame, text=" ", command=lambda row=0, column=0: self.choseBlock(row, column))
        button0.grid(row=0, column=0, padx=(5,5), pady=(5,5))
        button1 = Button(frame, text=" ", command=lambda row=0, column=1: self.choseBlock(row, column))
        button1.grid(row=0, column=1, padx=(5,5), pady=(5,5))
        button2 = Button(frame, text=" ", command=lambda row=0, column=2: self.choseBlock(row, column))
        button2.grid(row=0, column=2, padx=(5,5), pady=(5,5))
        button3 = Button(frame, text=" ", command=lambda row=1, column=0: self.choseBlock(row, column))
        button3.grid(row=1, column=0, padx=(5,5), pady=(5,5))
        button4 = Button(frame, text=" ", command=lambda row=1, column=1: self.choseBlock(row, column))
        button4.grid(row=1, column=1, padx=(5,5), pady=(5,5))
        button5 = Button(frame, text=" ", command=lambda row=1, column=2: self.choseBlock(row, column))
        button5.grid(row=1, column=2, padx=(5,5), pady=(5,5))
        button6 = Button(frame, text=" ", command=lambda row=2, column=0: self.choseBlock(row, column))
        button6.grid(row=2, column=0, padx=(5,5), pady=(5,5))
        button7 = Button(frame, text=" ", command=lambda row=2, column=1: self.choseBlock(row, column))
        button7.grid(row=2, column=1, padx=(5,5), pady=(5,5))
        button8 = Button(frame, text=" ", command=lambda row=2, column=2: self.choseBlock(row, column))
        button8.grid(row=2, column=2, padx=(5,5), pady=(5,5))
        
        self.gameboard[0]=[button0, button1, button2]
        self.gameboard[1]=[button3, button4, button5]
        self.gameboard[2]=[button6, button7, button8]
        
        resetButton = Button(frame, text="Reset", command=self.resetGameboard)
        resetButton.grid(row=3, column=0, columnspan=3, padx=(5,5), pady=(5,5))
        
        self.configureSquares()
        root.mainloop()


root = Tk()
app = Application(master=root)
app.mainloop()

