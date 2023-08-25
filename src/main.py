import sys
import os

from utils import warn_and_exit
from app import App
from file_reader import File_reader

STORE = os.environ["STORE"]

if __name__ == "__main__":
    args = sys.argv
    arg_len = len(args)
    app = App(File_reader(STORE))

    warn_and_exit(arg_len < 2, "Please use a sub-command: [add, list, done, reset]\nadd: Adds an item to your list;\nlist: Show all items in your list;\ndone: Mark an item comleted;\nreset: Clear your entire list;")
    sub_command = args[1]

    match sub_command:
        case "add":
            warn_and_exit(arg_len < 3, "add sub-command requires a task to be added")
            new_task = args[2]
            app.add(new_task)
        case "list":
            app.show()
        case "done":
            warn_and_exit(arg_len < 3, "done sub-command requires a task number")
            task_i = sys.argv[2]
            app.done(task_i)
        case "reset":
            app.reset()
        case _:
            warn_and_exit(True, "sub-command not supported")
