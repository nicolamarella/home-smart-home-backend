# home-smart-home-backend
Python backend of Home Smart Home app that is developed at HackaTUM 2018.


## Installation

### Setup and run
1. Clone the project
2. Setup virutal env `$: python -m venv env`
3. Install reqs `$: pip install -r requirements.txt`
4. See env setup below before going on!
5. Run migrations `$: python manage.py migrate`
6. Run `$: python manage.py runserver`

### Environments config setup

1. Since each env has a different settings, create your own file under home_smart_home/settings/your_env.py
2. Import all the confs from base.py and override when needed. Example:
    ```
    ## home_smart_home/settings/your_env.py
    from .base import *
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'my_other_db.sqlite3'),
        }
    }
    ```
3. Either export the settings module as env variable `$: export DJANGO_SETTINGS_MODULE=home_smart_home.settings.your_env `<br>
    OR<br>
    run EACH command with `--settings=home_smart_home.settings.your_env` param