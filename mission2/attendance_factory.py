from datahandler import DataHandler
from printer import PlayerPrinter, RemoverPrinter

class AttendanceFactory:
    def __init__(self, attendance_file):
        self.data_handler = DataHandler(attendance_file)
        self.info_printer = PlayerPrinter()
        self.remover_printer = RemoverPrinter()
