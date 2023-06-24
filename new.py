class note:
    allnotes = list()

    def addnote(self, thenote):
        note.allnotes.append(thenote)

    def showallnotes(self):
        num = 0
        for i in note.allnotes:
            print(f"[{num}]", f"{i} \n")
            num += 1

    def delNote(self):
        note.showallnotes(self)
        a = int(
            input("chose the note you wnat to delete\nEnter the Index of the note: "))
        note.allnotes.pop(a)

    def markAsDone(self):
        note.showallnotes(self)
        a = int(input("Which have you done: "))
        note.allnotes[a] = "\u0336".join(note.allnotes[a])
        note.showallnotes(self)


a = note()
<<<<<<< HEAD
a.addnote("this is a test")
a.addnote("hello")
a.addnote("this is a another text just to test thigs")
a.addnote("hello from the other side")
a.addnote("yolo")
a.delNote()

=======
a.addnote("get the milk")
a.addnote("write the new project Code")
a.addnote("call Mom")
a.addnote("go to gym")
a.markAsDone()
a.markAsDone()
a.markAsDone()
>>>>>>> adding_MarkDone
