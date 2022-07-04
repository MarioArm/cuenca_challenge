import solutions_db
import cuenca_logging
import logging
from models import Solution
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


def is_queen_present_in_column(grid: list, current_row: int, column: int) -> bool:
    for index in range(current_row):
        if grid[index][column] == 'Q':
            return True
    return False


def is_queen_present_in_top_to_down_diagonal(grid: list, row: int, column: int) -> bool:
    (current_row, current_column) = (row, column)
    while current_row >= 0 and current_column >= 0:
        if grid[current_row][current_column] == 'Q':
            return True
        current_row -= 1
        current_column -= 1
    return False


def is_queen_present_in_down_to_top_diagonal(grid: list, row: int, column: int) -> bool:
    (current_row, current_column) = (row, column)
    while current_row >= 0 and current_column < len(grid):
        if grid[current_row][current_column] == 'Q':
            return True
        current_row -= 1
        current_column += 1
    return False


def is_safe_to_place_queen(grid, row, column):
    if is_queen_present_in_column(grid, row, column):
        return False
    if is_queen_present_in_top_to_down_diagonal(grid, row, column):
        return False
    if is_queen_present_in_down_to_top_diagonal(grid, row, column):
        return False
    return True


def remove_queen_from(grid: list, row: int, column: int):
    grid[row][column] = '–'


def set_queen_at(grid: list, row: int, column: int):
    grid[row][column] = 'Q'


def calculate_solutions(grid: list, row: int) -> None:
    if row == len(grid):
        if len(grid) not in (2, 3):
            global solution_counter
            solution_counter += 1
        return

    for column in range(len(grid)):
        if is_safe_to_place_queen(grid, row, column):
            set_queen_at(grid, row, column)
            calculate_solutions(grid, row + 1)
            remove_queen_from(grid, row, column)


solution_counter = 0


def get_number_of_solutions(number_of_queens: int) -> int:
    initial_time: datetime = datetime.now()

    global solution_counter
    solution_counter = 0
    grid: list = [['–' for _ in range(number_of_queens)] for _ in range(number_of_queens)]

    calculate_solutions(grid, 0)

    final_time: datetime = datetime.now()
    delta_time: timedelta = final_time - initial_time
    logger.debug(f"The time required for a board of size {number_of_queens} was {delta_time.total_seconds()} seconds\n")

    return solution_counter


def persist_solution_to_db(board_size: int, number_of_solutions: int) -> None:
    solution: Solution = Solution(board_size, number_of_solutions)
    solutions_db.session.add(solution)
    solutions_db.session.commit()


if __name__ == '__main__':
    initial_time: datetime = datetime.now()

    processed_solutions_counter: int = 0
    default_maximum_board_size: int = 17
    default_minimum_board_size: int = 8
    for board_size in range(default_minimum_board_size, default_maximum_board_size + 1):
        current_time: datetime = datetime.now()
        time_elapsed: timedelta = current_time - initial_time
        logger.debug(
            f'time remaining before processing for board size = {board_size} is {timedelta(minutes=10) - time_elapsed}')
        if time_elapsed >= timedelta(minutes=10):
            break
        try:
            number_of_solutions: int = get_number_of_solutions(board_size)
        except KeyboardInterrupt:
            break
        persist_solution_to_db(board_size, number_of_solutions)
        processed_solutions_counter += 1

    final_time: datetime = datetime.now()
    delta_time: timedelta = final_time - initial_time
    logger.info(f">>>TOTAL time required to process {[processed_solutions_counter]} cases of "
                f"N-queen puzzle was {delta_time.total_seconds()} seconds")
