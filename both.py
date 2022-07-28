import pickle
import pickle
import tkinter as tk
def signin():
    root=tk.Tk()
    root.geometry("600x400")
    name_var=tk.StringVar()
    passw_var=tk.StringVar()
    def sign():
        with open("log.dat","rb") as s:
            y=pickle.load(s)
            s=open("log.dat","wb")
            user=input("enter username:")
            passw=input("enter password:")
            info=[user,passw]
            y.append(info)
            pickle.dump(y,s)
            s.close()
            print("acc succesfully created")
    def submit():
        with open("log.dat","rb") as l:
            y=pickle.load(l)
            user=name_var.get()
            password=passw_var.get()
            for info in y:
                if info[0]==user and info[1]==password:
                    print("login successful")
                    root.destroy()
                    from main import base
                    base()
    name_var.set("")
    passw_var.set("")
    name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
    name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
    passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
    passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
    sub_btn=tk.Button(root,text = 'Submit', command = submit)
    name_label.grid(row=0,column=0)
    name_entry.grid(row=0,column=1)
    passw_label.grid(row=1,column=0)
    passw_entry.grid(row=1,column=1)
    sub_btn.grid(row=2,column=1)
        
                

