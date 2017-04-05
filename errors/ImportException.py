from errors import notify_webapp


@notify_webapp(case="FunctionNotFound")
def no_function_found(function_name):
    return "No function found. Please define function with name " + function_name


@notify_webapp(case="IncorrectOutput")
def incorrect_output():
    return "Incorrect output return by function"
