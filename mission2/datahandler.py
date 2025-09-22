from schema import Player

class DataHandler:

    def __init__(self, file_path):
        self.file_path = file_path
        self.name_id_dict = {}
        self.id_player_data = {}

    def load_data(self):
        f = open(self.file_path, 'r')
        lines = f.readlines()
        return lines

    def refine_data(self, all_datas):
        refine_data = []

        for line_data in all_datas:
            refine_data.append(line_data.strip().split())

        return refine_data

    def get_new_id(self,):
        id_list = []
        for name, id in self.name_id_dict.items():
            id_list.append(id)

        return max(id_list) + 1

    def get_id_from_name(self, name):
        if name in self.name_id_dict.keys():
            return self.name_id_dict[name]

        if len(self.name_id_dict) == 0:
            new_id = 0
        else:
            new_id = self.get_new_id()

        self.add_new_player(name, new_id)
        return new_id

    def add_new_player(self, name, new_id: int):
        self.name_id_dict[name] = new_id
        self.id_player_data[new_id] = Player(id_number=new_id, name=name)

    def update_playday(self, name, playday):
        player_id = self.get_id_from_name(name)
        self.id_player_data[player_id].update_playday(playday)

    def get_id_player_data(self):
        return self.id_player_data


