from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

class AppTokenGenerator(PasswordResetTokenGenerator):
    def __make_hash_value(self, new_user, timestamp):
        
        return (text_type(new_user.is_active)+text_type(new_user.pk)+text_type(timestamp))

token_generator = AppTokenGenerator()