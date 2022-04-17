from models.location import Location


class Restaurant:

    def __init__(self, name, x_coordinate, y_coordinate, restaurant_counter):
        self.id = restaurant_counter
        self.name = name
        self.location = Location(x_coordinate, y_coordinate)

    def get_restaurant_location(self):
        return self.location.get_geo_coordinates()