#MINI PROJECT 1


balance=0
def check_balance():
      print("Total Balance:",balance)

def deposit(amt):
      global balance
      balance=balance+amt
      print(amt,"Rs.deposit!")

def withdraw(amt):
      global balance
      balance=balance-amt
      print(amt,"Rs.withdraw!")

while True:
    ch=int(input("\n\n1.deposit \t2.withdraw \n3.check balance \n4.Exit"))
    if ch==1:
        print("code for deposit")
        d_amt=int(input("Enter Amt To Deposit:"))
        deposit(d_amt)

    elif ch==2:
         print("code for withdraw")
         w_amt=int(input("Enter Amt To Withdraw:"))
         withdraw(w_amt)

    elif ch==3:
        print("code for check Balance:")
        check_balance()

    elif ch==4:
          print("code for Exit")
          break

    else:
           print("invalid choice")
    







    
      
