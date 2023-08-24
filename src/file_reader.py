from typing import List
from json import JSONDecodeError
import json

from utils import warn_and_exit

# TODO: Handle errors around opening the db (file)

class File_reader:
    def __init__(self, path: str):
        self.path = path

    def get_all(self) -> List[str]:
        with open(self.path, "r") as store:
            try:
                task_list = json.load(store)
                return task_list
            except JSONDecodeError:
                with open(self.path, "w") as w_store:
                    json.dump([], w_store)
                    w_store.close()

            finally:
                store.close()

        return []

    def find_one(self, tasks: List[str], id: int) -> str | None:
        try:
            return tasks[id]
        except:
            return None

    def update_one(self, id: int) -> None:
        tasks = self.get_all()
        task = self.find_one(tasks, id)
        print(task)
        if task is not None:
            tasks[id] = task.replace(" -", " +")

            try:
                with open(self.path, "w") as store:
                    json.dump(tasks, store)
                    store.close()
            except (OSError, IOError) as e:
                warn_and_exit(True, "ERROR: {0}".format(e))


    def append_one(self, item: str) -> None:
        records = self.get_all()
        records.append(item)

        with open(self.path, "w") as store:
            json.dump(records, store)
            store.close()

    def reset_store(self) -> None:
        try:
            with open(self.path, "w") as store:
                json.dump([], store)
                store.close()
        except (OSError, IOError) as e:
            warn_and_exit(True, "ERROR: {0}".format(e))
