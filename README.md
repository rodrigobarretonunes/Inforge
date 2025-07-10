# Inforge

Inforge is a web application developed with Django focused on user authentication, account management, and a modular structure for future expansion. The project already includes custom templates, organized static files, and a dedicated authentication app.

## Features

- Initial Django structure ready for development
- `authcore` app for authentication and user management
- Templates for login, signup, and user management
- Organization of static files (CSS, JS, images) by module
- SQLite database configured for development environment

## Project Structure

```
Inforge/
│
├── authcore/                # Custom authentication app
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│
├── core/                    # Main Django configuration
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── statics/                 # Static files organized by module
│   ├── accounts/
│   └── authcore/
│
├── templates/               # HTML templates organized by module
│   ├── account/
│   └── authcore/
│
├── db.sqlite3               # SQLite database for development
├── manage.py                # Django management utility
├── pyproject.toml           # Python dependencies configuration
├── uv.lock                  # Dependencies lockfile
└── README.md                # Project documentation
```

## How to Run the Project

1. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
   or use `pyproject.toml` with Poetry/PDM.

2. Apply the migrations:
   ```
   python manage.py migrate
   ```

3. Start the development server:
   ```
   python manage.py runserver
   ```

4. Access at: http://127.0.0.1:8000/

## Suggested Next Steps

- Implement automated tests for authentication and signup
- Add API documentation (if applicable)
- Configure deployment for production environment

---
