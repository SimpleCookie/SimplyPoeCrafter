from tkinter import *

def setup_main_window(geo):
  mainWindow = Tk()
  mainWindow.title("Simply Crafter")
  mainWindow.geometry(geo)
  favicon = PhotoImage(file='favicon.png')
  mainWindow.iconphoto(True, favicon)
  mainWindow.config(background="#DDD")
  return mainWindow

def save_alt(pos):
  global altLoc
  print("pos" + str(pos))
  altLoc = "3"

def save_aug(pos):
  global augLoc
  print("pos: " + str(pos))

def scope(save):
  diameter = 60
  prmpt = Tk()
  prmpt.geometry("300x150")
  prmpt.wm_attributes("-transparentcolor", "#60b26c")
  frame = Frame(prmpt, width=diameter, height=diameter, bg="#60b26c")

  myCanvas = Canvas(frame, width=diameter, height=diameter, bg="#60b26c")
  myCanvas.create_line(0, 0, diameter, diameter, fill="red")
  myCanvas.create_line(diameter, 0, 0, diameter, fill="red")
  myCanvas.pack()

  pos = (myCanvas.winfo_rootx(), myCanvas.winfo_rooty())

  saveBtn = Button(prmpt, text="Save", command=lambda: save(pos))

  frame.pack(pady=20)
  saveBtn.pack()

def test_f():
  print(altLoc)

altLoc = "Not set"
augLoc = "Not set"

mainWindow = setup_main_window("800x500")
altLocLabel = Label(mainWindow, text=altLoc)
augLocLabel = Label(mainWindow, text=augLoc)
altBtn = Button(mainWindow, text="Configure alteration", command=lambda: scope(save_alt))
augBtn = Button(mainWindow, text="Configure Augmentation", command=lambda: scope(save_aug))



altBtn.pack()
altLocLabel.pack()

test = Button(mainWindow, text="test", command=test_f)
test.pack()

mainWindow.mainloop()
