# owwned-ril19

### Initialize venv (once):

```bash
python -m venv venv
```

### Activate venv:

MacOS/Linux: `bash. venv/bin/activate`

Windows (cmd): `bashvenv\Scripts\activate`

Windows (bash): `bashsource venv/Scripts/activate`

Django installation:

```bash
pip install django
```

(Once by app) Créer l'application

```bash
mkdir apps/<app_name>
python manage.py startapp <app_name> apps/<app_name>
```

Add apps. before app name in apps.py
Add application to settings.py

### Start Django Server (from backend):

```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Update Database Schema

```bash
python manage.py makemigrations
python manage.py migrate
```

### Update Frontend Graphql Schema

```bash
python manage.py graphql_schema --out ../frontend/src/schema.json
```
