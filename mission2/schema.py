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

    def count_training_day(self):
        return self.wed + self.sat + self.sun


@dataclass
class Player:
    id: int
    name: str
    playday: PlayDay
    remove: bool
    points: int = 0

    def __init__(self, id_number: int, name):
        self.id = int(id_number)
        self.name = name
        self.playday = PlayDay()
        self.remove = False

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

    def get_grade(self):
        if self.points >= 50:
            return 1

        if self.points >= 30:
            return 2

        return 3

    def update_remove(self):
        if self.get_grade() < 3:
            self.remove = False
            return

        if self.playday.count_training_day() < 1:
            self.remove = True
