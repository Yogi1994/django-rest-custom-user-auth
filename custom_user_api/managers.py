from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, is_superuser):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, is_superuser=is_superuser)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None):
        # extra_fields.setdefault('is_superuser', False)
        # user = {}
        # user['email'] = email
        # user['password'] = password
        # return user
        is_superuser = False
        return self._create_user(email, password, is_superuser)

    def create_superuser(self, email, password):
        # extra_fields.setdefault('is_superuser', True)
        is_superuser = True
        # if extra_fields.get('is_superuser') is not True:
        #   raise ValueError('Superuser must have is superuser=True.')

        return self._create_user(email, password, is_superuser)