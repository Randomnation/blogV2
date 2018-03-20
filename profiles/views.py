import django.shortcuts
from .models import UserProfile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    return django.shortcuts.render(request, 'profiles/index.html', locals())


@login_required
def user_profile(request, pk):
    profile = django.shortcuts.get_object_or_404(UserProfile, pk=pk)
    return django.shortcuts.render(request, 'profiles/profile.html', locals())


@login_required
def user_profile_edit(request, pk):
    profile = django.shortcuts.get_object_or_404(UserProfile, pk=pk)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Success! Your profile has been updated!',
                extra_tags='profile')
            return django.shortcuts.redirect('profiles:user_profile', pk=profile.pk)
    else:
        form = ProfileForm(instance=profile)
    return django.shortcuts.render(request, 'profiles/profile_edit.html', locals())