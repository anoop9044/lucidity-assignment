from models.customer import Customer
from models.driver import Driver
from models.order import Order
from models.restaurant import Restaurant
from utils.edges import create_edges
from utils.graph import Graph
from utils.min_path import min_path


class DeliveryOptimizer:
    def __init__(self):
        self.__customer_counter = 0
        self.__driver_counter = 0
        self.__restaurant_counter = 0
        self.__order_counter = 0
        self.drivers = {}
        self.customers = {}
        self.restaurants = {}
        self.orders = {}
        self.delivered_orders = {}

    def add_customer(self, name, x_coordinate, y_coordinate):
        self.__customer_counter += 1
        customer = Customer(name=name,
                            x_coordinate=x_coordinate,
                            y_coordinate=y_coordinate,
                            customer_id=self.__customer_counter)
        self.customers[customer.id] = customer
        print(f"Customer Added, id is {customer.id}")

    def add_driver(self, name, x_coordinate, y_coordinate):
        self.__driver_counter += 1
        driver = Driver(name=name,
                        x_coordinate=x_coordinate,
                        y_coordinate=y_coordinate,
                        driver_id=self.__driver_counter)
        self.drivers[driver.id] = driver
        print(f"Driver Added, id is {driver.id}")

    def add_restaurant(self, name, x_coordinate, y_coordinate):
        self.__restaurant_counter += 1
        restaurant = Restaurant(name=name,
                                x_coordinate=x_coordinate,
                                y_coordinate=y_coordinate,
                                restaurant_counter=self.__restaurant_counter)
        self.restaurants[restaurant.id] = restaurant
        print(f"Restaurant Added, id is {restaurant.id}")

    def add_order(self, customer_id, restaurant_id):
        self.__order_counter += 1
        if not self.customers.get(customer_id):
            print(f"Customer with id {customer_id} not found.")
            return
        if not self.restaurants.get(restaurant_id):
            print(f"Restaurant with id {restaurant_id} not found.")
            return
        order = Order(self.customers.get(customer_id), self.restaurants.get(customer_id), self.__order_counter)
        self.orders[order.id] = order
        print(f"Order generated with id {order.id}")

    def deliver_order(self, driver_id):
        if not self.drivers.get(driver_id):
            print(f"Driver with id {driver_id} not found.")
            return
        driver = self.drivers.get(driver_id)
        restaurant_orders = []
        customer_orders = []
        for order in self.orders:
            restaurant_orders.append(self.orders[order].restaurant)
            customer_orders.append(self.orders[order].customer)
            self.orders[order].set_driver(driver)
            self.orders[order].update_order_status("DELIVERED")

        graph = Graph()
        edges = create_edges(driver, restaurant_orders, customer_orders)
        for edge in edges:
            graph.add_edge(*edge)

        shortest_path = min_path(graph, driver.name,
                                 [restaurant_order.name for restaurant_order in restaurant_orders]
                                 , [customer_order.name for customer_order in customer_orders])
        driver_current_location = [self.customers[customer].location for customer in self.customers if
                                   self.customers[customer].name == shortest_path[-1]]
        driver.update_driver_location(driver_current_location)
        self.delivered_orders.update(self.orders)
        self.orders = {}
        print("-->".join(shortest_path))
