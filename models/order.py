class Order:

    def __init__(self, customer, restaurant, order_counter):
        self.id = order_counter
        self.customer = customer
        self.restaurant = restaurant
        self.driver = None
        self.status = "PENDING"

    def set_driver(self, driver):
        self.driver = driver

    def update_order_status(self, status):
        self.status = status