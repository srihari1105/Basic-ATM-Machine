import locale

# Set locale to Indian format
locale.setlocale(locale.LC_ALL, 'en_IN')

a=""" --------Please Select Your Option----------
            1--->Deposit Amount
            2--->Withdraw Amount
            3--->Balance Enquiry
            4--->exit
--------------------------------------------"""
users={"srihari":"1234","vamsi":"2005"}
amount={"srihari":1000,"vamsi":1000}

def login():
    if user_id in users and users[user_id]==Password:
        print("Login Success...")
        print(" ")
        return 1
    else:
        print("login failed. TRY AGAIN!!")
        print(" ")
        return 0

def credit():
    print("ONE TIME LIMIT---->₹1,00,000/- ONLY")
    temp=int(input("Enter your amount to Deposit:₹"))
    if temp<1000000:
        temp1=locale.format_string("%d", temp, grouping=True)
        print(f"₹ {temp1} Deposited Successfully...")
        print(" ")
        amount[user_id]+=temp
    else:
        print("LIMIT EXCEEDED...")
        print("-"*7,"TRY AGAIN","-"*7)
        print(" ")

def debit():
    print("ONE TIME LIMIT---->₹10,000/- ONLY")
    print("Enter Multiples of 100 Only")
    temp=int(input("Enter amount to Withdraw:₹"))
    if temp<1000000:
        if temp%100==0:
            if temp<=amount[user_id]:
                amount[user_id]-=temp
                temp1=locale.format_string("%d", temp, grouping=True)
                print(f"₹ {temp1} Withdrawl Successfully...")
                print(" ")
            else:
                print("Insufficient Balance")
                print("Try Again")
                print(" ")
                print(" ")
        else:
            print("ONLY MULTIPLES OF 100 ACCEPTED")
            print("-"*7,"TRY AGAIN","-"*7)
            print(" ")
    else:
        print("LIMIT EXCEEDED...")
        print("-"*7,"TRY AGAIN","-"*7)
        print(" ")


def display():
    x=locale.format_string("%d", amount[user_id], grouping=True)
    print("Your balance amount is ₹",x)
    print(" ")
    print(" ")

def exit():
    while True:
        print("Thanks for Visiting")
        print("Come Again...")
        print("-"*50)
        print(" ")
        break

def temp_disp():

    temp=int(input("Press 1 to Show balance else press 2:"))
    if temp==1:
        display()
    else:
        print(" ")

#main func

user_id= (input("Enter your name:").lower()).strip()
Password=input("Enter pin:")

if login()==1:
    while True:
        while True:
            print(a)
            print(" ")
            value=(input("Enter your option:"))
            if value=="1":
                credit()
                temp_disp()
            elif value=="2":
                debit()
                temp_disp()
            elif value=="3":
                display()
            else:
                break
        if value=="4":
            exit()
        else:
            print("You Entered wrong input...")
        break