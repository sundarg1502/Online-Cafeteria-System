import tkinter as tk
import pyodbc # type: ignore
import pandas as pd # type: ignore
from prettytable import PrettyTable  # type: ignore

class User:
    def __init__(self):
        self.userName = None
        self.get_RNO = None
        self.YearBranch = None
        self.PassWord = None
        self.Re_PassWord = None

    def login_details(self):
        try:
            self.reg_frame.pack_forget()
        except:
            home_frame.pack_forget()
        self.login_frame = tk.Frame(root)
        self.login_frame.pack()
        
        # RollNumber label and entry
        self.RollNumber_label = tk.Label(self.login_frame, text="RollNumber:")
        self.RollNumber_label.grid(row=0, column=0)
        self.RollNumber_entry = tk.Entry(self.login_frame)
        self.get_RNO =self.RollNumber_entry.get()
        self.RollNumber_entry.grid(row=0, column=1)

        # PassWord label and entry
        self.password_label = tk.Label(self.login_frame, text="PassWord:")
        self.password_label.grid(row=1, column=0)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.get_pass = self.password_entry.get()
        self.password_entry.grid(row=1, column=1)
        
        self.login_button = tk.Button(self.login_frame, text="Login", command=user_1.login)
        self.login_button.grid(row=3, column=1)

    def login(self):
        self.get_RNO =self.RollNumber_entry.get()
        self.get_pass = self.password_entry.get()
        self.error_label = tk.Label(self.login_frame, text="", fg="red")
        self.error_label.grid(row=4, columnspan=2)
        query = "Select * from Customers"
        df = pd.read_sql(query,conn)
        flag=0
        for index,rollno in enumerate(df['RollNo']):
            if self.get_RNO==rollno and df.iloc[index,3] ==self.get_pass :
                self.Checksts()
                flag=1
        if flag==0:
            self.error_label.config(text="Invalid username or password")

    def create_Registration(self ):
        try:
            self.HomeFrame.pack_forget()
        except:
            home_frame.pack_forget()
        # Registration page
        self.reg_frame = tk.Frame(root)
        self.reg_frame.pack()
        # Username label and entry
        self.username_label = tk.Label(self.reg_frame, text="Username:")
        self.username_label.grid(row=0, column=0)
        self.username_entry = tk.Entry(self.reg_frame)
        self.username_entry.grid(row=0, column=1)

        # Register Number Password label and entry
        self.RegNumber_label = tk.Label(self.reg_frame, text="RegisterNumber:")
        self.RegNumber_label.grid(row=1, column=0)
        self.RegNumber_label = tk.Entry(self.reg_frame)
        self.RegNumber_label.grid(row=1, column=1)

        # Department Password label and entry
        self.Department_label = tk.Label(self.reg_frame, text="Department:")
        self.Department_label.grid(row=2, column=0)
        self.Department_label = tk.Entry(self.reg_frame)
        self.Department_label.grid(row=2, column=1)

        # Renter Password label and entry
        self.password_label = tk.Label(self.reg_frame, text="Password:")
        self.password_label.grid(row=3, column=0)
        self.password_entry = tk.Entry(self.reg_frame, show="*")
        self.password_entry.grid(row=3, column=1)

        # Password label and entry
        self.re_password_label = tk.Label(self.reg_frame, text="ReEnterPass:")
        self.re_password_label.grid(row=4, column=0)
        self.re_password_entry = tk.Entry(self.reg_frame, show="*")
        self.re_password_entry.grid(row=4, column=1)

        self.reg_button =tk.Button(self.reg_frame,text="Register",command=self.Registration)
        self.reg_button.grid(row=5,column=1)
        
        self.login_reg_button =tk.Button(self.reg_frame,text="Login Back",command=self.login_details)
        self.login_reg_button.grid(row=5,column=0)
        
        # reg pass error label
        self.error_label = tk.Label(self.reg_frame, text="", fg="red")
        self.error_label.grid(row=6, columnspan=2)

    def Registration(self):
        self.userName = self.username_entry.get()
        self.PassWord = self.password_entry.get()
        self.re_pass = self.re_password_entry.get()
        self.get_RNO = self.RegNumber_label.get()
        self.Dept = self.Department_label.get()
        if self.PassWord == self.re_pass:
            #server connection
            query = "insert into Customers values(?,?,?,?)"
            parameters = self.get_RNO,self.userName,self.Dept,self.PassWord
            cursor.execute(query,parameters)
            cursor.commit()
            self.Checksts()
        else:
            self.error_label.config(text="Password and Re Entered password doesnt match")

    def Checksts(self ):
        try:
            self.reg_frame.pack_forget()
            self.login_frame.pack_forget()
        except:
            try:
                self.login_frame.pack_forget()
            except:
                pass
        self.sts_frame = tk.Frame(root)
        self.sts_frame.pack()
        self.chickenrice=5
        self.chickennoodles=5
        self.chickenbiriyani=10
        self.parotta=20
        self.chappathi=20
        self.available_label = tk.Label(self.sts_frame, text="Available Food... \n 1.chicken rice RS.80 \n 2.chicken noodles RS.100 \n 3.chicken biriyani RS.120\n 4.parotta RS.50/set\n 5.chappathi RS40/set", fg="Green")
        self.available_label.grid(row=0, columnspan=2)
        
        self.choice_label = tk.Label(self.sts_frame, text="Your Order:")
        self.choice_label.grid(row=3, column=0)
        self.choice_entry = tk.Entry(self.sts_frame)
        self.choice_entry.grid(row=3, column=1)

        self.quantity_label = tk.Label(self.sts_frame, text="Quantity:")
        self.quantity_label.grid(row=4, column=0)
        self.quantity_entry = tk.Entry(self.sts_frame)
        self.quantity_entry.grid(row=4, column=1)
        
        self.order_button = tk.Button(self.sts_frame, text="Place Order", command=user_1.makeOrder)
        self.order_button.grid(row=5, column=1)  

    def makeOrder(self, ):
        try:
            self.get_choice = self.choice_entry.get()
            self.get_quantity = int(self.quantity_entry.get())
            if self.get_choice=="chicken rice" :
                if int(self.get_quantity)<=self.chickenrice:
                    self.amount_cal()
            if self.get_choice=="chicken noodles" :
                if int(self.get_quantity)<=self.chickennoodles:
                    self.amount_cal()
            if self.get_choice=="chicken biriyani" :
                if int(self.get_quantity)<=self.chickenbiriyani:
                    self.amount_cal()
            if self.get_choice=="parotta" :
                if int(self.get_quantity)<=self.parotta:
                    self.amount_cal()
            if self.get_choice=="chappathi" :
                if int(self.get_quantity)<=self.chappathi:
                    self.amount_cal()
        except:
            insuff_error_label = tk.Label(self.sts_frame, text="UnKnown FOOD(Check Spelling)\n or \nInefficient FOOD Quantity(min 1", fg="Green")
            insuff_error_label.grid(row=6, columnspan=2)

    def amount_cal(self):
        try:
            if self.get_choice=="chicken rice" :
                self.amount = self.get_quantity*80
                self.bill() 
            elif self.get_choice == "chicken noodles":
                self.amount=self.get_quantity*80
                self.bill()
            elif self.get_choice == "chicken biriyani":
                self.amount=self.get_quantity*100
                self.bill()
            elif self.get_choice == "parotta":
                self.amount=self.get_quantity*12
                self.bill()
            elif self.get_choice == "chappathi":
                self.amount=self.get_quantity*12
                self.bill()
        except:
            insuff_error_label = tk.Label(self.sts_frame, text="UnKnown FOOD(Check Spelling)\n or \nInefficient FOOD Quantity(min 1", fg="Green")
            insuff_error_label.grid(row=6, columnspan=2)

    def bill(self):
        self.sts_frame.pack_forget()
        self.Bill_frame = tk.Frame(root)
        self.Bill_frame.pack()
        pay_label = tk.Label(self.Bill_frame,text=f"======Order Bill=====\nItem      : {self.get_choice}\nQuantity   : {self.get_quantity}\nBill     : {self.amount}\n==================")
        pay_label.grid(row =0,column = 0)

         #payment labels and entrys
        self.upi_label = tk.Label(self.Bill_frame, text="UPI Id")
        self.upi_label.grid(row=4, column=0)
        self.upi_entry = tk.Entry(self.Bill_frame)
        self.upi_entry.grid(row=4, column=1)

        self.upipass_label = tk.Label(self.Bill_frame, text="UPI Password")
        self.upipass_label.grid(row=5, column=0)
        self.upipass_entry = tk.Entry(self.Bill_frame,show="*")
        self.upipass_entry.grid(row=5, column=1)

        self.amt_label = tk.Label(self.Bill_frame, text="Pay Amount:")
        self.amt_label.grid(row=6, column=0)
        self.amt_entry = tk.Entry(self.Bill_frame)
        self.amt_entry.grid(row=6, column=1)
        paymet_button = tk.Button(self.Bill_frame,text = "Make Payment",command=self.pay)
        paymet_button.grid(row=7,column=0)

        # Update  to the Order Tabel
        self.query = "insert into OrderTable values(?,?,?,?,?)"
        self.Values =self.get_RNO,self.userName,self.get_choice,self.get_quantity,self.amount 
        cursor.execute(self.query,self.Values)
        cursor.commit()
    
    def pay(self):
        self.upi_get_entry =self.upi_entry.get()
        self.upipass_get_entry =self.upipass_entry.get()
        self.amt_get_entry = self.amt_entry.get()
        if int(self.amt_get_entry) == self.amount:
            msg_entry = tk.Label(self.Bill_frame,text = "Order Confirmd",fg= "Green")
            msg_entry.grid(row=8,columnspan=1)
        else:
            insuff_error_label = tk.Label(self.Bill_frame, text="Invalid Amount", fg="red")
            insuff_error_label.grid(row=8, columnspan=2)
        self.Return_button = tk.Button(self.Bill_frame,text = "Home",command=self.CusHome)
        self.Return_button.grid(row=9,column=0) 

    def CusHome(self, ):
        self.Bill_frame.pack_forget()
        self.HomeFrame =tk.Frame(root) 
        self.HomeFrame.pack()
        self.Home_label = tk.Label(self.HomeFrame,text=f"        Profile         \nName   :{self.userName}\nRollNumber  :{self.get_RNO}")
        self.Home_label.grid(row =0,column = 0)
        self.Homereg_button = tk.Button(self.HomeFrame,text = "Registration",command=self.create_Registration)
        self.Homereg_button.grid(row=1,column=0)
    
class Admin(User):
    def __init__(self):
        self.AdminName = "Admin"
        self.AdminPassWord = "PassWord"
    
    def Admin_login_details(self):
        home_frame.pack_forget()
        self.login_frame = tk.Frame(root)
        self.login_frame.pack()
        
        # RollNumber label and entry
        self.AName_label = tk.Label(self.login_frame, text="Name:")
        self.AName_label.grid(row=0, column=0)
        self.AName_entry = tk.Entry(self.login_frame)
        self.get_RNO =self.AName_entry.get()
        self.AName_entry.grid(row=0, column=1)

        # PassWord label and entry
        self.password_label = tk.Label(self.login_frame, text="PassWord:")
        self.password_label.grid(row=1, column=0)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.get_pass = self.password_entry.get()
        self.password_entry.grid(row=1, column=1)
        
        self.login_button = tk.Button(self.login_frame, text="Login", command=Admin_1.Admin_login)
        self.login_button.grid(row=3, column=1)

    def Admin_login(self):
        self.get_ANAme =self.AName_entry.get()
        self.get_pass = self.password_entry.get()
        self.error_label = tk.Label(self.login_frame, text="", fg="red")
        self.error_label.grid(row=4, columnspan=2)
        if self.get_ANAme=='Admin' and self.get_pass=='1':
            self.AdminView()
        else:
            self.error_label.config(text="Invalid username or password")
    
    def AdminView(self):
        self.login_frame.pack_forget()
        self.ViweFrame = tk.Frame(root)
        self.ViweFrame.pack()
        self.WelLabel = tk.Label(self.ViweFrame,text='Welcome Admin')
        self.WelLabel.grid(row=0,column=0)

        self.Cus_button = tk.Button(self.ViweFrame, text="View Customers", command=Admin_1.CusDetails)
        self.Cus_button.grid(row=1, column=0)

        self.Order_button = tk.Button(self.ViweFrame, text="View Order Details", command=Admin_1.OrderDetails)
        self.Order_button.grid(row=2, column=0)

    def CusDetails(self):
        self.ViweFrame.pack_forget()
        self.CusDetailsFrame = tk.Frame(root)
        self.CusDetailsFrame.pack()
        text = tk.Text(self.CusDetailsFrame)

        table = PrettyTable()

        table.field_names = ["Roll No","Name","Department"]
        for i in cursor.execute("select RollNo,Name,YearBranch from Customers"):
            print(i)
            table.add_row(i)

        text.insert(tk.INSERT,table)
        text.grid(row=0,column=0)
        
    def OrderDetails(self):
        self.ViweFrame.pack_forget()
        self.OrderDetailsFrame = tk.Frame(root)
        self.OrderDetailsFrame.pack()
        text = tk.Text(self.OrderDetailsFrame)

        table = PrettyTable()

        table.field_names = ["Roll No","Name","Item Purchase","Quantity","Total Amount"]
        for i in cursor.execute("select * from OrderTable"):
            print(i)
            table.add_row(i)

        text.insert(tk.INSERT,table)
        text.grid(row=0,column=0)

user_1=User()
Admin_1 = Admin()
# Create main window
root = tk.Tk()
root.title("Online Cafeteria System")
root.geometry('500x400')
# Home Page Frame
home_frame = tk.Frame(root)
home_frame.pack()
home_label = tk.Label(home_frame,text='Welcome To college Cafeteria ')
home_label.grid(row=0,column=0)
 
home_label = tk.Label(home_frame,text='Available Foods  \n 1->          chickenrice\n 2-> chickennoodles\n 3-> chickenbiriyani\n 4->                parotta\n 5->            chappathi\n ')
home_label.grid(row=1,column=0)

home_login_button = tk.Button( home_frame,text = "Login",command=user_1.login_details)
home_login_button.grid(row=2,column=0)

home_reg_button = tk.Button( home_frame,text = "Register",command=user_1.create_Registration)
home_reg_button.grid(row=3,column=1)

home_Admin_button = tk.Button( home_frame,text = "Admin",command=Admin_1.Admin_login_details)
home_Admin_button.grid(row=4,column=0)

# DAtaBase connection'
conn_str = ( "Driver={ODBC Driver 17 for SQL Server};"+
             "Server=SJ\SQLEXPRESS;"+
             "Database=Cafeteria;"+
             "Trusted_connection=yes;")
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

root.mainloop()