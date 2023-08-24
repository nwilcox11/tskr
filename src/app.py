from typing import List

from utils import warn_and_exit
from file_reader import File_reader

class App:
    def __init__(self, reader: File_reader) -> None:
        self.reader = reader

    def add(self, new_task: str) -> None:
        new_task = "{0} {1}".format(new_task, "-")
        self.reader.append_one(new_task)

    def list(self) -> None:
        tasks = self.reader.get_all()
        __render(tasks)

    def done(self, task_id: str) -> None:
        if str(task_id).isdigit():
            task_i_int = int(task_id) - 1
            self.reader.update_one(task_i_int)
        else:
            warn_and_exit(True, "done sub-command requires a digit")

    def clear(self) -> None:
        self.reader.reset_store()

def __render(tasks: List[str]) -> None:
    for i in range(len(tasks)):
        print("{0}. {1}".format(i + 1, tasks[i]))
