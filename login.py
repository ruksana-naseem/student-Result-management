from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
from dashboard import RMS
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)
        #========BG Images==========
        self.bg=ImageTk.PhotoImage(file="images/login.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        #=========login frame=======
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=350,y=150,height=340,width=500)

        tilte=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
        desc=Label(Frame_login,text="Admin Login Area",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)


        lbl_user=Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)

        lbl_password=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
        self.txt_password=Entry(Frame_login,font=("times new roman",15),bg="lightgray")

        self.txt_password.place(x=90,y=240,width=350,height=35)

       # forget=Button(Frame_login,text="Forgot password?",bg="white",fg="#d77337",bd=0 ,font=("times new roman",12)).place(x=90,y=280)
        Login_btn=Button(self.root,command=self.login_function,text="Login",fg="white",bg="#d77337" ,font=("times new roman",20)).place(x=480,y=470,width=180,height=40)

    def login_function(self):  
        if self.txt_password.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif  self.txt_password.get()!="12345" or self.txt_user.get()!="Admin":
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
        else:
            messagebox.showinfo("welcome",f"Welcome{self.txt_user.get()}\nYour Password: {self.txt_password.get()}",parent=self.root)
            self.dashboard()
            
    def dashboard(self):
        self.new_window=Toplevel(self.root)
        self.app=RMS(self.new_window)

if __name__== "__main__" :
  root=Tk()
  obj= Login(root)
  root.mainloop()   