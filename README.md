# Incubatour Lead Tracker

A **Django 5.1.5** web application for **lead management**, built to scale Incubatour’s intake and tracking of entrepreneur applications.

---

## 🏗️ Architecture Overview

- **Framework**: Django 5.1.5, Python 3.11+
- **Database**: SQLite (default) with Django ORM; configuration in `lead_tracker/settings.py` under `DATABASES`. Easily switchable to PostgreSQL/MySQL by updating `ENGINE`, `NAME`, `USER`, `PASSWORD`, `HOST`, and `PORT`.
- **Templates**: Django Templates with Bootstrap 5 for responsive UI.
- **Routing**: URL patterns defined in `lead_tracker/urls.py` and `leads/urls.py`.
- **Authentication**: Django’s built-in `auth` system for login/logout and view protection (`@login_required`).
- **Admin**: Auto-generated via `admin.site.register(Lead)` in `leads/admin.py` (create if not present) for quick CRUD operations.

---

## 📂 Code Structure

```
marketing_repo/
│
├── lead_tracker/           # Main project
│   ├── settings.py         # Core settings, INSTALLED_APPS, DATABASES, STATIC
│   ├── urls.py             # Global URL router
│   └── wsgi.py, asgi.py
│
├── leads/                  # Lead management app
│   ├── models.py           # Lead model with fields: full_name, company, email, phone, status, next_follow_up, etc.
│   ├── views.py            # Function-based views: lead_list, lead_create, lead_update, lead_delete, public_lead_form
│   ├── forms.py            # Django ModelForms: LeadForm, PublicLeadForm
│   ├── urls.py             # App-specific URL patterns
│   └── admin.py            # (Optional) Admin registration
│
├── templates/              # HTML templates
│   ├── base.html           # Base layout
│   ├── home.html           # Landing page for users
│   ├── leads/              # Authenticated user templates
│   └── public/             # Public submission templates
│
├── static/                 # Static assets (CSS, JS, images) [if present]
├── db.sqlite3              # SQLite database file (auto-generated)
└── manage.py               # Django CLI utility
```

---

## ⚙️ Technical Setup

1. **Clone & VirtualEnv**
   ```bash
   git clone https://github.com/yourusername/marketing_repo.git
   cd marketing_repo
   python3 -m venv env && source env/bin/activate
   ```

2. **Dependencies**
   - Core: `Django==5.1.5`
   - (Add a `requirements.txt` for pip install -r requirements.txt)

3. **Database Configuration**
   ```python
   # lead_tracker/settings.py
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   ```
   To switch to PostgreSQL:
   ```python
   'ENGINE': 'django.db.backends.postgresql',
   'NAME': 'your_db', 'USER': 'user', 'PASSWORD': 'pass', 'HOST': 'localhost', 'PORT': '5432'
   ```

4. **Migrations & Superuser**
   ```bash
   python manage.py makemigrations leads
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **Environment Variables**
   - SECRET_KEY: Override in `settings.py` or via `.env`.
   - DEBUG: `True` for dev, `False` for prod.
   - ALLOWED_HOSTS: Add domain/IP for production.

6. **Static Files**
   ```bash
   python manage.py collectstatic
   ```

7. **Run Server**
   ```bash
   python manage.py runserver
   ```

---

## 🔌 API Endpoints & Views

| Path                         | Method | View                    | Auth Required | Description                             |
| ---------------------------- | ------ | ----------------------- | ------------- | --------------------------------------- |
| `/`                          | GET    | `home_view`             | No            | Landing page                            |
| `/login/`                    | GET/POST | `LoginView`          | No            | User login                              |
| `/logout/`                   | GET    | `LogoutView`            | Yes           | User logout                             |
| `/leads/`                    | GET    | `lead_list`             | Yes           | List all leads                          |
| `/leads/lead/new/`           | GET/POST | `lead_create`        | Yes           | Create a new lead                       |
| `/leads/lead/<int:pk>/`      | GET    | `lead_detail`           | Yes           | View lead details                       |
| `/leads/lead/<int:pk>/update/` | GET/POST | `lead_update`      | Yes           | Edit lead                               |
| `/leads/lead/<int:pk>/delete/` | POST | `lead_delete`         | Yes           | Delete lead                             |
| `/contact/`                  | GET/POST | `public_lead_form`   | No            | Public submission of new lead           |
| `/contact/thank-you/`        | GET    | `public_lead_thanks`     | No            | Submission confirmation page            |
| `/admin/`                    | GET/POST| `admin.site`           | Yes (superuser) | Django Admin UI for all models        |

---

## ⚙️ Testing & Quality

- **Unit Tests**: Add tests in `leads/tests.py` using Django’s `TestCase`.
- **Linting**: Integrate `flake8` or `pylint`.
- **CI/CD**: Configure GitHub Actions for automated tests and linting.

---

## 📦 Deployment

- **WSGI**: Ensure `wsgi.py` is configured for production.
- **Server**: Deploy on Gunicorn + Nginx or any PaaS (Heroku, AWS Elastic Beanstalk).
- **Env Vars**: Set `DEBUG=False`, `SECRET_KEY`, and `ALLOWED_HOSTS`.
- **Database**: Migrate to production DB (PostgreSQL/MySQL).
- **Static & Media**: Serve via CDN or static file server.

---

## 🤝 Contributing

Feature requests and pull requests are welcome. Please follow standard GitHub flow:
1. Fork repo → 2. Create branch → 3. Implement → 4. Write tests → 5. Submit PR

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

