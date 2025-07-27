from pathlib import Path

# === Base directory ===
BASE_DIR = Path(__file__).resolve().parent.parent

# === Security ===
SECRET_KEY = 'django-insecure-5^m9y#l)16oyd3kdnh@ntb6!*ah!x*@5zyzq!@@!(6peggnf6h'
DEBUG = True
ALLOWED_HOSTS = []

# === Installed apps ===
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your apps
    'bookshelf',
    'relationship_app',
    'core',

    # Security
    'csp',
]

# === Middleware ===
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # CSP Middleware
    'csp.middleware.CSPMiddleware',
]

# === URLConf and Templates ===
ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'

# === Database ===
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# === Password validation ===
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# === Internationalization ===
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# === Static files ===
STATIC_URL = 'static/'

# === Primary Key ===
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# === Custom User Model ===
AUTH_USER_MODEL = 'bookshelf.CustomUser'

# === Login/Logout redirects ===
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

# === Security Headers ===

# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True  # ✅ Forces all HTTP to HTTPS

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # ✅ Browser should only access via HTTPS for 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # ✅ Apply HSTS to all subdomains
SECURE_HSTS_PRELOAD = True  # ✅ Allow browser preload

# Prevent content type sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True  # ✅ Block MIME-type sniffing

# Enable XSS filter in browser
SECURE_BROWSER_XSS_FILTER = True  # ✅ Enable XSS protection

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Prevent clickjacking
X_FRAME_OPTIONS = 'DENY'  # ✅ Deny iframe embedding

# Secure cookies over HTTPS only
CSRF_COOKIE_SECURE = True  # ✅ CSRF cookie sent only via HTTPS
SESSION_COOKIE_SECURE = True  # ✅ Session cookie sent only via HTTPS

# === Content Security Policy (CSP) ===
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'",)
