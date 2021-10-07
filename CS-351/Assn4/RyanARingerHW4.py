from tkinter import *
from tkinter import ttk

LIGHTGRAY = '#C4C5BF'
WHITE = '#FFFFFF'
DARKGRAY = '#65696B'

class LexerGui:
    def __init__(self, root):
        self.linecount = 0
        self.lastText = ""
        self.master = root
        self.lastindex = 0
        self.master.title("TinyPie GUI")

        self.frame = Frame(self.master, width=800, height=500, bg=LIGHTGRAY)
        self.frame.grid(row=0, column=0)

        self.inputLabel = Label(self.frame, text="INPUT", bg=LIGHTGRAY)
        self.inputLabel.grid(row=0, column=0, padx = 10, pady = 10)

        self.outputLabel = Label(self.frame, text="OUTPUT", bg=LIGHTGRAY)
        self.outputLabel.grid(row=0, column=1, padx=10, pady=10)

        self.textField1 = Text(self.frame, width=30, height=20, bg=WHITE)
        self.textField1.grid(row=1, column=0, padx=10, pady=10)

        self.textField2 = Text(self.frame, width=30, height=20,  bg=WHITE)
        self.textField2.grid(row=1, column=1, padx=10, pady=10)

        self.lineValue = StringVar()
        self.lineValue.set("Current Line: N/A")
        self.lineNumber = Label(self.frame, textvariable=self.lineValue, bg=LIGHTGRAY)
        self.lineNumber.grid(row=2, column=0, padx=10, pady=10)

        # self.lineDisplay = Entry(self.frame)
        # self.lineDisplay.insert(0, self.linecount)
        # self.lineDisplay.grid(row=1, column=1)

        self.nextLineButton = Button(self.frame, text="Next Line", command=self.nextLine, width=10,  bg=DARKGRAY)
        self.nextLineButton.grid(row=3, column=0, padx=5, pady=5)

        self.quitButton = Button(self.frame, text="Quit", command=self.master.destroy, width=10, bg=DARKGRAY)
        self.quitButton.grid(row=3, column=1, padx=5, pady=5)


    def nextLine(self):
        newIndex = 0
        tempString = self.textField1.get("1.0", END)
        # print(tempString)
        if self.lastindex < len(tempString):
            if tempString != self.lastText:
                self.linecount = 0
                self.lastindex = 0
                self.lastText = tempString
                self.textField2.delete("1.0", END)

            for i in range(self.lastindex, len(tempString)):
                if tempString[i] == '\n':
                    # print(i)
                    newIndex = i
                    break

            # print(type(newIndex))
            # print(type(self.lastindex))
            # print(type(tempString))
            outputText = tempString[self.lastindex: newIndex: 1]
            # print(outputText)
            self.textField2.insert(END, outputText + '\n')
            self.lastindex = newIndex + 1
            # print("Last Index = " + str(self.lastindex))


            self.lineValue.set("Current Line: " + str(self.linecount))
            self.linecount = self.linecount + 1



if __name__ == '__main__':
    root = Tk()
    myGui = LexerGui(root)
    root.mainloop()
