import random

class UserData:
    def __init__(self, userFile="userData_file.txt"):
        self.filename = userFile
        self.logged_in_user = None
    
    # Register a New User
    def register_user(self):
        print("="*20 + "  Register New User  " + "="*20)

        username = input("\t\t  Create Username : ")
        password = input("\t\t  Create a strong Password : ")

        # Check the entered username is already exist or not. if exist not accept the data
        try:
            with open(self.filename, 'r') as Userfile:
                users = Userfile.readlines()
                for user in users:
                    stored_username,_ = user.strip().split(", ")
                    if stored_username == username:
                        print("Username already exists. please choose another one.")
                        return
        
        except FileNotFoundError:
            pass
        except ValueError:
            print("Username Can not be in digits. ")
            return
        
        otp = random.randint(100000, 999999)
        print(f"An OTP has been sent to your device : {otp} \n")
        try:
            entered_otp = int(input("Ente OTP here : "))
        except ValueError:
            print("Invalid OTP input. please enter valid number. ")
            return
        if entered_otp == otp:
            print("*"*20 + " OTP Verified Successfully " + "*"*20) 

            # Save the user data in user_data.txt file
            try:
                with open(self.filename, 'a') as userFile:
                    userFile.write(f"{username}, {password}\n")
                print("Registration Successful ! you can now log in. ")
            except:
                print("An error occurred while saving user data. ")
        else:
            print("Invalid OTP. Registration failed. ")

    def login_user(self):
        print("="*15 + "  User Login  " + "="*15 + "\n")
        username = input("\t\t Enter Your username: ")
        password = input("\t\t Enter Password: ")

        try:
            with open(self.filename, 'r') as userFile:
                users = userFile.readlines()
                
            for user in users:
                stored_username, stored_password = user.strip().split(", ")
                if  stored_username == username :
                    if stored_password == password:
                        print("Login Successful !")
                        self.logged_in_user = stored_username
                        return True
                    else:
                        print("Password is incorrect.")
                        return False
            print("Username is invalid. ")
            return False
                    
        except FileNotFoundError:
            print("No Registered Data found. please register first. ")
            return False
    
    def logged_userName(self):
        return self.logged_in_user



