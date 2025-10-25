#for user
class User:
    def __init__(self,username,email,age):
        self.username = username
        self.email= email
        self.age= age
    def login(self):
        print(f"{self.username} is logged in")

    def logout(self):
        print(f"{self.username} has logged out")

    def show_details(self):
        print(f"Username: {self.username}, Email: {self.email}, Age: {self.age}")
#Admin 
class Admin(User):
    def __init__(self, username, email, age, phone):
        super().__init__(username, email, age)
        self.role = "admin"
        self.phone = phone

   
    def login(self):
        print("Admin is logged in")

    def showProduct(self):
        print("Showing all products")

    def addProducts(self):
        print("Product added successfully")

    def editProducts(self):
        print("Product edited successfully")

user = User("user", "user@gmail.com", 20)
admin = Admin("tayyaba", "tayyaba@gmail.com", 30, "4567893211")
#usercall
user.login()
user.show_details()
user.logout()

#admincall
admin.login()
admin.show_details()
admin.showProduct()
admin.addProducts()
admin.editProducts()
admin.logout()