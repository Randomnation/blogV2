from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from account.forms import UserRegistrationForm
from .models import EmailVerification
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


@login_required()
def login_success(request):
    messages.add_message(
        request,
        messages.SUCCESS,
        'Login Successful! Welcome ' + request.user.first_name,
        extra_tags='auth')
    return HttpResponseRedirect(reverse('blog:index'))


def logout_success(request):
    return HttpResponseRedirect(reverse('blog:index'))


def not_verified(request):
    template = 'account/not_verified.html'
    return render(request, template, {})


def register_success(request):
    template = 'account/register_success.html'
    return render(request, template, {})


@login_required()
def login_next_test(request):
    template = 'account/login_next_test.html'
    return render(request, template, {})


def register(request):
    template = 'account/register.html'
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect(reverse('account:register_success'))
    else:
        form = UserRegistrationForm()
    return render(request, template, {
        'form': form,
    })


def verify(request, user, code):
    """
    View for email verification. Takes a user and verification code and sets
    verified in EmailVerification and adds account.verified to user if successful
    :param user: The username of the user being verified
    :param code: A string of the UUID stored in EmailVerification.verification_code
    :return: HTTPRequest object
    """
    template = 'account/verify.html'
    verified = False
    error = False
    if code and user:
        try:
            user_verify = EmailVerification.objects.get(user__username=user)
            if user_verify.verified:
                verified = False
                error = "User already verified."
            elif str(user_verify.verification_code) == code:
                user_verify.verified = True
                user_verify.save()
                verified = True
                verified_user = User.objects.get(username=user)
                content_type = ContentType.objects.get_for_model(EmailVerification)
                permission = Permission.objects.get(content_type=content_type, codename='verified')
                verified_user.user_permissions.add(permission)
            else:
                verified = False
                error = "Verification code did not match."
        except ObjectDoesNotExist:
            verified = False
            error = "User was not found."
        return render(request, template, {'verified': verified, 'error': error})