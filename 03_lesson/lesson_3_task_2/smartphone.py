class Smartphone:

    def __init__(self, phone_mark, phone_model, phone_number):
        self.pmark = phone_mark
        self.pmod = phone_model
        self.pnum = phone_number

    def say_info(self):
        return f"{self.pmark}-{self.pmod}. {self.pnum}"