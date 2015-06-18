from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

import kerberos


class KerbAuth(ModelBackend):

    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
            
        # print "trying to authenticate ", username, password

        try:
            kerberos.checkPassword(username, password,
                                   "",  settings.KRB5_REALM)
        except kerberos.BasicAuthError:
            # print "Kerberos auth failed"
            return None

        # print "kerberos succeeded" 

        user, created = User.objects.get_or_create(
            username=username
        )

        # print "user, created: ", user, type(user), created
        
        if created:
            # no local password for such users
            user.set_unusable_password()

            # allow access to admin:
            user.is_staff = True

            try:
                # have to set a reasonable default group
                g = Group.objects.get(name="lehrender")
                user.groups.add(g)
            except:
                # print "adding user to group did not work"
                pass
            
            user.save()

        return user

    # def get_user(self, user_id):
    #     print "getting user: ", user_id
        
    #     UserModel = get_user_model()
    #     try:
    #         user = UserModel._default_manager.get(pk=user_id)
    #         print "user: ", user
    #     except UserModel.DoesNotExist:
    #         return None

    #     return user

