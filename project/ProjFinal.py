from tkinter import *
import mysql.connector
from tkinter import messagebox
root = Tk()

heading = Label(root, text="Welcome to COVID-19 Database ", bg="blue2",fg="Lightgrey")
heading.pack(side=TOP, fill=X)
heading.config(font=("Helvetica", 19,"bold"))


photo = PhotoImage(file="doc.png")
label = Label(root, image=photo )
label.place(x=120, y=70)

toolbar = Frame(root, bg="blue2")
toolbar.place(x=0, y=450, height=55, width=800)


# *******************************************NEW ENTRY***********************************************

def open_entry():
    top = Toplevel()
    top.geometry("800x500+200+100")
    testno = StringVar()
    name = StringVar()
    age = StringVar()
    mobno = StringVar()
    address = StringVar()
    day = StringVar()
    month = StringVar()
    year = StringVar()

    l1 = Label(top, text="Testno.  :", bg="light cyan",font=("Helvetica", 9,"bold"))
    l2 = Label(top, text="Name  :", bg="light cyan",font=("Helvetica", 9,"bold"))
    l3 = Label(top, text="Age  :", bg="light cyan",font=("Helvetica", 9,"bold"))
    l4 = Label(top, text="Mobile No  :", bg="light cyan",font=("Helvetica", 9,"bold"))
    l9 = Label(top, text="(Mobile number should be 10 digit and start with either 7, 8, 9)", bg="light cyan",font=("Helvetica", 8,"bold"))
    l5 = Label(top, text="Address  :", bg="light cyan",font=("Helvetica", 9,"bold"))
    l6 = Label(top, text="Date  :", bg="light cyan",font=("Helvetica", 9,"bold"))
    l7 = Label(top, text="DD  MM  YYYY", bg="light cyan",font=("Helvetica", 9,"bold"))
    l8 = Label(top, text="(Please enter a Unique Testno)", bg="light cyan",font=("Helvetica", 8,"bold"))

    l1.place(x=170, y=100, height=25, width=60)
    l2.place(x=170, y=200, height=25, width=60)
    l3.place(x=170, y=300, height=25, width=60)
    l4.place(x=170, y=400, height=25, width=65)
    l9.place(x=130, y=430, height=20, width=400)
    l5.place(x=420, y=100, height=25, width=60)
    l6.place(x=420, y=200, height=25, width=60)
    l7.place(x=500, y=230, height=20, width=100)
    l8.place(x=230, y=136, height=20, width=170)

    e1 = Entry(top, textvariable=testno).place(x=250, y=103)
    e2 = Entry(top, textvariable=name).place(x=250, y=203)
    e3 = Entry(top, textvariable=age).place(x=250, y=303)
    e4 = Entry(top, textvariable=mobno).place(x=250, y=403)
    e5 = Entry(top, textvariable=address).place(x=500, y=103)
    e6 = Entry(top, textvariable=day).place(x=500, y=203, width=20)
    e7 = Entry(top, textvariable=month).place(x=530, y=203, width=20)
    e8 = Entry(top, textvariable=year).place(x=560, y=203, width=40)

    def submit():
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="orvell1830", database="db1") # change password here
        mycursor = mydb.cursor()
        a = testno.get()
        b = address.get()
        c = name.get()
        d = year.get()
        d = d + "-" + month.get() + "-" + day.get()
        e = age.get()
        f= mobno.get()
        x=""
        if f!="":
            len_tmp_str=len(f)
            if(len_tmp_str!=10):
                 ##"LENGTH PROBLEM"
                x="Invalid"
                messagebox.showerror('Error','Error! Invalid Mobile Number')
            elif(f[0]!="7" and f[0]!="8" and f[0]!="9"):
            ##"START PROBLEM"
                 x="Invalid"
                 messagebox.showerror('Error','Error! Invalid Mobile Number')
            else:
                check=1
                for i in f:
                    if(i>="0" and i<="9"):
                        continue
                    else:
                        check=0
                        break
                if(check==1):
                   f= mobno.get()
                else:
                    ##"NUMBER PROBLEM"
                     x="Invalid"
                     messagebox.showerror('Error','Error! Invalid Mobile Number')
       
        mycursor.execute("SELECT Testno FROM patients")
        check=mycursor.fetchall()
        nos=list(sum(check,()))
        N=a
        if N=="":
           messagebox.showerror('Error','Error! You have left some fields empty')
        else:
            N=int(N)
        
        if N in nos:
            messagebox.showerror('Error','Error! The Test No already Exist, Please enter a unique number')
        else:
            if x=="Invalid":
                pass
            else:
                if (a!="" and b!="" and c!="" and d!="" and e!="" and f!=""):
                    sql = "INSERT INTO patients (Testno ,Address ,Nameofpatient,Datefound,Age ,Mobno) VALUES (%s, %s,%s, %s,%s, %s)"
                    val = (a, b, c, d, e, f)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    mydb.close()
                    messagebox.showinfo('Success','Registration Succussful')
                    testno.set("")
                    address.set("")
                    name.set("")
                    year.set("")
                    month.set("")
                    day.set("")
                    age.set("")
                    mobno.set("")
                else:
                    messagebox.showerror('Error','Error! You have left some fields empty')
            

    sub_butt = Button(top, text="Submit", bg="blue2", command=lambda:[submit(),cases()],fg="Lightgrey",font=("Helvetica", 10,"bold"),bd=5,relief="raised")
    sub_butt.place(x=420, y=300, height=25, width=60)

    heading = Label(top, text="Please enter the patients details", bg="blue2",fg="Lightgrey")
    heading.pack(fill=X)
    heading.config(font=("Helvetica", 18,"bold"))
    

    top.resizable(width=False, height=False)
    top.configure(bg="light cyan")


# *******************************************EDIT***********************************************

def open_edit():
    top = Toplevel()
    top.geometry("800x500+200+100")
    no = StringVar()
    name = StringVar()
    age = StringVar()
    mobno = StringVar()
    address = StringVar()
    day = StringVar()
    month = StringVar()
    year = StringVar()
    def editing():
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="orvell1830", database="db1") # change password here
        mycursor = mydb.cursor()
        mycursor.execute("SELECT Testno FROM patients")
        check=mycursor.fetchall()
        nos=list(sum(check,()))
        N=no.get()
        if N=="":
           messagebox.showerror('Error','Error! You have left some fields empty')
        else:
            N=int(N)
        mydb.close()
        if N in nos:
            top1 = Toplevel()
            top.destroy()
            top1.geometry("800x500+200+100")

            l1 = Label(top1, text="Name  :", bg="light cyan",font=("Helvetica", 9,"bold"))
            l2 = Label(top1, text="Age  :",  bg="light cyan",font=("Helvetica", 9,"bold"))
            l3 = Label(top1, text="Mobile No  :",  bg="light cyan",font=("Helvetica", 9,"bold"))
            l9 = Label(top1, text="(Mobile number should be 10 digit and start with either 7, 8, 9)", bg="light cyan",font=("Helvetica", 8,"bold"))
            l5 = Label(top1, text="Address  :",  bg="light cyan",font=("Helvetica", 9,"bold"))
            l6 = Label(top1, text="Date  :", bg="light cyan",font=("Helvetica", 9,"bold"))
            l7 = Label(top1, text="DD    MM    YYYY", bg="light cyan",font=("Helvetica", 9,"bold"))

            l1.place(x=170, y=100, height=25, width=60)
            l2.place(x=170, y=200, height=25, width=60)
            l3.place(x=170, y=300, height=25, width=65)
            l5.place(x=420, y=100, height=25, width=60)
            l6.place(x=420, y=200, height=25, width=60)
            l7.place(x=490, y=230, height=20, width=120)
            l9.place(x=130, y=330, height=20, width=400)

            e1 = Entry(top1,textvariable=name).place(x=250, y=103) 
            e2 = Entry(top1,textvariable=age).place(x=250, y=203) 
            e3 = Entry(top1,textvariable=mobno).place(x=250, y=303) 
            e5 = Entry(top1,textvariable=address).place(x=500, y=103) 
            e6 = Entry(top1,textvariable=day).place(x=500, y=203, width=20) 
            e7 = Entry(top1,textvariable=month).place(x=530, y=203, width=20) 
            e8 = Entry(top1,textvariable=year).place(x=560, y=203, width=40) 
            def submit():
                mydb = mysql.connector.connect(host="localhost", user="root", passwd="orvell1830", database="db1") # change password here
                mycursor = mydb.cursor()
                b = address.get()
                c = name.get()
                d = year.get()
                d = d + "-" + month.get() + "-" + day.get()
                e = age.get()
                f = mobno.get()
                x=""
                if f=="":
                    pass
                else:
                    len_tmp_str=len(f)
                    if(len_tmp_str!=10):
                    ##"LENGTH PROBLEM"
                        x="Invalid"
                        messagebox.showerror('Error','Error! Invalid Mobile Number')
                    elif(f[0]!="7" and f[0]!="8" and f[0]!="9"):
                    ##"START PROBLEM"
                        x="Invalid"
                        messagebox.showerror('Error','Error! Invalid Mobile Number')
                    else:
                        check=1
                        for i in f:
                            if(i>="0" and i<="9"):
                                continue
                            else:
                                check=0
                                break
                        if(check==1):
                            pass
                        else:
                        ##"NUMBER PROBLEM"
                            x="Invalid"
                            messagebox.showerror('Error','Error! Invalid Mobile Number')
                if x=="Invalid":
                    pass
                else:
                    if (b!="" and c!="" and d!="" and e!="" and f!=""):
                        sql = "UPDATE patients SET Address=%s WHERE Testno=%s"
                        val = (b,N)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        sql = "UPDATE patients SET Nameofpatient=%s WHERE Testno=%s"
                        val = (c,N)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        sql = "UPDATE patients SET Datefound=%s WHERE Testno=%s"
                        val = (d,N)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        sql = "UPDATE patients SET Age=%s WHERE Testno=%s"
                        val = (e,N)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        sql = "UPDATE patients SET Mobno=%s WHERE Testno=%s"
                        val = (f,N)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        mydb.close()
                        messagebox.showinfo('Success','Updated Succussfully')
                    
                        address.set("")
                        name.set("")
                        year.set("")
                        month.set("")
                        day.set("")
                        age.set("")
                        mobno.set("")
                    else:
                        messagebox.showerror('Error','Error! You have left some fields empty')
                
            sub_butt = Button(top1, text="Submit", bg="Blue2",command=submit,fg="Lightgrey",font=("Helvetica", 10,"bold"),bd=5,relief="raised")
            sub_butt.place(x=420, y=300, height=25, width=60)

            upper = Frame(top1, bg="blue2")
            upper.pack(side=TOP, fill=X)

            l1 = Label(upper, text="Edit", bg="blue2",font=("Helvetica", 18,"bold"),fg="lightgrey")
            l1.pack()
            top1.resizable(width=False, height=False)
            top1.configure(bg="light cyan")
        else:
            messagebox.showerror('Error','Error! The number entered does not exist')


    e1 = Entry(top,textvariable=no).place(x=380, y=103)
        
    del_butt = Button(top, text="Edit", bg="blue2",command=editing,fg="Lightgrey",font=("Helvetica", 10,"bold"),bd=5,relief="raised")
    del_butt.place(x=480, y=150, height=25, width=60)



    l1 = Label(top, text="Enter the Testno.", bg="light cyan",font=("Helvetica", 8,"bold"))
    l1.place(x=265, y=100, height=25, width=100)


    heading = Label(top, text="Edit", bg="blue2",fg="Lightgrey")
    heading.pack(fill=X)
    heading.config(font=("Helvetica", 18,"bold"))

    top.resizable(width=False, height=False)

    top.configure(bg="light cyan")


# *******************************************Delete***********************************************

def open_delete():
    
    top = Toplevel()
    top.geometry("800x500+200+100")
    no = StringVar()
    
    heading = Label(top, text="Delete", bg="blue2",fg="lightgrey")
    heading.pack(fill=X)
    heading.config(font=("Helvetica", 18,"bold"))

    top.resizable(width=False, height=False)
    top.configure(bg="light cyan")


    e1 = Entry(top,textvariable=no).place(x=380, y=103)
    def delete():
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="orvell1830", database="db1") # change password here
        mycursor = mydb.cursor()
        mycursor.execute("SELECT Testno FROM patients")
        check=mycursor.fetchall()
        nos=list(sum(check,()))
        N=no.get()
        if N=="":
           messagebox.showerror('Error','Error! You have left some fields empty')
        else:
            N=int(N)
        mydb.close()
        if N in nos:
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="orvell1830", database="db1") # change password here
            mycursor = mydb.cursor()
            sql = "DELETE FROM patients WHERE Testno=%s"
            val = (N,)
            mycursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo('Success','Deleted Succussfully')
        else:
            messagebox.showerror('Error','Error! The number entered does not exist')
        
    del_butt = Button(top, text="Delete", bg="Blue2",command=lambda:[delete(),cases()],fg="Lightgrey",font=("Helvetica", 10,"bold"),bd=5,relief="raised")
    del_butt.place(x=480, y=150, height=25, width=60)



    l1 = Label(top, text="Enter the Testno.", bg="light cyan",font=("Helvetica", 8,"bold"))
    l1.place(x=265, y=100, height=25, width=100)

    l2 = Label(top, text="Note: Entry once deleted cannot be recovered back", fg="red",bg="light cyan",font=("Helvetica", 10,"bold"))
    l2.place(x=140, y=200, height=25, width=500)



    upper = Frame(top, bg="blue2")
    upper.pack(side=TOP, fill=X)


# ******************************************* View ***********************************************
def open_view():
    top = Toplevel()
    top.geometry("800x500+200+100")

    upper = Frame(top, bg="DodgerBlue2")
    upper.pack(side=TOP, fill=X)
    top.resizable(width=False, height=False)

    top.configure(bg="light cyan")
    l1 = Label(upper, text="Test No                              Name of patient                             Address                            Age                          Mobile No                 Date ", bg="blue2",fg="lightgrey",font=("Helvetica", 8,"bold"))
    l1.pack(fill=X)
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="orvell1830", database="db1") # change password here
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Datefound FROM patients")
    records=mycursor.fetchall()
    print_records= ''
    for record in records:
        print_records += str(record[0])+"\n"
    query_label4=Label(top,text=print_records,width=8,bg="light cyan")
    query_label4.place(x=683,y=25)

    mycursor.execute("SELECT Mobno FROM patients")
    records=mycursor.fetchall()
    print_records= ''
    for record in records:
        print_records += str(record[0])+"\n"
    query_label6=Label(top,text=print_records,width=8,bg="light cyan")
    query_label6.place(x=595,y=25)
    mycursor.execute("SELECT Age FROM patients")
    records=mycursor.fetchall()
    print_records= ''
    for record in records:
        print_records += str(record[0])+"\n"
    query_label5=Label(top,text=print_records,width=4,bg="light cyan")
    query_label5.place(x=500,y=25)
    
    mycursor.execute("SELECT Address FROM patients")
    records=mycursor.fetchall()
    print_records= ''
    for record in records:
        print_records += str(record[0])+"\n"
    query_label2=Label(top,text=print_records,width=16,bg="light cyan")
    query_label2.place(x=340,y=25)
    
    mycursor.execute("SELECT Nameofpatient FROM patients")
    records=mycursor.fetchall()
    print_records= ''
    for record in records:
        print_records += str(record[0])+"\n"
    query_label3=Label(top,text=print_records,width=13,bg="light cyan")
    query_label3.place(x=200,y=25)

    mycursor.execute("SELECT Testno FROM patients")
    records=mycursor.fetchall()
    print_records= ''
    for record in records:
        print_records += str(record[0])+"\n"
    query_label1=Label(top,text=print_records,width=4,bg="light cyan")
    query_label1.place(x=80,y=25)
    
    
# ****************************************** Help ***********************************************
def open_help():
    top = Toplevel()
    top.geometry("800x500+200+100")

    heading = Label(top, text="Help", bg="blue2",fg="lightgrey")
    heading.pack(fill=X)
    heading.config(font=("Helvetica", 18,"bold"))
    

    l1 = Label(top, text="1.Please check the Testno before submiting it. ", bg="light cyan",anchor=W)
    l2 = Label(top, text="2.Please check the installation of My Sql for Database related issues. ", bg="light cyan",anchor=W)
    l3 = Label(top, text="3.Before running this program open MYSQL and run the following Queries", bg="light cyan",anchor=W)
    l5 = Label(top, text=" create database db1", bg="light cyan",anchor=W)
    l6 = Label(top, text=" use db1", bg="light cyan",anchor=W)
    l7 = Label(top, text=" create table patients(Testno int unique,Address text NOT NULL,Nameofpatient text NOT NULL,Datefound Date NOT NULL", bg="light cyan",anchor=W)
    l10 = Label(top, text=" ,Age int NOT NULL,Mobno numeric(10))", bg="light cyan",anchor=W)
    l8 = Label(top, text="4.Please change the password in the code to your root password.", bg="light cyan",anchor=W)
    l11 = Label(top, text="5.Run the following command in CMD(Windows) (pip install mysql-connector-python).", bg="light cyan",anchor=W)
    l9 = Label(top, text="6.For any further assistance please contact us at abc@fake.com", bg="light cyan",anchor=W)


    
    l4 = Label(top, text="Developed by Clint Ferreira(8670) and Orvell Ferreira(8671)",bg="light cyan")


    l1.place(x=56, y=60, height=25, width=720)
    l2.place(x=56, y=90, height=25, width=720)
    l3.place(x=56, y=120, height=25, width=720)
    l5.place(x=56, y=150, height=25, width=720)
    l6.place(x=56, y=180, height=25, width=720)
    l7.place(x=56, y=210, height=25, width=720)
    l10.place(x=56, y=240, height=25, width=720)
    l8.place(x=56, y=270, height=25, width=720)
    l11.place(x=56, y=300, height=25, width=720)
    l9.place(x=56, y=330, height=25, width=720)

             
    l4.place(x=420, y=470, height=25, width=400)

    l1.config(font=("Helvetica", 9,"bold"))
    l2.config(font=("Helvetica", 9,"bold"))
    l3.config(font=("Helvetica", 9,"bold"))
    l5.config(font=("Helvetica", 9,"bold"))
    l6.config(font=("Helvetica", 9,"bold"))
    l7.config(font=("Helvetica", 9,"bold"))
    l8.config(font=("Helvetica", 9,"bold"))
    l9.config(font=("Helvetica", 9,"bold"))
    l10.config(font=("Helvetica",9,"bold"))
    l11.config(font=("Helvetica",9,"bold"))
    l4.config(font=("Helvetica",9,"bold"))

    top.resizable(width=False, height=False)
    top.configure(bg="light cyan")


# **********************************************Home page widgets*******************************************************

butt1 = Button(root, text="New Entry", command=open_entry, bg="DodgerBlue2",bd=5,relief="raised",highlightcolor="lightgrey",font=("Helvetica", 8,"bold"))
butt1.place(x=107, y=461, height=30, width=65)

butt2 = Button(root, text="Edit", command=open_edit, bg="DodgerBlue2",bd=5,relief="raised",highlightcolor="lightgrey",font=("Helvetica", 9,"bold"))
butt2.place(x=239, y=461, height=30, width=65)

butt3 = Button(root, text="Delete", command=open_delete, bg="DodgerBlue2",bd=5,relief="raised",highlightcolor="lightgrey",font=("Helvetica", 9,"bold"))
butt3.place(x=372, y=461, height=30, width=65)

butt4 = Button(root, text="View", command=open_view, bg="DodgerBlue2",bd=5,relief="raised",highlightcolor="lightgrey",font=("Helvetica", 9,"bold"))
butt4.place(x=505, y=461, height=30, width=65)

butt5 = Button(root, text="Help", command=open_help, bg="DodgerBlue2",bd=5,relief="raised",highlightcolor="lightgrey",font=("Helvetica", 9,"bold"))
butt5.place(x=638, y=461, height=30, width=65)

cas = Label(root, text="Total People Infected:",bg="light cyan",anchor=E)
cas.place(x=270, y=40, height=25, width=200)
cas.config(font=("Helvetica", 12,"bold"))




def cases():
    x=''
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="orvell1830", database="db1") # change password here
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Testno FROM patients")
    check=mycursor.fetchall()
    nos=list(sum(check,()))
    x=len(nos)
    lab=Label(root,text=x,bg="light cyan",fg="red")
    lab.place(x=480,y=40, height=25)
    lab.config(font=("Helvetica", 16,"bold"))


cases()

root.configure(bg="light cyan")
root.geometry("800x500+200+100")
root.resizable(width=False, height=False)
root.mainloop()
