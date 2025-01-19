import os
import random

class Admin:
    def login_admin(self):
        admin_UserName = "Car_managementAdmin18"
        admin_Password = "management@2003"

        try:
            input_username = input("\t\t  Enter Username : ")
            input_password = input("\t\t  Enter Password : ")
            if input_username == admin_UserName:
                if input_password == admin_Password:
                    print("Login Successfully !!! ")
                    return True
                else:
                    return False
            else:
                return False
        except ValueError:
            print("Please enter valid input. Admin data Can not be in numbers. ")

































#     def __init__(self, filename="admin_data.txt"):
#         self.filename = filename

#     # Register new admin
#     def register_admin(self):
#         print("="*20 + "  Register New Admin  "+ "="*20)
#         # Get Admin name, mobile number, username and password 
        
#         Admin_name = input("\t\t  Enter your name : ")
#         mobile_num = int(input("\t\t  Enter Mobile Number: "))
#         username = input("\t\t  Enter Username : ")
#         password = input("\t\t  Enter password : ")
#         otp = random.randint(100000,999999)  # generate a 6 digit otp
#         print(f"An OTP has been sent to your device: {otp}\n")
#         entered_otp = int(input("\t\t  Enter the OTP : "))
#         if entered_otp == otp :
#             print(" " *30 + "  OTP Verified Successfully!  " + " " * 30 + "\n")
#             if not os.path.exists(self.filename):
#                 with open(self.filename, 'w') as adminFile:
#                     adminFile.write(f"{Admin_name}, {mobile_num}, {username}, {password}\n")
#             else:
#                 with open(self.filename, 'a') as adminFile:
#                     adminFile.write(f"{Admin_name}, {mobile_num}, {username}, {password}\n")
#             print("Registration successful ! You can now log in. ")

#     def login_admin(self):
#         print("="*15 + "  Admin Login " + "=" * 15)
#         username = input("\t\t Enter your username: ")
#         password = input("\t\t Enter password: ")

#         try:
#             with open(self.filename, 'r+') as adminFile:
#                 users = adminFile.readlines()
#                 for admin in adminFile:
#                     adminData = admin.strip().split(", ")   
#                     admin_username = adminData[2]
#                     admin_password = adminData[3]
#                     if username == admin_username and password == admin_password:
#                         print("Login Successful !")
#                         return True
#                     if username == admin_username and password != admin_username:
#                         print("Password is Incorrect. ")
#                         return False
#                     if username != admin_username and password == admin_password:
#                         print("Username is invalid. ")
#                         return False
#                     elif username != admin_username and password != admin_password:
#                         print("Invalid Credentials, please try again. ")
#                         return False
                        

#         except FileNotFoundError:
#             print("No Registerd admins found. please register first. ")
#             return False
# admin = Admin()
# admin.login_admin()
