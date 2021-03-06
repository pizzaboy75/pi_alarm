import os
basedir = os.path.abspath(os.path.dirname(__file__))

# -- Alarm Settings
ALARM_DURATION = 30            # Light duration in minutes

# -- General Config
DEBUG = True
CSRF_ENABLED = True
BASIC_AUTH_FORCE = False
BASIC_AUTH_USERNAME = 'alarm'
BASIC_AUTH_PASSWORD = 'password'
