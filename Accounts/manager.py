from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations=True

    def create_user(self,username=None,email=None,phone=None,password=None,**extra):
        # if not email and not phone:
        #     raise ValueError('Either Email or Phone is required')
        if not username:
            raise ValueError('Username is required.')
        # email = self.normalize_email(email)
        '''email=email,phone=phone,'''
        extra.setdefault('is_active',True)
        user = self.model(username = username,**extra)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self,username,password,**extra):
        extra.setdefault('is_staff',True)
        extra.setdefault('is_superuser',True)
        extra.setdefault('is_active',True)
        # phone = 'default'

        if extra.get('is_staff') is not True:
            raise ValueError(('is_staff should be True for Superuser'))

        return self.create_user(username = username,password=password,**extra) 