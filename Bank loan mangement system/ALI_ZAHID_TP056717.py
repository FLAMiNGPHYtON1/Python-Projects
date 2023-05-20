# ALI_ZAHID
# TP056717


# This function is responsible for checking the inputted User_Name and User_Password variables to see if it is equal to the data present in the system
# If they are equal, user is allowed to login into the system, if it is not, they receive an error message.
def Reg_Cus_Login(User_Name, User_Password):
    with open("Customer_Account.txt", "r") as Reg_Cus_login_txt:
        for line in Reg_Cus_login_txt:
            Cus_login_detail_list = line.split(",")
            if User_Name == Cus_login_detail_list[1]:
                if User_Password == Cus_login_detail_list[2]:
                    Answer = "Yes"
                    break
                else:
                    Answer = "No"
            else:
                Answer = "No"
    with open("Registered_Customer.txt", "r") as Approved_Or_Not_Txt:
        for line in Approved_Or_Not_Txt:
            Reg_Cus_List = line.split(",")
            if User_Name == Reg_Cus_List[0]:
                Answer1 = "Yes"
                break
            else:
                Answer1 = "No"
    if Answer == "Yes" and Answer1 == "Yes":
        return "Yes"
    elif Answer == "Yes" and Answer1 == "No":
        return "Not Approved"
    else:
        return "No"

# This function is responsible for checking the inputted User_Name and User_Password variables to see if
# it is equal to the data present in the system If they are equal, the user logged into the system as an admin,
# and is allowed access to several options in the system unique to the admin.
def Admin_Login(User_Name, User_Password):
    with open("Admin_User.txt", "r") as Admin_login_txt:
        for line in Admin_login_txt:
            Admin_login_detail_list = line.split(",")
            if User_Name == Admin_login_detail_list[0]:
                if User_Password == Admin_login_detail_list[1]:
                    return "Yes"
                else:
                    return "No"
            else:
                return "No"

# This function is responsible for automatically calculating when is the next installment date of a loan after it is paid by taking in the current due date of the loan
def Automatic_Installment_Date_Calculator(Source_Date):
    from dateutil.relativedelta import relativedelta
    Next_Installment_Date = Source_Date + relativedelta(months=+1)
    Next_Installment_Date = Next_Installment_Date.strftime("%d/%m/%Y")
    return Next_Installment_Date

# This function takes in multiple values from the user and outputs monthly installment amount and total amount paid back to the bank including interest accured.
def Loan_Calculator():
    BreakCondition = False
    while True:
        if BreakCondition:
            break
        else:
            while True:
                try:
                    print("")
                    print("==================================================================")
                    Loan_Amount = float(input("Enter the amount of money you wish to borrow:- "))
                    print("==================================================================")
                except ValueError:
                    print("")
                    print("------------------------------------------------------------------")
                    print("Please only enter numbers!")
                    print("------------------------------------------------------------------")
                else:
                    if Loan_Amount <= 0:
                        print("")
                        print("------------------------------------------------------------------")
                        print("You cannot enter a loan amount less than or equal to 0")
                        print("------------------------------------------------------------------")
                    else:
                        break
            while True:
                try:
                    print("")
                    print("==================================================================")
                    Loan_Interest = float(input("Enter the annual interest rate for this loan:- "))
                    print("==================================================================")
                except ValueError:
                    print("")
                    print("------------------------------------------------------------------")
                    print("Please only enter numbers!")
                    print("------------------------------------------------------------------")
                else:
                    if Loan_Interest <= 0:
                        print("")
                        print("------------------------------------------------------------------")
                        print("You cannot enter a interest rate less than or equal to 0")
                        print("------------------------------------------------------------------")
                    else:
                        Loan_Interest = Loan_Interest / 100
                        break
            while True:
                try:
                    print("")
                    print("==================================================================")
                    Loan_Term = int(input("How many years do you wish to borrow this loan for?:- "))
                    print("==================================================================")
                except ValueError:
                    print("")
                    print("------------------------------------------------------------------")
                    print("Please only enter numbers!")
                    print("------------------------------------------------------------------")
                else:
                    if Loan_Term <= 0:
                        print("")
                        print("------------------------------------------------------------------")
                        print("You cannot enter a loan term less than or equal to 0")
                        print("------------------------------------------------------------------")
                    else:
                        break
            MonthlyInstallments = ((Loan_Term * Loan_Amount * Loan_Interest) + Loan_Amount) / (Loan_Term * 12)
            MonthlyInstallments = round(MonthlyInstallments, 2)
            TotalRepayments = ((Loan_Term * Loan_Amount * Loan_Interest) + Loan_Amount)
            TotalRepayments = round(TotalRepayments, 2)
            print("")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("The monthly installments you have to pay for this loan are:-", "RM", MonthlyInstallments)
            print("The total amount you pay at the completion of this loan is:-", "RM", TotalRepayments)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("")
            while True:
                print("")
                print("==================================================================")
                print("Do you wish to recalculate or return to the previous menu?")
                print("==================================================================")
                print("1. Recalculate")
                print("2. Return to previous menu?")
                print("==================================================================")
                Answer = input("Enter choice here:- ")
                if Answer == "1":
                    break
                elif Answer == "2":
                    BreakCondition = True
                    break
                else:
                    print("")
                    print("------------------------------------------------------------------")
                    print("You have entered an invalid answer, please try again")
                    print("------------------------------------------------------------------")

# This function allows a user to become a registered customer in the system by providing several unique details
def Registration():
    import os
    import re
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You can enter 'Exit' anytime to cancel the registration process and go back to the New Customer menu")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    while True:
        print("==================================================================")
        New_Customer_ID = input("Please enter your desired Account Name:- ")
        print("==================================================================")
        with open("Customer_Account.txt") as Duplicate_checking:
            for line in Duplicate_checking:
                ID_List = line.split(",")
                if New_Customer_ID == ID_List[1]:
                    No_Duplicates = False
                    break
                else:
                    No_Duplicates = True
            if No_Duplicates:
                if New_Customer_ID == 'Exit':
                    return
                else:
                    x = re.fullmatch(r"^\S+$", New_Customer_ID)
                    if not x:
                        print("")
                        print("------------------------------------------------------------------")
                        print("You have entered an invalid Account name, please try again")
                        print("------------------------------------------------------------------")
                        print("")
                    else:
                        break
            else:
                print("------------------------------------------------------------------")
                print("this account name is already taken, please try again")
                print("------------------------------------------------------------------")
    while True:
        print("")
        print("==================================================================")
        New_Customer_Password = input("Please enter your desired password:- ")
        print("==================================================================")
        if New_Customer_Password == 'Exit':
            return
        else:
            x = re.fullmatch(r"^\S+$", New_Customer_Password)
            if not x:
                print("")
                print("------------------------------------------------------------------")
                print("You have entered an invalid Account password, please try again")
                print("------------------------------------------------------------------")
                print("")
            else:
                break
    while True:
        print("")
        print("==================================================================")
        New_Customer_Name = input("Please enter your name in this format, FirstName_LastName:- ")
        print("==================================================================")
        if New_Customer_Name == 'Exit':
            return
        else:
            import re
            x = re.fullmatch(r"^[a-zA-Z]+_[a-zA-Z]+$", New_Customer_Name)
            if not x:
                print("")
                print("------------------------------------------------------------------")
                print("You have entered an invalid name, please try again")
                print("------------------------------------------------------------------")
                print("")
            else:
                break
    while True:
        print("")
        print("==================================================================")
        New_Customer_Email_Address = input("Please enter your email address:- ")
        print("==================================================================")
        with open("New_Customer.txt") as Duplicate_checking:
            for line in Duplicate_checking:
                Email_Address_List = line.split(",")
                if New_Customer_Email_Address == Email_Address_List[1]:
                    No_Duplicates = False
                    break
                else:
                    No_Duplicates = True
        if No_Duplicates:
            if New_Customer_Email_Address == 'Exit':
                return
            else:
                x = re.search(r"^\S*@gmail.com$|^\S*@yahoo.com$|^\S*@outlook.com$|^\S*@hotmail.com$",
                              New_Customer_Email_Address)
                if not x:
                    print("")
                    print("------------------------------------------------------------------")
                    print("You have entered an invalid email address, please try again")
                    print("------------------------------------------------------------------")
                    print("")
                else:
                    break
        else:
            print("------------------------------------------------------------------")
            print("this email address is already taken, please try again!")
            print("------------------------------------------------------------------")
    while True:
        print("")
        print("==================================================================")
        New_Customer_Contact_Number = input("Please enter your primary phone number in this format, 011-xxxxxxxx:- ")
        print("==================================================================")
        if New_Customer_Contact_Number == "Exit":
            return
        else:
            import re
            x = re.search(r"^011-\d{8}$", New_Customer_Contact_Number)
            if not x:
                print("")
                print("------------------------------------------------------------------")
                print("You have entered an invalid contact number, please try again")
                print("------------------------------------------------------------------")
                print("")
            else:
                break
    while True:
        print("")
        print("==================================================================")
        New_Customer_Date_of_Birth = input("Please enter your Date of birth in this format, DD/MM/YYYY:- ")
        print("==================================================================")
        if New_Customer_Date_of_Birth == 'Exit':
            break
        else:
            try:
                from datetime import datetime
                Date_of_Birth = datetime.strptime(New_Customer_Date_of_Birth, '%d/%m/%Y').date()
                New_Customer_Date_of_Birth = Date_of_Birth.strftime('%d/%m/%Y')
            except ValueError:
                print("")
                print("------------------------------------------------------------------")
                print("You have entered an invalid date of birth, please try again")
                print("------------------------------------------------------------------")
                print("")
            else:
                break
    while True:
        print("")
        print("==================================================================")
        print("I                 Please select your gender                      I")
        print("==================================================================")
        print("")
        print("1. Male")
        print("2. Female")
        print("3. Other")
        print("")
        print("==================================================================")
        Answer = input("Enter your choice here:-  ")
        print("==================================================================")
        if Answer == "1":
            New_Customer_Gender = 'Male'
            break
        elif Answer == "2":
            New_Customer_Gender = 'Female'
            break
        elif Answer == "3":
            New_Customer_Gender = 'Other'
            break
        elif Answer == 'Exit':
            return
        else:
            print("")
            print("------------------------------------------------------------------")
            print("You have entered an invalid answer, please try again")
            print("------------------------------------------------------------------")
            print("")
    while True:
        print("")
        print("==================================================================")
        print("    Which Loan would you like to apply for in Malaysian Bank?     ")
        print("==================================================================")
        print("")
        print("1. Education Loan (EL)")
        print("2. Car Loan (CL)")
        print("3. Home Loan (HL)")
        print("4. Personal Loan (PL)")
        print("")
        print("==================================================================")
        Answer = input("Enter your choice here:-  ")
        print("==================================================================")
        if Answer == "1":
            New_Customer_Loan = 'Education Loan (EL)'
            break
        elif Answer == "2":
            New_Customer_Loan = 'Car Loan (CL)'
            break
        elif Answer == "3":
            New_Customer_Loan = 'Home Loan (HL)'
            break
        elif Answer == "4":
            New_Customer_Loan = 'Personal Loan (PL)'
            break
        elif Answer == "Exit":
            return
        else:
            print("")
            print("------------------------------------------------------------------")
            print("You have entered an invalid answer, please try again")
            print("------------------------------------------------------------------")
            print("")
    while True:
        if New_Customer_Loan == "Education Loan (EL)":
            try:
                print("==================================================================")
                New_Customer_Loan_Amount = int(
                    input("How much would you like to borrow for your Education Loan from Malaysian Bank? "
                          "You can borrow as low as RM5000, to as a high as RM150,000:- "))
                print("==================================================================")
            except ValueError:
                print("")
                print("------------------------------------------------------------------")
                print("You have entered an incorrect borrow amount, please try again")
                print("------------------------------------------------------------------")
                print("")
            else:
                if 5000 <= New_Customer_Loan_Amount <= 150000:
                    break
                else:
                    print("")
                    print("------------------------------------------------------------------")
                    print("You have entered an incorrect borrow amount, please try again")
                    print("------------------------------------------------------------------")
                    print("")
        elif New_Customer_Loan == "Car Loan (CL)":
            try:
                print("==================================================================")
                New_Customer_Loan_Amount = int(
                    input("How much would you like to borrow for your Car Loan from Malaysian Bank? "
                          "You can borrow as low as RM25000, to as a high as RM1,000,000:- "))
                print("==================================================================")
            except ValueError:
                print("")
                print("------------------------------------------------------------------")
                print("You have entered an incorrect borrow amount, please try again")
                print("------------------------------------------------------------------")
                print("")
            else:
                if 25000 <= New_Customer_Loan_Amount <= 1000000:
                    break
                else:
                    print("")
                    print("------------------------------------------------------------------")
                    print("You have entered an incorrect borrow amount, please try again")
                    print("------------------------------------------------------------------")
                    print("")
        elif New_Customer_Loan == "Home Loan (HL)":
            try:
                print("==================================================================")
                print(
                    "How much would you like to borrow for your Home Loan from Malaysian Bank? You can borrow as low as RM10000, ")
                New_Customer_Loan_Amount = int(
                    input("to as a high as the value of the property you are borrowing this loan for:- "))
                print("==================================================================")
            except ValueError:
                print("")
                print("------------------------------------------------------------------")
                print("You have entered an incorrect borrow amount, please try again")
                print("------------------------------------------------------------------")
                print("")
            else:
                if 10000 <= New_Customer_Loan_Amount:
                    break
                else:
                    print("")
                    print("------------------------------------------------------------------")
                    print("You have entered an incorrect borrow amount, please try again")
                    print("------------------------------------------------------------------")
                    print("")
        else:
            try:
                print("==================================================================")
                New_Customer_Loan_Amount = int(
                    input("How much would you like to borrow for your Personal Loan from Malaysian Bank? "
                          "You can borrow as low as RM5000, to as a high as RM100,000:- "))
                print("==================================================================")
            except ValueError:
                print("")
                print("------------------------------------------------------------------")
                print("You have entered an incorrect borrow amount, please try again")
                print("------------------------------------------------------------------")
                print("")
            else:
                if 5000 <= New_Customer_Loan_Amount <= 1000000:
                    break
                else:
                    print("")
                    print("------------------------------------------------------------------")
                    print("You have entered an incorrect borrow amount, please try again")
                    print("------------------------------------------------------------------")
                    print("")
    while True:
        if New_Customer_Loan == "Education Loan (EL)":
            try:
                print("==================================================================")
                New_Customer_Loan_Term = int(
                    input("How many years would you like to borrow your Education Loan from Malaysian Bank? "
                          "The Maximum Tenure for this loan is 15 years after graduation:- "))
                print("==================================================================")
            except ValueError:
                print("")
                print("------------------------------------------------------------------")
                print("You have entered an incorrect tenure value, please try again")
                print("------------------------------------------------------------------")
                print("")
            else:
                if 1 <= New_Customer_Loan_Term <= 15:
                    break
                else:
                    print("")
                    print("------------------------------------------------------------------")
                    print("You have entered an incorrect borrow tenure value, please try again")
                    print("------------------------------------------------------------------")
                    print("")
        elif New_Customer_Loan == "Car Loan (CL)":
            try:
                print("==================================================================")
                New_Customer_Loan_Term = int(
                    input("How many years would you like to borrow your Car loan from Malaysian Bank? "
                          "The Maximum Tenure for this loan is 10 years:- "))
                print("==================================================================")
            except ValueError:
                print("")
                print("------------------------------------------------------------------")
                print("You have entered an incorrect tenure value, please try again")
                print("------------------------------------------------------------------")
                print("")
            else:
                if 1 <= New_Customer_Loan_Term <= 10:
                    break
                else:
                    print("")
                    print("------------------------------------------------------------------")
                    print("You have entered an incorrect tenure value, please try again")
                    print("------------------------------------------------------------------")
                    print("")
        elif New_Customer_Loan == "Home Loan (HL)":
            try:
                print("==================================================================")
                New_Customer_Loan_Term = int(input(
                    "How many years would you like to borrow your Home Lone from Malaysian Bank? The Maximum Tenure for this loan is 35 years:-  "))
                print("==================================================================")
            except ValueError:
                print("")
                print("------------------------------------------------------------------")
                print("You have entered an incorrect tenure value, please try again")
                print("------------------------------------------------------------------")
                print("")
            else:
                if 1 <= New_Customer_Loan_Term <= 35:
                    break
                else:
                    print("")
                    print("------------------------------------------------------------------")
                    print("You have entered an incorrect tenure value, please try again")
                    print("------------------------------------------------------------------")
                    print("")
        else:
            try:
                print("==================================================================")
                New_Customer_Loan_Term = int(
                    input("How many years would you like to borrow your Personal lone from Malaysian Bank? "
                          "The Minimum Tenure for this loan is 2 years, while the Maximum is 6 years:- "))
                print("==================================================================")
            except ValueError:
                print("")
                print("------------------------------------------------------------------")
                print("You have entered an incorrect tenure value, please try again")
                print("------------------------------------------------------------------")
                print("")
            else:
                if 2 <= New_Customer_Loan_Term <= 6:
                    break
                else:
                    print("")
                    print("------------------------------------------------------------------")
                    print("You have entered an incorrect tenure value, please try again")
                    print("------------------------------------------------------------------")
                    print("")
    from datetime import date
    Current_Date = date.today()
    Current_Date = Current_Date.strftime("%d/%m/%Y")
    if os.path.getsize('Customer_Account.txt') == 0:
        Customer_Account_Details = New_Customer_Name + ',' + New_Customer_ID + ',' + New_Customer_Password + ","
        with open("Customer_Account.txt", "a+") as Customer_Account_file:
            Customer_Account_file.write(Customer_Account_Details)
    else:
        Customer_Account_Details = '\n' + New_Customer_Name + ',' + New_Customer_ID + ',' + New_Customer_Password
        with open("Customer_Account.txt", "a+") as Customer_Account_file:
            Customer_Account_file.write(Customer_Account_Details)

    if os.path.getsize('New_Customer.txt') == 0:
        New_Customer_Details = New_Customer_ID + ',' + New_Customer_Name + ',' + New_Customer_Email_Address + ',' + New_Customer_Contact_Number + ',' + New_Customer_Date_of_Birth + ',' + New_Customer_Gender + ',' + New_Customer_Loan + ',' + str(
            New_Customer_Loan_Amount) + ',' + str(New_Customer_Loan_Term) + ',' + Current_Date + ',' + "Pending"
        with open("New_Customer.txt", "a+") as New_customer_file:
            New_customer_file.write(New_Customer_Details)
    else:
        New_Customer_Details = '\n' + New_Customer_ID + ',' + New_Customer_Name + ',' + New_Customer_Email_Address + ',' + New_Customer_Contact_Number + ',' + New_Customer_Date_of_Birth + ',' + New_Customer_Gender + ',' + New_Customer_Loan + ',' + str(
            New_Customer_Loan_Amount) + ',' + str(New_Customer_Loan_Term) + ',' + Current_Date + ',' + "Pending"
        with open("New_Customer.txt", "a+") as New_customer_file:
            New_customer_file.write(New_Customer_Details)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("I                             You are now registered!                           I")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Note: The interest rate of your selected loan will be based on amount of loan")
    print("       requested and will be under Malaysian Bank's discretion")
    print("")
    print("      If approved, you will be able to login into the system using the Account Name ")
    print("      and Password you provided")
    print("")
    print("      Your loan has not yet finalized. It will be approved shortly after,")
    print("      making it visible under your approved loan's detail option when you")
    print("      login into the system including the interest rate, next Monthly installment ")
    print("      date as well as the the amount of monthly installment you will be paying")
    print("      according to the loan you have registered for.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# This function gives users multiple options
# It makes users registered customers by calling the Registration function
# It allows users access to the loan calculator by calling the Loan_Calculator function
# It allows users to see the specific details of each loan offered in the system
def New_Customer_Menu():
    while True:
        print("")
        print("==================================================================")
        print("I         Welcome to Malaysian Bank's New Customer menu          I")
        print("I               What would you like to do?                       I")
        print("==================================================================")
        print("")
        print("1. Check specific details of loans offered by Malaysian Bank")
        print("2. Use our loan calculator to see if you are eligible for any of our loans")
        print("3. Become a Registered Customer with Malaysian Bank by applying for a loan request")
        print("4. Back to previous menu")
        print("5. Exit the program")
        print("")
        print("==================================================================")
        Answer = input("Enter your choice here:-  ")
        print("==================================================================")
        print("")
        if Answer == "1":
            while True:
                print("")
                print("==================================================================")
                print("I    The details of which loan would you like to know about?     I")
                print("==================================================================")
                print("")
                print("1. Education Loan (EL)")
                print("2. Car Loan (CL)")
                print("3. Home Loan (HL)")
                print("4. Personal Loan (PL)")
                print("5. Back to previous menu")
                print("")
                print("==================================================================")
                Answer = input("Enter your choice here:-  ")
                print("==================================================================")
                if Answer == "1":
                    print("")
                    print("")
                    print("")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    with open("Education_Loan.txt", "r") as Education_Loan_Info:
                        Education_Loan_Info = Education_Loan_Info.read()
                        print(Education_Loan_Info)
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("")
                    print("")
                    print("")
                elif Answer == "2":
                    print("")
                    print("")
                    print("")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    with open("Car_Loan.txt", "r") as Education_Loan_Info:
                        Education_Loan_Info = Education_Loan_Info.read()
                        print(Education_Loan_Info)
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("")
                    print("")
                    print("")
                elif Answer == "3":
                    print("")
                    print("")
                    print("")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    with open("Home_Loan.txt", "r") as Education_Loan_Info:
                        Education_Loan_Info = Education_Loan_Info.read()
                        print(Education_Loan_Info)
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("")
                    print("")
                    print("")
                elif Answer == "4":
                    print("")
                    print("")
                    print("")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    with open("Personal_Loan.txt", "r") as Education_Loan_Info:
                        Education_Loan_Info = Education_Loan_Info.read()
                        print(Education_Loan_Info)
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("")
                    print("")
                    print("")
                elif Answer == "5":
                    break
                else:
                    print("")
                    print("")
                    print("")
                    print("----------------------------------------------------")
                    print("You have entered an invalid answer, please try again")
                    print("----------------------------------------------------")
                    print("")
                    print("")
                    print("")
        elif Answer == "2":
            Loan_Calculator()
        elif Answer == "3":
            Registration()
        elif Answer == "4":
            break
        elif Answer == "5":
            exit("You have exited the Program")
        else:
            print("------------------------------------------------------------------")
            print("You have entered an invalid answer, please try again")
            print("------------------------------------------------------------------")

# This function gives users the option to either login into the system if they are already registered and approved in the system
# It allows users access to the new customer menu by calling the New_Customer_Menu function
def Customer_Menu():
    while True:
        print("")
        print("==================================================================")
        print("I  Welcome to Malaysia Bank's Online Loan Management System      I")
        print("I               What would you like to do?                       I")
        print("==================================================================")
        print("")
        print("1. Login into system if you are already registered")
        print("2. Go to the new customer menu")
        print("3. Back to Main Menu")
        print("4. Exit the Program")
        print("")
        print("==================================================================")
        Answer = input("Enter your choice here:-  ")
        print("==================================================================")
        print("")
        if Answer == "1":
            Reg_Cus_Menu()
        elif Answer == "2":
            New_Customer_Menu()
        elif Answer == "3":
            break
        elif Answer == "4":
            exit("You have exited the Program")
        else:
            print("------------------------------------------------------------------")
            print("You have entered an invalid answer, please try again")
            print("------------------------------------------------------------------")

# This function allows a user currently logged into the system to view their specific approved loan's details
# Pay their next due monthly installment
# View every monthly installment they have ever paid for their loan
# View the status of their monthly installments and loan
# Log out of the system
def Reg_Cus_Menu():
    BreakCondition = False
    while True:
        if BreakCondition:
            break
        else:
            print("")
            print("==================================================================")
            print("I  Welcome to Malaysian Bank's Registered Customer sign in menu  I")
            print("I           Please sign in to be granted full access             I")
            print("I           Enter 'Exit' to return to the main menu              I")
            print("==================================================================")
            print("")
            print("==================================================================")
            User_Name = str(input("Enter username here:- "))
            print("==================================================================")
            if User_Name == "Exit":
                break
            else:
                print("==================================================================")
                User_Password = str(input("Enter password here:- "))
                print("==================================================================")
            # noinspection PyUnboundLocalVariable
            Reg_Cus_Login(User_Name, User_Password)
            if Reg_Cus_Login(User_Name, User_Password) == "Yes":
                while True:
                    print("")
                    print("==================================================================")
                    print("I               Welcome back", User_Name, "!                     I")
                    print("I               What would you like to do?                       I")
                    print("==================================================================")
                    print("")
                    print("1. View your approved loan's details")
                    print("2. Pay your next monthly installment")
                    print("3. View all monthly installments paid for this loan")
                    print("4. View status of your loan.")
                    print("5. Return to sign in menu")
                    print("")
                    print("==================================================================")
                    Answer = input("Enter your choice here:- ")
                    print("==================================================================")
                    if Answer == "1":
                        Not_Approved = False
                        import datetime
                        with open("Loan_Registered_Customer.txt") as Loan_Details_Txt:
                            for line in Loan_Details_Txt:
                                line = line.strip('\n')
                                Loan_Details_List = line.split(",")
                                Installment_Due_Date = Loan_Details_List[8]
                                Installment_Due_Date_Date = datetime.datetime.strptime(Installment_Due_Date, '%d/%m/%Y').date()
                                if User_Name == Loan_Details_List[0]:
                                    print("")
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Account Name:- ", "              ", Loan_Details_List[0])
                                    print("Name:- ", "                      ", Loan_Details_List[1])
                                    print("Loan ID:- ", "                   ", Loan_Details_List[2])
                                    print("Loan Type:- ", "                 ", Loan_Details_List[3])
                                    print("Loan Amount:- ", "               ", Loan_Details_List[4])
                                    print("Interest Rate:- ", "             ", float(Loan_Details_List[5]) * 100, "%")
                                    print("Monthly Installment Amount:- ", "", "RM", Loan_Details_List[6])
                                    print("Loan Status:- ", "               ", Loan_Details_List[7])
                                    print("Next Installment Due:- ", "      ", Installment_Due_Date_Date)
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    Not_Approved = False
                                    break
                                else:
                                    Not_Approved = True
                        if Not_Approved:
                            print("")
                            print("------------------------------------------------------------------")
                            print("Your Loan has not been approved yet!")
                            print("------------------------------------------------------------------")
                            print("")
                    elif Answer == "2":
                        BreakCondition = False
                        Not_Approved = False
                        while True:
                            if BreakCondition:
                                break
                            else:
                                with open("Loan_Registered_Customer.txt") as Monthly_Installment_Payment_Txt:
                                    for line in Monthly_Installment_Payment_Txt:
                                        line = line.strip('\n')
                                        Loan_Registered_Customer_List = line.split(",")
                                        Account_Name = Loan_Registered_Customer_List[0]
                                        Name = Loan_Registered_Customer_List[1]
                                        Loan_ID = Loan_Registered_Customer_List[2]
                                        Monthly_Installments = Loan_Registered_Customer_List[6]
                                        Installment_Due_Date = Loan_Registered_Customer_List[8]
                                        if User_Name == Loan_Registered_Customer_List[0]:
                                            print("")
                                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("Next Installment:- ", "  ", Loan_Registered_Customer_List[8])
                                            print("Loan ID:- ", "           ", Loan_Registered_Customer_List[2])
                                            print("Loan Amount:- ", "       ", "RM", Loan_Registered_Customer_List[4])
                                            print("Installment Amount:- ", "", "RM", Loan_Registered_Customer_List[6])
                                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("")
                                            Not_Approved = False
                                            break
                                        else:
                                            Not_Approved = True
                                if Not_Approved:
                                    BreakCondition = True
                                    print("")
                                    print("------------------------------------------------------------------")
                                    print("Your Loan has not been approved yet!")
                                    print("------------------------------------------------------------------")
                                    print("")
                                else:
                                    print("==================================================================")
                                    print("Do you wish to pay this month's monthly installment of your loan?")
                                    print("")
                                    print("1. Pay Monthly Installment")
                                    print("2. Do not pay Monthly Installment")
                                    print("3. Return to previous menu")
                                    print("")
                                    print("==================================================================")
                                    Answer1 = input("Enter your choice here:- ")
                                    print("==================================================================")
                                    if Answer1 == "3":
                                        break
                                    elif Answer1 == "1":
                                        import datetime
                                        while True:
                                            while True:
                                                try:
                                                    print("==================================================================")
                                                    Payment_Date = input("On which date do you wish pay this month's installment for your loan?:- ")
                                                    print("==================================================================")
                                                    Payment_Date = datetime.datetime.strptime(Payment_Date, '%d/%m/%Y')
                                                    with open("Registered_Customer.txt") as Reg_Date_Txt:
                                                        for line in Reg_Date_Txt:
                                                            Reg_Date_List = line.split(",")
                                                            if User_Name == Reg_Date_List[0]:
                                                                if Payment_Date < datetime.datetime.strptime(Reg_Date_List[9], '%d/%m/%Y'):
                                                                    Before_Reg_Date = True
                                                                    break
                                                                else:
                                                                    Before_Reg_Date = False
                                                            else:
                                                                pass
                                                        if Before_Reg_Date:
                                                            print("")
                                                            print("------------------------------------------------------------------")
                                                            print("Your payment date can't be before your registration date!")
                                                            print("------------------------------------------------------------------")
                                                            print("")
                                                        else:
                                                            break
                                                except ValueError:
                                                    print("")
                                                    print("------------------------------------------------------------------")
                                                    print("You have entered an invalid payment date, please try again")
                                                    print("------------------------------------------------------------------")
                                                    print("")
                                            try:
                                                Installment_Due_Date_Date = datetime.datetime.strptime(Installment_Due_Date, '%d/%m/%Y')
                                                if Payment_Date <= Installment_Due_Date_Date:
                                                    import os
                                                    Payment_Date = Payment_Date.strftime('%d/%m/%Y')
                                                    Payment_Status = "Installment Paid"
                                                    if os.path.getsize('Customer_Transaction.txt') == 0:
                                                        Customer_Transaction_List = Account_Name + ',' + Loan_ID + "," + Name + "," + Monthly_Installments + "," + Payment_Date + "," + Payment_Status + ","
                                                        with open("Customer_Transaction.txt", "a+") as Customer_Transaction_Txt:
                                                            Customer_Transaction_Txt.write(Customer_Transaction_List)
                                                        with open("Loan_Registered_Customer.txt") as Installment_Due_Date_Update_Txt:
                                                            for line in Installment_Due_Date_Update_Txt:
                                                                Installment_Date_List = line.split(",")
                                                                if User_Name == Installment_Date_List[0]:
                                                                    New_Installment_Date = Automatic_Installment_Date_Calculator(Installment_Due_Date_Date)
                                                                    Installment_Date_List[8] = New_Installment_Date
                                                                    Installment_Date_List = [','.join(Installment_Date_List)]
                                                                    break
                                                                else:
                                                                    pass
                                                        with open("Loan_Registered_Customer.txt") as Installment_Due_Date_Update_Txt:
                                                            Installment_Due_Date_Update_List = Installment_Due_Date_Update_Txt.read().splitlines()
                                                            for x in Installment_Due_Date_Update_List:
                                                                if User_Name in x:
                                                                    Position = Installment_Due_Date_Update_List.index(x)
                                                                    Installment_Due_Date_Update_List[Position:Position+1] = Installment_Date_List
                                                                    break
                                                                else:
                                                                    pass
                                                        with open("Loan_Registered_Customer.txt", "w+") as New_Loan_Reg_Cus_Txt:
                                                            New_Loan_Reg_Cus_Txt.write('\n'.join(Installment_Due_Date_Update_List))
                                                            New_Loan_Reg_Cus_Txt.write('\n')
                                                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                        print("I                           Installment Paid!                                   I")
                                                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                        BreakCondition = True
                                                        break
                                                    else:
                                                        Customer_Transaction_List = '\n' + Account_Name + ',' + Loan_ID + "," + Name + "," + Monthly_Installments + "," + Payment_Date + "," + Payment_Status + ","
                                                        with open("Customer_Transaction.txt", "a+") as Customer_Transaction_Txt:
                                                            Customer_Transaction_Txt.write(Customer_Transaction_List)
                                                        with open("Loan_Registered_Customer.txt") as Installment_Due_Date_Update_Txt:
                                                            for line in Installment_Due_Date_Update_Txt:
                                                                Installment_Date_List = line.split(",")
                                                                if User_Name == Installment_Date_List[0]:
                                                                    New_Installment_Date = Automatic_Installment_Date_Calculator(Installment_Due_Date_Date)
                                                                    Installment_Date_List[8] = New_Installment_Date
                                                                    Installment_Date_List = [','.join(Installment_Date_List)]
                                                                    break
                                                                else:
                                                                    pass
                                                        with open("Loan_Registered_Customer.txt") as Installment_Due_Date_Update_Txt:
                                                            Installment_Due_Date_Update_List = Installment_Due_Date_Update_Txt.read().splitlines()
                                                            for x in Installment_Due_Date_Update_List:
                                                                if User_Name in x:
                                                                    Position = Installment_Due_Date_Update_List.index(x)
                                                                    Installment_Due_Date_Update_List[Position:Position + 1] = Installment_Date_List
                                                                    break
                                                                else:
                                                                    pass
                                                        with open("Loan_Registered_Customer.txt", "w+") as New_Loan_Reg_Cus_Txt:
                                                            New_Loan_Reg_Cus_Txt.write('\n'.join(Installment_Due_Date_Update_List))
                                                            New_Loan_Reg_Cus_Txt.write('\n')
                                                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                        print("I                           Installment Paid!                                   I")
                                                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                        BreakCondition = True
                                                        break
                                                else:
                                                    import os
                                                    Payment_Date = Payment_Date.strftime('%d/%m/%Y')
                                                    Payment_Status = "Late Installment Payment"
                                                    if os.path.getsize('Customer_Transaction.txt') == 0:
                                                        Customer_Transaction_List = Account_Name + ',' + Loan_ID + "," + Name + "," + Monthly_Installments + "," + Payment_Date + "," + Payment_Status + ","
                                                        with open("Customer_Transaction.txt", "a+") as Customer_Transaction_Txt:
                                                            Customer_Transaction_Txt.write(Customer_Transaction_List)
                                                        with open("Loan_Registered_Customer.txt") as Installment_Due_Date_Update_Txt:
                                                            for line in Installment_Due_Date_Update_Txt:
                                                                Installment_Date_List = line.split(",")
                                                                if User_Name == Installment_Date_List[0]:
                                                                    New_Installment_Date = Automatic_Installment_Date_Calculator(Installment_Due_Date_Date)
                                                                    Installment_Date_List[8] = New_Installment_Date
                                                                    Installment_Date_List = [','.join(Installment_Date_List)]
                                                                    break
                                                                else:
                                                                    pass
                                                        with open("Loan_Registered_Customer.txt") as Installment_Due_Date_Update_Txt:
                                                            Installment_Due_Date_Update_List = Installment_Due_Date_Update_Txt.read().splitlines()
                                                            for x in Installment_Due_Date_Update_List:
                                                                if User_Name in x:
                                                                    Position = Installment_Due_Date_Update_List.index(x)
                                                                    Installment_Due_Date_Update_List[Position:Position + 1] = Installment_Date_List
                                                                    break
                                                                else:
                                                                    pass
                                                        with open("Loan_Registered_Customer.txt", "w+") as New_Loan_Reg_Cus_Txt:
                                                            New_Loan_Reg_Cus_Txt.write('\n'.join(Installment_Due_Date_Update_List))
                                                            New_Loan_Reg_Cus_Txt.write('\n')
                                                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                        print("I                           Installment Paid!                                   I")
                                                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                        BreakCondition = True
                                                        break
                                                    else:
                                                        Customer_Transaction_List = '\n' + Account_Name + ',' + Loan_ID + "," + Name + "," + Monthly_Installments + "," + Payment_Date + "," + Payment_Status + ","
                                                        with open("Customer_Transaction.txt", "a+") as Customer_Transaction_Txt:
                                                            Customer_Transaction_Txt.write(Customer_Transaction_List)
                                                        with open("Loan_Registered_Customer.txt") as Installment_Due_Date_Update_Txt:
                                                            for line in Installment_Due_Date_Update_Txt:
                                                                Installment_Date_List = line.split(",")
                                                                if User_Name == Installment_Date_List[0]:
                                                                    New_Installment_Date = Automatic_Installment_Date_Calculator(Installment_Due_Date_Date)
                                                                    Installment_Date_List[8] = New_Installment_Date
                                                                    Installment_Date_List = [','.join(Installment_Date_List)]
                                                                    break
                                                                else:
                                                                    pass
                                                        with open("Loan_Registered_Customer.txt") as Installment_Due_Date_Update_Txt:
                                                            Installment_Due_Date_Update_List = Installment_Due_Date_Update_Txt.read().splitlines()
                                                            for x in Installment_Due_Date_Update_List:
                                                                if User_Name in x:
                                                                    Position = Installment_Due_Date_Update_List.index(x)
                                                                    Installment_Due_Date_Update_List[Position:Position + 1] = Installment_Date_List
                                                                    break
                                                                else:
                                                                    pass
                                                        with open("Loan_Registered_Customer.txt", "w+") as New_Loan_Reg_Cus_Txt:
                                                            New_Loan_Reg_Cus_Txt.write('\n'.join(Installment_Due_Date_Update_List))
                                                            New_Loan_Reg_Cus_Txt.write('\n')
                                                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                        print("I                           Installment Paid!                                   I")
                                                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                        BreakCondition = True
                                                        break
                                            except ValueError:
                                                print("")
                                                print("------------------------------------------------------------------")
                                                print("You have entered an invalid payment date, please try again")
                                                print("------------------------------------------------------------------")
                                                print("")
                                    elif Answer1 == "2":
                                        import os
                                        Payment_Date = "N/A"
                                        Payment_Status = "Over Due Payment"
                                        if os.path.getsize('Customer_Transaction.txt') == 0:
                                            Customer_Transaction_List = Account_Name + ',' + Loan_ID + "," + Name + "," + Monthly_Installments + "," + Payment_Date + "," + Payment_Status + ","
                                            with open("Customer_Transaction.txt", "a+") as Customer_Transaction_Txt:
                                                Customer_Transaction_Txt.write(Customer_Transaction_List)
                                            break
                                        else:
                                            Customer_Transaction_List = '\n' + Account_Name + ',' + Loan_ID + "," + Name + "," + Monthly_Installments + "," + Payment_Date + "," + Payment_Status + ","
                                            with open("Customer_Transaction.txt", "a+") as Customer_Transaction_Txt:
                                                Customer_Transaction_Txt.write(Customer_Transaction_List)
                                            break
                                    else:
                                        print("")
                                        print("------------------------------------------------------------------")
                                        print("You have entered an invalid answer, please try again")
                                        print("------------------------------------------------------------------")
                    elif Answer == "3":
                        Made_Payments = False
                        import os
                        if os.path.getsize('Loan_Registered_Customer.txt') == 0:
                            print("")
                            print("------------------------------------------------------------------")
                            print("You have made no transactions!")
                            print("------------------------------------------------------------------")
                        else:
                            with open("Customer_Transaction.txt") as Transactions_Txt:
                                for line in Transactions_Txt:
                                    Transactions_List = line.split(",")
                                    if User_Name == Transactions_List[0]:
                                        print("")
                                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Name:-", "                                   ", Transactions_List[2])
                                        print("Payment Date for Monthly Installment:- ", "  ", Transactions_List[4])
                                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        Made_Payments = True
                                    else:
                                        pass
                            if not Made_Payments:
                                print("")
                                print("------------------------------------------------------------------")
                                print("You have not made any payments yet!")
                                print("------------------------------------------------------------------")
                                print("")
                    elif Answer == "4":
                        Not_Approved = False
                        Made_Payments = False
                        with open("Loan_Registered_Customer.txt") as Loan_Status_Txt:
                            for line in Loan_Status_Txt:
                                Loan_Status_List = line.split(",")
                                if Loan_Status_List[0] == User_Name:
                                    Not_Approved = False
                                    break
                                else:
                                    Not_Approved = True
                        if not Not_Approved:
                            with open("Customer_Transaction.txt") as Status_Txt:
                                for line in Status_Txt:
                                    Status_List = line.split(",")
                                    if User_Name == Status_List[0]:
                                        print("")
                                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Name:-", "           ", Status_List[2])
                                        print("Payment Status:- ", "", Status_List[5])
                                        print("Loan Status:- ", "   ",    "Loan Approved")
                                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        Made_Payments = True
                                    else:
                                        pass
                        else:
                            print("")
                            print("------------------------------------------------------------------")
                            print("Your Loan has not been approved yet!")
                            print("------------------------------------------------------------------")
                            print("")
                        if not Made_Payments:
                            print("")
                            print("------------------------------------------------------------------")
                            print("You have not made any payments yet!")
                            print("------------------------------------------------------------------")
                            print("")
                    elif Answer == "5":
                        break
                    else:
                        print("")
                        print("------------------------------------------------------------------")
                        print("You have entered an invalid answer, please try again")
                        print("------------------------------------------------------------------")
            elif Reg_Cus_Login(User_Name, User_Password) == "Not Approved":
                print("")
                print("------------------------------------------------------------------")
                print("Your account has not been approved by the admin yet!")
                print("------------------------------------------------------------------")
                print("")
            else:
                while True:
                    print("")
                    print("------------------------------------------------------------------")
                    print("You have entered invalid login details!")
                    print("------------------------------------------------------------------")
                    print("")
                    print("==================================================================")
                    print("Do you wish to try again? or return to the main menu?")
                    print("")
                    print("1. Try again")
                    print("2. Return to the main menu")
                    print("")
                    print("==================================================================")
                    Answer = input("Enter your choice here:- ")
                    print("==================================================================")
                    if Answer == "1":
                        break
                    elif Answer == "2":
                        BreakCondition = True
                        break
                    else:
                        print("------------------------------------------------------------------")
                        print("You have entered an invalid answer, please try again")
                        print("------------------------------------------------------------------")

# This function allows a currently logged in user to either
# Display all registration requests present in the system made by new customers
# Approve or reject a registration request, allowing or disallowing a user to login into the system
# Search for all monthly installments made by a specific registered customer present in the system
# Search all monthly installments paid by multiple registered customer towards a specific loan type
# Display all transactions made by all registered customers for all types of loans
def Admin_Menu():
    BreakCondition = False
    while True:
        if BreakCondition:
            break
        else:
            print("")
            print("==================================================================")
            print("I        Welcome to Malaysian Bank's Admin sign in menu          I")
            print("I           Please sign in to be granted full access             I")
            print("I           Enter 'Exit' to return to the main menu              I")
            print("==================================================================")
            print("")
            print("==================================================================")
            User_Name = str(input("Enter username here:- "))
            print("==================================================================")
            if User_Name == "Exit":
                break
            else:
                print("==================================================================")
                User_Password = str(input("Enter password here:- "))
                print("==================================================================")
            # noinspection PyUnboundLocalVariable
            Admin_Login(User_Name, User_Password)
            if Admin_Login(User_Name, User_Password) == "Yes":
                while True:
                    Exit_All_Loop = False
                    BreakCondition = False
                    print("")
                    print("==================================================================")
                    print("I               Welcome back Administrator!                      I")
                    print("I               What would you like to do?                       I")
                    print("==================================================================")
                    print("")
                    print("1. Display all registration requests from new customers")
                    print("2. Approve or Reject a new customer's registration request")
                    print("3. Provide loan details to a new registered customer")
                    print("4. Search for all monthly installments made by a specific registered customer.")
                    print("5. Search and display all monthly installments made for a specific loan type (EL/CL/HL/PL)")
                    print("6. Display all transactions of all customers.")
                    print("7. Display all transactions of all types of loans")
                    print("8. Return to Admin sign in menu")
                    print("")
                    print("==================================================================")
                    Answer = input("Enter your choice here:- ")
                    print("==================================================================")
                    if Answer == "1":
                        with open("New_Customer.txt") as New_Customer_Registration_Request_Txt:
                            for line in New_Customer_Registration_Request_Txt:
                                line = line.strip('\n')
                                New_Customer_Registration_Request_List = line.split(",")
                                print("")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Account Name:-", "      ", New_Customer_Registration_Request_List[0])
                                print("Name:-", "              ", New_Customer_Registration_Request_List[1])
                                print("Email:-", "             ", New_Customer_Registration_Request_List[2])
                                print("Contact Number:-", "    ", New_Customer_Registration_Request_List[3])
                                print("Birth Date:-", "        ", New_Customer_Registration_Request_List[4])
                                print("Gender:-", "            ", New_Customer_Registration_Request_List[5])
                                print("Loan Type:-", "         ", New_Customer_Registration_Request_List[6])
                                print("Loan Amount:-", "       ", "RM", New_Customer_Registration_Request_List[7])
                                print("Tenure:-", "            ", New_Customer_Registration_Request_List[8], "years")
                                print("Registration Date:-", " ", New_Customer_Registration_Request_List[9])
                                print("Status:-", "            ", New_Customer_Registration_Request_List[10])
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("")
                    elif Answer == "2":
                        while True:
                            if BreakCondition:
                                break
                            else:
                                BreakCondition = False
                                import os
                                if os.path.getsize('New_Customer.txt') == 0:
                                    print("------------------------------------------------------------------")
                                    print('No registration requests at this moment!')
                                    print("------------------------------------------------------------------")
                                    break
                                else:
                                    with open("New_Customer.txt") as New_Customer_Registration_Request_Txt:
                                        for line in New_Customer_Registration_Request_Txt:
                                            line = line.strip('\n')
                                            New_Customer_Registration_Request_List = line.split(",")
                                            print("")
                                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("Account Name:- ", "     ", New_Customer_Registration_Request_List[0])
                                            print("Name:-", "              ", New_Customer_Registration_Request_List[1])
                                            print("Email:-", "             ", New_Customer_Registration_Request_List[2])
                                            print("Contact Number:-", "    ", New_Customer_Registration_Request_List[3])
                                            print("Birth Date:-", "        ", New_Customer_Registration_Request_List[4])
                                            print("Gender:-", "            ", New_Customer_Registration_Request_List[5])
                                            print("Loan Type:-", "         ", New_Customer_Registration_Request_List[6])
                                            print("Loan Amount:-", "       ", "RM", New_Customer_Registration_Request_List[7])
                                            print("Tenure:-", "            ", New_Customer_Registration_Request_List[8], "years")
                                            print("Registration Date:-", " ", New_Customer_Registration_Request_List[9])
                                            print("Status:-", "            ", New_Customer_Registration_Request_List[10])
                                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("")
                                        No_Results_Found = False
                                        with open("New_Customer.txt") as New_Customer_Registration_Txt:
                                            break_for_loop = False
                                            while True:
                                                print("==================================================================")
                                                print("Which customer's registration request would you like to approve/reject? Enter 'Exit' to return to the admin menu")
                                                Selected_Customer = input("Enter their Account name here:- ")
                                                print("==================================================================")
                                                if Selected_Customer.isspace():
                                                    print("------------------------------------------------------------------")
                                                    print("You have entered an invalid customer name, please try again")
                                                    print("------------------------------------------------------------------")
                                                else:
                                                    break
                                            if Selected_Customer == "Exit":
                                                break
                                            else:
                                                for line in New_Customer_Registration_Txt:
                                                    if break_for_loop:
                                                        break
                                                    else:
                                                        line = line.strip('\n')
                                                        Selected_Customer_List = line.split(",")
                                                        if Selected_Customer == Selected_Customer_List[0]:
                                                            while True:
                                                                print("")
                                                                print("==================================================================")
                                                                print("Do you wish to approve or reject", Selected_Customer_List[0], "'s registration request?")
                                                                print("")
                                                                print("1. Approve")
                                                                print("2. Reject")
                                                                print("")
                                                                print("==================================================================")
                                                                Answer_Approval_Rejection = input("Enter your choice here:- ")
                                                                print("==================================================================")
                                                                if Answer_Approval_Rejection == "1":
                                                                    Selected_Customer_List[10] = "Approved"
                                                                    Selected_Customer_List = [",".join(Selected_Customer_List)]
                                                                    No_Results_Found = False
                                                                    break_for_loop = True
                                                                    break
                                                                elif Answer_Approval_Rejection == "2":
                                                                    Selected_Customer_List[10] = "Rejected"
                                                                    Selected_Customer_List = [",".join(Selected_Customer_List)]
                                                                    No_Results_Found = False
                                                                    break_for_loop = True
                                                                    break
                                                                else:
                                                                    print("------------------------------------------------------------------")
                                                                    print("You have entered an invalid answer, please try again")
                                                                    print("------------------------------------------------------------------")
                                                        else:
                                                            No_Results_Found = True
                                                if No_Results_Found:
                                                    print("")
                                                    print("------------------------------------------------------------------")
                                                    print("No registration requests of entered name found!")
                                                    print("------------------------------------------------------------------")
                                                else:
                                                    if Answer_Approval_Rejection == "1":
                                                        with open("Registered_Customer.txt", "a+") as Registered_Customer_Txt:
                                                            Registered_Customer_Txt.write('\n'.join(Selected_Customer_List))
                                                            Registered_Customer_Txt.write('\n')
                                                        with open("New_Customer.txt") as New_Customer_txt:
                                                            New_Customer_list = New_Customer_txt.read().splitlines()
                                                            for x in New_Customer_list:
                                                                if Selected_Customer in x:
                                                                    Position = New_Customer_list.index(x)
                                                                    New_Customer_list_Modified = New_Customer_list[Position].split(',')
                                                                    if Selected_Customer in New_Customer_list_Modified:
                                                                        break
                                                            del New_Customer_list[Position]
                                                            list(filter(str.strip, New_Customer_list))
                                                        with open("New_Customer.txt", "w+") as Modified_New_Customer_txt:
                                                            Modified_New_Customer_txt.write("\n".join(New_Customer_list))
                                                        print("")
                                                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                        print("I                        Approval Successful!                                   I")
                                                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                        print("")
                                                        print("=================================================================================")
                                                        print("Do you wish to approve/reject another registration request or return to the admin menu?")
                                                        print("")
                                                        print("1. Approve/Reject another registration request")
                                                        print("2. Return to admin menu")
                                                        print("")
                                                        while True:
                                                            print("==================================================================")
                                                            Answer = input("Enter your choice here:- ")
                                                            print("==================================================================")
                                                            if Answer == "1":
                                                                break
                                                            elif Answer == "2":
                                                                BreakCondition = True
                                                                break
                                                            else:
                                                                print("------------------------------------------------------------------")
                                                                print("You have entered an invalid answer, please try again")
                                                                print("------------------------------------------------------------------")
                                                    else:
                                                        with open("Rejected_Customer.txt", "a+") as Rejected_Customer_Txt:
                                                            Rejected_Customer_Txt.write('\n'.join(Selected_Customer_List))
                                                            Rejected_Customer_Txt.write('\n')
                                                        with open("New_Customer.txt") as New_Customer_txt:
                                                            New_Customer_list = New_Customer_txt.read().splitlines()
                                                            for x in New_Customer_list:
                                                                if Selected_Customer in x:
                                                                    Position = New_Customer_list.index(x)
                                                                    New_Customer_list_Modified = New_Customer_list[
                                                                        Position].split(',')
                                                                    if Selected_Customer in New_Customer_list_Modified:
                                                                        break
                                                            del New_Customer_list[Position]
                                                            list(filter(str.strip, New_Customer_list))
                                                        with open("New_Customer.txt", "w+") as Modified_New_Customer_txt:
                                                            Modified_New_Customer_txt.write("\n".join(New_Customer_list))
                                                        print("")
                                                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                        print("I                        Rejection Successful!                                   I")
                                                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                        print("")
                                                        print("=================================================================================")
                                                        print("Do you wish to approve/reject another registration request or return to the admin menu?")
                                                        print("")
                                                        print("1. Approve/Reject another registration request")
                                                        print("2. Return to admin menu")
                                                        print("")
                                                        while True:
                                                            print("==================================================================")
                                                            Answer = input("Enter your choice here:- ")
                                                            print("==================================================================")
                                                            if Answer == "1":
                                                                break
                                                            elif Answer == "2":
                                                                BreakCondition = True
                                                                break
                                                            else:
                                                                print("------------------------------------------------------------------")
                                                                print("You have entered an invalid answer, please try again")
                                                                print("------------------------------------------------------------------")
                    elif Answer == "3":
                        BreakCondition1 = False
                        import os
                        while True:
                            BreakCondition = False
                            if BreakCondition1:
                                break
                            elif os.path.getsize('Registered_Customer.txt') == 0:
                                print("")
                                print("------------------------------------------------------------------")
                                print('No registered customers found!!')
                                print("------------------------------------------------------------------")
                                break
                            else:
                                with open("Registered_Customer.txt") as Registered_Customer_Txt:
                                    No_Results_Found = False
                                    for line in Registered_Customer_Txt:
                                        line = line.strip('\n')
                                        Registered_Customer_Txt_List = line.split(",")
                                        print("")
                                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("Account Name:-", "     ", Registered_Customer_Txt_List[0])
                                        print("Name:-", "             ", Registered_Customer_Txt_List[1])
                                        print("Birth Date:-", "       ", Registered_Customer_Txt_List[3])
                                        print("Loan Type:-", "        ", Registered_Customer_Txt_List[6])
                                        print("Loan Amount:-", "      ", "RM", Registered_Customer_Txt_List[7])
                                        print("Tenure:-", "           ", Registered_Customer_Txt_List[8], "years")
                                        print("Registration Date:-", "", Registered_Customer_Txt_List[9])
                                        print("Status:-", "           ", Registered_Customer_Txt_List[10])
                                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                        print("")
                                while True:
                                    if BreakCondition:
                                        break
                                    else:
                                        print("")
                                        print("==================================================================")
                                        Selected_Loan_Customer = input("Please enter Account name of the registered customer you wish to provide loan details to"
                                                                       " Entering 'Exit' will return you to the admin menu:- ")
                                        print("==================================================================")
                                        if Selected_Loan_Customer == "Exit":
                                            Exit_All_Loop = True
                                            break
                                        if os.path.getsize('Loan_Registered_Customer.txt') == 0:
                                            break
                                        else:
                                            with open("Loan_Registered_Customer.txt", "r") as Loan_Registered_Customer_Txt:
                                                for line in Loan_Registered_Customer_Txt:
                                                    Loan_Registered_Customer_List = line.split(",")
                                                    if Selected_Loan_Customer == Loan_Registered_Customer_List[0]:
                                                        print("")
                                                        print("------------------------------------------------------------------")
                                                        print("Registered Customer has already been provided loan details!")
                                                        print("------------------------------------------------------------------")
                                                        BreakCondition = False
                                                        break
                                                    else:
                                                        BreakCondition = True
                                with open("Registered_Customer.txt") as Registered_Customer_Loan_Txt:
                                    Registered_Customer_Loan_List = Registered_Customer_Loan_Txt.read().splitlines()
                                    for x in Registered_Customer_Loan_List:
                                        if Selected_Loan_Customer in x:
                                            Position = Registered_Customer_Loan_List.index(x)
                                            Selected_Loan_Customer_List = Registered_Customer_Loan_List[Position].split(",")
                                            if Selected_Loan_Customer == Selected_Loan_Customer_List[0]:
                                                Name = Selected_Loan_Customer_List[1]
                                                Loan_Type = Selected_Loan_Customer_List[6]
                                                Loan_Amount = float(Selected_Loan_Customer_List[7])
                                                Tenure = int(Selected_Loan_Customer_List[8])
                                                Loan_Registration_Date = Selected_Loan_Customer_List[9]
                                                import datetime
                                                Loan_Registration_Date_Date = datetime.datetime.strptime(Loan_Registration_Date, '%d/%m/%Y')
                                                import uuid
                                                LoanID = uuid.uuid4()
                                                LoanID = 'LN' + str(LoanID)
                                                Installment_Date = Automatic_Installment_Date_Calculator(
                                                    Loan_Registration_Date_Date)
                                                if Loan_Type == "Education Loan (EL)":
                                                    Interest_Rate = float(0.01)
                                                elif Loan_Type == "Personal Loan (PL)":
                                                    if 5000 <= Loan_Amount <= 20000:
                                                        Interest_Rate = float(0.08)
                                                    elif 20000 <= Loan_Amount <= 50000:
                                                        Interest_Rate = float(0.07)
                                                    else:
                                                        Interest_Rate = float(0.065)
                                                elif Loan_Type == "Car Loan (CL)":
                                                    Interest_Rate = float(0.025)
                                                else:
                                                    Interest_Rate = float(0.012)
                                                MonthlyInstallments = ((Tenure * Loan_Amount * Interest_Rate) + Loan_Amount) / (Tenure * 12)
                                                MonthlyInstallments = round(MonthlyInstallments, 2)
                                                No_Results_Found = False
                                                break
                                        else:
                                            No_Results_Found = True
                                if Exit_All_Loop:
                                    break
                                elif No_Results_Found:
                                    print("")
                                    print("------------------------------------------------------------------")
                                    print("Registered Customer not found!")
                                    print("------------------------------------------------------------------")
                                else:
                                    import os
                                    if os.path.getsize('Loan_Registered_Customer.txt') == 0:
                                        Loan_Registered_Customer_List = Selected_Loan_Customer + ',' + Name + ',' + LoanID + ',' + Loan_Type + ',' + str(Loan_Amount) + ',' + str(Interest_Rate) + ',' + str(MonthlyInstallments) + ',' + "Loan Approved" + ',' + str(Installment_Date)
                                        with open("Loan_Registered_Customer.txt", "a+") as Loan_Registered_Customer_Txt:
                                            Loan_Registered_Customer_Txt.write(Loan_Registered_Customer_List)
                                    else:
                                        Loan_Registered_Customer_List = '\n' + Selected_Loan_Customer + ',' + Name + ',' + LoanID + ',' + Loan_Type + ',' + str(Loan_Amount) + ',' + str(Interest_Rate) + ',' + str(MonthlyInstallments) + ',' + "Loan Approved" + ',' + str(Installment_Date)
                                        with open("Loan_Registered_Customer.txt", "a+") as Loan_Registered_Customer_Txt:
                                            Loan_Registered_Customer_Txt.write(Loan_Registered_Customer_List)
                                    print("")
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("I                    Loan Details Successfully Provided!                        I")
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("")
                                    print("=================================================================================")
                                    print("Do you wish to provide loan details to another registered customer or return to the admin menu?")
                                    print("")
                                    print("1. provide loan details to another registered customer")
                                    print("2. Return to admin menu")
                                    print("")
                                    while True:
                                        print("==================================================================")
                                        Answer = input("Enter your choice here:- ")
                                        print("==================================================================")
                                        if Answer == "1":
                                            break
                                        elif Answer == "2":
                                            BreakCondition1 = True
                                            break
                                        else:
                                            print("------------------------------------------------------------------")
                                            print("You have entered an invalid answer, please try again")
                                            print("------------------------------------------------------------------")
                    elif Answer == "4":
                        print("")
                        print("==================================================================")
                        Selected_Customer = input("Which customer's transactions would you like to search for? "
                                                  "Enter their account name to search for their transactions made. "
                                                  "Enter 'Exit to return to the admin menu page:- ")
                        print("==================================================================")
                        import os
                        if os.path.getsize("Registered_Customer.txt") == 0:
                            print("------------------------------------------------------------------")
                            print("This customer is not registered in the system!")
                            print("------------------------------------------------------------------")
                        else:
                            with open("Registered_Customer.txt") as Reg_Cus_Txt:
                                for line in Reg_Cus_Txt:
                                    Reg_Cus_List = line.split(",")
                                    if Selected_Customer == Reg_Cus_List[0]:
                                        Exists = True
                                        break
                                    else:
                                        Exists = False
                            if Exists:
                                if Selected_Customer == 'Exit':
                                    pass
                                else:
                                    Made_Payments = False
                                    import os
                                    if os.path.getsize('Loan_Registered_Customer.txt') == 0:
                                        print("")
                                        print("------------------------------------------------------------------")
                                        print("This Customer has made no transactions!")
                                        print("------------------------------------------------------------------")
                                    else:
                                        with open("Customer_Transaction.txt") as Transactions_Txt:
                                            for line in Transactions_Txt:
                                                line = line.strip('\n')
                                                Transactions_List = line.split(",")
                                                if Selected_Customer == Transactions_List[0]:
                                                    print("")
                                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                    print("Name:-", "                                   ", Transactions_List[2])
                                                    print("Payment Date for Monthly Installment:- ", "  ", Transactions_List[4])
                                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                    Made_Payments = True
                                                else:
                                                    pass
                                        if not Made_Payments:
                                            print("")
                                            print("------------------------------------------------------------------")
                                            print("The Account specified has not made any payments!")
                                            print("------------------------------------------------------------------")
                                            print("")
                            else:
                                print("")
                                print("------------------------------------------------------------------")
                                print("This customer is not registered in the system!")
                                print("------------------------------------------------------------------")
                                print("")
                    elif Answer == "5":
                        while True:
                            Made_Payments = False
                            print("")
                            print("==================================================================")
                            print("Which loan type's transactions would you like to search for?")
                            print("Enter 'Exit to return to the admin menu page")
                            print("")
                            print("1. Education Loan (EL) ")
                            print("2. Car Loan (CL) ")
                            print("3. Personal Loan (PL) ")
                            print("4. Home Loan (HL) ")
                            print("")
                            print("==================================================================")
                            Selected_Loan_Type = input("Enter your choice here:- ")
                            print("==================================================================")
                            if Selected_Loan_Type == "1":
                                Loan_Type = "Education Loan (EL)"
                            elif Selected_Loan_Type == "2":
                                Loan_Type = "Car Loan (CL)"
                            elif Selected_Loan_Type == "3":
                                Loan_Type = "Personal Loan (PL)"
                            elif Selected_Loan_Type == "4":
                                Loan_Type = "Home Loan (HL)"
                            elif Selected_Loan_Type == "Exit":
                                break
                            else:
                                print("")
                                print("------------------------------------------------------------------")
                                print("You have entered an invalid Answer, please try again.")
                                print("------------------------------------------------------------------")
                                print("")
                            with open("Loan_Registered_Customer.txt") as Loan_Registered_Customer_Txt:
                                User_Name_List = []
                                for line in Loan_Registered_Customer_Txt:
                                    line = line.strip('\n')
                                    Loan_Registered_Customer_List = line.split(",")
                                    if Loan_Type == Loan_Registered_Customer_List[3]:
                                        User_Name = Loan_Registered_Customer_List[0]
                                        User_Name_List.append(User_Name)
                            with open("Customer_Transaction.txt") as Loan_Transactions_Txt:
                                for line in Loan_Transactions_Txt:
                                    line = line.strip('\n')
                                    Loan_Transactions_List = line.split(",")
                                    for x in User_Name_List:
                                        if x == Loan_Transactions_List[0]:
                                            print("")
                                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("Name:-", "                                   ", Loan_Transactions_List[2])
                                            print("Payment Date for Monthly Installment:- ", "  ", Loan_Transactions_List[4])
                                            print("Loan Type:-", "                              ", Loan_Registered_Customer_List[3])
                                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            Made_Payments = True
                                        else:
                                            pass
                            if not Made_Payments:
                                print("")
                                print("------------------------------------------------------------------")
                                print("No payments have been made for this loan as of yet.")
                                print("------------------------------------------------------------------")
                    elif Answer == "6":
                        with open("Customer_Transaction.txt") as Transactions_Txt:
                            Made_Payments = False
                            for line in Transactions_Txt:
                                Transactions_List = line.split(",")
                                print("")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Account Name:- ", "  ", Transactions_List[0])
                                print("Loan ID:- ", "       ", Transactions_List[1])
                                print("Name:- ", "          ", Transactions_List[2])
                                print("Loan Amount:- ", "   ", Transactions_List[3])
                                print("Payment Date:- ", "  ", Transactions_List[4])
                                print("Payment Status:- ", "", Transactions_List[5])
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("")
                                Made_Payments = True
                            if not Made_Payments:
                                print("")
                                print("------------------------------------------------------------------")
                                print("No payments have been made by customers as of yet.")
                                print("------------------------------------------------------------------")
                    elif Answer == "7":
                        with open("Customer_Transaction.txt") as Transactions_Txt:
                            Made_Payments = False
                            for line in Transactions_Txt:
                                Transactions_List = line.split(",")
                                print("")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Account Name:- ", "  ", Transactions_List[0])
                                print("Loan ID:- ", "       ", Transactions_List[1])
                                print("Name:- ", "          ", Transactions_List[2])
                                print("Loan Amount:- ", "   ", Transactions_List[3])
                                print("Payment Date:- ", "  ", Transactions_List[4])
                                print("Payment Status:- ", "", Transactions_List[5])
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("")
                                Made_Payments = True
                            if not Made_Payments:
                                print("")
                                print("------------------------------------------------------------------")
                                print("No payments have been made by customers as of yet.")
                                print("------------------------------------------------------------------")
                    elif Answer == "8":
                        break
                    else:
                        print("")
                        print("------------------------------------------------------------------")
                        print("You have entered an invalid answer, please try again")
                        print("------------------------------------------------------------------")
            else:
                while True:
                    print("")
                    print("------------------------------------------------------------------")
                    print("You have entered invalid login details!")
                    print("------------------------------------------------------------------")
                    print("")
                    print("==================================================================")
                    print("Do you wish to try again? or return to the main menu?")
                    print("==================================================================")
                    print("")
                    print("1. Try again")
                    print("2. Return to the main menu")
                    print("")
                    Answer = input("Enter your choice here:- ")
                    if Answer == "1":
                        break
                    elif Answer == "2":
                        BreakCondition = True
                        break
                    else:
                        print("------------------------------------------------------------------")
                        print("You have entered an invalid answer, please try again")
                        print("------------------------------------------------------------------")

# This function allows users to choose which user type they wish to login as, after which either the Admin_Menu or Cus_Menu function is called
# Users can also immedietly exit the system from this menu
def Main_Menu():
    while True:
        print("")
        print("==================================================================")
        print("I                  WELCOME TO Malaysia Bank!                     I")
        print("I     Please select which user type do you wish to login as      I")
        print("==================================================================")
        print("")
        print("1. Admin")
        print("2. Customer")
        print("3. Exit the Program")
        print("")
        print("==================================================================")
        UserType = input("Enter your choice here:-  ")
        print("==================================================================")
        print("")
        if UserType == "1":
            Admin_Menu()
        elif UserType == "2":
            Customer_Menu()
        elif UserType == "3":
            exit("You have exited the Program")
        else:
            print("------------------------------------------------------------------")
            print("You have entered an invalid answer, please try again")
            print("------------------------------------------------------------------")


Main_Menu()
