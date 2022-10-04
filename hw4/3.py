
class Password_manager:
    def __init__(self,old_password,your_password):
        self.old_password = old
        self.your_password = your

    def get_password(self):
        return old[-1]

    def is_correct(self):
        if your in old:
            return True
        else:
            print("password is wrong. Enter new password for resert")

    def set_password(self):
        npass = input("Enter new password: ")
        old= open('list.txt', 'a+')
        print(npass, file=old)
        old.close()

old= open('list.txt').read()
old = old.split()

your = input("Enter your pasword:")

s= Password_manager(old,your)

s.is_correct()

if your in old:
    print('match')
else:
    s.set_password()    