from schema import Player

name_id_data = {}
id_player_data = {}
total_player = 0

attendance_file = "attendance_weekday_500.txt"
grade_dict = {
    1: "GOLD",
    2: "SILVER",
    3: "NORMAL",
}


def get_new_id():
    id_list = []
    for name, id in name_id_data.items():
        id_list.append(id)

    return max(id_list) + 1


def get_id_from_name(name):
    global id_player_data, total_player, name_id_data
    if name in name_id_data.keys():
        return name_id_data[name]

    if len(name_id_data) == 0:
        new_id = 0
    else:
        new_id = get_new_id()

    name_id_data[name] = new_id
    total_player += 1
    id_player_data[new_id] = Player(id_number=new_id, name=name)

    return new_id


def update_attendance(name, day):
    id = get_id_from_name(name)
    id_player_data[id].update_playday(day)


def print_remove_player():
    print("\nRemoved player")
    print("==============")
    for id in range(total_player):
        id_player_data[id].update_remove()
        if id_player_data[id].remove == True:
            print(id_player_data[id].name)


def print_all_player_info():
    for id in range(total_player):
        id_player_data[id].update_points()

        name = id_player_data[id].name
        points = id_player_data[id].points
        grade = id_player_data[id].get_grade()

        print(f"NAME : {name}, POINT : {points}, GRADE : {grade_dict[grade]}")


def read_data():
    try:
        with open(attendance_file, encoding='utf-8') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                attendance_data = line.strip().split()
                if len(attendance_data) == 2:
                    update_attendance(name=attendance_data[0], day=attendance_data[1])
                else:
                    print("Wrong input type error")
                    raise TypeError

    except FileNotFoundError as e:
        print(f"파일을 찾을 수 없습니다. {e}")

class Attendance:

    def __init__(self):
        self.name_id_dict = dict()
        self.id_player_data_dict = dict()

    def get_total_player(self):
        return len(self.id_player_data_dict)

    def read_data(self, data_path):
        try:
            with open(data_path, encoding='utf-8') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    attendance_data = line.strip().split()
                    if len(attendance_data) == 2:
                        update_attendance(name=attendance_data[0], day=attendance_data[1])
                    else:
                        print("Wrong input type error")
                        raise TypeError

        except FileNotFoundError as e:
            print(f"파일을 찾을 수 없습니다. {e}")

def main():
    read_data()
    print_all_player_info()
    print_remove_player()


if __name__ == "__main__":
    main()
