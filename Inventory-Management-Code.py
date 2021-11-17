import cv2
import psycopg2
from tkinter import *
import tkinter.messagebox as box
from tkinter.messagebox import *
import time as tm
from datetime import datetime
import datetime
from tkinter import ttk
import pytz
import tkinter as tk
import itertools
import sqlite3
import tkinter as Tkinter
import qrcode
import smtplib


def main_login():
  login_time=datetime.datetime.now()
    
  def entrytab2():
    
    user_store_id=id_.get()
    user_store_password=passwd.get()
    user_store_id=int(user_store_id)
    try:
  
    
        top2=Tk()
        top2.geometry('1200x700+0+0')
        #top2.iconbitmap(r'icon.ico')
        top2.title("Inventory Check")
        frame7=Frame(top2,width=1200,height=100,relief=SUNKEN)
        frame7.pack(side=TOP)
        frame6=Frame(top2,width=600,height=600,relief=SUNKEN)
        frame6.pack(side=RIGHT)
        

        
        def adduser():
            def add__in(): 
                conn=psycopg2.connect('')               #PostgreSql Database link
                cur=conn.cursor()
                insert="INSERT INTO user_details (user_name,passwd,user_type,user_email) VALUES('%s','%s','n','%s')"%(lbl55i.get(),lbl66i.get(),emaili.get())
                cur.execute(insert)
                cur.execute("select * from user_details")
                data=cur.fetchall()
                conn.commit()
                
                for a in data:
                    if a[1]==lbl55i.get():
                       a0=str(a[0])
                       name=lbl55i.get()
                       email_of_user=emaili.get()
                       msg= name+" , u r added to the inventory management(CLUB) with userid = "+a0+" and password= "+lbl66i.get()+" ."
                       obj=smtplib.SMTP('smtp.gmail.com',587)
                       obj.ehlo()
                       obj.starttls()
                       obj.login("","")                   #login credentials    
                       receiver=["",email_of_user]            #reciever mail   
                       obj.sendmail("",receiver,msg)       #sender mail
                       top5.destroy()
                       mess1=Tk()
                       mess1.geometry("250x200+500+200")
                       mess1.title("USER ADDED")
                       lmess1=Label(mess1,text="USER ADDED",font=("consol 20 bold"),width=14,fg='white',bg='red')
                       lmess1.place(x=4,y=80)
                       mess1.configure(bg='#ffc2b3')
                       mess1.mainloop()


            
            top5=Tk()
            top5.geometry('500x300')
            top5.title('ADD USER')
            frame9=Frame(top5,width=600,height=600,relief=SUNKEN)
            frame9.pack()
            lbl55=Label(frame9,font=('arial',16,'italic','bold'),text='USER_NAME',bd=16,anchor='w').grid(row=2,column=2)  
            lbl55i=Entry(frame9,font=('Times New Roman',16),bd=5,insertwidth=4,bg='steel blue',justify='right')
            lbl55i.grid(row=2,column=3)
            lbl66=Label(frame9,font=('arial',16,'italic','bold'),text='PASSWORD',bd=16,anchor='w')
            lbl66.grid(row=3,column=2)
            lbl66i=Entry(frame9,font=('Times New Roman',16),show='*',bd=5,insertwidth=4,bg='steel blue',justify='right')
            lbl66i.grid(row=3,column=3)

            email=Label(frame9,font=('arial',16,'italic','bold'),text='EMAIL',bd=16,anchor='w')
            email.grid(row=4,column=2)
            emaili=Entry(frame9,font=('Times New Roman',16),bd=5,insertwidth=4,bg='steel blue',justify='right')
            emaili.grid(row=4,column=3)


            
            btn1=Button(frame9,padx=30,pady=10,text='ADD USER',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=add__in).grid(row=5,columnspan=5)


        def removeuser():
            userid=StringVar()
            userpasswd=StringVar()
            username=StringVar()
            def remove__in():
                userid=int(lblid_i.get())
                conn=psycopg2.connect('')
                cur=conn.cursor()
                rem="DELETE FROM user_details WHERE uid=%d"%(lblid_i.get())
                cur.execute(rem)
                conn.commit()

                top6.destroy()
                mess1=Tk()
                mess1.geometry("250x200+500+200")
                mess1.title("USER")
                lmess1=Label(mess1,text="USER REMOVED",font=("consol 20 bold"),width=14,fg='white',bg='red')
                lmess1.place(x=4,y=80)
                mess1.configure(bg='#ffc2b3')
                mess1.mainloop()              


            
            top6=Tk()
            top6.geometry('500x300')
            top6.title('REMOVE USER')
            frame10=Frame(top6,width=600,height=600,relief=SUNKEN)
            frame10.pack()
            lbluser=Label(frame10,font=('arial',16,'italic','bold'),text='USER_NAME',bd=16,anchor='w').grid(row=2,column=2)  
            lbluser_i=Entry(frame10,font=('Times New Roman',16),bd=5,insertwidth=4,textvariable=username,bg='steel blue',justify='right')
            lbluser_i.grid(row=2,column=3)
            lblid=Label(frame10,font=('arial',16,'italic','bold'),text='USER_ID',bd=16,anchor='w').grid(row=3,column=2)
            lblid_i=Entry(frame10,font=('Times New Roman',16),bd=5,insertwidth=4,textvariabe = userid,bg='steel blue',justify='right').grid(row=3,column=3)
            btn1=Button(frame10,padx=30,pady=10,text='REMOVE USER',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=remove__in).grid(row=4,columnspan=5)


        def showproduct():
            try:
                conn=psycopg2.connect('')#PostgreSql Database link     
                cur=conn.cursor()
                cur.execute("SELECT * FROM product_details ORDER BY pid")
                data=cur.fetchall()
                list99=[]
                for row in data:
                    list99.append(row[0])
                    list99.append(row[1])
                    list99.append(row[2])
                    list99.append(row[3])
                def tabular0():
                    lbl1=Label(frame,text='PID',width=12,fg='red').grid(row=0,column=0)
                    lbl2=Label(frame,text='PRODUCT_NAME',width=12,fg='red').grid(row=0,column=1)
                    lbl3=Label(frame,text='CONDITION',width=12,fg='red').grid(row=0,column=2)
                    lbl4=Label(frame,text='AVAILABILITY',width=12,fg='red').grid(row=0,column=3)
                    r=cur.fetchall()
                    for k in range(0,1000000,4):
                        lbl11=Label(frame,text=list99[k],width=12)
                        lbl12=Label(frame,text=list99[k+1],width=12)
                        lbl13=Label(frame,text=list99[k+2],width=12)
                        lbl14=Label(frame,text=list99[k+3],width=12)
                        lbl11.grid(row=k+1,column=0)
                        lbl12.grid(row=k+1,column=1)
                        lbl13.grid(row=k+1,column=2)
                        lbl14.grid(row=k+1,column=3)
                            
                def myfunction0(event):
                    canvas.configure(scrollregion=canvas.bbox("all"),width=400,height=200)
                            

                root1=Tk()
                sizex = 500
                sizey = 300
                posx  = 100
                posy  = 150
                root1.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
                root1.title('Check It')
                myframe1=Frame(root1,relief=GROOVE,width=30,height=70,bd=1)
                myframe1.place(x=10,y=10)

                canvas=Canvas(myframe1)
                frame=Frame(canvas)
                myscrollbar=Scrollbar(myframe1,orient="vertical",command=canvas.yview)
                canvas.configure(yscrollcommand=myscrollbar.set)

                myscrollbar.pack(side="right",fill="y")
                canvas.pack(side="left")
                canvas.create_window((10,10),window=frame,anchor='nw')
                frame.bind("<Configure>",myfunction0)
                tabular0()
                root1.mainloop()
            except Exception as e:
                print(e)

        def showuser():
            try:
                conn=psycopg2.connect('')
                cur=conn.cursor()
                cur.execute("SELECT * FROM user_details")
                data=cur.fetchall()
                list99=[]
                for row in data:
                    list99.append(row[0])
                    list99.append(row[1])
                    list99.append(row[2])
                    list99.append(row[3])
                def tabular2():
                    lbl1=Label(frame,text='UID',width=12,fg='red').grid(row=0,column=0)
                    lbl2=Label(frame,text='USER NAME',width=12,fg='red').grid(row=0,column=1)
                    lbl3=Label(frame,text='PASSWORD',width=12,fg='red').grid(row=0,column=2)
                    lbl4=Label(frame,text='USER TYPE',width=12,fg='red').grid(row=0,column=3)
                    r=cur.fetchall()
                    for k in range(0,1000000,4):
                        lbl11=Label(frame,text=list99[k],width=12)
                        lbl12=Label(frame,text=list99[k+1],width=12)
                        lbl13=Label(frame,text=list99[k+2],width=12)
                        lbl14=Label(frame,text=list99[k+3],width=12)
                        lbl11.grid(row=k+1,column=0)
                        lbl12.grid(row=k+1,column=1)
                        lbl13.grid(row=k+1,column=2)
                        lbl14.grid(row=k+1,column=3)
                            
                def myfunction2(event):
                    canvas.configure(scrollregion=canvas.bbox("all"),width=400,height=200)
                            

                root2=Tk()
                sizex = 500
                sizey = 300
                posx  = 100
                posy  = 150
                root2.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
                root2.title('Check It')
                myframe2=Frame(root2,relief=GROOVE,width=30,height=70,bd=1)
                myframe2.place(x=10,y=10)

                canvas=Canvas(myframe2)
                frame=Frame(canvas)
                myscrollbar=Scrollbar(myframe2,orient="vertical",command=canvas.yview)
                canvas.configure(yscrollcommand=myscrollbar.set)

                myscrollbar.pack(side="right",fill="y")
                canvas.pack(side="left")
                canvas.create_window((10,10),window=frame,anchor='nw')
                frame.bind("<Configure>",myfunction2)
                tabular2()
                root2.mainloop()
            except Exception as e:
                print(e)

        def borrowdetail():
            try:
                conn=psycopg2.connect('')
                cur=conn.cursor()
                cur.execute("SELECT * FROM borrow")
                data=cur.fetchall()
                list99=[]
                for row in data:
                    list99.append(row[0])
                    list99.append(row[1])
                    list99.append(row[2])
                    list99.append(row[3])
                    list99.append(row[4])
                    list99.append(row[5])
                def tabular3():
                    lbl1=Label(frame,text='UID',width=12,fg='red').grid(row=0,column=0)
                    lbl2=Label(frame,text='USER NAME',width=12,fg='red').grid(row=0,column=1)
                    lbl3=Label(frame,text='PID',width=12,fg='red').grid(row=0,column=2)
                    lbl4=Label(frame,text='DATE',width=12,fg='red').grid(row=0,column=3)
                    lbl5=Label(frame,text='TIME',width=12,fg='red').grid(row=0,column=4)
                    lbl6=Label(frame,text='PURPOSE',width=12,fg='red').grid(row=0,column=5)
                    r=cur.fetchall()
                    for k in range(0,1000000,6):
                        lbl11=Label(frame,text=list99[k],width=12)
                        lbl12=Label(frame,text=list99[k+1],width=12)
                        lbl13=Label(frame,text=list99[k+2],width=12)
                        lbl14=Label(frame,text=list99[k+3],width=12)
                        lbl15=Label(frame,text=list99[k+4],width=12)
                        lbl16=Label(frame,text=list99[k+5],width=12)
                        lbl11.grid(row=k+1,column=0)
                        lbl12.grid(row=k+1,column=1)
                        lbl13.grid(row=k+1,column=2)
                        lbl14.grid(row=k+1,column=3)
                        lbl15.grid(row=k+1,column=4)
                        lbl16.grid(row=k+1,column=5)
                            
                def myfunction3(event):
                    canvas.configure(scrollregion=canvas.bbox("all"),width=550,height=200)
                            

                root3=Tk()
                sizex = 700
                sizey = 300
                posx  = 100
                posy  = 150
                root3.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
                root3.title('Check It')
                myframe3=Frame(root3,relief=GROOVE,width=700,height=400,bd=1)
                myframe3.place(x=10,y=10)

                canvas=Canvas(myframe3)
                frame=Frame(canvas)
                myscrollbar=Scrollbar(myframe3,orient="vertical",command=canvas.yview)
                canvas.configure(yscrollcommand=myscrollbar.set)

                myscrollbar.pack(side="right",fill="y")
                canvas.pack(side="left")
                canvas.create_window((10,10),window=frame,anchor='nw')
                frame.bind("<Configure>",myfunction3)
                tabular3()
                root3.mainloop()
            except Exception as e:
                print(e)

        def returndetail():
            try:
                conn=psycopg2.connect('')#PostgreSql Database link     
                cur=conn.cursor()
                cur.execute("SELECT * FROM return_")
                data=cur.fetchall()
                list99=[]
                for row in data:
                    list99.append(row[0])
                    list99.append(row[1])
                    list99.append(row[2])
                    list99.append(row[3])
                    list99.append(row[4])
                    list99.append(row[5])
                    
                def tabular4():
                    lbl1=Label(frame,text='UID',width=12,fg='red').grid(row=0,column=0)
                    lbl2=Label(frame,text='USER NAME',width=12,fg='red').grid(row=0,column=1)
                    lbl3=Label(frame,text='PID',width=12,fg='red').grid(row=0,column=2)
                    lbl4=Label(frame,text='CONDITION',width=12,fg='red').grid(row=0,column=3)
                    lbl5=Label(frame,text='DATE',width=12,fg='red').grid(row=0,column=4)
                    lbl6=Label(frame,text='TIME',width=12,fg='red').grid(row=0,column=5)
                    r=cur.fetchall()
                    for k in range(0,1000000,6):
                        lbl11=Label(frame,text=list99[k],width=12)
                        lbl12=Label(frame,text=list99[k+1],width=12)
                        lbl13=Label(frame,text=list99[k+2],width=12)
                        lbl14=Label(frame,text=list99[k+3],width=12)
                        lbl15=Label(frame,text=list99[k+4],width=12)
                        lbl16=Label(frame,text=list99[k+5],width=12)
                        lbl11.grid(row=k+1,column=0)
                        lbl12.grid(row=k+1,column=1)
                        lbl13.grid(row=k+1,column=2)
                        lbl14.grid(row=k+1,column=3)
                        lbl15.grid(row=k+1,column=4)
                        lbl16.grid(row=k+1,column=5)
                            
                def myfunction4(event):
                    canvas.configure(scrollregion=canvas.bbox("all"),width=550,height=200)
                            

                root4=Tk()
                sizex = 700
                sizey = 300
                posx  = 100
                posy  = 150
                root4.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
                root4.title('Check It')
                myframe4=Frame(root4,relief=GROOVE,width=700,height=400,bd=1)
                myframe4.place(x=10,y=10)

                canvas=Canvas(myframe4)
                frame=Frame(canvas)
                myscrollbar=Scrollbar(myframe4,orient="vertical",command=canvas.yview)
                canvas.configure(yscrollcommand=myscrollbar.set)

                myscrollbar.pack(side="right",fill="y")
                canvas.pack(side="left")
                canvas.create_window((10,10),window=frame,anchor='nw')
                frame.bind("<Configure>",myfunction4)
                tabular4()
                root4.mainloop()
            except Exception as e:
                print(e)

            
        def count():
            try:
                conn=psycopg2.connect('')   #PostgreSql Database link     
                cur=conn.cursor()
                cur.execute("select r.pid, p.product_name, count(r.pid) from product_details p, return_ r where r.pid=p.pid group by r.pid ,p.product_name")
                data=cur.fetchall()
                list99=[]
                for row in data:
                    list99.append(row[0])
                    list99.append(row[1])
                    list99.append(row[2])
                def tabular5():
                    lbl1=Label(frame,text='PID',width=12,fg='red').grid(row=0,column=0)
                    lbl2=Label(frame,text='PRODUCT NAME',width=12,fg='red').grid(row=0,column=1)
                    lbl3=Label(frame,text='COUNT',width=12,fg='red').grid(row=0,column=2)
                    r=cur.fetchall()
                    for k in range(0,1000000,3):
                        lbl11=Label(frame,text=list99[k],width=12)
                        lbl12=Label(frame,text=list99[k+1],width=12)
                        lbl13=Label(frame,text=list99[k+2],width=12)
                        lbl11.grid(row=k+1,column=0)
                        lbl12.grid(row=k+1,column=1)
                        lbl13.grid(row=k+1,column=2)
                                
                def myfunction5(event):
                    canvas.configure(scrollregion=canvas.bbox("all"),width=400,height=200)
                                

                root5=Tk()
                sizex = 500
                sizey = 300
                posx  = 100
                posy  = 150
                root5.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
                root5.title('Check It')
                myframe5=Frame(root5,relief=GROOVE,width=30,height=70,bd=1)
                myframe5.place(x=10,y=10)

                canvas=Canvas(myframe5)
                frame=Frame(canvas)
                myscrollbar=Scrollbar(myframe5,orient="vertical",command=canvas.yview)
                canvas.configure(yscrollcommand=myscrollbar.set)

                myscrollbar.pack(side="right",fill="y")
                canvas.pack(side="left")
                canvas.create_window((10,10),window=frame,anchor='nw')
                frame.bind("<Configure>",myfunction5)
                tabular5()
                root5.mainloop()
            except Exception as e:
                print(e)

                
        def workshop():
            try:
                def work1():
                    conn=psycopg2.connect('')     #PostgreSql Database link    
                    cur=conn.cursor()
                    cur.execute("insert into workshop values('%s',%d)"%(drop.get(),int(lblwork11.get())))
                    conn.commit()
                def work2():
                    curs1="select p.product_name, count(*) , p.condition_ from workshop w, product_details p where p.product_name=w.product_name group by p.product_name ,p.condition_ having p.condition_ != 'bad' order by p.product_name;"
                    cur.execute(curs1)
                    data1=cur.fetchall()
                    list1=[]
                    n=lblwork22.get()
                    curs2="update workshop set require2=require1 * %d"%(int(n))
                    cur.execute(curs2)
                    curs3="SELECT * FROM workshop ORDER BY product_name"
                    cur.execute(curs3)
                    data2=cur.fetchall()
                    list2=[]
                    list4=[]
                    conn.commit()
                    for row in data1:
                        list1.append(row[1])
                    for row1 in data2:
                        list2.append(row1[2])
                        list4.append(row1[0])
        
                    def calc():
                        list3=[]
                        for i in range(0,len(list1)):
                            list3.append(list2[i]-list1[i])
                        print(list3)
                        lbl1=Label(frame,text='PRODUCT NAME',width=25,fg='red').grid(row=0,column=0)
                        lbl2=Label(frame,text='IN INVENTORY',width=25,fg='red').grid(row=0,column=1)
                        lbl3=Label(frame,text='REQUIRED FOR WORKSHOP',width=25,fg='red').grid(row=0,column=2)
                        lbl4=Label(frame,text='NEED TO PURCHASE',width=25,fg='red').grid(row=0,column=3)
                        for k in range(0, 100000000):
                            lbl11=Label(frame,text=list4[k],width=12)
                            lbl12=Label(frame,text=list1[k],width=12)
                            lbl13=Label(frame,text=list2[k],width=12)
                            lbl14=Label(frame,text=list3[k],width=12)
                            lbl11.grid(row=k+1,column=0)
                            lbl12.grid(row=k+1,column=1)
                            lbl13.grid(row=k+1,column=2)
                            lbl14.grid(row=k+1,column=3)
                    def myfunction6(event):
                        canvas.configure(scrollregion=canvas.bbox("all"),width=800,height=200)
                        

                    root7=Tk()
                    sizex = 800
                    sizey = 300
                    posx  = 100
                    posy  = 150
                    root7.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
                    root7.title('WORKSHOP INVENTORY')
                    myframe6=Frame(root7,relief=GROOVE,width=30,height=70,bd=1)
                    myframe6.place(x=10,y=10)

                    canvas=Canvas(myframe6)
                    frame=Frame(canvas)
                    myscrollbar=Scrollbar(myframe6,orient="vertical",command=canvas.yview)
                    canvas.configure(yscrollcommand=myscrollbar.set)

                    myscrollbar.pack(side="right",fill="y")
                    canvas.pack(side="left")
                    canvas.create_window((10,10),window=frame,anchor='nw')
                    frame.bind("<Configure>",myfunction6)
                    calc()
                    root7.mainloop()

                
                def updatein():

                    def update1():
                        conn=psycopg2.connect('')           #PostgreSql Database link    
                        cur=conn.cursor()
                        cur.execute("UPDATE workshop SET require1=%d WHERE product_name='%s'"% (int(lblup2.get()),lblup11.get()))
                        conn.commit()
                        
                        top8.destroy()
                        mess1=Tk()
                        mess1.geometry("250x200+500+200")
                        mess1.title("UPDATE")
                        lmess1=Label(mess1,text="UPDATE COMPLETE",font=("consol 20 bold"),width=14,fg='white',bg='red')
                        lmess1.place(x=4,y=80)
                        mess1.configure(bg='#ffc2b3')
                        mess1.mainloop()              


                    root8=Tk()
                    root8.geometry('500x400')
                    root8.title("UPDATE")
                    frame07=Frame(root8,width=400,height=300,relief=SUNKEN)
                    frame07.pack()
                    lblup1=Label(frame07,font=('arial',16,'italic','bold'),text='PRODUCT NAME',bd=16,anchor='w')
                    lblup1.grid(row=2,column=0)
                    lblup11 = ttk.Combobox(frame07, values=["ESC","Motor","Battery","Wing","Fuselage","Transmitter","Reciever","Servo","Gum Tape","Drilling machine","Glue Gun","Glue Stick"])
                    lblup11.grid(row=2,column=1)
                    lblup2=Label(frame07,font=('arial',16,'italic','bold'),text='COUNT',bd=16,anchor='w')
                    lblup2.grid(row=3,column=0)
                    lblup2=Entry(frame07,font=('Times New Roman',16),bd=5,insertwidth=4,bg='steel blue',justify='center')
                    lblup2.grid(row=3,column=1)
                    btn67=Button(frame07,padx=30,pady=10,text='UPDATE',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=update1).grid(row=4,columnspan=2)
                def deletein():
                    
                    def delete1():
                        conn=psycopg2.connect('')         #PostgreSql Database link     
                        cur1=conn.cursor()
                        cur1.execute("DELETE FROM workshop WHERE product_name='%s'"% (lblup11.get()))
                        conn.commit()
                        top89.destroy()
                        mess1=Tk()
                        mess1.geometry("250x200+500+200")
                        mess1.title("DELETE")
                        lmess1=Label(mess1,text="DELETE COMPLETE",font=("consol 20 bold"),width=14,fg='white',bg='red')
                        lmess1.place(x=4,y=80)
                        mess1.configure(bg='#ffc2b3')
                        mess1.mainloop()   
                        
                        
                                    
                    root89=Tk()
                    root89.geometry('500x400')
                    root89.title("DELETE")
                    frame87=Frame(root89,width=400,height=300,relief=SUNKEN)
                    frame87.pack()
                    lblup1=Label(frame87,font=('arial',16,'italic','bold'),text='PRODUCT NAME',bd=16,anchor='w')
                    lblup1.grid(row=2,column=0)
                    lblup11 = ttk.Combobox(frame87, values=["ESC","Motor","Battery","Wing","Fuselage","Transmitter","Reciever","Servo","Gum Tape","Drilling machine","Glue Gun","Glue Stick"])
                    lblup11.grid(row=2,column=1)
                    
                    btn78=Button(frame87,padx=30,pady=10,text='DELETE',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=delete1).grid(row=4,columnspan=2)

    
                
                root6=Tk()
                root6.geometry('700x700')
                root6.title("WORKSHOP CHECK")
                frame09=Frame(root6,width=400,height=300,relief=SUNKEN)
                frame09.pack()
                lblwork=Label(frame09,font=('arial',16,'italic','bold'),text='Product_name',bd=16,anchor='w')
                lblwork.grid(row=1,column=0)
                drop = ttk.Combobox(frame09, values=["ESC","Motor","Battery","Wing","Fuselage","Transmitter","Reciever","Servo","Gum Tape","Drilling machine","Glue Gun","Glue Stick"])
                drop.grid(row=1,column=1)
                lblwork11=Label(frame09,font=('arial',16,'italic','bold'),text='Required for a Team',bd=16,anchor='w')
                lblwork11.grid(row=2,column=0)
                lblwork11=Entry(frame09,font=('Times New Roman',16),bd=5,insertwidth=4,bg='steel blue',justify='center')
                lblwork11.grid(row=2,column=1)
                btn23=Button(frame09,padx=30,pady=10,text='ADD',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=work1).grid(row=3,columnspan=5)
                lblwork22=Label(frame09,font=('arial',16,'italic','bold'),text='No. of teams',bd=16,anchor='w')
                lblwork22.grid(row=4,column=0)
                lblwork22=Entry(frame09,font=('Times New Roman',16),bd=5,insertwidth=4,bg='steel blue',justify='center')
                lblwork22.grid(row=4,column=1)
                btn34=Button(frame09,padx=30,pady=10,text='ADD',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=work2).grid(row=5,columnspan=5)
                
                lblsim=Label(frame09,font=('arial',16,'italic','bold'),text="",bd=16,anchor='w')
                lblsim.grid(row=7,column=2)

                lblsim=Label(frame09,font=('arial',16,'italic','bold'),text='',bd=16,anchor='w')
                lblsim.grid(row=7,column=3)
                btn45=Button(frame09,padx=30,pady=10,text='UPDATE',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=updatein).grid(row=7,column=0)
                btn67=Button(frame09,padx=30,pady=10,text='DELETE',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=deletein).grid(row=7,column=4)         

                
            except Exception as e:
                print(e)


        def competition():
            root6=Tk()
            root6.geometry('700x700')
            root6.title("WORKSHOP CHECK")
            frame90=Frame(root6,width=400,height=300,relief=SUNKEN)
            frame90.pack()
            lblwork=Label(frame90,font=('arial',16,'italic','bold'),text='Product_name',bd=16,anchor='w')
            lblwork.grid(row=1,column=0)
            drop1 = ttk.Combobox(frame90, values=["ESC","Motor","Battery","Wing","Fuselage","Transmitter","Reciever","Servo","Gum Tape","Drilling machine","Glue Gun","Glue Stick"])
            drop1.grid(row=1,column=1)
            lblwork01=Label(frame90,font=('arial',16,'italic','bold'),text='Required for a Team',bd=16,anchor='w')
            lblwork01.grid(row=2,column=0)
            lblwork01=Entry(frame90,font=('Times New Roman',16),bd=5,insertwidth=4,bg='steel blue',justify='center')
            lblwork01.grid(row=2,column=1)
            lblwork02=Label(frame90,font=('arial',16,'italic','bold'),text='No. of teams',bd=16,anchor='w')
            lblwork02.grid(row=4,column=0)
            lblwork02=Entry(frame90,font=('Times New Roman',16),bd=5,insertwidth=4,bg='steel blue',justify='center')
            lblwork02.grid(row=4,column=1)   
            lblsim1=Label(frame90,font=('arial',16,'italic','bold'),text="",bd=16,anchor='w')
            lblsim1.grid(row=7,column=2)
            lblsim=Label(frame90,font=('arial',16,'italic','bold'),text='',bd=16,anchor='w')
            lblsim.grid(row=7,column=3)
            
            
            
            try:
                def comp1():
                    conn=psycopg2.connect('')     #PostgreSql Database link    
                    cur=conn.cursor()
                    cur.execute("insert into competition values('%s',%d)"%(drop1.get(),int(lblwork01.get())))
                    conn.commit()
                def comp2():
                    curs2="select p.product_name, count(*) , p.condition_ from competition c, product_details p where p.product_name=c.product_name group by p.product_name ,p.condition_ having p.condition_ != 'bad' order by p.product_name;"
                    cur.execute(curs1)
                    data1=cur.fetchall()
                    list1=[]
                    n=lblwork22.get()
                    curs2="update competition set require2=require1 * %d"%(int(n))
                    cur.execute(curs2)
                    curs3="SELECT * FROM competition ORDER BY product_name"
                    cur.execute(curs3)
                    data2=cur.fetchall()
                    list2=[]
                    list4=[]
                    conn.commit()
                    for row in data1:
                        list1.append(row[1])
                    for row1 in data2:
                        list2.append(row1[2])
                        list4.append(row1[0])
        
                    def calc4():
                        list3=[]
                        for i in range(0,len(list1)):
                            list3.append(list2[i]-list1[i])
                        lbl1=Label(frame,text='PRODUCT NAME',width=25,fg='red').grid(row=0,column=0)
                        lbl2=Label(frame,text='IN INVENTORY',width=25,fg='red').grid(row=0,column=1)
                        lbl3=Label(frame,text='REQUIRED FOR COMPETITION',width=25,fg='red').grid(row=0,column=2)
                        lbl4=Label(frame,text='NEED TO PURCHASE',width=25,fg='red').grid(row=0,column=3)
                        for k in range(0, 100000000):
                            lbl11=Label(frame,text=list4[k],width=12)
                            lbl12=Label(frame,text=list1[k],width=12)
                            lbl13=Label(frame,text=list2[k],width=12)
                            lbl14=Label(frame,text=list3[k],width=12)
                            lbl11.grid(row=k+1,column=0)
                            lbl12.grid(row=k+1,column=1)
                            lbl13.grid(row=k+1,column=2)
                            lbl14.grid(row=k+1,column=3)
                    def myfunction90(event):
                        canvas.configure(scrollregion=canvas.bbox("all"),width=800,height=200)
                        

                    root73=Tk()
                    sizex = 800
                    sizey = 300
                    posx  = 100
                    posy  = 150
                    root73.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
                    root73.title('COMPETITION INVENTORY')
                    myframe60=Frame(root73,relief=GROOVE,width=30,height=70,bd=1)
                    myframe60.place(x=10,y=10)

                    canvas=Canvas(myframe60)
                    frame=Frame(canvas)
                    myscrollbar=Scrollbar(myframe6,orient="vertical",command=canvas.yview)
                    canvas.configure(yscrollcommand=myscrollbar.set)

                    myscrollbar.pack(side="right",fill="y")
                    canvas.pack(side="left")
                    canvas.create_window((10,10),window=frame,anchor='nw')
                    frame.bind("<Configure>",myfunction90)
                    calc4()
                    root73.mainloop()

                
                def updatein1():

                    def update2():
                        conn=psycopg2.connect('')       #PostgreSql Database link     
                        cur=conn.cursor()
                        cur.execute("UPDATE competition SET require1=%d WHERE product_name='%s'"% (int(lblup02.get()),lblup110.get()))
                        conn.commit()
                        box.showinfo("UPDATE","UPDATED")
                        
                        root8.destroy()
                        mess1=Tk()
                        mess1.geometry("250x200+500+200")
                        mess1.title("UPDATE")
                        lmess1=Label(mess1,text="UPDATED",font=("consol 20 bold"),width=14,fg='white',bg='red')
                        lmess1.place(x=4,y=80)
                        mess1.configure(bg='#ffc2b3')
                        mess1.mainloop()

                    root8=Tk()
                    root8.geometry('500x400')
                    root8.title("UPDATE")
                    frame07=Frame(root8,width=400,height=300,relief=SUNKEN)
                    frame07.pack()
                    lblup01=Label(frame07,font=('arial',16,'italic','bold'),text='PRODUCT NAME',bd=16,anchor='w')
                    lblup01.grid(row=2,column=0)
                    lblup110 = ttk.Combobox(frame07, values=["ESC","Motor","Battery","Wing","Fuselage","Transmitter","Reciever","Servo","Gum Tape","Drilling machine","Glue Gun","Glue Stick"])
                    lblup110.grid(row=2,column=1)
                    lblup02=Label(frame07,font=('arial',16,'italic','bold'),text='COUNT',bd=16,anchor='w')
                    lblup02.grid(row=3,column=0)
                    lblup02=Entry(frame07,font=('Times New Roman',16),bd=5,insertwidth=4,bg='steel blue',justify='center')
                    lblup02.grid(row=3,column=1)
                    btn60=Button(frame07,padx=30,pady=10,text='UPDATE',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=update2).grid(row=4,columnspan=2)

                    
                def deletein1():
                    
                    def delete2():
                        conn=psycopg2.connect('')         #PostgreSql Database link     
                        cur1=conn.cursor()
                        cur1.execute("DELETE FROM competition WHERE product_name='%s'"% (lblup11.get()))
                        conn.commit()
                        box.showinfo("DELETE","DELETED")
                        root89.destroy()
                        mess1=Tk()
                        mess1.geometry("250x200+500+200")
                        mess1.title("DELETE")
                        lmess1=Label(mess1,text="DELETED",font=("consol 20 bold"),width=14,fg='white',bg='red')
                        lmess1.place(x=4,y=80)
                        mess1.configure(bg='#ffc2b3')
                        mess1.mainloop()
                        
                        
                                    
                    root89=Tk()
                    root89.geometry('500x400')
                    root89.title("DELETE")
                    frame87=Frame(root89,width=400,height=300,relief=SUNKEN)
                    frame87.pack()
                    lblup1=Label(frame87,font=('arial',16,'italic','bold'),text='PRODUCT NAME',bd=16,anchor='w')
                    lblup1.grid(row=2,column=0)
                    lblup11 = ttk.Combobox(frame87, values=["ESC","Motor","Battery","Wing","Fuselage","Transmitter","Reciever","Servo","Gum Tape","Drilling machine","Glue Gun","Glue Stick"])
                    lblup11.grid(row=2,column=1)
                    
                    btn78=Button(frame87,padx=30,pady=10,text='DELETE',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=delete2).grid(row=4,columnspan=2)

    
                
                
                
            except Exception as e:
                print(e)
                
            btn23=Button(frame90,padx=30,pady=10,text='ADD',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=comp1).grid(row=3,columnspan=5)
            btn04=Button(frame90,padx=30,pady=10,text='ADD',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=comp2).grid(row=5,columnspan=5)
            btn45=Button(frame90,padx=30,pady=10,text='UPDATE',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=updatein1).grid(row=7,column=0)
            btn67=Button(frame90,padx=30,pady=10,text='DELETE',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=deletein1).grid(row=7,column=4)         

        def qrcod():
                            def create_qrcode():

                        

                                
                                conn=psycopg2.connect('')             #PostgreSql Database link     
                                cur=conn.cursor()
                                curs="SELECT * FROM product_details order by pid"
                                cur.execute(curs)
                                xy=cur.fetchall()
                                
                                conn.commit()
                                
                                for row in xy:
                                        pid=lbl22i.get()
                                        if row[0]== pid:
                                            row0=str(row[0])
                                            row1=str(row[1])
                                            
                                                    #Create qr code instance
                                            qr = qrcode.QRCode(
                                                version = 1,
                                                error_correction = qrcode.constants.ERROR_CORRECT_H,
                                                box_size = 10,
                                                border = 4,
                                            )

                                            # The data that you want to store
                                            data = lbl22i.get()

                                            # Add data
                                            qr.add_data(data)
                                            qr.make(fit=True)

                                            # Create an image from the QR Code instance
                                            img = qr.make_image()
                                            
                                            # Save it somewhere, change the extension as needed:  
                                            #print(img+" THIS IS QR CODE")
                                            
                                            img.show()
                                            if lbl33i.get() =="YES" or lbl33i.get() =="yes" or lbl33i.get() =="Y" or lbl33i.get() =="y":
                                                img.save(lbl22i.get()+".jpg")
                                                print("okk")
                                            elif lbl33i.get() =="NO" or lbl33i.get() =="no" or lbl33i.get() =="N" or lbl33i.get() =="n":
                                                print("")
                                            else:
                                                showinfo("save","enter YES if u would like to save else keep it empty")
                                    
                            
                            top4=Tk()
                            top4.geometry('500x300')
                            top4.title('ADD ITEM')
                            frame8=Frame(top4,width=600,height=600,relief=SUNKEN)
                            frame8.pack()
                            lbl22=Label(frame8,font=('arial',16,'italic','bold'),text='Product_id',bd=16,anchor='w')
                            lbl22.grid(row=1,column=0)
                            lbl22i=Entry(frame8,font=('arial',16),bd=5,insertwidth=4,justify='center')
                            lbl22i.grid(row=1,column=2)
                            lbl33=Label(frame8,font=('arial',16,'italic','bold'),text='SAVE ?',bd=16,anchor='w')
                            lbl33.grid(row=2,column=0)
                            lbl33i=Entry(frame8,font=('arial',16),textvariable="YES OR NO",bg="blue",bd=5,insertwidth=4,justify='center')
                            lbl33i.grid(row=2,column=2)


                            btn1=Button(frame8,padx=30,pady=10,text='ADD',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=create_qrcode).grid(row=3,columnspan=5)
                            
                            
               
        def re_login():
            logout_time=datetime.datetime.now()
            conn=psycopg2.connect('')
            cur=conn.cursor()                 
            cur.execute("INSERT INTO LOGIN_TIME(name,login_time,logout_time,total_time) values('%s','%s','%s','%s')" %('admin',login_time,logout_time,logout_time-login_time))
            conn.commit()
            
            top2.destroy()
            main_login()

        def reset_password():
                                
                                def reset():                          
                                    
                                    if lbl55i.get() == lbl66i.get():
                                        conn=psycopg2.connect('')
                                        cur=conn.cursor()
                                        cur.execute("UPDATE user_details SET passwd= '%s' WHERE uid='%d'"%(lbl55i.get(),user_store_id))
                                        cur.execute("select * from user_details where uid= %d"%(user_store_id))
                                        data2=cur.fetchall()
                                        data2=str(data2)
                                        cur.execute("select * from user_details ")
                                        data=cur.fetchall()
                                        conn.commit()
                                        
                                        for a in data:
                                             if a[0]==user_store_id:
                                                 a0=str(a[0])
                                                 name=a[1]
                                                 email_of_user=a[4]
                                                 msg= name+" , you have changed the password of the inventory management(AEROCLUB) with userid = "+a0+"  to  "+lbl66i.get()+" ."
                                                 obj=smtplib.SMTP('smtp.gmail.com',587)
                                                 obj.ehlo()
                                                 obj.starttls()
                                                 obj.login("","")                                         #("sender_mail","password")
                                                 receiver=["",email_of_user]                              #["reciever_mail",....]
                                                 obj.sendmail("",receiver,msg)                            #("sender_mail")

                                                 top5.destroy()
                                                 mess1=Tk()
                                                 mess1.geometry("350x200")
                                                 mess1.title("password")
                                                 lmess1=Label(mess1,text="PASSWORD CHANGED",font=("consol 20 bold"),width=19,fg='white',bg='red')
                                                 lmess1.place(x=4,y=80)
                                                 mess1.configure(bg='#ffc2b3')
                                                 mess1.mainloop()     
                                                 

                                top5=Tk()
                                top5.geometry('700x300')
                                top5.title('CHANGE PASSWORD')
                                frame9=Frame(top5,width=600,height=600,relief=SUNKEN)
                                frame9.pack()
                                lbl55=Label(frame9,font=('arial',16,'italic','bold'),text='ENTER NEW PASSWORD',bd=16,anchor='w').grid(row=2,column=2)  
                                lbl55i=Entry(frame9,font=('Times New Roman',16),bd=5,insertwidth=4,bg='steel blue',justify='right',show='*')
                                lbl55i.grid(row=2,column=3)
                                lbl66=Label(frame9,font=('arial',16,'italic','bold'),text='VERIFY PASSWORD',bd=16,anchor='w')
                                lbl66.grid(row=3,column=2)
                                lbl66i=Entry(frame9,font=('Times New Roman',16),show='*',bd=5,insertwidth=4,bg='steel blue',justify='right')
                                lbl66i.grid(row=3,column=3)
                                btn1=Button(frame9,padx=30,pady=10,text='SUBMIT',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=reset).grid(row=5,columnspan=5)
            
        def login_details():
             conn=psycopg2.connect('')          #PostgreSql Database link     
             cur=conn.cursor()
             cur.execute("select * from login_time")
             data2=cur.fetchall()
             
            
             conn.commit()
                                        

          
        menubar = Menu(top2,bg="blue",fg="RED")
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Product Details",command=showproduct)
        filemenu.add_command(label="User Details",command=showuser)
        filemenu.add_command(label="Borrow Details",command=borrowdetail)
        filemenu.add_command(label="Return Details",command=returndetail)
        filemenu.add_command(label="LOG OUT",command=re_login)
        filemenu.add_separator()
        filemenu.add_command(label="Exit",command=top2.destroy)
        menubar.add_cascade(label="View", menu=filemenu)

        updatemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="User", menu=updatemenu)
        updatemenu.add_command(label="Add User",command=adduser)
        updatemenu.add_command(label="Remove User",command=removeuser)

        countmenu= Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Count',menu=countmenu)
        countmenu.add_command(label="Usage",command=count)
        countmenu.add_command(label="QRCODE",command=qrcod)

        countmenu= Menu(menubar, tearoff=0)
        menubar.add_cascade(label='CLUB',menu=countmenu)
        countmenu.add_command(label="Workshop Inventory",command=workshop)
        countmenu.add_command(label="Competition Inventory",command=competition)

        countmenu= Menu(menubar, tearoff=0)
        menubar.add_cascade(label='EXTRA FEATURES',menu=countmenu)
        countmenu.add_command(label="QRCODE",command=qrcod)
        countmenu.add_command(label="LOGIN DETAILS",command=login_details)
        countmenu.add_command(label="PASSWORD",command=reset_password)
        

        top2.config(menu=menubar)

        
        def borrow_data():
            try:
                def borrow():
                    tz_India = pytz.timezone('Asia/Kolkata')
                    datetime_India = datetime.now(tz_India)
                    t_m=datetime_India.strftime("%H:%M:%S")
                    date=datetime.now(tz_India)
                    dt=date.strftime('20%y-%m-%d')
                    conn=psycopg2.connect('')
                    cur=conn.cursor()
                    curs="INSERT INTO borrow (uid,user_name,pid,date1,time1,purpose) VALUES(%d,'%s','%s','%s','%s','%s')"%(int(id_.get()),b,r,dt,t_m,lblpurp1.get())
                    curs2="UPDATE product_details SET availability='NO' WHERE pid='%s'"%(r)
                    cur.execute(curs)
                    cur.execute(curs2)
                    conn.commit()

                cap = cv2.VideoCapture(0)
                detector = cv2.QRCodeDetector()
                while True:
                    _, img = cap.read()
                    data, bbox, _ = detector.detectAndDecode(img)
                    if bbox is not None:
                        for i in range(len(bbox)):
                            cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
                        if data:
                            r=data
                            a=1
                            if a==1:
                                break
                    cv2.imshow("img", img)
           
                    if cv2.waitKey(1) == ord("q"):
                       break
                cap.release()
                cv2.destroyAllWindows()


                conn=psycopg2.connect('')       #PostgreSql Database link   
                cur9=conn.cursor()
                                    
                sq25="SELECT * FROM user_details WHERE uid=%d"%(int(id_.get()))
                cur9.execute(sq25)
                data55=cur9.fetchall()
                            
                for row77 in data55:
                                     
                    b=row77[1]
                lbluser=Label(frame6,font=('arial',16,'italic','bold'),text='USER ID',bd=16,anchor='w')
                lbluser.grid(row=1,column=0)
                lbluser=Label(frame6,font=('Times New Roman',16),text=id_.get(),height=1,width=19,justify='right')
                lbluser.grid(row=1,column=1)
                lblu_n=Label(frame6,font=('arial',16,'italic','bold'),text='USER_NAME',bd=16,anchor='w')
                lblu_n.grid(row=2,column=0)
                lblu_n=Label(frame6,font=('Times New Roman',16),text=b,height=1,width=19,justify='right')
                lblu_n.grid(row=2,column=1)
                lblp_id=Label(frame6,font=('arial',16,'italic','bold'),text='PRODUCT ID',bd=16,anchor='w')
                lblp_id.grid(row=3,column=0)
                lblp_id=Label(frame6,font=('Times New Roman',16),text=r,justify='right')
                lblp_id.grid(row=3,column=1)
                lblpurp1=Label(frame6,font=('arial',16,'italic','bold'),text='PURPOSE',bd=16,anchor='w')
                lblpurp1.grid(row=4,column=0)
                lblpurp1=Entry(frame6,font=('Times New Roman',16),bd=5,insertwidth=4,bg='steel blue',justify='right')
                lblpurp1.grid(row=4,column=1)
                btn3=Button(frame6,padx=30,pady=10,text='SUBMIT',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=borrow).grid(row=8,columnspan=2)
                lblu_u=Label(frame6,font=('arial',16,'italic','bold'),text='',bd=16,anchor='w').grid(row=5,column=2)

            except Exception as e:
                print(e)
                
                
            
        def return_data():
            try:
                def return_n ():
                    tz_India = pytz.timezone('Asia/Kolkata')
                    datetime_India = datetime.now(tz_India)
                    t_m=datetime_India.strftime("%H:%M:%S")
                    date=datetime.now(tz_India)
                    dt=date.strftime('20%y-%m-%d')
                    conn=psycopg2.connect('')
                    cur=conn.cursor()
                    curs="INSERT INTO return_ (uid,user_name,pid,condition_,date2,time2) VALUES(%d,'%s','%s','%s','%s','%s')"%(int(id_.get()),b,r,lblcond.get(),dt,t_m)
                    curs2="UPDATE product_details SET condition_='%s' WHERE pid='%s'"%(lblcond.get(),r)
                    curs3="DELETE FROM borrow WHERE pid='%s'"%(r)
                    cur.execute(curs)
                    cur.execute(curs2)
                    cur.execute(curs3)
                    conn.commit()
                    

                cap = cv2.VideoCapture(0)
                detector = cv2.QRCodeDetector()
                while True:
                    _, img = cap.read()
                    data, bbox, _ = detector.detectAndDecode(img)
                    if bbox is not None:
                        for i in range(len(bbox)):
                            cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
                        if data:
                            r=data
                            a=1
                            if a==1:
                                break
                    cv2.imshow("img", img)
           
                    if cv2.waitKey(1) == ord("q"):
                       break
                cap.release()
                cv2.destroyAllWindows()

                conn=psycopg2.connect('')
                cur1=conn.cursor()
                                    
                sql2="SELECT * FROM user_details WHERE uid=%d"%(int(id_.get()))
                cur1.execute(sql2)
                data11=cur1.fetchall()
                            
                for row99 in data11:
                                     
                    b=row99[1]
                
                lbluser=Label(frame6,font=('arial',16,'italic','bold'),text='USER ID',bd=16,anchor='w')
                lbluser.grid(row=1,column=0)
                lbluser=Label(frame6,font=('Times New Roman',16),text=id_.get(),height=1,width=19,justify='center')
                lbluser.grid(row=1,column=1)
                lblu_n=Label(frame6,font=('arial',16,'italic','bold'),text='USER_NAME',bd=16,anchor='w')
                lblu_n.grid(row=2,column=0)
                lblu_n=Label(frame6,font=('Times New Roman',16),text=b,height=1,width=19,justify='center')
                lblu_n.grid(row=2,column=1)
                lblp_id=Label(frame6,font=('arial',16,'italic','bold'),text='PRODUCT ID',bd=16,anchor='w')
                lblp_id.grid(row=3,column=0)
                lblp_id=Label(frame6,font=('Times New Roman',16),text=r,justify='center')
                lblp_id.grid(row=3,column=1)
                lblcond=Label(frame6,font=('arial',16,'italic','bold'),text='CONDITION',bd=16,anchor='w')   
                lblcond.grid(row=4,column=0)
                label=Label(frame6,height=5,width=33)
                label.grid(row=4,column=1)
                lblcond=ttk.Combobox(frame6,values=["good","moderate","bad"])
                lblcond.grid(row=4,column=1)
                
                
                
                btn3=Button(frame6,padx=30,pady=10,text='SUBMIT',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=return_n).grid(row=8,columnspan=2)
                lblu_u=Label(frame6,font=('arial',16,'italic','bold'),text='',bd=16,anchor='w').grid(row=5,column=2)


            except Exception as e:
                print(e)


        def delete():
            
            def delete_in():
                conn=psycopg2.connect('')       #PostgreSql Database link  
                cur=conn.cursor()
                curs="delete from product_details where pid='%s'"%(lbl22i.get())
                curs2="SELECT product_name FROM product_details WHERE pid='%s'"%(lbl22i.get())
                cur.execute(curs2)
                e=cur.fetchall()
                for row in e:
                    a=str(row[0])
                cur.execute(curs)
                
                conn.commit()
                top3.destroy()
                mess1=Tk()
                mess1.geometry("250x200+500+200")
                mess1.title("DELETE ITEM")
                lmess1=Label(mess1,text="ITEM DELETED",font=("consol 20 bold"),width=14,fg='white',bg='red')
                lmess1.place(x=4,y=80)
                mess1.configure(bg='#ffc2b3')
                mess1.mainloop()
                
                
                
            top3=Tk()
            top3.geometry('500x300')
            top3.title('DELETE ITEM')
            frame8=Frame(top3,width=600,height=600,relief=SUNKEN)
            frame8.pack()
            lbl22=Label(frame8,font=('arial',16,'italic','bold'),text='Enter Product_ID',bd=16,anchor='w')
            lbl22.grid(row=1,column=0)
            lbl22i=Entry(frame8,font=('arial',16,'italic','bold'),bd=5,insertwidth=4,justify='center')
            lbl22i.grid(row=1,column=2)
            btn1=Button(frame8,padx=30,pady=10,text='DELETE',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=delete_in).grid(row=2,columnspan=5)
            
            
        def add():
            def add_in():
                conn=psycopg2.connect('')         #PostgreSql Database link     
                cur=conn.cursor()
                curs="INSERT INTO product_details (pid,product_name,condition_,availability) VALUES('%s','%s','good','yes')"%(lbl22i.get(),lbl33i.get())
                cur.execute(curs)
                
                
                conn.commit()
                top4.destroy()
                mess=Tk()
                mess.geometry("250x200+500+200")
                mess.title("ADD ITEM")
                lmess=Label(mess,text="Item Added",font=("consol 20 bold"),width=14,fg='white',bg='red')
                lmess.grid(row=1,column=1)
                mess.configure(bg='#ffc2b3')
                mess.mainloop()
            
            top4=Tk()
            top4.geometry('500x300')
            top4.title('ADD ITEM')
            frame8=Frame(top4,width=600,height=600,relief=SUNKEN)
            frame8.pack()
            lbl22=Label(frame8,font=('arial',16,'italic','bold'),text='Product_id',bd=16,anchor='w')
            lbl22.grid(row=1,column=0)
            lbl22i=Entry(frame8,font=('arial',16),bd=5,insertwidth=4,justify='center')
            lbl22i.grid(row=1,column=2)
            lbl33=Label(frame8,font=('arial',16,'italic','bold'),text='Product_name',bd=16,anchor='w')
            lbl33.grid(row=2,column=0)
            lbl33i=Entry(frame8,font=('arial',16),bd=5,insertwidth=4,justify='center')
            lbl33i.grid(row=2,column=2)


            btn1=Button(frame8,padx=30,pady=10,text='ADD',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=add_in).grid(row=3,columnspan=5)

                
            






               
        lbluser_=Label(frame6,font=('arial',16,'italic','bold'),text='',bd=16,anchor='w').grid(row=7,column=4)
        btn1=Button(frame6,padx=30,pady=10,text='ADD',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=add).grid(row=0,column=3)
        lblr_=Label(frame6,font=('arial',16,'italic','bold'),text='',bd=16,anchor='w').grid(row=1,column=3)
        
        btn2=Button(frame6,padx=30,pady=10,text='DELETE',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=delete).grid(row=2,column=3)
        lbluser_=Label(frame6,font=('arial',16,'italic','bold'),text='',bd=16,anchor='w').grid(row=3,column=3)

        btn3=Button(frame6,padx=30,pady=10,text='BORROW',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=borrow_data).grid(row=4,column=3)
        lblr_=Label(frame6,font=('arial',16,'italic','bold'),text='',bd=16,anchor='w').grid(row=5,column=3)
        
        btn4=Button(frame6,padx=30,pady=10,text='RETURN',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=return_data).grid(row=6,column=3)
        lbluser_=Label(frame6,font=('arial',16,'italic','bold'),text='',bd=16,anchor='w').grid(row=7,column=3)

                
    


    
    
        #------------------------------------------------CHECK IF THIS IS REQUIRED-------------------------------------------------------------------------------
        def tab1():
                try:
                    conn=psycopg2.connect('')         #PostgreSql Database link    
                    cur=conn.cursor()
                    print(comboExample.get())
                    cur.execute("SELECT pid,product_name,condition_,availability FROM product_details WHERE product_name='%s'" %(comboExample.get()))
                    data=cur.fetchall()
                    list99=[]
                    for row in data:
                        list99.append(row[0])
                        list99.append(row[1])
                        list99.append(row[2])
                        list99.append(row[3])
                    def tabular1():
                        lbl1=Label(frame,text='PID',width=12,fg='red').grid(row=0,column=0)
                        lbl2=Label(frame,text='PRODUCT_NAME',width=12,fg='red').grid(row=0,column=1)
                        lbl3=Label(frame,text='CONDITION',width=12,fg='red').grid(row=0,column=2)
                        lbl4=Label(frame,text='AVAILABILITY',width=12,fg='red').grid(row=0,column=3)
                        r=cur.fetchall()
                        for k in range(0,1000000,4):
                            lbl11=Label(frame,text=list99[k],width=12)
                            lbl12=Label(frame,text=list99[k+1],width=12)
                            lbl13=Label(frame,text=list99[k+2],width=12)
                            lbl14=Label(frame,text=list99[k+3],width=12)
                            lbl11.grid(row=k+1,column=0)
                            lbl12.grid(row=k+1,column=1)
                            lbl13.grid(row=k+1,column=2)
                            lbl14.grid(row=k+1,column=3)
                        
                    def myfunction1(event):
                        canvas.configure(scrollregion=canvas.bbox("all"),width=400,height=200)
                        

                    root=Tk()
                    sizex = 500
                    sizey = 400
                    posx  = 100
                    posy  = 150
                    root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
                    root.title('Check It')
                    myframe=Frame(root,relief=GROOVE,width=30,height=70,bd=1)
                    myframe.place(x=10,y=10)

                    canvas=Canvas(myframe)
                    frame=Frame(canvas)
                    myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
                    canvas.configure(yscrollcommand=myscrollbar.set)

                    myscrollbar.pack(side="right",fill="y")
                    canvas.pack(side="left")
                    canvas.create_window((10,10),window=frame,anchor='nw')
                    frame.bind("<Configure>",myfunction1)
                    tabular1()
                    root.mainloop()
                except Exception as e:
                    print(e)

        #-----------------------------------------------------------------------------------------------------------------------------------------------------
        frame5=Frame(top2,width=600,height=600,relief=SUNKEN)
        frame5.pack(side=LEFT)
        frame3=Frame(top2,width=600,height=600,relief=SUNKEN)
        frame3.pack(side=LEFT)
        
                        
                        
        curs="SELECT product_name from workshop "
                              
        cur.execute(curs)
        x=cur.fetchall()
        conn.commit()
                        

        abc=x
        test_list=list(itertools.chain(*abc))

                        
        class AutocompleteCombobox(ttk.Combobox):
           
                                   def set_completion_list(self, completion_list):
                                        """Use our completion list as our drop down selection menu, arrows move through menu."""
                                        self._completion_list = sorted(completion_list, key=str.lower) # Work with a sorted list
                                        self._hits = []
                                        self._hit_index = 0
                                        self.position = 0
                                        self.bind('<KeyRelease>', self.handle_keyrelease)
                                        self['values'] = self._completion_list# Setup our popup menu
                                       
                                        
                                        
                                   def autocomplete(self, delta=0):
                                        def productss():
                                            try:
                                                conn=psycopg2.connect('')     #PostgreSql Database link     
                                                cur=conn.cursor()
                                                cur.execute('SELECT * FROM product_details ORDER BY product_name ')
                                                data=cur.fetchall()
                                                list99=[]
                                             
                                                for row in data:
                                                  c=self.get()                          
                                                  if row[1] ==c:
                                                    list99.append(row[0])
                                                    list99.append(row[1])
                                                    list99.append(row[2])
                                                    list99.append(row[3])
                                                    
                                                def tabular0():
                                                    lbl1=Label(frame,text='PID',width=12,fg='red').grid(row=0,column=0)
                                                    lbl2=Label(frame,text='PRODUCT_NAME',width=12,fg='red').grid(row=0,column=1)
                                                    lbl3=Label(frame,text='CONDITION',width=12,fg='red').grid(row=0,column=2)
                                                    lbl4=Label(frame,text='AVAILABILITY',width=12,fg='red').grid(row=0,column=3)
                                                    r=cur.fetchall()
                                                    print("r7")
                                                    for k in range(0,1000000,4):
                                                        lbl11=Label(frame,text=list99[k],width=12)
                                                        lbl12=Label(frame,text=list99[k+1],width=12)
                                                        lbl13=Label(frame,text=list99[k+2],width=12)
                                                        lbl14=Label(frame,text=list99[k+3],width=12)
                                                        lbl11.grid(row=k+1,column=0)
                                                        lbl12.grid(row=k+1,column=1)
                                                        lbl13.grid(row=k+1,column=2)
                                                        lbl14.grid(row=k+1,column=3)
                                                            
                                                def myfunction0(event):
                                                    canvas.configure(scrollregion=canvas.bbox("all"),width=400,height=200)
                                                            

                                                root1=Tk()
                                                sizex = 500
                                                sizey = 300
                                                posx  = 100
                                                posy  = 150
                                                root1.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
                                                root1.title('Check It')
                                                myframe1=Frame(root1,relief=GROOVE,width=30,height=70,bd=1)
                                                myframe1.place(x=10,y=10)

                                                canvas=Canvas(myframe1)
                                                frame=Frame(canvas)
                                                myscrollbar=Scrollbar(myframe1,orient="vertical",command=canvas.yview)
                                                canvas.configure(yscrollcommand=myscrollbar.set)

                                                myscrollbar.pack(side="right",fill="y")
                                                canvas.pack(side="left")
                                                canvas.create_window((10,10),window=frame,anchor='nw')
                                                frame.bind("<Configure>",myfunction0)
                                                tabular0()
                                                root1.mainloop()
                                            except Exception as e:
                                                print(e)
                                        
                                        """autocomplete the Combobox, delta may be 0/1/-1 to cycle through possible hits"""
                                        if delta: # need to delete selection otherwise we would fix the current position
                                                self.delete(self.position, Tkinter.END)
                                                
                                        else: # set position to end so selection starts where textentry ended
                                                self.position = len(self.get())
                                               
                                        # collect hits
                                        _hits = []
                                       
                                        for element in self._completion_list:
                                                
                                                if element.lower().startswith(self.get().lower()): # Match case insensitively
                                                        _hits.append(element)
                                                        
                                        # if we have a new hit list, keep this in mind
                                        if _hits != self._hits:
                                              
                                                self._hit_index = 0
                                                self._hits=_hits
                                                
                                        # only allow cycling if we are in a known hit list
                                        if _hits == self._hits and self._hits:
                                                self._hit_index = (self._hit_index + delta) % len(self._hits)
                                                c=self.get()
                                                
                                                for x in test_list:
                                                        if c == x:
                                                             productss()
                                                             
                                                         
                                                    
                                                
                                                
                                                
                                        # now finally perform the auto completion
                                        if self._hits:
                                                
                                                self.delete(0,Tkinter.END)
                                                self.insert(0,self._hits[self._hit_index])
                                                self.select_range(self.position,Tkinter.END)
                                                
                                                
                                                
                                                
                                        
                                   def handle_keyrelease(self, event):
                                        def productss():
                                            try:
                                                conn=psycopg2.connect('')         #PostgreSql Database link     
                                                cur=conn.cursor()
                                                cur.execute('SELECT * FROM product_details ORDER BY product_name ')
                                                data=cur.fetchall()
                                                list99=[]
                                             
                                                for row in data:
                                                  c=self.get()                          
                                                  if row[1] ==c:
                                                    list99.append(row[0])
                                                    list99.append(row[1])
                                                    list99.append(row[2])
                                                    list99.append(row[3])
                                                    
                                                def tabular0():
                                                    lbl1=Label(frame,text='PID',width=12,fg='red').grid(row=0,column=0)
                                                    lbl2=Label(frame,text='PRODUCT_NAME',width=12,fg='red').grid(row=0,column=1)
                                                    lbl3=Label(frame,text='CONDITION',width=12,fg='red').grid(row=0,column=2)
                                                    lbl4=Label(frame,text='AVAILABILITY',width=12,fg='red').grid(row=0,column=3)
                                                    r=cur.fetchall()
                                                    print("r7")
                                                    for k in range(0,1000000,4):
                                                        lbl11=Label(frame,text=list99[k],width=12)
                                                        lbl12=Label(frame,text=list99[k+1],width=12)
                                                        lbl13=Label(frame,text=list99[k+2],width=12)
                                                        lbl14=Label(frame,text=list99[k+3],width=12)
                                                        lbl11.grid(row=k+1,column=0)
                                                        lbl12.grid(row=k+1,column=1)
                                                        lbl13.grid(row=k+1,column=2)
                                                        lbl14.grid(row=k+1,column=3)
                                                            
                                                def myfunction0(event):
                                                    canvas.configure(scrollregion=canvas.bbox("all"),width=400,height=200)
                                                            

                                                root1=Tk()
                                                sizex = 500
                                                sizey = 300
                                                posx  = 100
                                                posy  = 150
                                                root1.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
                                                root1.title('Check It')
                                                myframe1=Frame(root1,relief=GROOVE,width=30,height=70,bd=1)
                                                myframe1.place(x=10,y=10)

                                                canvas=Canvas(myframe1)
                                                frame=Frame(canvas)
                                                myscrollbar=Scrollbar(myframe1,orient="vertical",command=canvas.yview)
                                                canvas.configure(yscrollcommand=myscrollbar.set)

                                                myscrollbar.pack(side="right",fill="y")
                                                canvas.pack(side="left")
                                                canvas.create_window((10,10),window=frame,anchor='nw')
                                                frame.bind("<Configure>",myfunction0)
                                                tabular0()
                                                root1.mainloop()
                                            except Exception as e:
                                                print(e)
                                         


                                       
                                                """event handler for the keyrelease event on this widget"""
                                        
                                        if event.keysym == "BackSpace":
                                               
                                                self.delete(self.index(Tkinter.INSERT), Tkinter.END)
                                                self.position = self.index(Tkinter.END)
                                        
                                        if event.keysym == "Left":
                                                
                                                if self.position < self.index(Tkinter.END): # delete the selection
                                                        
                                                        self.delete(self.position, Tkinter.END)
                                                else:
                                                        
                                                        self.position = self.position-1 # delete one character
                                                        self.delete(self.position, Tkinter.END)
                                        if event.keysym == "Right":
                                                
                                                self.position = self.index(Tkinter.END) # go to end (no selection)
                                                
                                               
                                                c=self.get()
                                                for x in test_list:
                                                        if c == x:
                                                             productss()
                                                            
                                       
                                        def mousePressEvent():
                                                print("mouse")
                                                
                                        if len(event.keysym) == 1:
                                                self.autocomplete()
   
                                        # No need for up/down, we'll jump to the popup
                                        # list at the position of the autocompletion

        def test(test_list):

                                
                                """Run a mini application to test the AutocompleteEntry Widget."""
                                #root = Tkinter.Tk(className='AutocompleteCombobox')

                                
                                combo = AutocompleteCombobox(frame5)
                                combo.set_completion_list(test_list)
                                
                                combo.pack()
                                combo.focus_set()
                                # I used a tiling WM with no controls, added a shortcut to quit
                                frame3.bind('<Control-Q>', lambda event=None: frame3.destroy())
                                frame3.bind('<Control-q>', lambda event=None: frame3.destroy())                     
        test(test_list)

        #-------------------------------------------------------------------------------CHECK IF THIS IS REQUIRED-------------------------------------------------
        
        lbluser=Label(frame5,text='',bd=16,anchor='w')
        lbluser.grid(row=2,column=3)
        lbluser=Label(frame5,text='',bd=16,anchor='w')
        lbluser.grid(row=3,column=3)
        lbluser=Label(frame5,text='',bd=16,anchor='w')
        lbluser.grid(row=4,column=3)
        lbluser=Label(frame5,text='',bd=16,anchor='w')
        lbluser.grid(row=3,column=4)
        btnn=Button(frame5,padx=30,pady=10,text='CHECK',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=tab1)
        btnn.grid(row=3,column=3)
                
        lbluser=Label(frame5,text='',bd=16,anchor='w')
        lbluser.grid(row=0,column=0)
        lbluser=Label(frame5,text='',bd=16,anchor='w')
        lbluser.grid(row=1,column=0)
        lbluser=Label(frame5,text='',bd=16,anchor='w')
        lbluser.grid(row=2,column=0)
        #------------------------------------------------------------------------------------------------------------------------------------------------------------------
    except Exception as e:
        print(e)

  def entrytab():
    login_time=datetime.datetime.now()
    user_store_id=id_.get()
    user_store_password=passwd.get()
    user_store_id=int(user_store_id)
    try:

        flag=0
        cur.execute('SELECT * FROM user_details')
        x=cur.fetchall()
        conn.commit()

     
       
        for row in x:
            a=str(row[0])
            name=row[1]
            b=row[2]              
            c=row[3]
            
            
            v1='ad1234'
            c1='n'
            c2='s'
            
        
            
            if (a!='' and b!=''):
               
                 if c==c1:
                   
                
                    if (a==id_.get() and b==passwd.get()):
                    
                        flag=0
                        top1=Tk()
                        top.destroy()
                        top1.geometry('1200x700+0+0')
                        top1.title("Inventory Check")
                        top1.iconbitmap(r'icon.ico')
                        frame0=Frame(top1,width=1200,height=100,relief=SUNKEN)
                        frame0.pack(side=TOP)
                        frame3=Frame(top1,width=600,height=600,relief=SUNKEN)
                        frame3.pack(side=LEFT)
                        frame4=Frame(top1,width=600,height=600,relief=SUNKEN)
                        frame4.pack(side=RIGHT)
                        lbl=Label(frame0,font=('arial',40,'italic','bold'),text='ENTER DETAILS',fg='steel blue',bd=16,anchor='w')
                        lbl.grid(row=0,column=0)
                        def borrow_data():
                            try:

                                def borrow():
                                    tz_India = pytz.timezone('Asia/Kolkata')
                                    datetime_India = datetime.now(tz_India)
                                    t_m=datetime_India.strftime("%H:%M:%S")
                                    date=datetime.now(tz_India)
                                    dt=date.strftime('20%y-%m-%d')
                                    conn=psycopg2.connect('')
                                    cur=conn.cursor()
                                    
                                    
                                    
                                    sql1="SELECT * FROM product_details WHERE pid='%s'"%(r)
                                    cur.execute(sql1)
                                    data=cur.fetchall()

                                   
                                    
                                    
                                    for row in data:
                                        a=row[3]
                                        if a=='yes':
                                            
                                            curs="INSERT INTO borrow (uid,user_name,pid,date1,time1,purpose) VALUES(%d,'%s','%s','%s','%s','%s')"%(int(id_.get()),b,r,dt,t_m,lblpurp.get())
                                            curs2="UPDATE product_details SET availability='no' WHERE pid='%s'"%(r)
                                            cur.execute(curs)
                                            cur.execute(curs2)
                                            conn.commit()
                                        else:
                                            messagebox3=box.showinfo('ERROR','Item Is Already taken')
                                            
                                                                                                                                        
                                cap = cv2.VideoCapture(0)
                                detector = cv2.QRCodeDetector()
                                while True:
                                    _, img = cap.read()
                                    data, bbox, _ = detector.detectAndDecode(img)
                                    if bbox is not None:
                                        for i in range(len(bbox)):
                                            cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(0,255, 0), thickness=2)
                                        if data:
                                            r=data
                                            a=1
                                            if a==1:
                                                break
                                    cv2.imshow("img", img)
                           
                                    if cv2.waitKey(1) == ord("q"):
                                       break
                                cap.release()
                                cv2.destroyAllWindows()
                         

                                conn=psycopg2.connect('')
                                cur1=conn.cursor()
                                    
                                sql2="SELECT * FROM user_details WHERE uid=%d"%(int(id_.get()))
                                cur1.execute(sql2)
                                data11=cur1.fetchall()
                            
                                for row99 in data11:
                                     
                                    b=row99[1]
                                    
                                lbluser=Label(frame4,font=('arial',16,'italic','bold'),text='USER ID',bd=16,anchor='w')
                                lbluser.grid(row=1,column=0)
                                lbluseri=Label(frame4,font=('Times New Roman',16),bd=16,text=id_.get(),anchor='w')
                                lbluseri.grid(row=1,column=1)
                                lblu_n=Label(frame4,font=('arial',16,'italic','bold'),text='USER_NAME',bd=16,anchor='w')
                                lblu_n.grid(row=2,column=0)
                                lblu_ni=Label(frame4,font=('Times New Roman',16),bd=16,text=b,anchor='w')
                                lblu_ni.grid(row=2,column=1)
                                lblp_id=Label(frame4,font=('arial',16,'italic','bold'),text='PRODUCT ID',bd=16,anchor='w')
                                lblp_id.grid(row=3,column=0)
                                lblp_idi=Label(frame4,font=('Times New Roman',16),bd=16,anchor='w',text=r)
                                lblp_idi.grid(row=3,column=1)
                                lblpurp=Label(frame4,font=('arial',16,'italic','bold'),text='PURPOSE',bd=16,anchor='w')
                                lblpurp.grid(row=4,column=0)
                                lblpurp=Entry(frame4,font=('Times New Roman',16),bd=2,insertwidth=4,bg='steel blue',justify='right')
                                lblpurp.grid(row=4,column=1)
                                btn3=Button(frame4,padx=30,pady=10,text='SUBMIT',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=borrow).grid(row=8,columnspan=2)
                                lblu_u=Label(frame4,font=('arial',16,'italic','bold'),text='',bd=16,anchor='w').grid(row=5,column=2) 
                            
                            except Exception as e:
                                print(e)
                            

                        def return_data():
                            try:
                                cap = cv2.VideoCapture(0)
                                detector = cv2.QRCodeDetector()
                                while True:
                                    _, img = cap.read()
                                    data, bbox, _ = detector.detectAndDecode(img)
                                    if bbox is not None:
                                        for i in range(len(bbox)):
                                            cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
                                        if data:
                                            r=data
                                            a=1
                                            if a==1:
                                                break
                                    cv2.imshow("img", img)
                       
                                    if cv2.waitKey(1) == ord("q"):
                                       break
                                cap.release()
                                cv2.destroyAllWindows()
                                def return_n ():
                                    tz_India = pytz.timezone('Asia/Kolkata')
                                    datetime_India = datetime.now(tz_India)
                                    t_m=datetime_India.strftime("%H:%M:%S")
                                    date=datetime.now(tz_India)
                                    dt=date.strftime('20%y-%m-%d')
                                    conn=psycopg2.connect('')
                                    cur=conn.cursor()
                                    curs5="SELECT * FROM borrow WHERE pid='%s'"%(r)
                                    cur.execute(curs5)
                                    data=cur.fetchall()
                                    for row in data:
                                        a=row[2]
                        
                                        if a is not None:
                                            
                                            curs="INSERT INTO return_ (uid,user_name,pid,condition_,date2,time2) VALUES(%d,'%s','%s','%s','%s','%s')"%(int(id_.get()),b,r,lblcond1.get(),dt,t_m)
                                            curs2="UPDATE product_details SET condition_='%s' WHERE pid='%s'"%(lblcond1.get(),r)
                                            curs3="UPDATE product_details SET availability='yes' WHERE pid='%s'"%(r)
                                            curs4="DELETE FROM borrow WHERE pid='%s'"%(r)
                                            cur.execute(curs)
                                            cur.execute(curs2)
                                            cur.execute(curs3)
                                            cur.execute(curs4)
                                            conn.commit()
                                        else:
                                            print('Hi')
                                            messagebox5=box.showinfo('Dialogue Box','Item Is Already Returned')

                                conn=psycopg2.connect('')
                                cur9=conn.cursor()
                                    
                                sq25="SELECT * FROM user_details WHERE uid=%d"%(int(id_.get()))
                                cur9.execute(sq25)
                                data55=cur9.fetchall()
                            
                                for row77 in data55:
                                     
                                    b=row77[1]

                                lbluser=Label(frame4,font=('arial',16,'italic','bold'),text='USER ID',bd=16,anchor='w')
                                lbluser.grid(row=1,column=0)
                                lbluseri=Label(frame4,font=('Times New Roman',16),bd=16,text=id_.get(),anchor='w')
                                lbluseri.grid(row=1,column=1)
                                lblu_n=Label(frame4,font=('arial',16,'italic','bold'),text='USER_NAME',bd=16,anchor='w')
                                lblu_n.grid(row=2,column=0)
                                lblu_ni=Label(frame4,font=('Times New Roman',16),bd=16,text=b,anchor='w')
                                lblu_ni.grid(row=2,column=1)
                                lblp_id=Label(frame4,font=('arial',16,'italic','bold'),text='PRODUCT ID',bd=16,anchor='w')
                                lblp_id.grid(row=3,column=0)
                                lblp_idi=Label(frame4,font=('Times New Roman',16),bd=16,text=r,anchor='w')
                                lblp_idi.grid(row=3,column=1)
                                lblcond=Label(frame4,font=('arial',16,'italic','bold'),text='CONDITION',bd=16,anchor='w')   
                                lblcond.grid(row=4,column=0)
                                label=Label(frame4,height=5,width=33)
                                label.grid(row=4,column=1)
                                lblcond1=ttk.Combobox(frame4,values=["good","moderate","bad"])
                                lblcond1.grid(row=4,column=1)
                            
                            
                                btn3=Button(frame4,padx=30,pady=10,text='SUBMIT',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=return_n).grid(row=8,columnspan=2)
                                lblu_u=Label(frame4,font=('arial',16,'italic','bold'),text='',bd=16,anchor='w').grid(row=5,column=2)                                                                                                                            
                        
                            except Exception as e:
                                print(e)
                        def re_login():
                              logout_time=datetime.datetime.now()
                              conn=psycopg2.connect('')
                              cur=conn.cursor()
                              
                              cur.execute("INSERT INTO LOGIN_TIME(name,login_time,logout_time,total_time) values('%s','%s','%s','%s')" %(name,login_time,logout_time,logout_time-login_time))
                              conn.commit()
                              top1.destroy()
                              
                              
                              main_login()
                        def reset_password():
                                
                                def reset():                          
                                    
                                    if lbl55i.get() == lbl66i.get():
                                        conn=psycopg2.connect('')         #PostgreSql Database link 
                                        cur=conn.cursor()
                                        cur.execute("UPDATE user_details SET passwd= '%s' WHERE uid='%d'"%(lbl55i.get(),user_store_id))
                                        cur.execute("select * from user_details where uid= %d"%(user_store_id))
                                        data2=cur.fetchall()
                                        data2=str(data2)
                                        cur.execute("select * from user_details ")
                                        data=cur.fetchall()
                                        
                                        conn.commit()
                                      
                                        for a in data:
                                             if a[0]==user_store_id:
                                                 a0=str(a[0])
                                                 name=a[1]
                                                 email_of_user=a[4]
                                                 msg= name+" , you have changed the password of the inventory management(AEROCLUB) with userid = "+a0+"  to  "+lbl66i.get()+" ."
                                                 obj=smtplib.SMTP('smtp.gmail.com',587)
                                                 obj.ehlo()
                                                 obj.starttls()
                                                 obj.login("","")
                                                 receiver=["",email_of_user]
                                                 obj.sendmail("",receiver,msg)

                                                 top5.destroy()
                                                 mess1=Tk()
                                                 mess1.geometry("350x200")
                                                 mess1.title("password")
                                                 lmess1=Label(mess1,text="PASSWORD CHANGED",font=("consol 20 bold"),width=19,fg='white',bg='red')
                                                 lmess1.place(x=4,y=80)
                                                 mess1.configure(bg='#ffc2b3')
                                                 mess1.mainloop()     
                                                 

                                top5=Tk()
                                top5.geometry('700x300')
                                top5.title('CHANGE PASSWORD')
                                frame9=Frame(top5,width=600,height=600,relief=SUNKEN)
                                frame9.pack()
                                lbl55=Label(frame9,font=('arial',16,'italic','bold'),text='ENTER NEW PASSWORD',bd=16,anchor='w').grid(row=2,column=2)  
                                lbl55i=Entry(frame9,font=('Times New Roman',16),bd=5,insertwidth=4,bg='steel blue',justify='right',show='*')
                                lbl55i.grid(row=2,column=3)
                                lbl66=Label(frame9,font=('arial',16,'italic','bold'),text='VERIFY PASSWORD',bd=16,anchor='w')
                                lbl66.grid(row=3,column=2)
                                lbl66i=Entry(frame9,font=('Times New Roman',16),show='*',bd=5,insertwidth=4,bg='steel blue',justify='right')
                                lbl66i.grid(row=3,column=3)
                                btn1=Button(frame9,padx=30,pady=10,text='SUBMIT',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=reset).grid(row=5,columnspan=5)
    

                        btn1=Button(frame4,padx=30,pady=10,text='BORROW',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=borrow_data).grid(row=1,column=3)
                        lblr_=Label(frame4,font=('arial',16,'italic','bold'),text='',bd=16,anchor='w').grid(row=2,column=3)
                        lblr_=Label(frame4,font=('arial',16,'italic','bold'),text='',bd=16,anchor='w').grid(row=1,column=4)
                        lbl_=Label(frame4,font=('arial',16,'italic','bold'),text='',bd=16,anchor='w').grid(row=3,column=3)
                        btn2=Button(frame4,padx=30,pady=10,text='RETURN',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=return_data).grid(row=4,column=3)
                        lblr_=Label(frame4,font=('arial',16,'italic','bold'),text='',bd=16,anchor='w').grid(row=4,column=4)
                        lbluser_=Label(frame4,font=('arial',16,'italic','bold'),text='',bd=16,anchor='w').grid(row=5,column=3)
                        lbluser_=Label(frame4,font=('arial',16,'italic','bold'),text='',bd=16,anchor='w').grid(row=6,column=3)
                        btn2=Button(frame4,padx=30,pady=10,text='LOG OUT',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=re_login).grid(row=7,column=3)

                        menubar = Menu(top1,bg="blue",fg="RED")
                        filemenu = Menu(menubar, tearoff=0)
                        filemenu.add_command(label="Change Password",command=reset_password)
                        menubar.add_cascade(label="Extra", menu=filemenu)
                        top1.config(menu=menubar)

                        
                        #--------------------------------------------------------------------check if this is required--------------------------------------------------------------------------
                    
                        def tab():
                            try:
                                conn=psycopg2.connect('')         #PostgreSql Database link   
                                cur=conn.cursor()
                                print(comboExample.get())
                                cur.execute("SELECT pid,product_name,condition_,availability FROM product_details WHERE product_name='%s'" %(comboExample.get()))
                                data=cur.fetchall()
                                list99=[]
                                for row in data:
                                    list99.append(row[0])
                                    list99.append(row[1])
                                    list99.append(row[2])
                                    list99.append(row[3])
                                def tabular():
                                    lbl1=Label(frame,text='PID',width=12,fg='powder blue').grid(row=0,column=0)
                                    lbl2=Label(frame,text='PRODUCT_NAME',width=12,fg='powder blue').grid(row=0,column=1)
                                    lbl3=Label(frame,text='CONDITION',width=12,fg='powder blue').grid(row=0,column=2)
                                    lbl4=Label(frame,text='AVAILABILITY',width=12,fg='powder blue').grid(row=0,column=3)
                                    r=cur.fetchall()
                                    for k in range(0,1000000,4):
                                        lbl11=Label(frame,text=list99[k],width=12)
                                        lbl12=Label(frame,text=list99[k+1],width=12)
                                        lbl13=Label(frame,text=list99[k+2],width=12)
                                        lbl14=Label(frame,text=list99[k+3],width=12)
                                        lbl11.grid(row=k+1,column=0)
                                        lbl12.grid(row=k+1,column=1)
                                        lbl13.grid(row=k+1,column=2)
                                        lbl14.grid(row=k+1,column=3)
                                    
                                def myfunction(event):
                                    canvas.configure(scrollregion=canvas.bbox("all"),width=400,height=200)
                                    

                                root=Tk()
                                sizex = 500
                                sizey = 400
                                posx  = 100
                                posy  = 150
                                root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
                                root.title('Check It')
                                myframe=Frame(root,relief=GROOVE,width=30,height=70,bd=1)
                                myframe.place(x=10,y=10)

                                canvas=Canvas(myframe)
                                frame=Frame(canvas)
                                myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
                                canvas.configure(yscrollcommand=myscrollbar.set)

                                myscrollbar.pack(side="right",fill="y")
                                canvas.pack(side="left")
                                canvas.create_window((10,10),window=frame,anchor='nw')
                                frame.bind("<Configure>",myfunction)
                                tabular()
                                root.mainloop()
                            except Exception as e:
                                print(e)

                        #-------------------------------------------------------------check whether the above part is required----------------------------------------------------------
                        
                       

                        
                        
                        curs="SELECT product_name from workshop "
                        cur.execute(curs)
                        x=cur.fetchall()
                        
                        conn.commit()
                       



                       

                        abc=x
                        test_list=list(itertools.chain(*abc))

                        
                        class AutocompleteCombobox(ttk.Combobox):
           
                                   def set_completion_list(self, completion_list):
                                        """Use our completion list as our drop down selection menu, arrows move through menu."""
                                        self._completion_list = sorted(completion_list, key=str.lower) # Work with a sorted list
                                        self._hits = []
                                        self._hit_index = 0
                                        self.position = 0
                                        self.bind('<KeyRelease>', self.handle_keyrelease)
                                        self['values'] = self._completion_list# Setup our popup menu
                                       
                                        
                                        
                                   def autocomplete(self, delta=0):
                                        def productss():
                                            try:
                                                conn=psycopg2.connect('')
                                                cur=conn.cursor()
                                                cur.execute('SELECT * FROM product_details ORDER BY product_name ')
                                                data=cur.fetchall()
                                                list99=[]
                                             
                                                for row in data:
                                                  c=self.get()                          
                                                  if row[1] ==c:
                                                    list99.append(row[0])
                                                    list99.append(row[1])
                                                    list99.append(row[2])
                                                    list99.append(row[3])
                                                    
                                                def tabular0():
                                                    lbl1=Label(frame,text='PID',width=12,fg='red').grid(row=0,column=0)
                                                    lbl2=Label(frame,text='PRODUCT_NAME',width=12,fg='red').grid(row=0,column=1)
                                                    lbl3=Label(frame,text='CONDITION',width=12,fg='red').grid(row=0,column=2)
                                                    lbl4=Label(frame,text='AVAILABILITY',width=12,fg='red').grid(row=0,column=3)
                                                    r=cur.fetchall()
                                                   
                                                    for k in range(0,1000000,4):
                                                        lbl11=Label(frame,text=list99[k],width=12)
                                                        lbl12=Label(frame,text=list99[k+1],width=12)
                                                        lbl13=Label(frame,text=list99[k+2],width=12)
                                                        lbl14=Label(frame,text=list99[k+3],width=12)
                                                        lbl11.grid(row=k+1,column=0)
                                                        lbl12.grid(row=k+1,column=1)
                                                        lbl13.grid(row=k+1,column=2)
                                                        lbl14.grid(row=k+1,column=3)
                                                            
                                                def myfunction0(event):
                                                    canvas.configure(scrollregion=canvas.bbox("all"),width=400,height=200)
                                                            

                                                root1=Tk()
                                                sizex = 500
                                                sizey = 300
                                                posx  = 100
                                                posy  = 150
                                                root1.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
                                                root1.title('Check It')
                                                myframe1=Frame(root1,relief=GROOVE,width=30,height=70,bd=1)
                                                myframe1.place(x=10,y=10)

                                                canvas=Canvas(myframe1)
                                                frame=Frame(canvas)
                                                myscrollbar=Scrollbar(myframe1,orient="vertical",command=canvas.yview)
                                                canvas.configure(yscrollcommand=myscrollbar.set)

                                                myscrollbar.pack(side="right",fill="y")
                                                canvas.pack(side="left")
                                                canvas.create_window((10,10),window=frame,anchor='nw')
                                                frame.bind("<Configure>",myfunction0)
                                                tabular0()
                                                root1.mainloop()
                                            except Exception as e:
                                                print(e)
                                        
                                        """autocomplete the Combobox, delta may be 0/1/-1 to cycle through possible hits"""
                                        if delta: # need to delete selection otherwise we would fix the current position
                                                self.delete(self.position, Tkinter.END)
                                                
                                        else: # set position to end so selection starts where textentry ended
                                                self.position = len(self.get())
                                               
                                        # collect hits
                                        _hits = []
                                       
                                        for element in self._completion_list:
                                                
                                                if element.lower().startswith(self.get().lower()): # Match case insensitively
                                                        _hits.append(element)
                                                        
                                        # if we have a new hit list, keep this in mind
                                        if _hits != self._hits:
                                              
                                                self._hit_index = 0
                                                self._hits=_hits
                                                
                                        # only allow cycling if we are in a known hit list
                                        if _hits == self._hits and self._hits:
                                                self._hit_index = (self._hit_index + delta) % len(self._hits)
                                                c=self.get()
                                                
                                                for x in test_list:
                                                        if c == x:
                                                             productss()
                                                            
                                                
                                                
                                        # now finally perform the auto completion
                                        if self._hits:
                                                
                                                self.delete(0,Tkinter.END)
                                                self.insert(0,self._hits[self._hit_index])
                                                self.select_range(self.position,Tkinter.END)
                                                
                                                
                                                
                                                
                                        
                                   def handle_keyrelease(self, event):
                                        def productss():
                                            try:
                                                conn=psycopg2.connect('')         #PostgreSql Database link  
                                                cur=conn.cursor()
                                                cur.execute('SELECT * FROM product_details ORDER BY product_name ')
                                                data=cur.fetchall()
                                                list99=[]
                                             
                                                for row in data:
                                                  c=self.get()                          
                                                  if row[1] ==c:
                                                    list99.append(row[0])
                                                    list99.append(row[1])
                                                    list99.append(row[2])
                                                    list99.append(row[3])
                                                    
                                                def tabular0():
                                                    lbl1=Label(frame,text='PID',width=12,fg='red').grid(row=0,column=0)
                                                    lbl2=Label(frame,text='PRODUCT_NAME',width=12,fg='red').grid(row=0,column=1)
                                                    lbl3=Label(frame,text='CONDITION',width=12,fg='red').grid(row=0,column=2)
                                                    lbl4=Label(frame,text='AVAILABILITY',width=12,fg='red').grid(row=0,column=3)
                                                    r=cur.fetchall()
                                                    
                                                    for k in range(0,1000000,4):
                                                        lbl11=Label(frame,text=list99[k],width=12)
                                                        lbl12=Label(frame,text=list99[k+1],width=12)
                                                        lbl13=Label(frame,text=list99[k+2],width=12)
                                                        lbl14=Label(frame,text=list99[k+3],width=12)
                                                        lbl11.grid(row=k+1,column=0)
                                                        lbl12.grid(row=k+1,column=1)
                                                        lbl13.grid(row=k+1,column=2)
                                                        lbl14.grid(row=k+1,column=3)
                                                            
                                                def myfunction0(event):
                                                    canvas.configure(scrollregion=canvas.bbox("all"),width=400,height=200)
                                                            

                                                root1=Tk()
                                                sizex = 500
                                                sizey = 300
                                                posx  = 100
                                                posy  = 150
                                                root1.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
                                                root1.title('Check It')
                                                myframe1=Frame(root1,relief=GROOVE,width=30,height=70,bd=1)
                                                myframe1.place(x=10,y=10)

                                                canvas=Canvas(myframe1)
                                                frame=Frame(canvas)
                                                myscrollbar=Scrollbar(myframe1,orient="vertical",command=canvas.yview)
                                                canvas.configure(yscrollcommand=myscrollbar.set)

                                                myscrollbar.pack(side="right",fill="y")
                                                canvas.pack(side="left")
                                                canvas.create_window((10,10),window=frame,anchor='nw')
                                                frame.bind("<Configure>",myfunction0)
                                                tabular0()
                                                root1.mainloop()
                                            except Exception as e:
                                                print(e)
                                         


                                       
                                                """event handler for the keyrelease event on this widget"""
                                        
                                        if event.keysym == "BackSpace":
                                               
                                                self.delete(self.index(Tkinter.INSERT), Tkinter.END)
                                                self.position = self.index(Tkinter.END)
                                        
                                        if event.keysym == "Left":
                                                
                                                if self.position < self.index(Tkinter.END): # delete the selection
                                                        
                                                        self.delete(self.position, Tkinter.END)
                                                else:
                                                        
                                                        self.position = self.position-1 # delete one character
                                                        self.delete(self.position, Tkinter.END)
                                        if event.keysym == "Right":
                                                
                                                self.position = self.index(Tkinter.END) # go to end (no selection)
                                                
                                               
                                                c=self.get()
                                                for x in test_list:
                                                        if c == x:
                                                             productss()
                                                             
                                        
                                        def mousePressEvent():
                                                print("mouse")
                                                
                                                
                                        if len(event.keysym) == 1:
                                                
                                                self.autocomplete()
                                               
                                        
                                                
                                        # No need for up/down, we'll jump to the popup
                                        # list at the position of the autocompletion

                              

                        def test(test_list):

                                
                                
                                """Run a mini application to test the AutocompleteEntry Widget."""
                                #root = Tkinter.Tk(className='AutocompleteCombobox')

                                
                                combo = AutocompleteCombobox(frame3)
                                combo.set_completion_list(test_list)
                                
                                combo.pack()
                                combo.focus_set()
                                # I used a tiling WM with no controls, added a shortcut to quit
                                frame3.bind('<Control-Q>', lambda event=None: frame3.destroy())
                                frame3.bind('<Control-q>', lambda event=None: frame3.destroy())
                                
                               
        
                        
                        test(test_list)


                        
                        lbluser=Label(frame3,text='',bd=16,anchor='w')
                        lbluser.grid(row=2,column=3)
                        lbluser=Label(frame3,text='',bd=16,anchor='w')
                        lbluser.grid(row=3,column=3)
                        lbluser=Label(frame3,text='',bd=16,anchor='w')
                        lbluser.grid(row=4,column=3)
                        lbluser=Label(frame3,text='',bd=16,anchor='w')
                        lbluser.grid(row=3,column=4)
                        btnn=Button(frame3,padx=30,pady=10,text='CHECK',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=tab)
                        btnn.grid(row=4,column=4)
                            
                        lbluser=Label(frame3,text='',bd=16,anchor='w')
                        lbluser.grid(row=0,column=0)
                        lbluser=Label(frame3,text='',bd=16,anchor='w')
                        lbluser.grid(row=1,column=0)
                        lbluser=Label(frame3,text='',bd=16,anchor='w')
                        lbluser.grid(row=2,column=0)
                        break
                    else:
                        continue
                      
                 elif c==c2:
                   
                    if (a==id_.get() and b==passwd.get()):
                        user_store_id =id_.get()
                        user_store_password =passwd.get()
                        flag=0
                        
                        top.destroy()
                        entrytab2()
                        break 
                 else:
                    flag=1
                    
        if flag==1:
             invalid=Label(frame2,font=('arial',16),text='Invalid Credentials',bd=16,fg='red',anchor='w').grid(row=7,columnspan=5)
             
        

    except Exception as e:
        print(e)


  top=Tk()

  try:
    conn=psycopg2.connect('')
    cur=conn.cursor()

    print('Connection Sucessful')
  except:
    print("Connection failed--")




  id_=StringVar()
  user=StringVar()
  passwd=StringVar()
  top.geometry('600x600+0+0')
  top.title("Inventory Check")
  #top.iconbitmap(r'icon.ico')
  frame1=Frame(top,width=500,height=100,bg='powder blue',relief=SUNKEN)
  frame1.pack(side=TOP)
  frame2=Frame(top,width=500,height=400,relief=SUNKEN)
  frame2.pack()
  lblinfo=Label(frame1,font=('arial',23,'bold'),text="INVENTORY MANAGEMENT",fg='steel blue',bd=70,anchor='w')
  lblinfo.grid(row=0,column=0)

  lblid=Label(frame2,font=('arial',16,'italic','bold'),text='USER_ID',bd=16,anchor='w').grid(row=3,column=2)
  lblid_i=Entry(frame2,font=('Times New Roman',16),textvariable=id_,bd=5,insertwidth=4,bg='steel blue',justify='right').grid(row=3,column=3)
  lblpass=Label(frame2,font=('arial',16,'italic','bold'),text='PASSWORD',bd=16,anchor='w').grid(row=4,column=2)
  lblpass=Entry(frame2,font=('Times New Roman',16),textvariable=passwd,show='*',bd=5,insertwidth=4,bg='steel blue',justify='right').grid(row=4,column=3)

  btn=Button(frame2,padx=30,pady=10,text='Log-in',bd=3,font=('Times New Roman',15,'bold'),fg='black',command=entrytab).grid(row=6,columnspan=5)

  top.mainloop()
main_login()
