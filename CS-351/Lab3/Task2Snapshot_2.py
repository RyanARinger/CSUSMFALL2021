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

        #Row 1
        self.label1 = Label(self.master, text="Cat Name: ")
        self.label1.grid(row=0, column=0, sticky=E)

        self.catnameentry = Entry(self.master)
        self.catnameentry.grid(row=0, column=1, sticky=E)

        self.label2 = Label(self.master, text="Cat ID: ")
        self.label2.grid(row=0, column=2, sticky=E)

        self.idEntry = Entry(self.master)
        self.idEntry.grid(row=0, column=3, sticky=E)

        self.submitbutton = Button(self.master, text="Submit name", command=self.submitname)
        self.submitbutton.grid(row=0, column=4, sticky=E)

        #Row 2
        self.outputLabel = Label(self.master, text="Registered Cat Name: ")
        self.outputLabel.grid(row=1, column=0, sticky=E)

        self.catNameOutput = Entry(self.master)
        self.catNameOutput.grid(row=1, column=1, sticky=E)

        self.catIDLabel = Label(self.master, text="Registered ID: ")
        self.catIDLabel.grid(row=1, column=2, sticky=E)

        self.catIDOutput = Entry(self.master)
        self.catIDOutput.grid(row=1, column=3, sticky=E)

        self.printDatabase = Button(self.master, text="Print Database", command=self.submitname)
        self.printDatabase.grid(row=1, column=4, sticky=E)



    def submitname(self):

        if self.catnameentry.get() == "" or self.idEntry.get() == "":

            print("ERROR: Missing field")

        else:
            self.catNameOutput.delete(0, END)
            self.catNameOutput.insert(0, self.catnameentry.get())

            self.catIDOutput.delete(0, END)
            self.catIDOutput.insert(0, self.idEntry.get())



if __name__ == '__main__':
    myTkRoot = Tk()
    my_gui = MyFirstGUI(myTkRoot)
    myTkRoot.mainloop()

