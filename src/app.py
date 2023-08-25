from typing import List

from utils import warn_and_exit
from file_reader import File_reader

class App:
    def __init__(self, reader: File_reader) -> None:
        self.reader = reader

    def add(self, new_task: str) -> None:
        self.reader.append_one(new_task)

    def show(self) -> None:
        tasks = self.reader.get_all()
        render(tasks)

    def done(self, task_id: str) -> None:
        if str(task_id).isdigit():
            task_i_int = int(task_id) - 1
            self.reader.remove_one(task_i_int)
        else:
            warn_and_exit(True, "done sub-command requires a digit")

    def reset(self) -> None:
        self.reader.reset_store()

def render(items: List[str]) -> None:
    for i in range(len(items)):
        print("{0}. {1}".format(i + 1, items[i]))

