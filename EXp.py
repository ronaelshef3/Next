class UsernameContainsIllegalCharacter (Exception):
   def __init__(self,username):
       pass
       self.username = username
   def __str__(self):
       return " Username contains illegal character {}".format(self.username)

class UsernameTooShort (Exception):
    def __init__(self, username):
        pass
        self.username = username

    def __str__(self):
        return " Username too short  {}".format(self.username)



class UsernameTooLong (Exception):
    def __init__(self, username):
        pass
        self.username = username

    def __str__(self):
        return " username too long  {}".format(self.username)



class PasswordMissingCharacter(Exception):
    def __init__(self, password ):
        pass
        self.password  = "*"*len(password)

    def __str__(self):
        return "Password Missing Character {}".format(self.password)
def check(username, password):
    if '1' in username:
        raise UsernameContainsIllegalCharacter(username)
    elif len(username)> 30:
        raise UsernameTooLong(username)
    elif len(username) < 3 :
        raise UsernameTooShort(username)
    elif "&"  in password:
        raise PasswordMissingCharacter(password)

check("th",'454758878')