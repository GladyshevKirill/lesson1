class Address:

    def __init__(self, index, town, street, building, apartment):
        self.index = index
        self.town = town
        self.street = street
        self.building = building
        self.apartment = apartment

    def get_info(self):
        return f"{self.index}, {self.town}, {self.street}, {self.building}-{self.apartment}"
    


    