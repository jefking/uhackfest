from flask import request, Response


class Authenticator:
    """
    Don't ever use this for production ...
    """

    def __init__(self):
        # BAD BAD BAD
        self.username = 'user'
        self.password = 'pass'
        # BAD BAD BAD

    def authenticate(self):
        auth = request.authorization
        if not auth:
            return False

        is_set = auth.username and self.username and auth.password and self.password
        match = auth.username == self.username and auth.password == self.password
        good = is_set and match
        return (auth.type == "basic" and good)

    @staticmethod
    def challenge():
        """
        Challenge the client for username and password.
        This method is called when the client did not provide username and
        password in the request.

        :returns: a :class:`~flask.Response` with 401 response code, including
            the required authentication scheme and authentication realm.
        """
        return Response(
            status=401, headers={
                "WWW-Authenticate": "Basic realm=\"Dummy API\""
            })
