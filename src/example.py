import logging


def foo():
    print("This is a function in example module.")
    print("This is a function in example module.")

if __name__ == "__main__":
    logging.debug("hi hi")
    print("This is the main program.")
    foo()
else:
    print("This module was imported.")
