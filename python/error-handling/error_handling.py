def handle_error_by_throwing_exception():
    raise Exception("This is a sample of error")


def handle_error_by_returning_none(input_data):
    try:
        return int(input_data)
    except ValueError:
        return None

def handle_error_by_returning_tuple(input_data, test=False):
    try:
        return True, int(input_data)
    except ValueError:
        return False, None


def filelike_objects_are_closed_on_exception(filelike_object):
    with filelike_object as fl:
        try:
            fl.open()
            fl.do_something()
        except Exception:
            fl.close()
            fl.__exit__()
            raise FileExistsError
