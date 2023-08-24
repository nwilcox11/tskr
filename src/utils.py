import sys

def warn_and_exit(cond: bool, message: str):
    if cond:
        print(message)
        sys.exit(1)

