"""
Map
"""
from tkinter import *
gold=100

root = Tk()
x=1
if x == 1: z="green"
else:z="red"
c=2
if c == 1: p="green"
else:p="red"
f=2
if f == 1: r="green"
else:r="red"

class Map:
    def __int__(self, name):
        self.name=name

    def showMap(self):
        canvas = Canvas(root, width="750", height="750")
        canvas.create_rectangle(0, 0, 750, 750, fill="blue")
        canvas.create_polygon(500,500,485,480,475,475,460,480,430,500,420,500,400,460,370,440,330,430,290,420,220,410,
                              200,420,190,435,180,455,185,460,200,490,210,500,225,505,235,510,195,530,
                              160,530,155,540,150,550,145,560,150,570,160,585,175,590,200,585,210,580,
                              240,569,250,569,300,560,320,560, 420,575, 460,650,470,660,480,665,540,650,
                              570,640,580,630,585,620, 587,610, 590,600,585,500
                              ,fill=z, outline="black")
        canvas.create_polygon(585,500,500, 500, 485, 480, 475, 475, 460, 480, 430, 500, 420, 500, 400, 460, 370, 440, 330, 430,
                              320,200, 330,100,370,90,420,85,510,83,600,90,650,100,700,120,710,130,715,140,717,150,715,160,
                              710,170,700,180,670,190,620,260,610,270,615,285,650,340,660,350,665,360,667,370,665,380,
                              660,390,650,400,645,403,635,408,625,410,600,413
                               ,fill=p, outline="black")
        canvas.create_polygon(330,430,290,420,220,410,225,400,225,394,220,300,170,250,160,240,155,220,140,215,130,205,
                              100,130,90,70,100,60,105,50,107,40,117,42,125,50,135,55,300,85,330,100,320,200
                              ,fill=r, outline="black")
        canvas.pack()
        root.mainloop()

class Hi:
    gold=100


    def __init__(self,name):
        self.name = name

    def showShop(self):
        def buyArcher():
            if Hi.gold<10:
                alert_popup("Uh Oh!","You do not have enought gold",":(")
            else:
                Hi.gold = int(Hi.gold) - 10
                updateScreen(canva)

        def buySwordsman():
            if Hi.gold<15:
                alert_popup("Uh Oh!","You do not have enought gold",":(")
            else:
                Hi.gold = int(Hi.gold) - 15
                updateScreen(canva)

        def alert_popup(title, message, path):
            """Generate a pop-up window for special messages."""
            root = Tk()
            root.title(title)
            w = 400  # popup window width
            h = 200  # popup window height
            sw = root.winfo_screenwidth()
            sh = root.winfo_screenheight()
            x = (sw - w) / 2
            y = (sh - h) / 2
            root.geometry('%dx%d+%d+%d' % (w, h, x, y))
            m = message
            m += '\n'
            m += path
            w = Label(root, text=m, width=120, height=10)
            w.pack()
            b = Button(root, text="OK", command=root.destroy, width=10)
            b.pack()
            mainloop()

        def updateScreen(name: Canvas):
            self.name = name
            self.name.after(200,changeText())

        def changeText():
            label = Label(text=Hi.gold, width=10)
            label.configure(width=10, activebackground="brown", relief=FLAT)
            label_window = canva.create_window(700, 10, anchor=NW, window=label)

        canva = Canvas(root, width="750", height="750",bg="brown")
        button1 = Button(root,text="Archer", command=buyArcher)
        button1.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button1_window = canva.create_window(10, 10, anchor=NW, window=button1)
        labe2 = Label(text="Cost: 10 Gold.", width=10)
        labe2.configure(width=30, activebackground="brown", relief=FLAT)
        labe2_window = canva.create_window(200, 10, anchor=NW, window=labe2)
        button2 = Button(root, text="Swordsman", command=buySwordsman)
        button2.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button2_window = canva.create_window(10, 40, anchor=NW, window=button2)
        labe2 = Label(text="Cost: 15 Gold.",width=10)
        labe2.configure(width=30, activebackground="brown", relief=FLAT)
        labe2_window = canva.create_window(200, 40, anchor=NW, window=labe2)
        label = Label(text="Gold:" + str(Hi.gold), width=10)
        label.configure(width=10, activebackground="brown", relief=FLAT)
        label_window = canva.create_window(660, 10, anchor=NW, window=label)
        canva.pack()
        root.mainloop()

