from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import ReCaptchaField
from .models import EmailVerification
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.conf import settings


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, )
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ("username", 'first_name', 'last_name', "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            self.verify(user)
        return user

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError(u'Email addresses must be unique.')

        return email

    @staticmethod
    def verify(user):
        email_verification = EmailVerification.objects.create(user=user)
        email_verification.save()
        url = 'http://{host}{path}{user}/{code}'.format(host=settings.ALLOWED_HOSTS[0],
                                                        path=reverse('account:verify'),
                                                        user=user.username,
                                                        code=str(email_verification.verification_code))
        send_mail(
            subject='Verify account',
            message='Please follow this link to verify: {url}'.format(url=url),
            html_message="Please follow this link to verify: <a {url}'> "
                         "{url}</a>".format(url=url),
            from_email='noreply@luz.io',
            recipient_list=[user.email],
            fail_silently=False,
        )