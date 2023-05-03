from .models import Profile,AccessItem

def chech_profile(user, code):
    profile = user.profile
    access = AccessItem.objects.filter(Profile=profile)
    for i in access:
        if code == i.Access.code:
            return True
    return False
