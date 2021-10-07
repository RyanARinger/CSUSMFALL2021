# This is an example of using the tkinter python extension to create a basic window with button

from tkinter import *


class MyFirstGUI:  # class definition

    # This is the initialize function for a class.
    # Variables belonging to this class will get created and initialized in this function
    # What is the self parameter? It represents this class itself.
    # By using self.functionname, you can call functions belonging to this class.
    # By using self.variablename, you can create and use variables belonging to this class.
    # It needs to be the first parameter of all the functions in your class

    def __init__(self, root):
        # Master is the default parent object of all widgets.
        # You can think of it as the window that pops up when you run the GUI code.
        self.master = root
        self.master.title("My Cat Registration System")

        # grid function puts a widget at a certain location
        # return value is none, please do not use it like self.label=Label().grad()
        # it will make self.label=none and you will no longer be able to change the label's content
        self.label = Label(self.master, text="Cat Name: ")
        self.label.grid(row=0, column=0, sticky=E)

        self.catnameentry = Entry(self.master)
        self.catnameentry.grid(row=0, column=1, sticky=E)

        self.submitbutton = Button(self.master, text="Submit name", command=self.submitname)
        self.submitbutton.grid(row=0, column=2, sticky=E)

        self.output = Entry(self.master)
        self.output.grid(row=1, column=1, sticky=E)

        self.outputLabel = Label(self.master, text="Registered Cat Name: ")
        self.outputLabel.grid(row=1, column=0, sticky=E)

        self.printDatabase = Button(self.master, text="Print Database", command=self.submitname)
        self.printDatabase.grid(row=1, column=2, sticky=E)
        


    def submitname(self):
        print("a cat name submitted: ")
        self.output.delete(0,END)
        self.output.insert(0,self.catnameentry.get())




if __name__ == '__main__':
    myTkRoot = Tk()
    my_gui = MyFirstGUI(myTkRoot)
    myTkRoot.mainloop()

