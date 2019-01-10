from tkinter import *
import sqlite3
import time
import datetime

class window():
    def __init__(self):
        self.window = Tk()
        self.window.title("Giriş Yapın")
        self.window.geometry("300x300+150+150")
        self.window.resizable(False,False)

        self.connector = sqlite3.connect("users.db")
        self.cursor = self.connector.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (register_time,username,password)")

    def login(self):
        username = self.user_ent.get()
        password = self.pass_ent.get()
        self.user_ent.delete(0,'end')
        self.pass_ent.delete(0,'end')

        if username and password:
        
            self.cursor.execute("SELECT * FROM users")
            data = self.cursor.fetchall()
            check = False
            for i in data:
                if username == i[1] and password == i[2]:
                    check = True
                    break
            if check:
                try:
                    self.window.destroy()
                    self.window2.destroy()
                except:
                    quit()
            else:
                self.info_login["text"] = "Yanlış kullanıcı adı ve şifre."
        else:
            self.info_login["text"] = "Kullanıcı adı ve şifre boş bırakılamaz!"
    
    def createWindow(self):
        win = self.get_win
        self.user_label = Label(win,text="Kullanıcı Adı: ").place(x=43,y=45)

        self.user_ent = Entry(win)
        self.user_ent.pack()
        self.user_ent.place(x=43,y=78)
        
        self.pass_label = Label(win,text="Şifre: ").place(x=43,y=137)

        self.pass_ent = Entry(win,show="*")
        self.pass_ent.pack()
        self.pass_ent.place(x=43,y=175)

        self.info_login = Label(win,text="")
        self.info_login.pack()
        self.info_login.place(x=32,y=219)

        self.giris_but = Button(win,text="Giriş Yap",command=self.login).place(x=180,y=175)
        self.register_but = Button(win,text="Kayıt Ol",command=self.registerWindow).place(x=180,y=150)

    def register(self):
        username = self.user_ent_kayit.get()
        password = self.pass_ent_kayit.get()
        self.user_ent_kayit.delete(0,'end')
        self.pass_ent_kayit.delete(0,'end')
        if username and password:

            self.cursor.execute("SELECT * FROM users")
            data = self.cursor.fetchall()
            check = False
            for i in data:
                if username == i[1]:
                    check = True
                    
            if check == False:
                zaman = time.time()
                zaman = str(datetime.datetime.fromtimestamp(zaman).strftime("%d/%m/%Y %H:%M:%S"))
                self.cursor.execute("INSERT INTO users (register_time,username,password) VALUES (?,?,?)",(zaman,username,password))
                self.connector.commit()
                self.window2.destroy()
            else:
                self.info_kayit["text"] = "Veritabanında böyle bir kullanıcı adı var."
        else:
            self.info_kayit["text"] = "Kullanıcı adı ve şifre boş bırakılamaz!"
        
    def registerWindow(self):
        self.window2 = Tk()
        self.window2.title("Kayıt")
        self.window2.geometry("300x300+75+75")
        self.window2.resizable(False,False)

        self.user_label2 = Label(self.window2,text="Kullanıcı Adı: ").place(x=43,y=45)

        self.user_ent_kayit = Entry(self.window2)
        self.user_ent_kayit.pack()
        self.user_ent_kayit.place(x=43,y=78)
        
        self.pass_label_kayit = Label(self.window2,text="Şifre: ").place(x=43,y=137)

        self.pass_ent_kayit = Entry(self.window2,show="*")
        self.pass_ent_kayit.pack()
        self.pass_ent_kayit.place(x=43,y=175)

        self.info_kayit = Label(self.window2,text="")
        self.info_kayit.pack()
        self.info_kayit.place(x=32,y=219)

        self.kayit_but = Button(self.window2,text="Kayıt Ol",command=self.register).place(x=180,y=175)

    @property
    def get_win(self):
        return self.window

frame = window()
frame.createWindow()

mainloop()
