# Issue Tracker
Simple issue tracker application.

- Feel free to ask about anything that is unclear, doesn't make sense or doesn't follow provided desscription. It's possible that I've overlooked, forgot or intentionally implemented something that doesn't follow **"best practices"**. 

- At first, I thought that I'll implement front-end/client app using `React`, but admin-site will do just fine.

### References
 + [Official django documentation](https://docs.djangoproject.com/en/2.1/ref/contrib/admin/)
 + [Custom admin-site views (Medium article)](https://medium.com/@hakibenita/how-to-turn-django-admin-into-a-lightweight-dashboard-a0e0bbf609ad)


## Installation / Setup

**Note**: Make sure your located in the root of project (there's `server` folder at your current level). This guide assumes that you have `pip` and `virtualenv` installed and that you're using `*nix` system.

```python
# prepare virtual environment
virtualenv venv -p python3.6

# activate virtual environment
source ./venv/bin/activate

# install dependencies
pip install -r requirement

# navigate to server app folder
cd server

# migrate database (create tables, etc...)
python manage.py migrate

# load prepared data into database
python manage.py loaddata fixture.json

# serve backend
python manage.py runserver
```
