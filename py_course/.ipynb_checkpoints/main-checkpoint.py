# def do_stuff(num):
#     return num + 5

def do_stuff(num):
    try:
        return int(num) + 5
    except TypeError as err:
        return err
