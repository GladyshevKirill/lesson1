from smartphone import Smartphone

phone1 = Smartphone('iphone', '13', '+79095678990')
phone2 = Smartphone('iphone', '14 pro', '+79800987765')
phone3 = Smartphone('Xaomi', '10', '+79909876545')
phone4 = Smartphone('realme', 'ultra super 1', '+79603456234')
phone5 = Smartphone('iphone', 'XX', '+77777777777')

p1 = phone1.say_info()
p2 = phone2.say_info()
p3 = phone3.say_info()
p4 = phone4.say_info()
p5 = phone5.say_info()
phone_catalog = [p1, p2, p3, p4, p5]

for i in phone_catalog:
    print(i)
