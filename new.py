class note:
    allnotes = list()

    def addnote(self, thenote):
        note.allnotes.append(thenote)

    def showallnotes(self):
        num = 0
        for i in note.allnotes:
            print(num, f"{i} \n")
            num += 1

    def delNote(self):
        note.showallnotes(self)
        a = int(
            input("chose the note you wnat to delete\nEnter the Index of the note:"))
        note.allnotes.pop(a)
        note.showallnotes(self)

    def markAsDone(self):
        pass


a = note()
a.addnote("this is a test")
a.addnote("hello")
a.addnote("this is a another text just to test thigs")
a.addnote("hello from the other side")
a.addnote("yolo")
a.delNote()


# all the func i have now works just fine
# SO to test the branching and other things in git
# lets make a new branch to develop rest of the project




#this is where i wnat to add the markDone function
