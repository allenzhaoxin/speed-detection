import math


class SpeedController:

    frames_per_second = 0
    pixels_per_meters = 8

    def speed_calculation(self, old_location, new_location):
        new_start_x = new_location[0]
        new_start_y = new_location[1]

        old_start_x = old_location[0]
        old_start_y = old_location[1]

        distance_moved = math.sqrt(math.pow(new_start_x - old_start_x, 2) + math.pow(new_start_y - old_start_y, 2))
        pixels_moved = distance_moved / self.pixels_per_meters
        pixels_moved_per_second = pixels_moved * self.frames_per_second
        speed = pixels_moved_per_second * 3.6

        return speed
