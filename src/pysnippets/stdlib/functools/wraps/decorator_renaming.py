from functools import wraps


def tags_v1(tag_name):
    """
    A parametrized decorator without @wraps, harder to debug 
    :param tag_name: 
    :return: 
    """

    def tags_decorator(func):
        def func_wrapper(name):
            return '<{0}>{1}</{0}>'.format(tag_name, func(name))

        return func_wrapper

    return tags_decorator


def tags_v2(tag_name):
    """
    A parametrized decorator with @wraps, easier to debug
    :param tag_name: 
    :return: 
    """

    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return '<{0}>{1}</{0}>'.format(tag_name, func(name))

        return func_wrapper

    return tags_decorator


@tags_v1('div')
@tags_v1('p')
@tags_v1('strong')
def get_text_v1(name):
    return 'Hello ' + name


@tags_v2('div')
@tags_v2('p')
@tags_v2('strong')
def get_text_v2(name):
    return 'Hello ' + name


print(get_text_v1('John'))
# <div><p><strong>Hello John</strong></p></div>
print(get_text_v2('John'))
# <div><p><strong>Hello John</strong></p></div>

print(get_text_v1.__name__)
# func_wrapper
print(get_text_v2.__name__)
# get_text_v2
