from abc import abstractmethod
from schema import Player

grade_dict = {
    1: "GOLD",
    2: "SILVER",
    3: "NORMAL",
}


class Printer:

    @abstractmethod
    def print(self, ):
        pass

    @abstractmethod
    def update_data(self, id_player_data):
        pass


class PlayerPrinter(Printer):

    def print(self, ):
        for player_id in range(self.data_size):
            name = self.id_player_data[player_id].name
            points = self.id_player_data[player_id].points
            grade = self.id_player_data[player_id].get_grade()

            print(f"NAME : {name}, POINT : {points}, GRADE : {grade_dict[grade]}")

    def update_data(self, id_player_data):
        self.data_size = len(id_player_data)
        self.id_player_data = id_player_data


class RemoverPrinter(Printer):

    def print(self, ):
        print("\nRemoved player")
        print("==============")
        for player_id in range(self.data_size):
            self.id_player_data[player_id].update_remove()
            if self.id_player_data[player_id].remove:
                print(self.id_player_data[player_id].name)

    def update_data(self, id_player_data):
        self.data_size = len(id_player_data)
        self.id_player_data = id_player_data
