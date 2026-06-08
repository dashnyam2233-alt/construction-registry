
with open('/var/www/construction-registry/config/settings.py', 'r') as f:
    s = f.read()

s = s.replace("INSTALLED_APPS = [", "INSTALLED_APPS = [\n    'social_django',", 1)
s = s.replace(
    "'django.contrib.auth.backends.ModelBackend',",
    "'social_core.backends.facebook.FacebookOAuth2',\n    'django.contrib.auth.backends.ModelBackend',"
)
fb = '''
SOCIAL_AUTH_FACEBOOK_KEY = os.getenv('SOCIAL_AUTH_FACEBOOK_KEY', '')
SOCIAL_AUTH_FACEBOOK_SECRET = os.getenv('SOCIAL_AUTH_FACEBOOK_SECRET', '')
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'fields': 'id,name,email'}
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/public/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/public/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/login/'
'''
s = s + fb

with open('/var/www/construction-registry/config/settings.py', 'w') as f:
    f.write(s)

print('OK')
