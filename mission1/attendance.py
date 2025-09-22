from schema import Player

# name, id
name_dict = {}

# id, player
player_info = {}
total_player = 0

# attendance_file = "mission1/attendance_weekday_500.txt"


attendance_file = "attendance_weekday_500.txt"

def get_new_id():
    id_list = []
    for name, id in name_dict.items():
        id_list.append(id)

    return max(id_list) + 1


def get_id_from_name(name):
    global player_info, total_player, name_dict
    if name in name_dict.keys():
        return name_dict[name]

    if len(name_dict) == 0:
        new_id = 0
    else:
        new_id = get_new_id()

    name_dict[name] = new_id
    total_player += 1
    player_info[new_id] = Player(id_number=new_id, name=name)

    return new_id


def update_player_info(player, day):
    player.update_playday(day)


def update_attendance(name, day):
    id = get_id_from_name(name)

    update_player_info(player_info[id], day)


def get_grade(points):
    if points >= 50:
        return 1

    if points >= 30:
        return 2

    return 3


def print_remove_player():
    print("\nRemoved player")
    print("==============")
    for id in range(total_player):
        player_info[id].update_remove()
        if player_info[id].remove:
            print(player_info[id].name)


def print_all_player_info():
    for id in range(total_player):
        player_info[id].update_points()

        name = player_info[id].name
        points = player_info[id].points
        grade = player_info[id].get_grade()

        print(f"NAME : {name}, POINT : {points}, GRADE : ", end="")
        if grade == 1:
            print("GOLD")
        elif grade == 2:
            print("SILVER")
        else:
            print("NORMAL")


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
    except FileNotFoundError as e:
        print(f"파일을 찾을 수 없습니다. {e}")


def main():
    read_data()
    print_all_player_info()
    print_remove_player()


if __name__ == "__main__":
    main()
