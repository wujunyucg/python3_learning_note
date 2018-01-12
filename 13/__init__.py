def p_decorator(func):
    def wrapper(*args, **kwargs):
        return '<p>' + func(*args, **kwargs) + '</p>'

    return wrapper


@p_decorator
def get_text():
    return 'aaaa'


print(get_text())
