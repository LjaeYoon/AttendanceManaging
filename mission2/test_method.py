import pytest

import attendance
from attendance import *
from datahandler import DataHandler
from printer import PlayerPrinter, RemoverPrinter
from schema import PlayDay


# @pytest.mark.skip()
def test_data_load():
    attendance_file = "attendance_weekday_500.txt"
    data_handler = DataHandler(attendance_file)
    answer = ['Umar monday\n', 'Daisy tuesday\n', 'Alice tuesday\n', 'Xena saturday\n', 'Ian tuesday\n',
              'Hannah monday\n', 'Hannah thursday\n', 'Ethan wednesday\n', 'Xena wednesday\n', 'Daisy tuesday\n',
              'Vera saturday\n', 'Xena sunday\n', 'Rachel friday\n', 'Charlie tuesday\n', 'Hannah friday\n',
              'Steve sunday\n', 'Ian friday\n', 'Xena saturday\n', 'Vera saturday\n', 'Nina sunday\n', 'Bob friday\n',
              'Ethan friday\n', 'Xena sunday\n', 'Nina wednesday\n', 'Hannah saturday\n', 'Xena friday\n',
              'Vera friday\n', 'Xena tuesday\n', 'Alice monday\n', 'Nina tuesday\n', 'Nina friday\n', 'Steve sunday\n',
              'Ian wednesday\n', 'Alice friday\n', 'Charlie monday\n', 'Xena tuesday\n', 'George friday\n',
              'Hannah monday\n', 'Umar sunday\n', 'Charlie tuesday\n', 'Daisy thursday\n', 'Quinn friday\n',
              'Tina thursday\n', 'Alice tuesday\n', 'Hannah saturday\n', 'Rachel saturday\n', 'George thursday\n',
              'Xena monday\n', 'Hannah tuesday\n', 'Will wednesday\n', 'Xena monday\n', 'Umar monday\n',
              'Rachel monday\n', 'Charlie friday\n', 'Umar sunday\n', 'Charlie saturday\n', 'Hannah friday\n',
              'Steve wednesday\n', 'Rachel wednesday\n', 'Nina saturday\n', 'Will tuesday\n', 'Daisy sunday\n',
              'Vera tuesday\n', 'Steve saturday\n', 'Tina tuesday\n', 'Hannah friday\n', 'Hannah sunday\n',
              'Will thursday\n', 'Hannah sunday\n', 'Xena saturday\n', 'Hannah wednesday\n', 'Alice thursday\n',
              'Nina thursday\n', 'Rachel wednesday\n', 'Will tuesday\n', 'Nina sunday\n', 'George friday\n',
              'Will saturday\n', 'Xena wednesday\n', 'Alice monday\n', 'Daisy monday\n', 'Nina monday\n',
              'Alice tuesday\n', 'Hannah sunday\n', 'Charlie wednesday\n', 'George friday\n', 'Will wednesday\n',
              'Will tuesday\n', 'Alice tuesday\n', 'Daisy friday\n', 'Will sunday\n', 'Alice wednesday\n',
              'Ethan monday\n', 'Hannah wednesday\n', 'Rachel tuesday\n', 'Hannah tuesday\n', 'Oscar sunday\n',
              'Hannah wednesday\n', 'Steve wednesday\n', 'Nina friday\n', 'Rachel thursday\n', 'George sunday\n',
              'Alice saturday\n', 'Nina wednesday\n', 'Xena monday\n', 'Ethan monday\n', 'Xena thursday\n',
              'Daisy thursday\n', 'Steve thursday\n', 'Rachel saturday\n', 'Alice tuesday\n', 'George tuesday\n',
              'Hannah tuesday\n', 'Nina wednesday\n', 'George monday\n', 'Rachel sunday\n', 'George sunday\n',
              'Will thursday\n', 'Daisy sunday\n', 'Xena saturday\n', 'Charlie thursday\n', 'Tina friday\n',
              'Daisy friday\n', 'Ethan saturday\n', 'Tina saturday\n', 'Rachel friday\n', 'Charlie monday\n',
              'Hannah thursday\n', 'Nina wednesday\n', 'Rachel thursday\n', 'Hannah friday\n', 'Ian friday\n',
              'Hannah wednesday\n', 'Daisy tuesday\n', 'Hannah sunday\n', 'Tina thursday\n', 'George wednesday\n',
              'Hannah tuesday\n', 'Xena monday\n', 'Oscar sunday\n', 'Hannah saturday\n', 'George tuesday\n',
              'Vera saturday\n', 'Rachel wednesday\n', 'Nina wednesday\n', 'Nina sunday\n', 'Hannah saturday\n',
              'Tina saturday\n', 'Charlie thursday\n', 'Nina monday\n', 'Alice tuesday\n', 'Charlie saturday\n',
              'Alice wednesday\n', 'Ian friday\n', 'Vera wednesday\n', 'Ian wednesday\n', 'Nina sunday\n',
              'Ian wednesday\n', 'Quinn saturday\n', 'Nina sunday\n', 'Xena tuesday\n', 'Umar friday\n',
              'Hannah friday\n', 'Ethan thursday\n', 'Nina friday\n', 'Tina tuesday\n', 'Hannah tuesday\n',
              'Alice thursday\n', 'Alice thursday\n', 'Nina saturday\n', 'Xena monday\n', 'Xena monday\n',
              'Ian tuesday\n', 'Alice saturday\n', 'Alice saturday\n', 'Daisy sunday\n', 'Tina monday\n',
              'Bob monday\n', 'Ethan monday\n', 'Alice sunday\n', 'Hannah sunday\n', 'Umar monday\n', 'Ethan friday\n',
              'Alice thursday\n', 'Rachel friday\n', 'Rachel saturday\n', 'Ethan sunday\n', 'Will thursday\n',
              'Alice wednesday\n', 'Hannah thursday\n', 'Hannah thursday\n', 'Rachel tuesday\n', 'Daisy sunday\n',
              'Steve friday\n', 'Xena thursday\n', 'Alice thursday\n', 'Xena thursday\n', 'Oscar tuesday\n',
              'Steve sunday\n', 'Charlie friday\n', 'Charlie sunday\n', 'Alice monday\n', 'Charlie thursday\n',
              'Hannah tuesday\n', 'Ethan monday\n', 'Nina monday\n', 'Charlie tuesday\n', 'Rachel thursday\n',
              'Rachel sunday\n', 'Xena friday\n', 'Hannah tuesday\n', 'Tina tuesday\n', 'Tina tuesday\n',
              'Xena friday\n', 'Umar wednesday\n', 'Charlie wednesday\n', 'Ethan monday\n', 'Hannah thursday\n',
              'Xena saturday\n', 'Rachel friday\n', 'Rachel wednesday\n', 'Xena tuesday\n', 'Ian sunday\n',
              'Xena friday\n', 'Steve tuesday\n', 'Xena tuesday\n', 'Nina friday\n', 'Ethan thursday\n',
              'Nina thursday\n', 'George sunday\n', 'George monday\n', 'Hannah friday\n', 'Nina tuesday\n',
              'Oscar saturday\n', 'Umar saturday\n', 'George tuesday\n', 'Steve saturday\n', 'Umar tuesday\n',
              'Will friday\n', 'Alice tuesday\n', 'Daisy saturday\n', 'Umar wednesday\n', 'Umar saturday\n',
              'Umar sunday\n', 'Hannah sunday\n', 'Ethan wednesday\n', 'Xena friday\n', 'Umar monday\n',
              'Nina thursday\n', 'Bob thursday\n', 'Umar thursday\n', 'Xena monday\n', 'Xena sunday\n',
              'Daisy tuesday\n', 'Hannah thursday\n', 'Steve tuesday\n', 'Daisy wednesday\n', 'Xena wednesday\n',
              'Ethan thursday\n', 'Daisy tuesday\n', 'Steve sunday\n', 'Rachel thursday\n', 'Tina thursday\n',
              'Umar monday\n', 'Hannah saturday\n', 'Rachel saturday\n', 'George sunday\n', 'Charlie thursday\n',
              'Umar friday\n', 'Ethan thursday\n', 'Will saturday\n', 'Ethan thursday\n', 'Hannah sunday\n',
              'Bob thursday\n', 'Ethan wednesday\n', 'Rachel friday\n', 'Xena monday\n', 'Daisy friday\n',
              'Oscar monday\n', 'George saturday\n', 'Will tuesday\n', 'Will sunday\n', 'Charlie sunday\n',
              'Nina saturday\n', 'Nina wednesday\n', 'Charlie saturday\n', 'Alice sunday\n', 'Alice thursday\n',
              'Daisy monday\n', 'Charlie friday\n', 'Daisy friday\n', 'Ethan friday\n', 'Charlie wednesday\n',
              'Xena saturday\n', 'Steve friday\n', 'Charlie monday\n', 'Ian monday\n', 'Xena thursday\n',
              'Rachel tuesday\n', 'Hannah thursday\n', 'Rachel tuesday\n', 'Tina wednesday\n', 'Hannah thursday\n',
              'Hannah wednesday\n', 'Vera friday\n', 'Rachel friday\n', 'Rachel friday\n', 'Hannah tuesday\n',
              'Xena monday\n', 'Nina monday\n', 'Bob tuesday\n', 'Nina tuesday\n', 'Rachel saturday\n', 'Xena sunday\n',
              'Hannah thursday\n', 'Steve wednesday\n', 'Xena saturday\n', 'Charlie sunday\n', 'Nina thursday\n',
              'Umar wednesday\n', 'Hannah friday\n', 'George sunday\n', 'Rachel thursday\n', 'Daisy wednesday\n',
              'Hannah wednesday\n', 'Tina sunday\n', 'Xena tuesday\n', 'Daisy sunday\n', 'Alice wednesday\n',
              'Umar wednesday\n', 'Hannah saturday\n', 'Daisy friday\n', 'Ethan sunday\n', 'Charlie thursday\n',
              'Charlie friday\n', 'Daisy saturday\n', 'Umar monday\n', 'Xena tuesday\n', 'Oscar tuesday\n',
              'Will saturday\n', 'Xena saturday\n', 'Umar monday\n', 'Bob friday\n', 'Hannah wednesday\n',
              'Hannah thursday\n', 'Alice monday\n', 'Charlie monday\n', 'Daisy tuesday\n', 'Will sunday\n',
              'Charlie thursday\n', 'Rachel monday\n', 'Nina wednesday\n', 'Umar wednesday\n', 'Charlie tuesday\n',
              'Ethan tuesday\n', 'Rachel friday\n', 'Nina thursday\n', 'George friday\n', 'Steve sunday\n',
              'George sunday\n', 'Hannah sunday\n', 'George friday\n', 'Bob thursday\n', 'Charlie friday\n',
              'Hannah sunday\n', 'Will saturday\n', 'Vera saturday\n', 'Ethan sunday\n', 'Xena thursday\n',
              'Nina friday\n', 'Umar monday\n', 'Vera sunday\n', 'George saturday\n', 'Charlie wednesday\n',
              'Daisy thursday\n', 'Charlie wednesday\n', 'Daisy monday\n', 'Steve sunday\n', 'Quinn tuesday\n',
              'Ian sunday\n', 'George tuesday\n', 'Will friday\n', 'Hannah monday\n', 'Alice saturday\n',
              'Oscar saturday\n', 'Nina saturday\n', 'Nina wednesday\n', 'Umar saturday\n', 'Nina friday\n',
              'Alice thursday\n', 'Ethan sunday\n', 'Tina monday\n', 'Ian sunday\n', 'Charlie friday\n',
              'Umar wednesday\n', 'George wednesday\n', 'Alice wednesday\n', 'Hannah saturday\n', 'Alice saturday\n',
              'Ethan tuesday\n', 'Quinn tuesday\n', 'Hannah friday\n', 'Alice monday\n', 'Daisy sunday\n',
              'Hannah saturday\n', 'Ethan saturday\n', 'Umar thursday\n', 'Ethan tuesday\n', 'Nina thursday\n',
              'Hannah friday\n', 'Ethan wednesday\n', 'Will monday\n', 'Ethan thursday\n', 'George thursday\n',
              'Xena monday\n', 'Will tuesday\n', 'Xena saturday\n', 'Hannah wednesday\n', 'Hannah saturday\n',
              'Nina sunday\n', 'Hannah friday\n', 'Xena saturday\n', 'Rachel tuesday\n', 'Nina monday\n',
              'Daisy saturday\n', 'George monday\n', 'Charlie wednesday\n', 'Xena tuesday\n', 'Hannah saturday\n',
              'Hannah tuesday\n', 'Vera tuesday\n', 'Umar friday\n', 'Nina sunday\n', 'Daisy monday\n',
              'Xena saturday\n', 'Daisy thursday\n', 'Xena wednesday\n', 'Alice monday\n', 'Alice tuesday\n',
              'Charlie sunday\n', 'Oscar thursday\n', 'Daisy tuesday\n', 'Bob monday\n', 'Xena friday\n',
              'Steve monday\n', 'Rachel monday\n', 'Hannah saturday\n', 'Ethan friday\n', 'Tina wednesday\n',
              'Zane thursday\n', 'Charlie sunday\n', 'Rachel wednesday\n', 'Hannah wednesday\n', 'Steve wednesday\n',
              'Xena friday\n', 'Charlie thursday\n', 'Steve sunday\n', 'George wednesday\n', 'Xena saturday\n',
              'Charlie tuesday\n', 'Ethan thursday\n', 'Will saturday\n', 'Hannah wednesday\n', 'Umar friday\n',
              'Alice sunday\n', 'Alice wednesday\n', 'Hannah tuesday\n', 'Rachel thursday\n', 'Alice monday\n',
              'Umar monday\n', 'Quinn thursday\n', 'Alice monday\n', 'Hannah thursday\n', 'Xena tuesday\n',
              'Ian saturday\n', 'Umar saturday\n', 'Rachel monday\n', 'Alice wednesday\n', 'George saturday\n',
              'Rachel saturday\n', 'Xena wednesday\n', 'Hannah saturday\n', 'Steve tuesday\n', 'Tina saturday\n',
              'Hannah thursday\n', 'Vera wednesday\n', 'Ethan monday\n', 'Steve friday\n', 'Will sunday\n',
              'Xena friday\n', 'Oscar thursday\n', 'Charlie tuesday\n', 'Nina friday\n', 'George monday\n',
              'Nina sunday\n', 'Will tuesday\n', 'Vera sunday\n', 'Xena saturday\n', 'Charlie monday\n',
              'Daisy thursday']

    loaded_data = data_handler.load_data()

    assert answer == loaded_data


def test_data_refine():
    attendance_file = "attendance_weekday_500.txt"
    data_handler = DataHandler(attendance_file)
    loaded_data = data_handler.load_data()

    refine_data = data_handler.refine_data(loaded_data)
    answer = [['Umar', 'monday'], ['Daisy', 'tuesday'], ['Alice', 'tuesday'], ['Xena', 'saturday'], ['Ian', 'tuesday'],
              ['Hannah', 'monday'], ['Hannah', 'thursday'], ['Ethan', 'wednesday'], ['Xena', 'wednesday'],
              ['Daisy', 'tuesday'], ['Vera', 'saturday'], ['Xena', 'sunday'], ['Rachel', 'friday'],
              ['Charlie', 'tuesday'], ['Hannah', 'friday'], ['Steve', 'sunday'], ['Ian', 'friday'],
              ['Xena', 'saturday'], ['Vera', 'saturday'], ['Nina', 'sunday'], ['Bob', 'friday'], ['Ethan', 'friday'],
              ['Xena', 'sunday'], ['Nina', 'wednesday'], ['Hannah', 'saturday'], ['Xena', 'friday'], ['Vera', 'friday'],
              ['Xena', 'tuesday'], ['Alice', 'monday'], ['Nina', 'tuesday'], ['Nina', 'friday'], ['Steve', 'sunday'],
              ['Ian', 'wednesday'], ['Alice', 'friday'], ['Charlie', 'monday'], ['Xena', 'tuesday'],
              ['George', 'friday'], ['Hannah', 'monday'], ['Umar', 'sunday'], ['Charlie', 'tuesday'],
              ['Daisy', 'thursday'], ['Quinn', 'friday'], ['Tina', 'thursday'], ['Alice', 'tuesday'],
              ['Hannah', 'saturday'], ['Rachel', 'saturday'], ['George', 'thursday'], ['Xena', 'monday'],
              ['Hannah', 'tuesday'], ['Will', 'wednesday'], ['Xena', 'monday'], ['Umar', 'monday'],
              ['Rachel', 'monday'], ['Charlie', 'friday'], ['Umar', 'sunday'], ['Charlie', 'saturday'],
              ['Hannah', 'friday'], ['Steve', 'wednesday'], ['Rachel', 'wednesday'], ['Nina', 'saturday'],
              ['Will', 'tuesday'], ['Daisy', 'sunday'], ['Vera', 'tuesday'], ['Steve', 'saturday'], ['Tina', 'tuesday'],
              ['Hannah', 'friday'], ['Hannah', 'sunday'], ['Will', 'thursday'], ['Hannah', 'sunday'],
              ['Xena', 'saturday'], ['Hannah', 'wednesday'], ['Alice', 'thursday'], ['Nina', 'thursday'],
              ['Rachel', 'wednesday'], ['Will', 'tuesday'], ['Nina', 'sunday'], ['George', 'friday'],
              ['Will', 'saturday'], ['Xena', 'wednesday'], ['Alice', 'monday'], ['Daisy', 'monday'], ['Nina', 'monday'],
              ['Alice', 'tuesday'], ['Hannah', 'sunday'], ['Charlie', 'wednesday'], ['George', 'friday'],
              ['Will', 'wednesday'], ['Will', 'tuesday'], ['Alice', 'tuesday'], ['Daisy', 'friday'], ['Will', 'sunday'],
              ['Alice', 'wednesday'], ['Ethan', 'monday'], ['Hannah', 'wednesday'], ['Rachel', 'tuesday'],
              ['Hannah', 'tuesday'], ['Oscar', 'sunday'], ['Hannah', 'wednesday'], ['Steve', 'wednesday'],
              ['Nina', 'friday'], ['Rachel', 'thursday'], ['George', 'sunday'], ['Alice', 'saturday'],
              ['Nina', 'wednesday'], ['Xena', 'monday'], ['Ethan', 'monday'], ['Xena', 'thursday'],
              ['Daisy', 'thursday'], ['Steve', 'thursday'], ['Rachel', 'saturday'], ['Alice', 'tuesday'],
              ['George', 'tuesday'], ['Hannah', 'tuesday'], ['Nina', 'wednesday'], ['George', 'monday'],
              ['Rachel', 'sunday'], ['George', 'sunday'], ['Will', 'thursday'], ['Daisy', 'sunday'],
              ['Xena', 'saturday'], ['Charlie', 'thursday'], ['Tina', 'friday'], ['Daisy', 'friday'],
              ['Ethan', 'saturday'], ['Tina', 'saturday'], ['Rachel', 'friday'], ['Charlie', 'monday'],
              ['Hannah', 'thursday'], ['Nina', 'wednesday'], ['Rachel', 'thursday'], ['Hannah', 'friday'],
              ['Ian', 'friday'], ['Hannah', 'wednesday'], ['Daisy', 'tuesday'], ['Hannah', 'sunday'],
              ['Tina', 'thursday'], ['George', 'wednesday'], ['Hannah', 'tuesday'], ['Xena', 'monday'],
              ['Oscar', 'sunday'], ['Hannah', 'saturday'], ['George', 'tuesday'], ['Vera', 'saturday'],
              ['Rachel', 'wednesday'], ['Nina', 'wednesday'], ['Nina', 'sunday'], ['Hannah', 'saturday'],
              ['Tina', 'saturday'], ['Charlie', 'thursday'], ['Nina', 'monday'], ['Alice', 'tuesday'],
              ['Charlie', 'saturday'], ['Alice', 'wednesday'], ['Ian', 'friday'], ['Vera', 'wednesday'],
              ['Ian', 'wednesday'], ['Nina', 'sunday'], ['Ian', 'wednesday'], ['Quinn', 'saturday'], ['Nina', 'sunday'],
              ['Xena', 'tuesday'], ['Umar', 'friday'], ['Hannah', 'friday'], ['Ethan', 'thursday'], ['Nina', 'friday'],
              ['Tina', 'tuesday'], ['Hannah', 'tuesday'], ['Alice', 'thursday'], ['Alice', 'thursday'],
              ['Nina', 'saturday'], ['Xena', 'monday'], ['Xena', 'monday'], ['Ian', 'tuesday'], ['Alice', 'saturday'],
              ['Alice', 'saturday'], ['Daisy', 'sunday'], ['Tina', 'monday'], ['Bob', 'monday'], ['Ethan', 'monday'],
              ['Alice', 'sunday'], ['Hannah', 'sunday'], ['Umar', 'monday'], ['Ethan', 'friday'], ['Alice', 'thursday'],
              ['Rachel', 'friday'], ['Rachel', 'saturday'], ['Ethan', 'sunday'], ['Will', 'thursday'],
              ['Alice', 'wednesday'], ['Hannah', 'thursday'], ['Hannah', 'thursday'], ['Rachel', 'tuesday'],
              ['Daisy', 'sunday'], ['Steve', 'friday'], ['Xena', 'thursday'], ['Alice', 'thursday'],
              ['Xena', 'thursday'], ['Oscar', 'tuesday'], ['Steve', 'sunday'], ['Charlie', 'friday'],
              ['Charlie', 'sunday'], ['Alice', 'monday'], ['Charlie', 'thursday'], ['Hannah', 'tuesday'],
              ['Ethan', 'monday'], ['Nina', 'monday'], ['Charlie', 'tuesday'], ['Rachel', 'thursday'],
              ['Rachel', 'sunday'], ['Xena', 'friday'], ['Hannah', 'tuesday'], ['Tina', 'tuesday'], ['Tina', 'tuesday'],
              ['Xena', 'friday'], ['Umar', 'wednesday'], ['Charlie', 'wednesday'], ['Ethan', 'monday'],
              ['Hannah', 'thursday'], ['Xena', 'saturday'], ['Rachel', 'friday'], ['Rachel', 'wednesday'],
              ['Xena', 'tuesday'], ['Ian', 'sunday'], ['Xena', 'friday'], ['Steve', 'tuesday'], ['Xena', 'tuesday'],
              ['Nina', 'friday'], ['Ethan', 'thursday'], ['Nina', 'thursday'], ['George', 'sunday'],
              ['George', 'monday'], ['Hannah', 'friday'], ['Nina', 'tuesday'], ['Oscar', 'saturday'],
              ['Umar', 'saturday'], ['George', 'tuesday'], ['Steve', 'saturday'], ['Umar', 'tuesday'],
              ['Will', 'friday'], ['Alice', 'tuesday'], ['Daisy', 'saturday'], ['Umar', 'wednesday'],
              ['Umar', 'saturday'], ['Umar', 'sunday'], ['Hannah', 'sunday'], ['Ethan', 'wednesday'],
              ['Xena', 'friday'], ['Umar', 'monday'], ['Nina', 'thursday'], ['Bob', 'thursday'], ['Umar', 'thursday'],
              ['Xena', 'monday'], ['Xena', 'sunday'], ['Daisy', 'tuesday'], ['Hannah', 'thursday'],
              ['Steve', 'tuesday'], ['Daisy', 'wednesday'], ['Xena', 'wednesday'], ['Ethan', 'thursday'],
              ['Daisy', 'tuesday'], ['Steve', 'sunday'], ['Rachel', 'thursday'], ['Tina', 'thursday'],
              ['Umar', 'monday'], ['Hannah', 'saturday'], ['Rachel', 'saturday'], ['George', 'sunday'],
              ['Charlie', 'thursday'], ['Umar', 'friday'], ['Ethan', 'thursday'], ['Will', 'saturday'],
              ['Ethan', 'thursday'], ['Hannah', 'sunday'], ['Bob', 'thursday'], ['Ethan', 'wednesday'],
              ['Rachel', 'friday'], ['Xena', 'monday'], ['Daisy', 'friday'], ['Oscar', 'monday'],
              ['George', 'saturday'], ['Will', 'tuesday'], ['Will', 'sunday'], ['Charlie', 'sunday'],
              ['Nina', 'saturday'], ['Nina', 'wednesday'], ['Charlie', 'saturday'], ['Alice', 'sunday'],
              ['Alice', 'thursday'], ['Daisy', 'monday'], ['Charlie', 'friday'], ['Daisy', 'friday'],
              ['Ethan', 'friday'], ['Charlie', 'wednesday'], ['Xena', 'saturday'], ['Steve', 'friday'],
              ['Charlie', 'monday'], ['Ian', 'monday'], ['Xena', 'thursday'], ['Rachel', 'tuesday'],
              ['Hannah', 'thursday'], ['Rachel', 'tuesday'], ['Tina', 'wednesday'], ['Hannah', 'thursday'],
              ['Hannah', 'wednesday'], ['Vera', 'friday'], ['Rachel', 'friday'], ['Rachel', 'friday'],
              ['Hannah', 'tuesday'], ['Xena', 'monday'], ['Nina', 'monday'], ['Bob', 'tuesday'], ['Nina', 'tuesday'],
              ['Rachel', 'saturday'], ['Xena', 'sunday'], ['Hannah', 'thursday'], ['Steve', 'wednesday'],
              ['Xena', 'saturday'], ['Charlie', 'sunday'], ['Nina', 'thursday'], ['Umar', 'wednesday'],
              ['Hannah', 'friday'], ['George', 'sunday'], ['Rachel', 'thursday'], ['Daisy', 'wednesday'],
              ['Hannah', 'wednesday'], ['Tina', 'sunday'], ['Xena', 'tuesday'], ['Daisy', 'sunday'],
              ['Alice', 'wednesday'], ['Umar', 'wednesday'], ['Hannah', 'saturday'], ['Daisy', 'friday'],
              ['Ethan', 'sunday'], ['Charlie', 'thursday'], ['Charlie', 'friday'], ['Daisy', 'saturday'],
              ['Umar', 'monday'], ['Xena', 'tuesday'], ['Oscar', 'tuesday'], ['Will', 'saturday'], ['Xena', 'saturday'],
              ['Umar', 'monday'], ['Bob', 'friday'], ['Hannah', 'wednesday'], ['Hannah', 'thursday'],
              ['Alice', 'monday'], ['Charlie', 'monday'], ['Daisy', 'tuesday'], ['Will', 'sunday'],
              ['Charlie', 'thursday'], ['Rachel', 'monday'], ['Nina', 'wednesday'], ['Umar', 'wednesday'],
              ['Charlie', 'tuesday'], ['Ethan', 'tuesday'], ['Rachel', 'friday'], ['Nina', 'thursday'],
              ['George', 'friday'], ['Steve', 'sunday'], ['George', 'sunday'], ['Hannah', 'sunday'],
              ['George', 'friday'], ['Bob', 'thursday'], ['Charlie', 'friday'], ['Hannah', 'sunday'],
              ['Will', 'saturday'], ['Vera', 'saturday'], ['Ethan', 'sunday'], ['Xena', 'thursday'], ['Nina', 'friday'],
              ['Umar', 'monday'], ['Vera', 'sunday'], ['George', 'saturday'], ['Charlie', 'wednesday'],
              ['Daisy', 'thursday'], ['Charlie', 'wednesday'], ['Daisy', 'monday'], ['Steve', 'sunday'],
              ['Quinn', 'tuesday'], ['Ian', 'sunday'], ['George', 'tuesday'], ['Will', 'friday'], ['Hannah', 'monday'],
              ['Alice', 'saturday'], ['Oscar', 'saturday'], ['Nina', 'saturday'], ['Nina', 'wednesday'],
              ['Umar', 'saturday'], ['Nina', 'friday'], ['Alice', 'thursday'], ['Ethan', 'sunday'], ['Tina', 'monday'],
              ['Ian', 'sunday'], ['Charlie', 'friday'], ['Umar', 'wednesday'], ['George', 'wednesday'],
              ['Alice', 'wednesday'], ['Hannah', 'saturday'], ['Alice', 'saturday'], ['Ethan', 'tuesday'],
              ['Quinn', 'tuesday'], ['Hannah', 'friday'], ['Alice', 'monday'], ['Daisy', 'sunday'],
              ['Hannah', 'saturday'], ['Ethan', 'saturday'], ['Umar', 'thursday'], ['Ethan', 'tuesday'],
              ['Nina', 'thursday'], ['Hannah', 'friday'], ['Ethan', 'wednesday'], ['Will', 'monday'],
              ['Ethan', 'thursday'], ['George', 'thursday'], ['Xena', 'monday'], ['Will', 'tuesday'],
              ['Xena', 'saturday'], ['Hannah', 'wednesday'], ['Hannah', 'saturday'], ['Nina', 'sunday'],
              ['Hannah', 'friday'], ['Xena', 'saturday'], ['Rachel', 'tuesday'], ['Nina', 'monday'],
              ['Daisy', 'saturday'], ['George', 'monday'], ['Charlie', 'wednesday'], ['Xena', 'tuesday'],
              ['Hannah', 'saturday'], ['Hannah', 'tuesday'], ['Vera', 'tuesday'], ['Umar', 'friday'],
              ['Nina', 'sunday'], ['Daisy', 'monday'], ['Xena', 'saturday'], ['Daisy', 'thursday'],
              ['Xena', 'wednesday'], ['Alice', 'monday'], ['Alice', 'tuesday'], ['Charlie', 'sunday'],
              ['Oscar', 'thursday'], ['Daisy', 'tuesday'], ['Bob', 'monday'], ['Xena', 'friday'], ['Steve', 'monday'],
              ['Rachel', 'monday'], ['Hannah', 'saturday'], ['Ethan', 'friday'], ['Tina', 'wednesday'],
              ['Zane', 'thursday'], ['Charlie', 'sunday'], ['Rachel', 'wednesday'], ['Hannah', 'wednesday'],
              ['Steve', 'wednesday'], ['Xena', 'friday'], ['Charlie', 'thursday'], ['Steve', 'sunday'],
              ['George', 'wednesday'], ['Xena', 'saturday'], ['Charlie', 'tuesday'], ['Ethan', 'thursday'],
              ['Will', 'saturday'], ['Hannah', 'wednesday'], ['Umar', 'friday'], ['Alice', 'sunday'],
              ['Alice', 'wednesday'], ['Hannah', 'tuesday'], ['Rachel', 'thursday'], ['Alice', 'monday'],
              ['Umar', 'monday'], ['Quinn', 'thursday'], ['Alice', 'monday'], ['Hannah', 'thursday'],
              ['Xena', 'tuesday'], ['Ian', 'saturday'], ['Umar', 'saturday'], ['Rachel', 'monday'],
              ['Alice', 'wednesday'], ['George', 'saturday'], ['Rachel', 'saturday'], ['Xena', 'wednesday'],
              ['Hannah', 'saturday'], ['Steve', 'tuesday'], ['Tina', 'saturday'], ['Hannah', 'thursday'],
              ['Vera', 'wednesday'], ['Ethan', 'monday'], ['Steve', 'friday'], ['Will', 'sunday'], ['Xena', 'friday'],
              ['Oscar', 'thursday'], ['Charlie', 'tuesday'], ['Nina', 'friday'], ['George', 'monday'],
              ['Nina', 'sunday'], ['Will', 'tuesday'], ['Vera', 'sunday'], ['Xena', 'saturday'], ['Charlie', 'monday'],
              ['Daisy', 'thursday']]

    assert refine_data == answer



def test_getting_id():
    attendance_file = "attendance_weekday_500.txt"
    data_handler = DataHandler(attendance_file)

    id_check_1 = data_handler.get_id_from_name("umar")
    id_check_2 = data_handler.get_id_from_name("Daisy")
    id_check_3 = data_handler.get_id_from_name("Alice")
    id_check_4 = data_handler.get_id_from_name("umar")
    id_check_5 = data_handler.get_id_from_name("Alice")
    # print(id_check_1)

    assert id_check_1 == 0
    assert id_check_2 == 1
    assert id_check_3 == 2
    assert id_check_4 == 0
    assert id_check_5 == 2


def test_getting_player_data():
    attendance_file = "attendance_weekday_500.txt"
    data_handler = DataHandler(attendance_file)
    loaded_data = data_handler.load_data()
    line_datas = data_handler.refine_data(loaded_data)

    for [name, playday] in line_datas:
        data_handler.update_playday(name, playday)

    dd = data_handler.get_id_player_data()
    assert dd[0].name == "Umar"
    assert dd[0].playday == PlayDay(mon=9, tues=1, wed=6, thur=2, fri=4, sat=4, sun=3)


def test_points_and_remove():
    attendance_file = "attendance_weekday_500.txt"
    data_handler = DataHandler(attendance_file)
    loaded_data = data_handler.load_data()
    line_datas = data_handler.refine_data(loaded_data)

    for [name, playday] in line_datas:
        data_handler.update_playday(name, playday)

    player_data = data_handler.get_id_player_data()

    player_counts = len(player_data)
    for player in range(player_counts):
        player_data[player].update_points()
        player_data[player].update_remove()

    assert player_data[0].points == 48
    assert player_data[0].remove == False

    assert player_data[12].points == 8
    assert player_data[12].remove == True

    assert player_data[18].points == 1
    assert player_data[18].remove == True


def test_print_info(capfd):
    remove_printer = RemoverPrinter()

    attendance_file = "attendance_weekday_500.txt"
    data_handler = DataHandler(attendance_file)
    loaded_data = data_handler.load_data()
    line_datas = data_handler.refine_data(loaded_data)

    for [name, playday] in line_datas:
        data_handler.update_playday(name, playday)

    player_data = data_handler.get_id_player_data()

    player_counts = len(player_data)
    for player in range(player_counts):
        player_data[player].update_points()

    remove_printer.update_data(player_data)
    remove_printer.print()

    expected = '''
Removed player
==============
Bob
Zane
'''
    out, _ = capfd.readouterr()

    assert out == expected


def test_attendance_output(capfd):
    expected = """NAME : Umar, POINT : 48, GRADE : SILVER
NAME : Daisy, POINT : 45, GRADE : SILVER
NAME : Alice, POINT : 61, GRADE : GOLD
NAME : Xena, POINT : 91, GRADE : GOLD
NAME : Ian, POINT : 23, GRADE : NORMAL
NAME : Hannah, POINT : 127, GRADE : GOLD
NAME : Ethan, POINT : 44, GRADE : SILVER
NAME : Vera, POINT : 22, GRADE : NORMAL
NAME : Rachel, POINT : 54, GRADE : GOLD
NAME : Charlie, POINT : 58, GRADE : GOLD
NAME : Steve, POINT : 38, GRADE : SILVER
NAME : Nina, POINT : 79, GRADE : GOLD
NAME : Bob, POINT : 8, GRADE : NORMAL
NAME : George, POINT : 42, GRADE : SILVER
NAME : Quinn, POINT : 6, GRADE : NORMAL
NAME : Tina, POINT : 24, GRADE : NORMAL
NAME : Will, POINT : 36, GRADE : SILVER
NAME : Oscar, POINT : 13, GRADE : NORMAL
NAME : Zane, POINT : 1, GRADE : NORMAL

Removed player
==============
Bob
Zane
"""

    Attendance().run()
    out, _ = capfd.readouterr()
    assert out == expected
