from models.user import User


class Driver(User):

    def __init__(self, name, x_coordinate, y_coordinate, driver_id):
        super().__init__(name, x_coordinate, y_coordinate, driver_id)

    def update_driver_location(self, location):
        self.location = location