# Custom User Test
## Installation command

```
py -m venv .venv
.\.venv\Scripts\activate.bat
pip install django djangorestframework djangorestframework-simplejwt
py -m venv .venv
python manage.py makemigrations
python manage.py migrate
```

## Development server

```bash
python manage.py runserver
```

## Functionality
* Create custom user
* Create JWT stateless token
* Refresh JWT token <sub>i.e</sub> <ins>generate new access token</ins> 
* Blacklist JWT token <sub>i.e</sub> <ins> can't generate new access token</ins>


### Note:- 
* Token validity is 10 minutes
* After 10 minutes refresh and get new token
* In logout black list refresh token so user will not able to re-generate access token
* 