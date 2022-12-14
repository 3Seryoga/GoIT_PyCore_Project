def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError as e:
            return f"Key Error - Note with id[{e}] doesn't exist"
        except ValueError as e:
            return f"Value Error - {e}, you must input ID at first."
        except TypeError as e:
            return f"Type Error - {e}, you forgot to type data"
    return wrapper