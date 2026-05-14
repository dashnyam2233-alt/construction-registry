from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "REPLACE_ME_WITH_YOUR_EXISTING_SECRET_KEY"

DEBUG = True

# ✅ Domain-оор ажиллуулахын тулд host-уудыг зөвшөөрнө
ALLOWED_HOSTS = ["www.barilgainfo.mn", "barilgainfo.mn", "127.0.0.1", "localhost"]

# ✅ Domain дээр login/register POST хийхэд CSRF алдаа гарахаас сэргийлнэ
CSRF_TRUSTED_ORIGINS = [
    "https://www.barilgainfo.mn",
    "https://barilgainfo.mn",
    # Хэрвээ https тохируулаагүй, түр http-оор ажиллуулж байгаа бол:
    "http://www.barilgainfo.mn",
    "http://barilgainfo.mn",
]

# ✅ Email эсвэл username-ээр нэвтрэх backend нэмэв
AUTHENTICATION_BACKENDS = [
    "registry.backends.EmailOrUsernameModelBackend",
    "django.contrib.auth.backends.ModelBackend",
]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # ✅ Excel Import / Export
    "import_export",

    # ✅ Local app (ready() ажиллуулахын тулд ингэж заана)
    "registry.apps.RegistryConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",

                # ✅ Admin + User sidebar өгөгдөл
                "registry.context_processors.public_sidebar",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "mn"
TIME_ZONE = "Asia/Ulaanbaatar"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
# ── Email (SMTP) ──
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "your_email@gmail.com"
EMAIL_HOST_PASSWORD = "your_app_password"
DEFAULT_FROM_EMAIL = "БНБ Систем <your_email@gmail.com>"
TELEGRAM_BOT_TOKEN = ""
FACEBOOK_PAGE_ACCESS_TOKEN = ""
VIBER_AUTH_TOKEN = ""
SMS_GATEWAY_URL = ""
SMS_GATEWAY_TOKEN = ""
SMS_SENDER_NAME = "BNB"
