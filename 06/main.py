# try:
#     x = 5 / 0
# except ZeroDivisionError as e:
#     print('ZeroDivisionError', e)
# except AttributeError:
#     print('AttributeError')
# except:
#     print('error')
# else:
#     print("success")
# finally:
#     print('finally')
#
#
# def method():
#     raise NotImplementedError()


def get_formatted_name(first, last):
    full_name = '{} {}'.format(first, last)
    return full_name.title()


# print(get_formatted_name('tom', 'lee'))