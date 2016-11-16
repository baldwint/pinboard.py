import sys

if sys.version_info < (3,):
    from urllib2 import HTTPError
else:
    from urllib.error import HTTPError

class PinboardError(Exception):
    pass

class PinboardServerError(HTTPError):
    pass

class PinboardServiceUnavailable(HTTPError):
    pass

class PinboardAuthenticationError(HTTPError):
    pass

class PinboardForbiddenError(HTTPError):
    pass

