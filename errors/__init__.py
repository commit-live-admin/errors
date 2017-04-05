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