from django.shortcuts import redirect
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.contrib.auth import logout


def login_permission(permission):
    """
    A decorator that applies both login required and permission required to a view to both redirect to login if required
    and to check permission after a login
    :param permission: The permission required for the view
    :return: function
    """
    from django.contrib.auth.decorators import login_required, permission_required

    def decorate(f):
        def do(permission):
            return login_required(permission_required(permission, raise_exception=True)(f))
        return do(permission)
    return decorate


class EmailVerificationMiddleware(object):
    """
    Middleware that checks whether a user has the account.verified permission
    and forces logout if they do not, enable in settings.py if functionality
    is desired.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        if request.user.id:

            if request.user.has_perm('account.verified'):
                return None
            else:
                logout(request)
                return redirect('account:not_verified')
        else:
            return None

        # Code to be executed for each request/response after
        # the view is called.