
Balance=0.0

def Menu():
 global Balance
 print("\n\nPlease select an option:")
 option1="Enter 1 to Deposit"
 option2="Enter 2 to Withdraw"
 option3="Enter 3 to Exit"

 print(option1)
 print(option2)
 print(option3)
 print("Your current balance is {:.2f} \n\n".format(Balance))

 
 option=int(input("Enter number: "))

 if option==1:
    Deposit()      
 if option==2:
    Withdraw()
 if option==3:
    print("Thank you for using this ATM, you have successfully logged out")

 
    
#deposit function
def Deposit():
 global Balance   
 depositAmount=float(input("Enter Deposit Amount: "))
 #pass to the function
 validate=CheckDeposit(depositAmount)
 if validate==True:
   Balance+=depositAmount
   print("\n Succesfully deposited!")
   print("\n Your updated balance: ${:.2f}".format(Balance))
   Menu()

#check deposit function
def CheckDeposit(depAmount):
    if (depAmount<20 or depAmount>200):
        print("error,invalid deposit amount!")
        Menu()
        return False

    else:
        return True

    
#check withdraw function
def CheckWithdrawal(drawedAmount):
    global Balance
    if (drawedAmount<20 or drawedAmount>Balance):
     print("error invalid withdrawal amount!")
     Menu()
     return False
     
    else:
     return True

    
#withdraw function
def Withdraw():
 global Balance
 drawAmount=float(input("Enter withdrawal amount:"))

 #pass to the function to check valid or not
 validDraw=CheckWithdrawal(drawAmount)
 if validDraw==True:
     Balance-=drawAmount
     print("\n Succesfully withdrawn!")
     print("\n Updated balance is: {:.2f}".format(Balance))
     Menu()

                  
Menu()
