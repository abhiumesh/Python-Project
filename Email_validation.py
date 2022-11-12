class emailValid:
    def __init__(self,email) -> None:
        self.email = email

    def check(self) -> bool:
        d, k = 0, 0
        if len(self.email)>=6:
            if self.email[0].isalpha():
                if (self.email).count("@")==1:
                    if (self.email[-4]=='.') ^ (self.email[-3]=='.'):
                        if(' ' not in self.email):
                            for i in self.email:
                                if i.isalpha():
                                    if i == i.upper():
                                        d = 1
                                elif i.isdigit():
                                    continue
                                elif i=='.' or i=='@' or i=='_':
                                    continue
                                else:
                                    k = 1
                            if (d==1 or k ==1):
                                return False
                            else:
                                return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False


if __name__ == "__main__":
    emailId = input("Enter Your Email Id :- ")
    email = emailValid(emailId)
    
    result:bool = email.check()

    if(result):
        print("Your Email is Correct !!")
    else:
        print("Your Email is not correct !!")