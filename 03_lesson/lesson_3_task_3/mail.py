from addres import Addres

class Mailing:

    def __init__(self, to_addres, from_addres, cost, track):
        self.to_addres = to_addres
        self.from_addres = from_addres
        self.cost = int(cost)
        self.track = str(track)

    def get_to_addres(self):
        return self.to_addres
    
    def get_from_addres(self):
        return self.from_addres
    
    def get_cost(self):
        return self.cost
    
    def get_track(self):
        return self.track
    
addres1 = Addres('156987', 'Санкт-Петербург', 'Плесецкая', '10', '2670')
addres2 = Addres('156345', 'Санкт-Петербург', 'Беговая', '3', '32')
