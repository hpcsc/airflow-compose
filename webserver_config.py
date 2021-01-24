import os
from flask import session
from flask_appbuilder.security.manager import (
    AUTH_OAUTH,
)

basedir = os.path.abspath(os.path.dirname(__file__))

# Flask-WTF flag for CSRF
CSRF_ENABLED = True

# ------------------------------
# GLOBALS FOR APP Builder
# ------------------------------
# Uncomment to setup Your App name
# APP_NAME = "My App Name"

# Uncomment to setup Setup an App icon
# APP_ICON = "static/img/logo.jpg"

# ----------------------------------------------------
# AUTHENTICATION CONFIG
# ----------------------------------------------------
# The authentication type
# AUTH_OID : Is for OpenID
# AUTH_DB : Is for database (username/password()
# AUTH_LDAP : Is for LDAP
# AUTH_REMOTE_USER : Is for using REMOTE_USER from web server
AUTH_TYPE = AUTH_OAUTH

tenant_id = os.environ.get("AZURE_TENANT_ID")

OAUTH_PROVIDERS = [
    {
        "name": "azure",
        "icon": "fa-windows",
        "token_key": "access_token",
        "remote_app": {
            "client_id": os.environ.get("AZURE_APPLICATION_ID"),
            "client_secret": os.environ.get("AZURE_SECRET"),
            "api_base_url": f"https://login.microsoftonline.com/{tenant_id}/oauth2",
            "client_kwargs": {
                "scope": "User.read name preferred_username email profile upn",
                "resource": os.environ.get("AZURE_APPLICATION_ID"),
            },
            "request_token_url": None,
            "access_token_url": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token",
            "authorize_url": f"https://login.microsoftonline.com/{tenant_id}/oauth2/authorize",
        },
    },
]

# Uncomment to setup Full admin role name
AUTH_ROLE_ADMIN = 'Admin'

# Uncomment to setup Public role name, no authentication needed
# AUTH_ROLE_PUBLIC = 'Public'

# Will allow user self registration
AUTH_USER_REGISTRATION = True

# The default user self registration role for all users
AUTH_USER_REGISTRATION_ROLE = "Admin"

# Self registration role based on user info
# AUTH_USER_REGISTRATION_ROLE_JMESPATH = "contains(['alice@example.com', 'celine@example.com'], email) && 'Admin' || 'Public'"

# ---------------------------------------------------
# Babel config for translations
# ---------------------------------------------------
# Setup default language
BABEL_DEFAULT_LOCALE = "en"
# Your application default translation path
BABEL_DEFAULT_FOLDER = "translations"
# The allowed translation for you app
LANGUAGES = {
    "en": {"flag": "gb", "name": "English"}
}

# ---------------------------------------------------
# Image and file configuration
# ---------------------------------------------------
# The file upload folder, when using models with files
# UPLOAD_FOLDER = basedir + "/app/static/uploads/"

# The image upload folder, when using models with images
# IMG_UPLOAD_FOLDER = basedir + "/app/static/uploads/"

# The image upload url, when using models with images
# IMG_UPLOAD_URL = "/static/uploads/"
# Setup image size default is (300, 200, True)
# IMG_SIZE = (300, 200, True)

# Theme configuration
# these are located on static/appbuilder/css/themes
# you can create your own and easily use them placing them on the same dir structure to override
# APP_THEME = "bootstrap-theme.css"  # default bootstrap
# APP_THEME = "cerulean.css"
# APP_THEME = "amelia.css"
APP_THEME = "cosmo.css"
# APP_THEME = "cyborg.css"
# APP_THEME = "flatly.css"
# APP_THEME = "journal.css"
# APP_THEME = "readable.css"
# APP_THEME = "simplex.css"
# APP_THEME = "slate.css"
# APP_THEME = "spacelab.css"
# APP_THEME = "united.css"
# APP_THEME = "yeti.css"
