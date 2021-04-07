from django.contrib.sessions.backends.db import SessionStore


class InitSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Before view

        # Creating a session if it not exists
        session = request.session
        if session.session_key is None:
            session = SessionStore()
            session.create()
            request.session = session

        # Calling the view
        response = self.get_response(request)

        return response
