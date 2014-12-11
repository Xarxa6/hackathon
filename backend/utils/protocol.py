import log

def error(exception):
    log.error(exception)
    return {
    'status': 'error',
    'message' : exception.message
    }

def success(msg, result = None):
    log.debug(msg)
    return {
    'status' : 'ok',
    'message' : msg,
    'result' : result
     }
