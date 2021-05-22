from tkinter import *
import math,random
from tkinter import messagebox as m
import os
from datetime import date
import datetime as dt
import time
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+60+40")
        self.root.title('Billing software')
        self.root.resizable(False, False)
        bgc='#539CFF'
        title=Label(self.root,text="BILLING SOFTWARE",font=("times new roman",30,"bold"),bd=15,fg="white",relief=GROOVE,bg="#539CFF")
        title.pack(fill=X)
        #name bill pno variable
        self.cname=StringVar()
        self.billno=StringVar()
        self.s=random.randint(1000,9999)
        self.billno.set(str(self.s))
        self.cpno=StringVar()
        self.t=StringVar()

        #FRAME [CUSTOMER DETAIL FRAME]
        f1=LabelFrame(self.root,text="Customer Details",font=("times new roman",20,"bold"),bg=bgc)
        f1.place(x=0,y=80,relwidth=1)

        self.cnamel=Label(f1,text="Customer Name",font=("times new roman",17,"bold"),bg=bgc,fg="white").grid(row=0,column=0,padx=7,pady=5)
        self.cnamee=Entry(f1,width=15,textvariable=self.cname,font=("arial",15,"")).grid(row=0,column=1,padx=5,pady=5)

        self.cpnol=Label(f1,text="Customer Phone No.",font=("times new roman",17,"bold"),bg=bgc,fg="white").grid(row=0,column=2,padx=7,pady=5)
        self.cpnoe=Entry(f1,width=15,textvariable=self.cpno,font=("arial",15,"")).grid(row=0,column=3,padx=5,pady=5)

        #self.cbilll=Label(f1,text="Customer Bill no",font=("times new roman",17,"bold"),bg=bgc,fg="white").grid(row=0,column=4,padx=7,pady=5)
        #self.cbille=Entry(f1,width=12,font=("arial",15,"")).grid(row=0,column=5,padx=2,pady=5)
        #print(self.s)
        #self.cbille.insert(0,self.s)
        #self.cbille.configure(state='disabled')
        self.ctime=Label(f1,text=f'{dt.datetime.now():%a, %b %d %Y}',font=("times new roman",17,"bold"),bg=bgc,fg="white").grid(row=0,column=6,padx=300,pady=5)


        
        #Cosmetics variable
        self.cos=[]
        for _ in range(0,6):
            i=IntVar()
            i.set(0)
            self.cos.append(i)
        self.a=["Bath Soap","Face cream","Shampoo","Comb","Perfume","Oil"]

        #Cosmetics Frame
        f2=LabelFrame(self.root,text="Cosmatics",font=("times new roman",20,"bold"),bg=bgc)
        f2.place(x=0,y=156,width=325,height=380)

        self.bathl=Label(f2,text=self.a[0],font=("times new roman",17,"bold"),bg=bgc,fg='white').grid(row=0,column=0,padx=10,pady=10,sticky='e')
        self.bathe=Entry(f2,width=12,textvariable=self.cos[0],font=("times new roman",17,"bold"),bd=0).grid(row=0,column=1,padx=10,pady=10)
        
        self.facel=Label(f2,text=self.a[1],font=("times new roman",17,"bold"),bg=bgc,fg='white').grid(row=1,column=0,padx=10,pady=10,sticky='e')
        self.facee=Entry(f2,width=12,textvariable=self.cos[1],font=("times new roman",17,"bold"),bd=0).grid(row=1,column=1,padx=10,pady=10)

        self.shl=Label(f2,text=self.a[2],font=("times new roman",17,"bold"),bg=bgc,fg='white').grid(row=2,column=0,padx=10,pady=10,sticky='e')
        self.she=Entry(f2,width=12,textvariable=self.cos[2],font=("times new roman",17,"bold"),bd=0).grid(row=2,column=1,padx=10,pady=10)

        self.cl=Label(f2,text=self.a[3],font=("times new roman",17,"bold"),bg=bgc,fg='white').grid(row=3,column=0,padx=10,pady=10,sticky='e')
        self.ce=Entry(f2,width=12,textvariable=self.cos[3],font=("times new roman",17,"bold"),bd=0).grid(row=3,column=1,padx=10,pady=10)

        self.perl=Label(f2,text=self.a[4],font=("times new roman",17,"bold"),bg=bgc,fg='white').grid(row=4,column=0,padx=10,pady=10,sticky='e')
        self.pere=Entry(f2,width=12,textvariable=self.cos[4],font=("times new roman",17,"bold"),bd=0).grid(row=4,column=1,padx=10,pady=10)

        self.oill=Label(f2,text=self.a[5],font=("times new roman",17,"bold"),bg=bgc,fg='white').grid(row=5,column=0,padx=10,pady=10,sticky='e')
        self.oile=Entry(f2,width=12,textvariable=self.cos[5],font=("times new roman",17,"bold"),bd=0).grid(row=5,column=1,padx=10,pady=10)


        #Cold drinks variables
        self.cold=[]
        for _ in range(0,6):
            i=IntVar()
            i.set(0)
            self.cold.append(i)
        self.b=["Coke","Pepsi","Fanta","Miranda","Red bull","Soda"]

        #Cold drinks
        f3=LabelFrame(self.root,text="Cold drinks",font=("times new roman",20,"bold"),bg=bgc)
        f3.place(x=325,y=156,width=325,height=380)

        self.cokel=Label(f3,text=self.b[0],font=("times new roman",17,"bold"),bg=bgc,fg='white').grid(row=0,column=0,padx=10,pady=10,sticky='e')
        self.cokee=Entry(f3,width=12,textvariable=self.cold[0],font=("times new roman",17,"bold"),bd=0).grid(row=0,column=1,padx=10,pady=10)
        
        self.pepl=Label(f3,text=self.b[1],font=("times new roman",17,"bold"),bg=bgc,fg='white').grid(row=1,column=0,padx=10,pady=10,sticky='e')
        self.pepe=Entry(f3,width=12,textvariable=self.cold[1],font=("times new roman",17,"bold"),bd=0).grid(row=1,column=1,padx=10,pady=10)

        self.fanl=Label(f3,text=self.b[2],font=("times new roman",17,"bold"),bg=bgc,fg='white').grid(row=2,column=0,padx=10,pady=10,sticky='e')
        self.fane=Entry(f3,width=12,textvariable=self.cold[2],font=("times new roman",17,"bold"),bd=0).grid(row=2,column=1,padx=10,pady=10)

        self.mirl=Label(f3,text=self.b[3],font=("times new roman",17,"bold"),bg=bgc,fg='white').grid(row=3,column=0,padx=10,pady=10,sticky='e')
        self.mire=Entry(f3,width=12,textvariable=self.cold[3],font=("times new roman",17,"bold"),bd=0).grid(row=3,column=1,padx=10,pady=10)

        self.rbl=Label(f3,text=self.b[4],font=("times new roman",17,"bold"),bg=bgc,fg='white').grid(row=4,column=0,padx=10,pady=10,sticky='e')
        self.rbe=Entry(f3,width=12,textvariable=self.cold[4],font=("times new roman",17,"bold"),bd=0).grid(row=4,column=1,padx=10,pady=10)

        self.sl=Label(f3,text=self.b[5],font=("times new roman",17,"bold"),bg=bgc,fg='white').grid(row=5,column=0,padx=10,pady=10,sticky='e')
        self.se=Entry(f3,width=12,textvariable=self.cold[5],font=("times new roman",17,"bold"),bd=0).grid(row=5,column=1,padx=10,pady=10)

        #Chips
        self.chip=[]
        for _ in range(0,6):
            i=IntVar()
            i.set(0)
            self.chip.append(i)
        self.c=["Lays","Kurkure","Cheetos","Little\nHearts","Bingo","Dorito"]

        #Chips
        f4=LabelFrame(self.root,text="Chips",font=("times new roman",20,"bold"),bg=bgc)
        f4.place(x=650,y=156,width=325,height=380)

        self.layl=Label(f4,text=self.c[0],font=("times new roman",17,"bold"),bg=bgc,fg='white').grid(row=0,column=0,padx=10,pady=10,sticky='e')
        self.laye=Entry(f4,width=12,textvariable=self.chip[0],font=("times new roman",17,"bold"),bd=0).grid(row=0,column=1,padx=10,pady=10)
        
        self.kurl=Label(f4,text=self.c[1],font=("times new roman",17,"bold"),bg=bgc,fg='white').grid(row=1,column=0,padx=10,pady=10,sticky='e')
        self.kure=Entry(f4,width=12,textvariable=self.chip[1],font=("times new roman",17,"bold"),bd=0).grid(row=1,column=1,padx=10,pady=10)

        self.chl=Label(f4,text=self.c[2],font=("times new roman",17,"bold"),bg=bgc,fg='white').grid(row=2,column=0,padx=10,pady=10,sticky='e')
        self.che=Entry(f4,width=12,textvariable=self.chip[2],font=("times new roman",17,"bold"),bd=0).grid(row=2,column=1,padx=10,pady=10)

        self.lhl=Label(f4,text=self.c[3],font=("times new roman",17,"bold"),bg=bgc,fg='white').grid(row=3,column=0,padx=10,pady=10,sticky='e')
        self.lhe=Entry(f4,width=12,textvariable=self.chip[3],font=("times new roman",17,"bold"),bd=0).grid(row=3,column=1,padx=10,pady=10)

        self.bl=Label(f4,text=self.c[4],font=("times new roman",17,"bold"),bg=bgc,fg='white').grid(row=4,column=0,padx=10,pady=10,sticky='e')
        self.be=Entry(f4,width=12,textvariable=self.chip[4],font=("times new roman",17,"bold"),bd=0).grid(row=4,column=1,padx=10,pady=10)

        self.dl=Label(f4,text=self.c[5],font=("times new roman",17,"bold"),bg=bgc,fg='white').grid(row=5,column=0,padx=10,pady=10,sticky='e')
        self.de=Entry(f4,width=12,textvariable=self.chip[5],font=("times new roman",17,"bold"),bd=0).grid(row=5,column=1,padx=10,pady=10)

        #BILL AREA
        f5=Frame(self.root,bd=2,relief=GROOVE,bg=bgc)
        f5.place(x=975,y=156,width=380,height=380)
        bt=Label(f5,text="Bill Area",font='arial 17 bold',bg=bgc,fg='white').pack(fill=X)
        scroly=Scrollbar(f5,orient=VERTICAL)
        self.textarea=Text(f5,yscrollcommand=scroly.set)
        scroly.pack(fill=Y,side=RIGHT)
        scroly.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #total and tax
        self.cop=StringVar()
        self.clp=StringVar()
        self.chp=StringVar()
        self.cot=StringVar()
        self.clt=StringVar()
        self.cht=StringVar()
        self.ct=StringVar()
        self.cp=StringVar()

        #BUTTON FRAME
        f6=LabelFrame(self.root,bd=2,relief=GROOVE,bg=bgc,text='Bill Menu',font=("times new roman",20,"bold"))
        f6.place(x=0,y=535,relwidth=1,height=165)

        self.m11=Label(f6,text='Total Comestic Price',font=("times new roman",14,"bold"),bg=bgc,fg='white').grid(row=0,column=0,padx=18,pady=2,sticky='e')
        self.m1e=Entry(f6,font=("times new roman",10,"bold"),state='disabled',textvariable=self.cop,width=18,bd=2,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=2)

        self.m21=Label(f6,text='Total Cold drinks Price',font=("times new roman",14,"bold"),bg=bgc,fg='white').grid(row=1,column=0,padx=18,pady=2,sticky='e')
        self.m2e=Entry(f6,font=("times new roman",10,"bold"),state='disabled',textvariable=self.clp,width=18,bd=2,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=2)

        self.m31=Label(f6,text='Total Chips Price',font=("times new roman",14,"bold"),bg=bgc,fg='white').grid(row=2,column=0,padx=18,pady=2,sticky='e')
        self.m3e=Entry(f6,font=("times new roman",10,"bold"),textvariable=self.chp,state='disabled',width=18,bd=2,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=2)

        self.mtl=Label(f6,text='Total Price',font=("times new roman",14,"bold"),bg=bgc,fg='white').grid(row=3,column=0,padx=18,pady=2,sticky='e')
        self.mte=Entry(f6,font=("times new roman",10,"bold"),textvariable=self.cp,width=18,bd=2,state='disabled',relief=SUNKEN).grid(row=3,column=1,padx=10,pady=2)

        self.c11=Label(f6,text='Comestic Tax',font=("times new roman",14,"bold"),bg=bgc,fg='white').grid(row=0,column=2,padx=18,pady=2,sticky='e')
        self.c1e=Entry(f6,font=("times new roman",10,"bold"),textvariable=self.cot,width=18,bd=2,state='disabled',relief=SUNKEN).grid(row=0,column=3,padx=10,pady=2)

        self.c21=Label(f6,text='Cold drinks Tax',font=("times new roman",14,"bold"),bg=bgc,fg='white').grid(row=1,column=2,padx=18,pady=2,sticky='e')
        self.c2e=Entry(f6,font=("times new roman",10,"bold"),textvariable=self.clt,width=18,bd=2,state='disabled',relief=SUNKEN).grid(row=1,column=3,padx=10,pady=2)

        self.c31=Label(f6,text='Chips Tax',font=("times new roman",14,"bold"),bg=bgc,fg='white').grid(row=2,column=2,padx=18,pady=2,sticky='e')
        self.c3e=Entry(f6,font=("times new roman",10,"bold"),textvariable=self.cht,width=18,bd=2,state='disabled',relief=SUNKEN).grid(row=2,column=3,padx=10,pady=2)

        self.ctl=Label(f6,text='Total Tax',font=("times new roman",14,"bold"),bg=bgc,fg='white').grid(row=3,column=2,padx=18,pady=2,sticky='e')
        self.cte=Entry(f6,font=("times new roman",10,"bold"),textvariable=self.ct,width=18,bd=2,state='disabled',relief=SUNKEN).grid(row=3,column=3,padx=10,pady=2)

        btnf=Frame(f6,bd=2,relief=GROOVE)
        btnf.place(x=750,width=580,height=80)

        tbtn=Button(btnf,command=self.total,text='Total',pady=15,width=11,bg=bgc,fg='white',font=("",10,"bold")).grid(row=0,column=0,padx=5,pady=10)
        gbtn=Button(btnf,text='Genrate Bill',command=self.bill_area,pady=15,width=11,bg=bgc,fg='white',font=("",10,"bold")).grid(row=0,column=1,padx=5,pady=10)
        clbtn=Button(btnf,text='Clear',command=self.clear_btn,pady=15,width=11,bg=bgc,fg='white',font=("",10,"bold")).grid(row=0,column=2,padx=5,pady=10)
        exbtn=Button(btnf,text='Exit',pady=15,width=11,bg=bgc,fg='white',font=("",10,"bold")).grid(row=0,column=3,padx=5,pady=10)
        self.welcome_bill()
        #abl=Label(f6,text="Developed by VK",font=("",20,""),bg=bgc,fg='white').place(x=750,y=85,sticky='e')
    def total(self):
        #total price variables
        self.cosp=[30,100,120,200,10,10]
        self.coldp=[20,30,15,20,100,40]
        self.chipp=[20,10,5,5,10,60]
        #calculation
        self.to=float((self.cos[0].get()*30)+(self.cos[1].get()*100)+(self.cos[2].get()*120)+(self.cos[3].get()*200)+(self.cos[4].get()*10)+(self.cos[5].get()*10))
        self.cop.set(str(self.to))
        self.tc=float((self.cold[0].get()*20)+(self.cold[1].get()*30)+(self.cold[2].get()*15)+(self.cold[3].get()*20)+(self.cold[4].get()*100)+(self.cold[5].get()*40))
        self.clp.set(str(self.tc))
        self.th=float((self.chip[0].get()*20)+(self.chip[1].get()*10)+(self.chip[2].get()*5)+(self.chip[3].get()*5)+(self.chip[4].get()*10)+(self.chip[5].get()*60))
        self.chp.set(str(self.th))
        self.cp.set(str(round((self.to+self.tc+self.th),2)))
        self.tx=round(self.to*0.28,2)
        self.ty=round(self.tc*0.18,2)
        self.tz=round(self.th*0.05,2)
        self.cot.set(str(self.tx))
        self.clt.set(str(self.ty))
        self.cht.set(str(self.tz))
        self.ct.set(str(round((self.tx+self.ty+self.tz),2)))
        self.t.set(str(round((self.to+self.tc+self.th+self.ty+self.tx+self.tz),2)))

    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t   Welcome VK Supermarket")
        self.textarea.insert(END,f"\nBill Number:{self.billno.get()}")
        self.textarea.insert(END,f"\nCustomer Name:{self.cname.get()}")
        self.textarea.insert(END,f"\nPhone Number: {self.cpno.get()}")
        self.textarea.insert(END,"\n============================================\n")
        self.textarea.insert(END,"Products		    QTY               Price")
        self.textarea.insert(END,"\n============================================\n")
        
    def bill_area(self):
        f=0
        self.welcome_bill()
        if self.cname.get()=='' or self.cpno.get()=='':
            m.showerror('Error','Enter the Customer details')
            return
        if self.cp.get()=='':
            m.showerror('Error','No product entered or click total and try again')
            return
        for i in range(0,6):
            if (self.cos[i].get()!=0):
                f=1
                self.textarea.insert(END,f"\n{self.a[i]}		     {self.cos[i].get()}                {(self.cos[i].get()*self.cosp[i])}")
            if (self.cold[i].get()!=0):
                f=1
                self.textarea.insert(END,f"\n{self.b[i]}		     {self.cold[i].get()}                {(self.cold[i].get()*self.coldp[i])}")
            if (self.chip[i].get()!=0):
                f=1
                self.textarea.insert(END,f"\n{self.c[i]}	   	     {self.chip[i].get()}                {(self.chip[i].get()*self.chipp[i])}")
        
        if f==1:
            self.textarea.insert(END,'\n--------------------------------------------')
            self.textarea.insert(END,f"                                Total {self.cp.get()}\n")
            self.textarea.insert(END,f"                                Tax  {self.ct.get()}\n")
            self.textarea.insert(END,'\n--------------------------------------------')
            self.textarea.insert(END,f"\n                Total Amount        {self.t.get()}\n")
            self.textarea.insert(END,'\n--------------------------------------------')
        self.savebill()
        self.clear_btn()
    def savebill(self):
        q=m.askyesno('Save Bill','Do you want to save bill?')
        if q!=0:
            try:
                z=str(date.today())
                o=str(self.s)+" "+z
                f=open("BILLS/"+o+'.txt','w')
                self.bill_d=self.textarea.get('1.0',END)
                f.write(self.bill_d)
                f.close()
                m.showinfo("Bill saved",'The bill saved succesfully')
            except():
                m.showerror("Error","Sorry and error occured try again")
        else:
            return




    def clear_btn(self):
        self.cname.set('')
        self.billno.set('')
        self.cpno.set('')
        self.t.set('')
        self.cop.set('')
        self.clp.set('')
        self.chp.set('')
        self.cot.set('')
        self.clt.set('')
        self.cht.set('')
        self.ct.set('')
        self.cp.set('')
        for i in range(0,6):
            self.chip[i].set(0)
            self.cold[i].set(0)
            self.cos[i].set(0)
        self.welcome_bill()
            

        
        

root=Tk()
obj=Bill_App(root)
root.mainloop()
