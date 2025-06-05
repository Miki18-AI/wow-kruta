class UserMail:
    def __init__(self, name, years, email, login):
        self.__email = email
        self.login = login

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        if new_email.count("@") == 1:
            self.__email = new_email
        else:
            self.__email = "Ошибочная почта"


k = UserMail("fdsfdsfdsfs", "fdsfdsfdsfds.you")
k.email = "fsdfdsfds@fdsfds.you"

print(k.email)
