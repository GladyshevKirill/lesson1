from addres import *
from mail import *

order = Mailing(addres1, addres2, 340, 8)

print('Отравление', order.get_track(), 'из', addres1.get_info(), 'в', addres2.get_info(),'. Стоимость', order.get_cost(), 'рублей.')