from dataclasses import dataclass


@dataclass
class PlayDay:
    mon: int = 0
    tues: int = 0
    wed: int = 0
    thur: int = 0
    fri: int = 0
    sat: int = 0
    sun: int = 0


@dataclass
class Player:
    id: int
    name: str
    playday: PlayDay
    points: int = 0

    def __init__(self, id_number: int, name):
        self.id = int(id_number)
        self.name = name
        self.playday = PlayDay()

    def update_playday(self, day):
        if day.lower() == "monday":
            self.playday.mon += 1
        elif day.lower() == "tuesday":
            self.playday.tues += 1
        elif day.lower() == "wednesday":
            self.playday.wed += 1
        elif day.lower() == "thursday":
            self.playday.thur += 1
        elif day.lower() == "friday":
            self.playday.fri += 1
        elif day.lower() == "saturday":
            self.playday.sat += 1
        elif day.lower() == "sunday":
            self.playday.sun += 1

    def update_points(self):
        points = 0

        points += self.playday.mon * 1
        points += self.playday.tues * 1
        points += self.playday.wed * 3
        points += self.playday.thur * 1
        points += self.playday.fri * 1
        points += self.playday.sat * 2
        points += self.playday.sun * 2

        if self.playday.wed >= 10:
            points += 10

        if self.playday.sat + self.playday.sun >= 10:
            points += 10

        self.points = points

    def get_points(self):
        return self.points

    def get_name(self):
        return self.name






