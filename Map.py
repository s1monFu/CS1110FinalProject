"""
Map
"""
from tkinter import *
import Country
day_count = 0
root = Tk()
x = 1
if x == 1:
    z = "green"
else:
    z = "red"
c = 2
if c == 1:
    p = "green"
else:
    p = "red"
f = 2
if f == 1:
    r = "green"
else:
    r = "red"


class map:
    def __int__(self, name):
        self.name = name

    def showMap(self):
        canvas = Canvas(root, width="750", height="750")
        canvas.create_rectangle(0, 0, 750, 750, fill="blue")
        canvas.create_polygon(500, 500, 485, 480, 475, 475, 460, 480, 430, 500, 420, 500, 400, 460, 370, 440, 330, 430,
                              290, 420, 220, 410,
                              200, 420, 190, 435, 180, 455, 185, 460, 200, 490, 210, 500, 225, 505, 235, 510, 195, 530,
                              160, 530, 155, 540, 150, 550, 145, 560, 150, 570, 160, 585, 175, 590, 200, 585, 210, 580,
                              240, 569, 250, 569, 300, 560, 320, 560, 420, 575, 460, 650, 470, 660, 480, 665, 540, 650,
                              570, 640, 580, 630, 585, 620, 587, 610, 590, 600, 585, 500
                              , fill=z, outline="black")
        canvas.create_polygon(585, 500, 500, 500, 485, 480, 475, 475, 460, 480, 430, 500, 420, 500, 400, 460, 370, 440,
                              330, 430,
                              320, 200, 330, 100, 370, 90, 420, 85, 510, 83, 600, 90, 650, 100, 700, 120, 710, 130, 715,
                              140, 717, 150, 715, 160,
                              710, 170, 700, 180, 670, 190, 620, 260, 610, 270, 615, 285, 650, 340, 660, 350, 665, 360,
                              667, 370, 665, 380,
                              660, 390, 650, 400, 645, 403, 635, 408, 625, 410, 600, 413
                              , fill=p, outline="black")
        canvas.create_polygon(330, 430, 290, 420, 220, 410, 225, 400, 225, 394, 220, 300, 170, 250, 160, 240, 155, 220,
                              140, 215, 130, 205,
                              100, 130, 90, 70, 100, 60, 105, 50, 107, 40, 117, 42, 125, 50, 135, 55, 300, 85, 330, 100,
                              320, 200
                              , fill=r, outline="black")
        canvas.create_oval(190, 225, 160, 160, fill="blue")
        canvas.pack()
        root.mainloop()


class MainShop:
    howTroops = 0
    timesBought = 0

    def __init__(self, name):
        self.name = name
        self.canva = None

    def showShop(self, player_country):

        def buyArcher():
            if checkLevel(1) == True:
                if checkCap():
                    if checkBal(10) == True:
                        player_country.num_gold = int(player_country.num_gold) - 10
                        MainShop.howTroops += 1
                        updateScreen(self.canva)

        def buySwordsman():
            if checkLevel(1) == True:
                if checkCap() == True:
                    if checkBal(15) == True:
                        player_country.num_gold = int(player_country.num_gold) - 15
                        MainShop.howTroops += 1
                        updateScreen(self.canva)

        def buyPriest():
            if checkLevel(2) == True:
                if checkCap() == True:
                    if checkBal(30) == True:
                        player_country.num_gold = int(player_country.num_gold) - 30
                        MainShop.howTroops += 1
                        updateScreen(self.canva)

        def buySpear():
            if checkLevel(2) == True:
                if checkCap() == True:
                    if checkBal(20) == True:
                        player_country.num_gold = int(player_country.num_gold) - 20
                        MainShop.howTroops += 1
                        updateScreen(self.canva)

        def buyHorse():
            if checkLevel(3) == True:
                if checkCap() == True:
                    if checkBal(30) == True:
                        player_country.num_gold = int(player_country.num_gold) - 30
                        MainShop.howTroops += 1
                        updateScreen(self.canva)

        def buyBlack():
            if checkLevel(3) == True:
                if checkCap() == True:
                    if checkBal(40) == True:
                        player_country.num_gold = int(player_country.num_gold) - 40
                        MainShop.howTroops += 1
                        updateScreen(self.canva)

        def buyBallista():
            if checkLevel(4) == True:
                if checkCap() == True:
                    if checkBal(50) == True:
                        player_country.num_gold = int(player_country.num_gold) - 50
                        MainShop.howTroops += 1
                        updateScreen(self.canva)

        def buyDragon():
            if checkLevel(5) == True:
                if checkCap() == True:
                    if checkBal(70) == True:
                        player_country.num_gold = int(player_country.num_gold) - 70
                        MainShop.howTroops += 1
                        updateScreen(self.canva)

        def checkCap():
            if player_country.max_troop > MainShop.howTroops:
                return True
            else:
                alert_popup("Uh Oh", "You don't have enough housing space!",
                            "You currently can only hold " + str(player_country.max_troop) + " soldiers.")

        def checkLevel(needed):
            if player_country.level >= needed:
                return True
            else:
                alert_popup("Uh Oh", "You are not high enough level!",
                            "You need to be level " + str(needed) + " to purchase this.")

        def checkBal(cost):
            if player_country.num_gold >= cost:
                return True
            else:
                alert_popup("Uh Oh!", "You do not have enough gold", ":(")

        def increaseMax():
            if MainShop.timesBought == 0:
                if checkBal(25) == True:
                    player_country.max_troop += 3
                    player_country.num_gold = int(player_country.num_gold) - 25
                    updateScreen(self.canva)
                    updateUpgrade(self.canva)
                    MainShop.timesBought += 1
            elif MainShop.timesBought == 1:
                if checkLevel(3) == True:
                    if checkBal(50) == True:
                        player_country.max_troop += 4
                        updateScreen(self.canva)
                        player_country.num_gold = int(player_country.num_gold) - 50
                        updateScreen(self.canva)
                        updateUpgrade(self.canva)
                        MainShop.timesBought += 1
            elif MainShop.timesBought == 2:
                if checkLevel(5) == True:
                    if checkBal(120) == True:
                        player_country.max_troop += 8
                        updateScreen(self.canva)
                        player_country.num_gold = int(player_country.num_gold) - 120
                        updateScreen(self.canva)
                        updateUpgrade(self.canva)
                        MainShop.timesBought += 1

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

        def changeText2():
            if MainShop.timesBought == 0:
                labe8 = Label(text="Cost: 50 Gold. Increase your maximum troops to 12.", width=10, anchor="w")
                labe8.configure(width=60, activebackground="brown", relief=FLAT)
                labe8_window = self.canva.create_window(100, 320, anchor=NW, window=labe8)
            elif MainShop.timesBought == 1:
                labe8 = Label(text="Cost: 120 Gold. Increase your maximum troops to 20.", width=10, anchor="w")
                labe8.configure(width=60, activebackground="brown", relief=FLAT)
                labe8_window = self.canva.create_window(100, 320, anchor=NW, window=labe8)
            elif MainShop.timesBought == 2:
                labe8 = Label(text="MAXED. You cannot purchase this anymore.", width=10, anchor="w")
                labe8.configure(width=60, activebackground="brown", relief=FLAT)
                labe8_window = self.canva.create_window(100, 320, anchor=NW, window=labe8)

        def updateUpgrade(name: Canvas):
            self.name = name
            self.name.after(200, changeText2())

        def updateScreen(name: Canvas):
            self.name = name
            self.name.after(200, changeText())

        def delete(name: Canvas):
            name.destroy()

        def quity():
            delete(self.canva)
            myshop.sleepScreen()

        def quit():
            delete(self.canva)
            myshop.mainScreen()

        def changeText():
            label = Label(text="Gold:" + str(player_country.num_gold), width=10)
            label.configure(width=10, activebackground="brown", relief=FLAT)
            label_window = self.canva.create_window(650, 10, anchor=NW, window=label)

        self.canva = Canvas(root, width="750", height="750", bg="brown")
        label2 = Label(text="Troops", width=40)
        label2.configure(width=15, activebackground="brown", relief=FLAT, font=("Courier", 15), bg="brown", fg="white")
        label2_window = self.canva.create_window(250, 10, anchor=NW, window=label2)

        label3 = Label(text="Upgrades", width=40)
        label3.configure(width=15, activebackground="brown", relief=FLAT, font=("Courier", 15), bg="brown", fg="white")
        label3_window = self.canva.create_window(260, 290, anchor=NW, window=label3)

        button1 = Button(root, text="Archer", command=buyArcher)
        button1.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button1_window = self.canva.create_window(10, 40, anchor=NW, window=button1)
        labe2 = Label(text="Cost: 10 Gold.  A long range marksman, while he only has 10 health, he has 15 attack",
                      width=10, anchor="w")
        labe2.configure(width=70, activebackground="brown", relief=FLAT)
        labe2_window = self.canva.create_window(100, 40, anchor=NW, window=labe2)

        button2 = Button(root, text="Swordsman", command=buySwordsman)
        button2.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button2_window = self.canva.create_window(10, 70, anchor=NW, window=button2)
        labe2 = Label(text="Cost: 15 Gold.  A short ranged fighter, he has 30 health, but only 10 attack", width=10,
                      anchor="w")
        labe2.configure(width=60, activebackground="brown", relief=FLAT)
        labe2_window = self.canva.create_window(100, 70, anchor=NW, window=labe2)

        button3 = Button(root, text="Priest", command=buyPriest)
        button3.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button3_window = self.canva.create_window(10, 100, anchor=NW, window=button3)
        labe3 = Label(text="Cost: 30 Gold. TEAM PLAYER: Randomly give 5 friendly soldiers +1 health."
                           " It has 40 health and 5 attack", width=10, anchor="w")
        labe3.configure(width=82, activebackground="brown", relief=FLAT)
        labe3_window = self.canva.create_window(100, 100, anchor=NW, window=labe3)

        button4 = Button(root, text="Spearman", command=buySpear)
        button4.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button4_window = self.canva.create_window(10, 130, anchor=NW, window=button4)
        labe4 = Label(text="Cost: 20 Gold. He keeps the stick on him, he has 20 health and 20 attack", width=10,
                      anchor="w")
        labe4.configure(width=60, activebackground="brown", relief=FLAT)
        labe4_window = self.canva.create_window(100, 130, anchor=NW, window=labe4)

        button5 = Button(root, text="Calvary Raider", command=buyHorse)
        button5.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button5_window = self.canva.create_window(10, 160, anchor=NW, window=button5)
        labe5 = Label(text="Cost: 30 Gold. A horse riding unit, he has 35 health, but only 25 attack", width=10,
                      anchor="w")
        labe5.configure(width=60, activebackground="brown", relief=FLAT)
        labe5_window = self.canva.create_window(100, 160, anchor=NW, window=labe5)

        button6 = Button(root, text="Blacksmith", command=buyBlack)
        button6.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button6_window = self.canva.create_window(10, 190, anchor=NW, window=button6)
        labe6 = Label(text="Cost: 40 Gold. TEAM PLAYER: Randomly give 5 friendly soldiers +1 attack,"
                           " he has 20 health, but hat 25 attack", width=10)
        labe6.configure(width=84, activebackground="brown", relief=FLAT)
        labe6_window = self.canva.create_window(100, 190, anchor=NW, window=labe6)

        button7 = Button(root, text="Ballista", command=buyBallista)
        button7.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button7_window = self.canva.create_window(10, 220, anchor=NW, window=button7)
        labe7 = Label(text="Cost: 50 Gold. A mechanical masterpiece, he has 75 health, and 45 attack", width=10,
                      anchor="w")
        labe7.configure(width=60, activebackground="brown", relief=FLAT)
        labe7_window = self.canva.create_window(100, 220, anchor=NW, window=labe7)

        button8 = Button(root, text="Dragon", command=buyDragon)
        button8.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button8_window = self.canva.create_window(10, 250, anchor=NW, window=button8)
        labe8 = Label(text="Cost: 70 Gold. Watch your 6, he has 85 health and 70 attack", width=10, anchor="w")
        labe8.configure(width=60, activebackground="brown", relief=FLAT)
        labe8_window = self.canva.create_window(100, 250, anchor=NW, window=labe8)

        button8 = Button(root, text="Troop Space", command=increaseMax)
        button8.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button8_window = self.canva.create_window(10, 320, anchor=NW, window=button8)
        labe8 = Label(text="Cost: 25 Gold. Increase your maximum troops to 8.", width=10, anchor="w")
        labe8.configure(width=60, activebackground="brown", relief=FLAT)
        labe8_window = self.canva.create_window(100, 320, anchor=NW, window=labe8)

        button9 = Button(root, text="Back", command=quit)
        button9.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button9_window = self.canva.create_window(340, 700, anchor=NW, window=button9)


        label = Label(text="Gold:" + str(player_country.num_gold), width=10)
        label.configure(width=10, activebackground="brown", relief=FLAT)
        label_window = self.canva.create_window(650, 10, anchor=NW, window=label)
        self.canva.pack()
        root.mainloop()

    def showMShop(self, player_country):

        def buyEle():
            if checkLevel(1) == True:
                if checkCap() == True:
                    if checkBal(40) == True:
                        player_country.num_gold = int(player_country.num_gold) - 40
                        MainShop.howTroops += 1
                        updateScreen(self.canva)

        def buyCross():
            if checkLevel(2) == True:
                if checkCap() == True:
                    if checkBal(20) == True:
                        player_country.num_gold = int(player_country.num_gold) - 20
                        MainShop.howTroops += 1
                        updateScreen(self.canva)

        def checkCap():
            if player_country.max_troop > MainShop.howTroops:
                return True
            else:
                alert_popup("Uh Oh", "You don't have enough housing space!",
                            "You currently can only hold " + str(player_country.max_troop) + " soldiers.")

        def checkLevel(needed):
            if player_country.level >= needed:
                return True
            else:
                alert_popup("Uh Oh", "You are not high enough level!",
                            "You need to be level " + str(needed) + " to purchase this.")

        def checkBal(cost):
            if player_country.num_gold >= cost:
                return True
            else:
                alert_popup("Uh Oh!", "You do not have enough gold", ":(")

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
            self.name.after(200, changeText())

        def changeText():
            label = Label(text=player_country.num_gold, width=10)
            label.configure(width=10, activebackground="brown", relief=FLAT)
            label_window = self.canva.create_window(700, 10, anchor=NW, window=label)

        self.canva = Canvas(root, width="750", height="750", bg="brown")
        labell = Label(text="Gold:" + str(player_country.num_gold), width=10)
        labell.configure(width=10, activebackground="brown", relief=FLAT)
        labell_window = self.canva.create_window(660, 10, anchor=NW, window=labell)

        buttony2 = Button(root, text="Crossbowman", command=buyCross)
        buttony2.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        buttony2_window = self.canva.create_window(10, 40, anchor=NW, window=buttony2)
        labey2 = Label(text="Cost: 20 Gold. An expert marksman, he has 20 health, and only 40 attack", width=10,
                       anchor="w")
        labey2.configure(width=60, activebackground="brown", relief=FLAT)
        labey2_window = self.canva.create_window(100, 40, anchor=NW, window=labey2)

        buttony3 = Button(root, text="War Elephant", command=buyEle)
        buttony3.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        buttony3_window = self.canva.create_window(10, 70, anchor=NW, window=buttony3)
        labey3 = Label(text="Cost: 40 Gold. A walking tank, he has 75 health, and only 35 attack", width=10,
                       anchor="w")
        labey3.configure(width=60, activebackground="brown", relief=FLAT)
        labey3_window = self.canva.create_window(100, 70, anchor=NW, window=labey3)

        label2 = Label(text="Merchant Shop", width=40)
        label2.configure(width=15, activebackground="brown", relief=FLAT, font=("Courier", 15), bg="brown", fg="white")
        label2_window = self.canva.create_window(250, 10, anchor=NW, window=label2)

        self.canva.pack()

    def showMap(self):
        canva = Canvas(root, width="750", height="750")
        canva.create_rectangle(0, 0, 750, 750, fill="blue")
        canva.create_polygon(500, 500, 485, 480, 475, 475, 460, 480, 430, 500, 420, 500, 400, 460, 370, 440, 330, 430,
                             290, 420, 220, 410,
                             200, 420, 190, 435, 180, 455, 185, 460, 200, 490, 210, 500, 225, 505, 235, 510, 195, 530,
                             160, 530, 155, 540, 150, 550, 145, 560, 150, 570, 160, 585, 175, 590, 200, 585, 210, 580,
                             240, 569, 250, 569, 300, 560, 320, 560, 420, 575, 460, 650, 470, 660, 480, 665, 540, 650,
                             570, 640, 580, 630, 585, 620, 587, 610, 590, 600, 585, 500
                             , fill=z, outline="black")
        canva.create_polygon(585, 500, 500, 500, 485, 480, 475, 475, 460, 480, 430, 500, 420, 500, 400, 460, 370, 440,
                             330, 430,
                             320, 200, 330, 100, 370, 90, 420, 85, 510, 83, 600, 90, 650, 100, 700, 120, 710, 130, 715,
                             140, 717, 150, 715, 160,
                             710, 170, 700, 180, 670, 190, 620, 260, 610, 270, 615, 285, 650, 340, 660, 350, 665, 360,
                             667, 370, 665, 380,
                             660, 390, 650, 400, 645, 403, 635, 408, 625, 410, 600, 413
                             , fill=p, outline="black")
        canva.create_polygon(330, 430, 290, 420, 220, 410, 225, 400, 225, 394, 220, 300, 170, 250, 160, 240, 155, 220,
                             140, 215, 130, 205,
                             100, 130, 90, 70, 100, 60, 105, 50, 107, 40, 117, 42, 125, 50, 135, 55, 300, 85, 330, 100,
                             320, 200
                             , fill=r, outline="black")
        canva.create_oval(190, 225, 160, 160, fill="blue")
        canva.pack()
        root.mainloop()


    def sleepScreen(self):
        self.canva = Canvas(root, width="750", height="750", bg="black")
        label2 = Label(text="Day: " + str(day_count), width=40)
        label2.configure(width=15, activebackground="black", relief=FLAT, font=("Courier", 50), bg="black", fg="white")
        label2_window = self.canva.create_window(100, 100, anchor=NW, window=label2)
        self.canva.pack()
        root.mainloop()
        print("something random")


    def mainScreen(self):

        def delete(name: Canvas):
            name.destroy()

        def quityy():
            delete(self.canva)
            myshop.showChooseB()

        def quity():
            delete(self.canva)
            myshop.sleepScreen()

        self.canva = Canvas(root, width="750", height="750", bg="sky blue")


        button9 = Button(root, text="Sleep", command=quity)
        button9.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button9_window = self.canva.create_window(10, 700, anchor=NW, window=button9)

        button9 = Button(root, text="Battle", command=quityy)
        button9.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button9_window = self.canva.create_window(180, 700, anchor=NW, window=button9)
        self.canva.pack()
        root.mainloop()

    def showChooseB(self):
        def delete(name: Canvas):
            name.destroy()

        def quityyy():
            delete(self.canva)
            myshop.showBScreen()

        def quityyyy():
            delete(self.canva)
            myshop.showBScreen()

        self.canva = Canvas(root, width="750", height="750", bg="black")

        button9 = Button(root, text="a", command=quityyy, font=("Courier", 25))
        button9.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button9_window = self.canva.create_window(10, 400, anchor=NW, window=button9)

        button7 = Button(root, text="b", command=quityyyy, font=("Courier", 25))
        button7.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button7_window = self.canva.create_window(400, 400, anchor=NW, window=button7)

        self.canva.pack()
        root.mainloop()

    def backtomain(self):
        MainShop.delete(self.canva)
        myshop.mainScreen(self)

    def showBScreen(self):

        roundnum = 0

        canva = Canvas(root, width="750", height="750", bg="blue")

        label2 = Label(text="Our Power", width=40)
        label2.configure(width=15, activebackground="brown", relief=FLAT, font=("Courier", 15), bg="brown", fg="white")
        label2_window = canva.create_window(10, 10, anchor=NW, window=label2)

        label22 = Label(text="Enemy Power", width=40)
        label22.configure(width=15, activebackground="brown", relief=FLAT, font=("Courier", 15), bg="brown", fg="white")
        label22_window = canva.create_window(550, 10, anchor=NW, window=label22)

        label222 = Label(text=str(Country.country.get_total_cp()), width=40)
        label222.configure(width=15, activebackground="brown", relief=FLAT, font=("Courier", 15), bg="brown", fg="white")
        label222_window = canva.create_window(10, 150, anchor=NW, window=label222)

        label2233 = Label(text="Enemy Power", width=40)
        label2233.configure(width=15, activebackground="brown", relief=FLAT, font=("Courier", 15), bg="brown", fg="white")
        label2233_window = canva.create_window(550, 150, anchor=NW, window=label2233)

        label3 = Label(text="Upgrades", width=40)
        label3.configure(width=15, activebackground="brown", relief=FLAT, font=("Courier", 15), bg="brown", fg="white")
        label3_window = canva.create_window(260, 290, anchor=NW, window=label3)

        button4 = Button(root, text="Start to attack", font=("Courier", 25))
        button4.configure(width=20, activebackground="#33B5E5", relief=FLAT)
        button4_window = canva.create_window(140, 400, anchor=NW, window=button4)

        button5 = Button(root, text="Aggressive", font=("Courier", 15))
        button5.configure(width=15, activebackground="#33B5E5", relief=FLAT)
        button5_window = canva.create_window(50, 500, anchor=NW, window=button5)

        button6 = Button(root, text="Neutral", font=("Courier", 15))
        button6.configure(width=15, activebackground="#33B5E5", relief=FLAT)
        button6_window = canva.create_window(275, 500, anchor=NW, window=button6)

        button7 = Button(root, text="Defensive", font=("Courier", 15))
        button7.configure(width=15, activebackground="#33B5E5", relief=FLAT)
        button7_window = canva.create_window(500, 500, anchor=NW, window=button7)

        label2 = Label(text="Round Number: " + str(roundnum), width=40)
        label2.configure(width=15, activebackground="brown", relief=FLAT, font=("Courier", 15), bg="brown", fg="white")
        label2_window = canva.create_window(250, 600, anchor=NW, window=label2)

        canva.pack()
        root.mainloop()
myshop = MainShop('shop')
