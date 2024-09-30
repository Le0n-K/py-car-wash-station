class Car:
    """
    comfort_class - comfort class of a car, from 1 to 7
    clean_mark - car cleanness mark, from very dirty - 1 to absolutely clean - 10
    brand - brand of the car
    """
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    """
    distance_from_city_center - how far station from the city center, from 1.0 to 10.0
    clean_power - clean_mark to which this car wash station washes (yes, not all stations can clean your car completely)
    average_rating - average rating of the station, from 1.0 to 5.0, rounded to 1 decimal
    count_of_ratings - number of people who rated
    """
    def __init__(
            self,
            distance_from_city_center: int,
            clean_power: int,
            average_rating: int,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        """
        method, that calculates cost for a single car wash
        """
        price = (car.comfort_class * (self.clean_power - car.clean_mark)
                 * self.average_rating / self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """
        method, that washes a single car
        """
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list) -> float:
        """
        method, that takes a list of Car's, washes only cars with clean_mark < clean_power of wash station
        """
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def rate_service(self, new_rating: int) -> None:
        """
        method that adds a single rate to the wash station
        """
        rating = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round((rating + new_rating) / self.count_of_ratings, 1)
