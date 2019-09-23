
class Frame:

    image = None

    cars = []

    def __init__(self, image, cars):
        self.image = image.copy()
        self.cars = cars
