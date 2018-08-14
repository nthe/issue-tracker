# Issue Tracker
Simple issue tracker application.

- Feel free to ask about anything that is unclear, doesn't make sense or doesn't follow provided desscription. It's possible that I've overlooked, forgot or intentionally implemented something that doesn't follow **"best practices"**. 

- At first, I thought that I'll implement front-end/client app using `React`, but admin-site will do just fine.

## Description
```
Navrhnout a implementovat v Djangu jednoduchý issue tracker:‎
- issue má zadavatele, řešitele, textový popis, stav, kategorii (např. bug, vylepšení, dokumentace)
- issues lze ve webovém rozhraní přidávat, editovat a budou mít stránku se seznamem (lze použít Django Admin nebo jakoukoliv jinou knihovnu)
- seznam issues zobrazuje v hlavičce jednoduché statistiky (průměrný, nejdelší a nejkratší čas řešení issue)
- kategorie stačí mít pouze v DB, bez administrace, ale v  budoucnu by její přidání mělo být co nejjednodušší
- 2 uživatelské role: superuser a staff, staff nesmí nic měnit ani přidávat, superuser může vše
- smysluplné verzování Gitem
- jako DB stačí sqlite‎
- musí být jasné, jak projet nainstalovat a spustit‎
```

### References
 + [Official Django REST framework documentation](http://www.django-rest-framework.org/)
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
# TODO: There's django-command that does exactly same thing
python ./load_fixtures.py

# serve backend
python manage.py runserver
```


## Notes

### Models
 - One can say, that `Status` can be implemented via `choices`. That's true, but it's not ideal since it's not editable via API (without explicit implementation).
 - `on_delete` behavior is debatable and would depend on other factors, current behavior was choosen without extensive thinking.
 - Yes, `__str__` method of `Issue` model does extra query to find out status. It was introduced to this app for `admin` portal.
 - To store or not to store stats (resolution time, etc...)? Calculating them during saving process is easy, but takes space. Calculating them during retrieval takes time and resources.  

### Views
 - Pretty straightforward in this case, no need to over-complicate it for no real reason.

### Serializers
 - I'm not big fan of `rest_frameworks`'s serializers. It takes too much code to optimize queries in case of "deep" relations - might use experimental `serpy` module, which can be easily rewritten to work similar to `ModelSerializer`.

### Roles / groups
 - I created two groups - `SuperUser` and `Staff` - and gave them specific model-permissions. Pretty simple and works nicely with admin-site.
