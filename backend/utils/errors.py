#TODO make it map more than just ProgrammingExceptions
def errorify(exception):
    return { "exception" : exception.message }
