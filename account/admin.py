from django.contrib import admin
from .models import EmailVerification


class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'verified', 'verification_code')

admin.site.register(EmailVerification, EmailVerificationAdmin)