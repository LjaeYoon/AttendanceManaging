from attendance_factory import AttendanceFactory

ATTENDANCEFILE = "attendance_weekday_500.txt"


class Attendance:
    id_player_data: dict

    def __init__(self):
        self.attendance_factory = AttendanceFactory(ATTENDANCEFILE)

    def run(self):
        text_datas = self.attendance_factory.data_handler.load_data()
        line_datas = self.attendance_factory.data_handler.refine_data(text_datas)

        self.update_player_data(line_datas)
        self.id_player_data = self.attendance_factory.data_handler.get_id_player_data()
        self.update_player_points_and_remove()

        self.attendance_factory.remover_printer.update_data(self.id_player_data)
        self.attendance_factory.info_printer.update_data(self.id_player_data)

        self.print_all()

    def get_player_counts(self):
        return len(self.id_player_data)

    def update_player_data(self, line_datas):
        for [name, playday] in line_datas:
            self.attendance_factory.data_handler.update_playday(name, playday)

    def update_player_points_and_remove(self):
        player_counts = self.get_player_counts()
        for player in range(player_counts):
            self.id_player_data[player].update_points()

    def print_all(self):
        self.attendance_factory.info_printer.print()
        self.attendance_factory.remover_printer.print()


if __name__ == "__main__":
    attendance = Attendance()
    attendance.run()
