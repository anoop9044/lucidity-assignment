class Location:
    def __init__(self, x_coordinate, y_coordinate):
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate

    def get_geo_coordinates(self):
        return [self.__x_coordinate, self.__y_coordinate]