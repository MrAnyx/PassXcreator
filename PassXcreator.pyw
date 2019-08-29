
from tkinter import *
import random
from tkinter import messagebox

def espace(arg):
    liste = arg.split(' ')
    return ''.join(liste)

def creation_password():
#25 max pour le password
    global password

    lettre = "a,A,z,Z,e,E,r,R,t,T,y,Y,u,U,i,I,o,O,p,P,q,Q,s,S,d,D,f,F,g,G,h,H,j,J,k,K,l,L,m,M,w,W,x,X,c,C,v,V,b,B,n,N,1,2,3,4,5,6,7,8,9,?,!,#,&,%,$"
    liste_lettre = lettre.split(',')

    if(len(value.get()) <= 0):
        valuePassword.set("Erreur")
        messagebox.showerror("Error | Size", "The size isn't correct")


    elif(int(value.get())>25):
        valuePassword.set("Erreur")
        messagebox.showerror("Error | Size", "Less than 25 !")

    elif(int(value.get())<0):
        valuePassword.set("Erreur")
        messagebox.showerror("Error | Size", "More than 0 !")


    else:
        try:
            password = ' '.join(random.sample(liste_lettre, int(value.get())))
            valuePassword.set(password)
            if(value_check.get() == 1):
                pw_ctrl.set(espace(password))

        except:#erreur si pas entier
            valuePassword.set("Erreur")
            messagebox.showerror("Error | Size", "The size isn't correct")




def touche_creation_password(event):
    creation_password()

def affiche_pw():
	global frameCopier, pw_ctrl

	frameCopier = Frame(fenetre, bg = "#969696")

	pw_ctrl = StringVar()
	pw_ctrl.set(espace(password))
	copie_pw = Entry(frameCopier, textvariable = pw_ctrl, bg = "bisque", font = ("Montserrat", 12), selectbackground = "bisque", selectforeground = "red", state = "readonly", readonlybackground = "bisque").pack(fill = X)

	frameCopier.pack(fill = X, padx = 10, pady = (0,10))


def delete_pw():
	frameCopier.destroy()


def copier():
	if(value_check.get() == 1):
		affiche_pw()
	else:
		delete_pw()

fenetre = Tk()
fenetre.title("PassXcreator")
fenetre.iconbitmap("icon.ico")
fenetre.config(bg = "#969696")
fenetre.resizable(width = False, height = False)
password=""


#frame pour le ombre de caractère
frame1 = Frame(fenetre, bg = "#969696")
labelNbCaract = Label(frame1,text = "Size : ", bg = "#969696", font = ("Montserrat", 12, "bold")).pack(side = LEFT, fill = X)
value = StringVar()
entry = Entry(frame1, textvariable = value, font = ("Montserrat", 12, "bold"), selectbackground = "bisque", selectforeground = "red", bg = "bisque").pack(side = LEFT, fill = X)
frame1.pack(fill = X, padx = 10, pady = (10, 5))

#frame pour le bouton et le label pour afficher le mdp
frame2 = Frame(fenetre, bg = "#969696")
boutonCreate = Button(frame2, bg = "#515151", foreground = "#ffffff", borderwidth = 4, text = "Create", font = ("Montserrat", 12, "bold"), command = creation_password).pack(fill = X, side = TOP, pady = (0,5))
valuePassword = StringVar()
valuePassword.set("Password")
LabelPassword = Label(frame2, textvariable = valuePassword, bg = "#eeeeee", borderwidth = 1, relief = "solid", height = 2, font = ("Calisto MT", 9)).pack(side = TOP, fill = X, pady = (5,0))
frame2.pack(fill = X, padx = 10, pady = (5,5))

#frame pour le bouton exit et le ctrl-c
frame3 = Frame(fenetre, bg = "#969696")
boutonExit = Button(frame3, text = "Exit", bg = "#515151", borderwidth = 4, fg = "white", font = ("Montserrat", 12, "bold"), command = fenetre.destroy).pack(side = LEFT, fill = X, expand = 1)
value_check = IntVar()
check = Checkbutton(frame3, text = "CTRL-C", command = copier ,variable = value_check,  onvalue = 1, offvalue = 0, bg = "#969696", activebackground = "#969696", font = ("Montserrat", 9)).pack(side = LEFT, fill = X, expand = 1)
frame3.pack(fill = X, padx = 10, pady = (5,10))

fenetre.bind("<Return>", touche_creation_password)

fenetre.mainloop()
