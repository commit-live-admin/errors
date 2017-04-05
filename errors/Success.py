from errors import notify_webapp


@notify_webapp(case="SUCCESS")
def succeed(function_name):
    return "Test case passed for " + function_name