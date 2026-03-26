class User:
    def __init__(self, first_name, last_name):
        self.fn = first_name
        self.ln = last_name

    def say_first_name(self):
        print('Ваше имя:', self.fn)

    def say_last_name(self):
        print('Ваша фамилия: ', self.ln)

    def say_last_first_name(self):
        print('Ваше имя/фамилия: ', self.fn, self.ln)


    