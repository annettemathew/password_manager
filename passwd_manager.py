# Question 1
# Write a class called Password_manager.
# The class should have a list called old_passwords that holds all of the user’s past passwords.
# The last item of the list is the user’s current password.
# There should be a method called get_password() that returns the current password
# and a method called set_password() that sets the user’s password.
# The set_password() method should only change the password if the attempted password
# is different from the user’s past three passwords.
# Finally, create a method called is_correct() that receives a string and
# returns a boolean True or False depending on whether the string entered by the user
# is equal to the current password or not.

from random import randint
class Password_manager:
    def __init__(self):
        self.old_passwords = []
    def get_password(self):
        if(len(self.old_passwords) == 0):
            print("Error: You don't have any password set yet.")
            return ""
        return self.old_passwords[len(self.old_passwords) - 1]
    def set_password(self, new_password):
        if (len(self.old_passwords) == 0):
            self.old_passwords.append(new_password)
        if(len(self.old_passwords) >= 3):
            if(new_password != self.old_passwords[len(self.old_passwords) - 1] \
                    and new_password != self.old_passwords[len(self.old_passwords) - 2] and \
                    new_password != self.old_passwords[len(self.old_passwords) - 3] ):
                self.old_passwords.append(new_password)
            else:
                print("Error: Your new password must be different from the last three passwords.")
        elif(len(self.old_passwords) == 2):
            if (new_password != self.old_passwords[0] and new_password != self.old_passwords[1]):
                self.old_passwords.append(new_password)
        else: # length of old_passwords = 1
            if(new_password != self.old_passwords[0]):
                self.old_passwords.append(new_password)
    # checks if user attempt is equal to current password
    def is_correct(self, attempt):
        if(attempt == self.old_passwords[len(self.old_passwords) - 1]):
            return True
        else:
            print("Error: This password is not correct.")
            return False

print("Hi! Welcome to Password Manager!")
P = Password_manager()
P.get_password()
P.set_password("123")


for x in range(0, 10):
    print('')
    attempt = input("Please enter your password: ")
    print(P.is_correct(attempt))
    choice = input("Would you like to change your password(Y/N)? ")
    choice = choice.upper()
    if(choice == 'Y'):
        input_passwd = input("Please enter your new password: ")
        # print(input_passwd)
        P.set_password(input_passwd)
    if(choice != 'Y' and choice != 'N'):
        print("Error: That is not a valid choice")