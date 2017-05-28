from functools import wraps
# import requests


def notify_webapp(case=None):
    def _notify_webapp(view_func):
        def _decorator(request, *args, **kwargs):
            response = view_func(request, *args, **kwargs)
            # requests.get("https://api.myjson.com/bins/1b7dvn")
            return response
        return wraps(view_func)(_decorator)
    return _notify_webapp


@notify_webapp(case="SUCCESS")
def succeed(function_name):
    return "Test case passed for " + function_name

@notify_webapp(case="FunctionNotFound")
def no_function_found(function_name):
    return "No function found. Please define function with name " + function_name


@notify_webapp(case="IncorrectOutput")
def incorrect_output(s = "incorrect output"):
    return "Incorrect output return by function"
