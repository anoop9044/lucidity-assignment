import math


def create_edges(driver, restaurants, customers):
    # Driver Location will be directly connected to every restaurant.
    edges = []
    driver_location = driver.get_user_location()
    for index in range(len(restaurants)):
        restaurant_1_location = restaurants[index].get_restaurant_location()
        distance = math.sqrt(
            (driver_location[0] - restaurant_1_location[0]) ** 2 + (driver_location[1] - restaurant_1_location[1]) ** 2)
        edges.append((driver.name, restaurants[index].name, distance))
        # Every Restaurant is connected to every other restaurant
        for index_2 in range(index+1, len(restaurants)):
            restaurant_2_location = restaurants[index_2].get_restaurant_location()
            distance = math.sqrt(
                (restaurant_2_location[0] - restaurant_1_location[0]) ** 2 + (
                            restaurant_2_location[1] - restaurant_1_location[1]) ** 2)

            edges.append((restaurants[index_2].name, restaurants[index].name, distance))
            edges.append((restaurants[index].name, restaurants[index_2].name, distance))
        # Every Restaurant is connected to every customer

        for customer in customers:
            customer_location = customer.get_user_location()
            distance = math.sqrt(
                (customer_location[0] - restaurant_1_location[0]) ** 2 + (
                            customer_location[1] - restaurant_1_location[1]) ** 2)
            edges.append((customer.name, restaurants[index].name, distance))
            edges.append((restaurants[index].name, customer.name, distance))

    # Every Customer is connected to every other customer

    for index_1 in range(len(customers)):
        customer_1_location = customers[index_1].get_user_location()
        for index_2 in range(index_1+1, len(customers)):
            customer_2_location = customers[index_2].get_user_location()
            distance = math.sqrt(
                (customer_2_location[0] - customer_1_location[0]) ** 2 + (
                            customer_2_location[1] - customer_1_location[1]) ** 2)

            edges.append((customers[index_1].name, customers[index_2].name, distance))
            edges.append((customers[index_2].name, customers[index_1].name, distance))
    return edges


