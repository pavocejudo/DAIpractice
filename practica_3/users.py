# -*- coding: utf-8 -*-

class Users:
    def __init__(self,name, second_name, email, pay, VISA, birthday, birthmoth, birthyear, adress, password):
        name = name
        second_name= second_name
        email=email
        pay=pay
        VISA=VISA
        birthday=birthday
        birthmoth=birthmoth
        birthyear=birthyear
        adress=adress
        password=password
    def toDBCollection (self):
        return {
            "name":self.name,
            "second_name":self.second_name,
            "email":self.email,
            "pay":self.pay,
            "VISA":self.VISA,
            "birthday":self.birthday,
            "birthmoth":self.birthmoth,
            "birthyear":self.birthyear,
            "adress":self.adress,
            "password":self.password
        }

    def __str__(self):
        return "Name: %s - Second name: %s - Email: %s - pay: %s - VISA: %s- birthday: %i- birthmoth: %i- birthyear: %i- adress: %s- password: %s" \
               %(self.name,self.second_name, self.email, self.pay, self.VISA, self.birthday, self.birthmoth, self.birthyear, self.adress, self.password)
