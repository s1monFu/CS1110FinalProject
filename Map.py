"""
Map
"""
from tkinter import *
import random
from Player_country import player_country
import AI_country
import Strategy

root = Tk()

Player = player_country(2, 'Kindom')


class MainShop:
    howTroops = 0
    timesBought = 0
    day_count = 0
    leveltimesBought = 0


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

    def __init__(self, name):
        self.name = name
        self.canva = None

    def showShop(self, Player):

        def buyArcher():
            if checkLevel(1) == True:
                if checkCap():
                    if checkBal(10) == True:
                        Player.num_gold = int(Player.num_gold) - 10
                        Player.troop_list['Ranger'][0] += 1
                        updateScreen(self.canva)

        def buySwordsman():
            if checkLevel(1) == True:
                if checkCap() == True:
                    if checkBal(15) == True:
                        Player.num_gold = int(Player.num_gold) - 15
                        Player.troop_list['Swordsman'][0] += 1
                        updateScreen(self.canva)

        def buyPriest():
            if checkLevel(2) == True:
                if checkCap() == True:
                    if checkBal(30) == True:
                        Player.num_gold = int(Player.num_gold) - 30
                        Player.troop_list['Priest'][0] += 1
                        updateScreen(self.canva)

        def buySpear():
            if checkLevel(2) == True:
                if checkCap() == True:
                    if checkBal(20) == True:
                        Player.num_gold = int(Player.num_gold) - 20
                        Player.troop_list['Spearman'][0] += 1
                        updateScreen(self.canva)

        def buyHorse():
            if checkLevel(3) == True:
                if checkCap() == True:
                    if checkBal(30) == True:
                        Player.troop_list['CalvaryRaider'][0] += 1
                        updateScreen(self.canva)

        def buyBlack():
            if checkLevel(3) == True:
                if checkCap() == True:
                    if checkBal(40) == True:
                        Player.num_gold = int(Player.num_gold) - 40
                        Player.troop_list['BlackSmith'][0] += 1
                        updateScreen(self.canva)

        def buyBallista():
            if checkLevel(4) == True:
                if checkCap() == True:
                    if checkBal(50) == True:
                        Player.num_gold = int(Player.num_gold) - 50
                        Player.troop_list['Ballista'][0] += 1
                        updateScreen(self.canva)

        def buyDragon():
            if checkLevel(5) == True:
                if checkCap() == True:
                    if checkBal(70) == True:
                        Player.num_gold = int(Player.num_gold) - 70
                        Player.troop_list['Dragon'][0] += 1
                        updateScreen(self.canva)

        def checkCap():
            if Player.max_troop > Player.getSoldiersNum():
                return True
            else:
                alert_popup("Uh Oh", "You don't have enough housing space!",
                            "You currently can only hold " + str(Player.max_troop) + " soldiers.")

        def checkLevel(needed):
            if Player.level >= needed:
                return True
            else:
                alert_popup("Uh Oh", "You are not high enough level!",
                            "You need to be level " + str(needed) + " to purchase this.")

        def checkBal(cost):
            if int(Player.num_gold) >= cost:
                return True
            else:
                alert_popup("Uh Oh!", "You do not have enough gold", ":(")

        def increaseMax():
            if MainShop.timesBought == 0:
                if checkBal(25) == True:
                    Player.max_troop += 3
                    Player.num_gold = int(Player.num_gold) - 25
                    updateScreen(self.canva)
                    updateUpgrade(self.canva)
                    MainShop.timesBought += 1
            elif MainShop.timesBought == 1:
                if checkLevel(3) == True:
                    if checkBal(50) == True:
                        Player.max_troop += 4
                        updateScreen(self.canva)
                        Player.num_gold = int(Player.num_gold) - 50
                        updateScreen(self.canva)
                        updateUpgrade(self.canva)
                        MainShop.timesBought += 1
            elif MainShop.timesBought == 2:
                if checkLevel(5) == True:
                    if checkBal(120) == True:
                        Player.max_troop += 8
                        updateScreen(self.canva)
                        Player.num_gold = int(Player.num_gold) - 120
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

        def updateUpgraded(name: Canvas):
            self.name = name
            self.name.after(200, changeText3())

        def updateUpgrade(name: Canvas):
            self.name = name
            self.name.after(200, changeText2())

        def updateScreen(name: Canvas):
            self.name = name
            self.name.after(200, changeText())

        def delete(name: Canvas):
            name.destroy()

        def increaseLMax():
            if MainShop.timesBought == 0:
                if checkBal(30) == True:
                    Player.level += 1
                    Player.num_gold = int(Player.num_gold) - 30
                    updateScreen(self.canva)
                    updateUpgraded(self.canva)
                    MainShop.leveltimesBought += 1
            elif MainShop.timesBought == 1:
                    if checkBal(40) == True:
                        Player.level += 1
                        updateScreen(self.canva)
                        Player.num_gold = int(Player.num_gold) - 40
                        updateScreen(self.canva)
                        updateUpgraded(self.canva)
                        MainShop.leveltimesBought += 1
            elif MainShop.timesBought == 2:
                    if checkBal(50) == True:
                        Player.level += 1
                        updateScreen(self.canva)
                        Player.num_gold = int(Player.num_gold) - 50
                        updateScreen(self.canva)
                        updateUpgraded(self.canva)
                        MainShop.leveltimesBought += 1
            elif MainShop.timeslevel == 3:
                    if checkBal(60) == True:
                        Player.level += 1
                        updateScreen(self.canva)
                        Player.num_gold = int(Player.num_gold) - 60
                        updateScreen(self.canva)
                        updateUpgraded(self.canva)
                        MainShop.leveltimesBought += 1

        def changeText3():
            if MainShop.leveltimesBought == 0:
                labe99 = Label(text="Cost: 40 Gold. Increase your level to 3.", width=10, anchor="w")
                labe99.configure(width=60, activebackground="brown", relief=FLAT)
                labe8_window99 = self.canva.create_window(100, 350, anchor=NW, window=labe99)
            elif MainShop.leveltimesBought == 1:
                labe99 = Label(text="Cost: 50 Gold. Increases your level to 4", width=10, anchor="w")
                labe99.configure(width=60, activebackground="brown", relief=FLAT)
                labe99_window = self.canva.create_window(100, 350, anchor=NW, window=labe99)
            elif MainShop.leveltimesBought == 2:
                labe99 = Label(text="Cost: 60 Gold. Increases your level to 5", width=10, anchor="w")
                labe99.configure(width=60, activebackground="brown", relief=FLAT)
                labe99_window = self.canva.create_window(100, 350, anchor=NW, window=labe99)
            elif MainShop.leveltimesBought == 3:
                labe99 = Label(text="MAXED. You cannot purchase this anymore.", width=10, anchor="w")
                labe99.configure(width=60, activebackground="brown", relief=FLAT)
                labe99_window = self.canva.create_window(100, 350, anchor=NW, window=labe99)

        def quit():
            delete(self.canva)
            myshop.mainScreen()

        def changeText():
            label = Label(text="Gold:" + str(Player.num_gold), width=10)
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

        button11 = Button(root, text="Troop Space", command=increaseMax)
        button11.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button11_window = self.canva.create_window(10, 320, anchor=NW, window=button11)
        labe11 = Label(text="Cost: 25 Gold. Increase your maximum troops to 8.", width=10, anchor="w")
        labe11.configure(width=60, activebackground="brown", relief=FLAT)
        labe11_window = self.canva.create_window(100, 320, anchor=NW, window=labe11)

        button99 = Button(root, text="Level", command=increaseLMax)
        button99.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button99_window = self.canva.create_window(10, 350, anchor=NW, window=button99)
        labe99 = Label(text="Cost: 30 Gold. Increases your level to 2", width=10, anchor="w")
        labe99.configure(width=60, activebackground="brown", relief=FLAT)
        labe99_window = self.canva.create_window(100, 350, anchor=NW, window=labe99)

        button9 = Button(root, text="Back", command=quit)
        button9.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button9_window = self.canva.create_window(340, 700, anchor=NW, window=button9)

        label = Label(text="Gold:" + str(Player.num_gold), width=10)
        label.configure(width=10, activebackground="brown", relief=FLAT)
        label_window = self.canva.create_window(650, 10, anchor=NW, window=label)
        self.canva.pack()
        root.mainloop()

    def showMShop(self, Player):
        a = random.randint(0,2)
        def buyEle():
            if checkLevel(1) == True:
                if checkCap() == True:
                    if checkBal(40) == True:
                        Player.num_gold = int(Player.num_gold) - 40
                        Player.troop_list['WarElephant'][0] += 1
                        MainShop.howTroops += 1
                        updateScreen(self.canva)


        def buyCross():
            if checkLevel(2) == True:
                if checkCap() == True:
                    if checkBal(20) == True:
                        Player.num_gold = int(Player.num_gold) - 20
                        Player.troop_list['CrossbowMan'][0] += 1
                        MainShop.howTroops += 1
                        updateScreen(self.canva)

        def checkCap():
            if Player.max_troop > MainShop.howTroops:
                return True
            else:
                alert_popup("Uh Oh", "You don't have enough housing space!",
                            "You currently can only hold " + str(Player.max_troop) + " soldiers.")

        def checkLevel(needed):
            if Player.level >= needed:
                return True
            else:
                alert_popup("Uh Oh", "You are not high enough level!",
                            "You need to be level " + str(needed) + " to purchase this.")

        def checkBal(cost):
            if Player.num_gold >= cost:
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

        def delete(name: Canvas):
            name.destroy()

        def backtomain():
            delete(self.canva)
            self.encounterenemy()
            myshop.mainScreen()

        def backtomain2():
            delete(self.canva)
            myshop.mainScreen()

        def changeText():
            label = Label(text=str(Player.num_gold), width=10)
            label.configure(width=10, activebackground="brown", relief=FLAT)
            label_window = self.canva.create_window(700, 10, anchor=NW, window=label)

        self.canva = Canvas(root, width="750", height="750", bg="brown")
        labell = Label(text="Gold:" + str(Player.num_gold), width=10)
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

        button9 = Button(root, text="Back", command=backtomain2)
        button9.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button9_window = self.canva.create_window(340, 700, anchor=NW, window=button9)

        self.canva.pack()
        root.mainloop()

    def showMap(self):

        def delete(name: Canvas):
            name.destroy()

        def backtomain():
            delete(self.canva)
            myshop.mainScreen()

        self.canva = Canvas(root, width="750", height="750")
        self.canva.create_rectangle(0, 0, 750, 750, fill="blue")
        self.canva.create_polygon(500, 500, 485, 480, 475, 475, 460, 480, 430, 500, 420, 500, 400, 460, 370, 440, 330,
                                  430,
                                  290, 420, 220, 410,
                                  200, 420, 190, 435, 180, 455, 185, 460, 200, 490, 210, 500, 225, 505, 235, 510, 195,
                                  530,
                                  160, 530, 155, 540, 150, 550, 145, 560, 150, 570, 160, 585, 175, 590, 200, 585, 210,
                                  580,
                                  240, 569, 250, 569, 300, 560, 320, 560, 420, 575, 460, 650, 470, 660, 480, 665, 540,
                                  650,
                                  570, 640, 580, 630, 585, 620, 587, 610, 590, 600, 585, 500
                                  , fill=MainShop.z, outline="black")
        self.canva.create_polygon(585, 500, 500, 500, 485, 480, 475, 475, 460, 480, 430, 500, 420, 500, 400, 460, 370,
                                  440,
                                  330, 430,
                                  320, 200, 330, 100, 370, 90, 420, 85, 510, 83, 600, 90, 650, 100, 700, 120, 710, 130,
                                  715,
                                  140, 717, 150, 715, 160,
                                  710, 170, 700, 180, 670, 190, 620, 260, 610, 270, 615, 285, 650, 340, 660, 350, 665,
                                  360,
                                  667, 370, 665, 380,
                                  660, 390, 650, 400, 645, 403, 635, 408, 625, 410, 600, 413
                                  , fill=MainShop.p, outline="black")
        self.canva.create_polygon(330, 430, 290, 420, 220, 410, 225, 400, 225, 394, 220, 300, 170, 250, 160, 240, 155,
                                  220,
                                  140, 215, 130, 205,
                                  100, 130, 90, 70, 100, 60, 105, 50, 107, 40, 117, 42, 125, 50, 135, 55, 300, 85, 330,
                                  100,
                                  320, 200
                                  , fill=MainShop.r, outline="black")
        self.canva.create_oval(190, 225, 160, 160, fill="blue")

        button9 = Button(root, text="Back", command=backtomain)
        button9.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button9_window = self.canva.create_window(340, 700, anchor=NW, window=button9)

        self.canva.pack()
        root.mainloop()

    def encounterenemy(self):
        rand_num = random.randint(0, 10)
        if rand_num < 3:
            self.showBScreen(AI_country.AI_country1)
        elif rand_num > 8:
            self.showBScreen(AI_country.AI_country2)

    def sleepScreen(self):

        def delete(name: Canvas):
            name.destroy()

        def backtomain():
            delete(self.canva)
            self.encounterenemy()
            myshop.mainScreen()

        self.canva = Canvas(root, width="750", height="750", bg="black")

        label2 = Label(text="Day: " + str(MainShop.day_count), width=40)
        label2.configure(width=15, activebackground="black", relief=FLAT, font=("Courier", 50), bg="black", fg="white")
        label2_window = self.canva.create_window(100, 100, anchor=NW, window=label2)

        button9 = Button(root, text="Next Day", command=backtomain)
        button9.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button9_window = self.canva.create_window(340, 700, anchor=NW, window=button9)

        self.canva.pack()
        root.mainloop()
        print("something random")

    def mainScreen(self):

        def delete(name: Canvas):
            name.destroy()

        def goBattle():
            delete(self.canva)
            myshop.showChooseB()

        def goSleep():
            delete(self.canva)
            MainShop.day_count += 1
            Player.num_gold += 30
            myshop.sleepScreen()

        def mapp():
            delete(self.canva)
            myshop.showMap()

        def merchantt():
            delete(self.canva)
            myshop.showMShop(Player)

        def shopp():
            delete(self.canva)
            myshop.showShop(Player)

        self.canva = Canvas(root, width="750", height="750", bg="sky blue")
        self.canva.create_rectangle(0,450,750,750, fill="green")
        self.canva.create_rectangle(325,300,425,450, fill="grey")
        self.canva.create_rectangle(300,350,450,450, fill="grey")
        self.canva.create_rectangle(250,325,300,450, fill="grey")
        self.canva.create_rectangle(450, 325, 500, 450, fill="grey")
        self.canva.create_rectangle(440,310,510,340, fill="grey")
        self.canva.create_rectangle(240, 310, 310, 340, fill="grey")
        self.canva.create_rectangle(365,430,385,450,fill="saddle brown")

        button9 = Button(root, text="Sleep", command=goSleep)
        button9.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button9_window = self.canva.create_window(50, 700, anchor=NW, window=button9)

        button4 = Button(root, text="Battle", command=goBattle)
        button4.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button4_window = self.canva.create_window(196, 700, anchor=NW, window=button4)

        button3 = Button(root, text="Map", command=mapp)
        button3.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button3_window = self.canva.create_window(342, 700, anchor=NW, window=button3)

        button1 = Button(root, text="Shop", command=shopp)
        button1.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button1_window = self.canva.create_window(488, 700, anchor=NW, window=button1)

        button = Button(root, text="Merchant Shop", command=merchantt)
        button.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button_window = self.canva.create_window(632, 700, anchor=NW, window=button)

        self.canva.pack()
        root.mainloop()

    def showChooseB(self):
        def delete(name: Canvas):
            name.destroy()

        def countryA():
            delete(self.canva)
            myshop.showBScreen(AI_country.AI_country1)

        def countryB():
            delete(self.canva)
            myshop.showBScreen(AI_country.AI_country2)

        def delete(name: Canvas):
            name.destroy()

        def backtomain():
            delete(self.canva)
            myshop.mainScreen()

        self.canva = Canvas(root, width="750", height="750", bg="light blue")

        button9 = Button(root, text="Kingdom Ketafa", command=countryA, font=("Courier", 25))
        button9.configure(width=20, activebackground="#33B5E5", relief=FLAT)
        button9_window = self.canva.create_window(150, 150, anchor=NW, window=button9)

        button7 = Button(root, text="Ezstabian Empire", command=countryB, font=("Courier", 25))
        button7.configure(width=20, activebackground="#33B5E5", relief=FLAT)
        button7_window = self.canva.create_window(150, 550, anchor=NW, window=button7)

        buttonquit = Button(root, text="Back", command=backtomain)
        buttonquit.configure(width=10, activebackground="brown", relief=FLAT)
        buttonquit_window = self.canva.create_window(310, 700, anchor=NW, window=buttonquit)

        self.canva.pack()
        root.mainloop()

    def backtomain(self):
        MainShop.delete(self.canva)
        myshop.mainScreen(self)

    def updatePower(self, name: Canvas, thecountry):
        self.name = name
        self.name.after(200, self.changeTextPowerSelf(thecountry))

    def updatePowerS(self, name: Canvas, thecountry):
        self.name = name
        self.name.after(20, self.changeTextPowerStratA(thecountry))

    def updatePowerDefensive(self, name: Canvas, thecountry):
        self.name = name
        self.name.after(200, self.changeTextPowerStratD(thecountry))

    def updatePowerN(self, name: Canvas, thecountry):
        self.name = name
        self.name.after(200, self.changeTextPowerStratN(thecountry))

    def changeTextPowerStratN(self, thecountry):
        label222 = Label(
            text=str(int(Player.get_total_cp(Player.troop_list, thecountry)) + int(Strategy.neutral(Player))), width=40)
        label222.configure(width=15, activebackground="brown", relief=FLAT, font=("Courier", 15), bg="brown",
                           fg="white")
        label222_window = self.canva.create_window(10, 150, anchor=NW, window=label222)

    def changeTextPowerStratD(self, thecountry):
        label222 = Label(
            text=str(int(Player.get_total_cp(Player.troop_list, thecountry)) + int(Strategy.defensive(Player))),
            width=40)
        label222.configure(width=15, activebackground="brown", relief=FLAT, font=("Courier", 15), bg="brown",
                           fg="white")
        label222_window = self.canva.create_window(10, 150, anchor=NW, window=label222)

    def changeTextPowerStratA(self, thecountry):
        label222 = Label(
            text=str(int(Player.get_total_cp(Player.troop_list, thecountry)) + int(Strategy.aggressive(Player))),
            width=40)
        label222.configure(width=15, activebackground="brown", relief=FLAT, font=("Courier", 15), bg="brown",
                           fg="white")
        label222_window = self.canva.create_window(10, 150, anchor=NW, window=label222)

    def changeTextPowerSelf(self, thecountry):
        label222 = Label(text=str(Player.get_total_cp(Player.troop_list, thecountry)), width=40)
        label222.configure(width=15, activebackground="brown", relief=FLAT, font=("Courier", 15), bg="brown",
                           fg="white")
        label222_window = self.canva.create_window(10, 150, anchor=NW, window=label222)

        label2234 = Label(text=str(thecountry.get_total_cp(thecountry.troop_list, Player)), width=40)
        label2234.configure(width=15, activebackground="brown", relief=FLAT, font=("Courier", 15), bg="brown",
                            fg="white")
        label2234_window = self.canva.create_window(550, 150, anchor=NW, window=label2234)

    def attack(self, thecountry):
        Player.attack_countries(thecountry)
        self.roundnum += 1
        label2 = Label(text="Round Number: " + str(self.roundnum), width=40)
        label2.configure(width=15, activebackground="brown", relief=FLAT, font=("Courier", 15), bg="brown", fg="white")
        label2_window = self.canva.create_window(250, 600, anchor=NW, window=label2)

    def showBScreen(self, country):

        def delete(name: Canvas):
            name.destroy()

        def backtomain():
            delete(self.canva)
            myshop.mainScreen()

        def gotoLose():
            delete(self.canva)
            myshop.loseScreen()

        def gotoWin():
            delete(self.canva)
            myshop.winScreen()

        def gotoWon():
            delete(self.canva)
            myshop.wonScreen()

        def defeat(country):
            if Player.get_total_cp(Player.troop_list, country) == 0:
                gotoLose()
            elif country.get_total_cp(country.troop_list, Player) == 0:
                if country.name == AI_country.AI_country1.name:
                    MainShop.p = "green"
                    if MainShop.r == "green":
                        gotoWin()
                    else:
                        gotoWin()
                elif country.name == AI_country.AI_country2.name:
                    MainShop.r = "green"
                    if MainShop.p == "green":
                        gotoWin()
                    else: gotoWin()

        self.roundnum = 0

        self.canva = Canvas(root, width="750", height="750", bg="blue")

        label2 = Label(text="Our Power", width=40)
        label2.configure(width=15, activebackground="brown", relief=FLAT, font=("Courier", 15), bg="brown", fg="white")
        label2_window = self.canva.create_window(10, 10, anchor=NW, window=label2)

        label22 = Label(text="Enemy Power", width=40)
        label22.configure(width=15, activebackground="brown", relief=FLAT, font=("Courier", 15), bg="brown", fg="white")
        label22_window = self.canva.create_window(550, 10, anchor=NW, window=label22)

        label222 = Label(text=str(Player.get_total_cp(Player.troop_list, country)), width=40)
        label222.configure(width=15, activebackground="brown", relief=FLAT, font=("Courier", 15), bg="brown",
                           fg="white")
        label222_window = self.canva.create_window(10, 150, anchor=NW, window=label222)

        label2234 = Label(text=str(country.get_total_cp(country.troop_list, Player)), width=40)
        label2234.configure(width=15, activebackground="brown", relief=FLAT, font=("Courier", 15), bg="brown",
                            fg="white")
        label2234_window = self.canva.create_window(550, 150, anchor=NW, window=label2234)
        """
        Attack
        """
        button4 = Button(root, text="Start to attack",
                         command=lambda: [self.attack(country), self.updatePower(self.canva, country), defeat(country)],
                         font=("Courier", 25))
        button4.configure(width=20, activebackground="#33B5E5", relief=FLAT)
        button4_window = self.canva.create_window(140, 400, anchor=NW, window=button4)

        button5 = Button(root, text="Aggressive", command=lambda: [Strategy.aggressive(Player),
                                                                   self.updatePowerS(self.canva, country)],
                         font=("Courier", 15))
        button5.configure(width=15, activebackground="#33B5E5", relief=FLAT)
        button5_window = self.canva.create_window(50, 500, anchor=NW, window=button5)

        button6 = Button(root, text="Neutral", command=lambda: [Strategy.neutral(Player),
                                                                self.updatePowerN(self.canva, country)],
                         font=("Courier", 15))
        button6.configure(width=15, activebackground="#33B5E5", relief=FLAT)
        button6_window = self.canva.create_window(275, 500, anchor=NW, window=button6)

        button7 = Button(root, text="Defensive", command=lambda: [Strategy.defensive(Player),
                                                                  self.updatePowerDefensive(self.canva, country)],
                         font=("Courier", 15))
        button7.configure(width=15, activebackground="#33B5E5", relief=FLAT)
        button7_window = self.canva.create_window(500, 500, anchor=NW, window=button7)

        label2 = Label(text="Round Number: " + str(self.roundnum), width=40)
        label2.configure(width=15, activebackground="brown", relief=FLAT, font=("Courier", 15), bg="brown", fg="white")
        label2_window = self.canva.create_window(250, 600, anchor=NW, window=label2)


        self.canva.pack()
        root.mainloop()

    def loseScreen(self):
        def delete(name: Canvas):
            name.destroy()

        def backtomain():
            delete(self.canva)
            myshop.mainScreen()

        self.canva = Canvas(root, width="750", height="750", bg="Black")
        self.canva.create_text((375,375), text="You Lost", font=("Impact", 30), fill="white")
        button9 = Button(root, text="Back", command=backtomain)
        button9.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button9_window = self.canva.create_window(350, 550, anchor=NW, window=button9)

        self.canva.pack()
        root.mainloop()

    def winScreen(self):
        def delete(name: Canvas):
            name.destroy()

        def backtomain():
            delete(self.canva)
            myshop.mainScreen()

        self.canva = Canvas(root, width="750", height="750", bg="Black")
        self.canva.create_text((375, 375), text="You Won", font=("Impact", 30), fill="white")
        button9 = Button(root, text="Back", command=backtomain)
        button9.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button9_window = self.canva.create_window(350, 550, anchor=NW, window=button9)

        self.canva.pack()
        root.mainloop()

    def wonScreen(self):


        self.canva = Canvas(root, width="750", height="750", bg="black")
        self.canva.create_text((375, 375), text="You Won The Game!", font=("Impact", 30))
        self.canva.create_text((375, 575), text="You Conquered In "+ MainShop.day_count + "Days", font=("Impact", 30))

        self.canva.pack()
        root.mainloop()

    def startScreen(self):

        def delete(name: Canvas):
            name.destroy()

        def backtomain():
            delete(self.canva)
            myshop.mainScreen()

        self.canva = Canvas(root, width="750", height="750", bg="sky blue")
        self.canva.create_rectangle(0, 450, 750, 750, fill="green")
        self.canva.create_rectangle(325, 300, 425, 450, fill="grey")
        self.canva.create_rectangle(300, 350, 450, 450, fill="grey")
        self.canva.create_rectangle(250, 325, 300, 450, fill="grey")
        self.canva.create_rectangle(450, 325, 500, 450, fill="grey")
        self.canva.create_rectangle(440, 310, 510, 340, fill="grey")
        self.canva.create_rectangle(240, 310, 310, 340, fill="grey")
        self.canva.create_rectangle(365, 430, 385, 450, fill="saddle brown")

        self.canva.create_text((400,200), text="Clash\n            Of\n                Kingdoms", font=("Impact",60), fill="White")
        self.canva.create_polygon(350, 240, 350, 270, 393, 270,393,240,382,250,371,240,360,250, fill="yellow", outline="black")

        button9 = Button(root, text="Start Game", command=backtomain, font=("Courier", 15))
        button9.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        button9_window = self.canva.create_window(310, 500, anchor=NW, window=button9)

        self.canva.create_text((375, 650), text="Developed By\n A+ Studios", font=("Arial", 35),fill="black")

        self.canva.pack()
        root.mainloop()



myshop = MainShop('shop')
myshop.startScreen()



