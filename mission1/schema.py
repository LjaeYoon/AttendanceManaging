from dataclasses import dataclass

@dataclass
class PlayDay:
    monday: int = 0
    tuesday: int = 0
    wednesday: int = 0
    thursday: int = 0
    friday: int = 0
    saturday: int = 0
    sunday: int = 0


@dataclass
class Player:
    id: int
    name: str
    playday: PlayDay
    score: int = 0

    def __init__(self, id_number: int):
        self.id = int(id_number)



