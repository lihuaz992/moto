from __future__ import unicode_literals
import json
from moto.core.exceptions import JsonRESTError


class AWSError(Exception):
    """ Copied from acm/models.py; this class now exists in >5 locations,
        maybe this should be centralised for use by any module?
    """

    TYPE = None
    STATUS = 400

    def __init__(self, message):
        self.message = message

    def response(self):
        resp = {"__type": self.TYPE, "message": self.message}
        return json.dumps(resp), dict(status=self.STATUS)


class AWSValidationException(JsonRESTError):
    def __init__(self, message, **kwargs):
        super(AWSValidationException, self).__init__(
            "ValidationException", message, **kwargs
        )
