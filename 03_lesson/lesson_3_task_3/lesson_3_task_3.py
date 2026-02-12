from address import *
from mail import *

addres1 = Address('156987', 'Санкт-Петербург', 'Плесецкая', '10', '2670')
addres2 = Address('156345', 'Санкт-Петербург', 'Беговая', '3', '32')

order = Mailing(addres1, addres2, 340, 8)

print('Отравление', order.get_track(), 'из', addres1.get_info(), 'в', addres2.get_info(),'. Стоимость', order.get_cost(), 'рублей.')