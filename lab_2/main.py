class Car:

    def __init__(self, wheel_width, width, height, length):
        self.wheel_width = wheel_width
        self.width = width
        self.height = height
        self.length = length


class PassengerCar(Car):

    def __init__(self, wheel_width, width, height, length, passenger_count, railroads_conductor, ticket_price):
        Car.__init__(self, wheel_width, width, height, length)
        self.passenger_count = passenger_count
        self.railroads_conductor = railroads_conductor
        self.ticket_price = ticket_price
        self.passenger_list = []

    def add_passenger(self, passenger):
        if self.passenger_list.length() >= self.passenger_count:
            raise Exception("PassengerCar is full")
        else:
            self.passenger_list.append(passenger)

    def remove_passenger(self, passenger):
        self.passenger_list.remove(passenger)


class CoupeCar(PassengerCar):

    def __init__(self, railroads_conductor):
        PassengerCar.__init__(self, 100, 120, 360, 6 * 360, 40, railroads_conductor, 50)


class RestaurantCar(PassengerCar):

    def __init__(self, railroads_conductor):
        pass


class FreightCar(Car):

    def __init__(self, wheel_width, width, height, length, volume):
        Car.__init__(self, wheel_width, width, height, length)
        self.volume = volume


class RailroadsConductor:

    def __init__(self, name):
        self.name = name


class Train:

    def __init__(self, name, engine, car_list):
        Train._check_cars(car_list)
        self.car_list = car_list
        self.engine = engine
        self.name = name

    @staticmethod
    def _check_cars(car_list):
        car_target_wheel_width = car_list[0].wheel_width
        for car in car_list:
            if car_target_wheel_width != car.wheel_width:
                raise Exception("Not all cars have same wheel_width")

    def _check_departure_ready(self):
        for car in self.car_list:
            if isinstance(car, PassengerCar):
                if not isinstance(car.railroads_conductor, RailroadsConductor):
                    raise Exception("Not all cars have railroads_conductor assigned")

    def depart(self):
        self._check_departure_ready()
        print(f"Train {self.name} departed")


if __name__ == '__main__':
    conductors = [RailroadsConductor("Kevin"), RailroadsConductor("Melanie")]
    cars = [CoupeCar(conductors[0]), CoupeCar(conductors[1]), RestaurantCar(conductors[1]),
            RestaurantCar(conductors[1]),
            FreightCar(100, 60, 360, 6 * 360, 1000)]
    train = Train("Big Alice", "WHT", cars)
    train.depart()
