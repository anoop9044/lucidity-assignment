from models.location import Location


class User:
    def __init__(self, name, x_coordinate, y_coordinate, id):
        self.id = id
        self.name = name
        self.location = Location(x_coordinate, y_coordinate)

    def get_user_location(self):
        return self.location.get_geo_coordinates()
