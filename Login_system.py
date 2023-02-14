# OOP - Login system

class User:
    name = ""
    email = ""
    password = ""
    login = False

    def login(self):
        email = input("Enter Email: ")
        password = input("Enter Password: ")

        if email == self.email and password == self.password:
            login = True
            print("Login Success")
        else:
            print("Login Failed")

    def logout(self):
        login = False
        print("Logout Successfully")

    def isLoggedIn(self):
        if (self.login):
            return True
        else:
            return False

    def profile(self):
        if self.isLoggedIn():
            print("Your Username: ", self.name, " & Email: ", self.email)
            input("")
        else:
            print("User is not Logged in !")


# calling object for User1.
user1 = User()
user1.name = "Irtaza"
user1.email = "irtaza@mail.com"
user1.password = "12345"

user1.login()
user1.profile()

# for stable to code output window
hello = input()
