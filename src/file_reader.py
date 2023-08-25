from typing import List, TextIO
from json import JSONDecodeError
import json

from utils import warn_and_exit

class File_reader:
    def __init__(self, path: str):
        self.path = path

    def __open_writeable_store(self) -> TextIO | None:
        try:
            return open(self.path, "w")
        except (IOError) as e :
            warn_and_exit(True, "ERROR: {0}".format(e))

    def __open_readable_store(self) -> TextIO | None:
        try:
            return open(self.path, "r")
        except (IOError) as e:
            warn_and_exit(True, "ERROR: {0}".format(e))

    def __find_one(self, tasks: List[str], id: int) -> str | None:
        try:
            return tasks[id]
        except:
            return None

    def get_all(self) -> List[str]:
        store = self.__open_readable_store()
        if store is not None:
            try:
                return json.load(store)
            except JSONDecodeError:
                store = self.__open_writeable_store()
                if store is not None:
                    json.dump([], store)
                    store.close()
        return []

    def remove_one(self, id: int) -> None:
        tasks = self.get_all()
        task = self.__find_one(tasks, id)

        if task is not None:
            tasks.remove(task)
            store = self.__open_writeable_store()
            if store is not None:
                json.dump(tasks, store)
                store.close()

    def append_one(self, item: str) -> None:
        records = self.get_all()
        records.append(item)

        store = self.__open_writeable_store()
        if store is not None:
            json.dump(records, store)
            store.close()

    def reset_store(self) -> None:
        store = self.__open_writeable_store()
        if store is not None:
            json.dump([], store)
            store.close()
