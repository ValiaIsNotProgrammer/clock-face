import math
import turtle
from time import sleep

from time_utils import generate_random_times


class ClockFace:
    def __init__(self, radius: int = 150):
        self.radius = radius
        self.center = (0, 0 + radius)
        self.turtle = turtle.Turtle()
        self.turtle.getscreen()
        self.hours_coordinates = self.get_coordinates_dict(30)
        self.minutes_coordinates = self.get_coordinates_dict(6)

    def draw_clock(self):
        self.turtle.speed(1000)
        self.turtle.circle(radius=self.radius)

        self.draw_coordinates(list(self.minutes_coordinates.values()), 3, "black")
        self.draw_coordinates(list(self.hours_coordinates.values()), 10, "red", legend=True)
        self.turtle.speed(1)

    def draw_coordinates(self, coordinates: list[tuple[int, int]], size: int, color: str, legend: bool = False):
        for i, coordinate in enumerate(coordinates):
            self.turtle.penup()
            self.turtle.goto(coordinate)
            self.turtle.dot(size, color)
            self.turtle.pendown()
            if legend:
                if i == 0:
                    i = 12
                self.turtle.write(i, font=("Arial", size, "normal"))

    def draw_arrows_from(self, time: tuple[int, int]):
        hours, minutes = time
        if hours == 12:
            hours = 0
        if minutes == 60:
            minutes = 0

        minutes_coordinates = self.minutes_coordinates[minutes]
        hour_coordinates = self.hours_coordinates[hours]
        hour_coordinates = self.get_line_by_length(direction_y=hour_coordinates[1], direction_x=hour_coordinates[0],
                                                   start_x=self.center[0], start_y=self.center[1], length=70)
        self._draw_arrows(hour_coordinates)
        self._draw_arrows(minutes_coordinates)

        mid_coordinates = self.get_midpoint(hour_coordinates, minutes_coordinates)
        angle_between = self.get_angle_from(time)

        self.turtle.penup()
        self.turtle.goto(mid_coordinates)
        self.turtle.pendown()

        align = "center" if angle_between < 150 else "right"
        self.turtle.write(str(angle_between) + "°", font=("Arial", 12, "normal"), align=align)
        self.turtle.hideturtle()

    def _draw_arrows(self, coordinates: tuple[int | float, int | float]):
        self.turtle.penup()
        self.turtle.goto(self.center)
        self.turtle.pendown()
        self.turtle.pensize(4)
        self.turtle.pencolor("red")
        self.turtle.goto(coordinates)

    @staticmethod
    def get_line_by_length(*,
                         direction_y: float, direction_x: float,
                         start_x: float = 0, start_y: float = 0,
                         length: float = 5) -> tuple[float, float]:

        angle = math.atan2(direction_y - start_y, direction_x - start_x)

        end_x = start_x + length * math.cos(angle)
        end_y = start_y + length * math.sin(angle)

        return end_x, end_y

    def get_coordinates_dict(self, degrees_step: int) -> dict[int, tuple[int, int]]:
        coordinates = self.get_coordinates(degrees_step)
        coordinates_dict = {}

        for i, coordinate in enumerate(coordinates, start=0):
            coordinates_dict[i] = coordinate
        return coordinates_dict

    def get_coordinates(self, degrees_step: int) -> list[tuple[int, int]]:
        coordinates = []
        for degree in range(90, -270, -degrees_step):
            radians = math.radians(degree)
            coordinates.append(self.get_coordinates_from(r=self.radius, theta=radians, cy=self.center[-1]))
        return coordinates

    @staticmethod
    def get_coordinates_from(*, r, theta, cx=0, cy=0):
        x = cx + r * math.cos(theta)
        y = cy + r * math.sin(theta)
        return x, y

    @staticmethod
    def get_midpoint(start: tuple[float, float], end: tuple[float, float]) -> tuple[float, float]:
        mid_x = (start[0] + end[0]) / 2
        mid_y = (start[1] + end[1]) / 2
        return mid_x, mid_y

    def clear_arrows(self):
        for _ in range(14):
            self.turtle.undo()

    @staticmethod
    def get_angle_from(time: tuple[int, int]) -> float:
        hour, minute = time

        round_ = 360

        hour_angle = hour * 30
        minute_angle = minute * 6

        diff = abs(hour_angle - minute_angle)
        if diff > 180:
            diff = round_ - diff
        return diff


if __name__ == '__main__':
    clock = ClockFace()
    clock.draw_clock()

    for time in generate_random_times(10, True):
        clock.draw_arrows_from(time)
        sleep(2)
        clock.clear_arrows()



