from models.user import User


class Customer(User):

    def __init__(self, name, x_coordinate, y_coordinate,  customer_id):
        super().__init__(name, x_coordinate, y_coordinate, customer_id)