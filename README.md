# 🔐 Vaultora

**Vaultora** is a Django-based document and file management application designed with a modular backend architecture, secure authentication, PostgreSQL database integration, document management workflows, REST API support, and a clean separation between frontend templates and backend application logic.

The project is built as a practical full-stack Django application with an architecture that can be extended for production-oriented features such as cloud storage, background processing, notifications, and API-driven integrations.

---

## ✨ Features

### 🔐 Authentication & User Management

* Custom Django User model
* User registration and login
* Session-based authentication
* User profile management
* Profile photo upload
* Password change
* Password reset workflow
* Email-based password reset
* Login/logout redirection
* Django authentication and authorization system

### 📄 Document Management

* Create documents
* View document details
* Update documents
* Delete documents
* Document listing
* Document-related forms and views
* Document storage service architecture
* Document signals
* File upload support

### 🗂️ Categories

* Category management
* Document categorization
* Dedicated categories application
* Extensible category architecture

### 🌐 REST API

Vaultora includes a versioned API structure:

```text
/api/v1/
```

The API architecture is designed to make the application easier to integrate with external clients and future frontend applications.

### 🧩 Modular Architecture

The backend is divided into separate Django applications:

```text
accounts
documents
categories
core_site
dashboard
```

Additional reusable backend components are organized into:

```text
core/
services/
api/
```

This keeps business logic, reusable utilities, services, and application-specific functionality separated.

### 📧 Email Integration

The project supports SMTP-based email functionality for features such as password reset and account-related communication.

### 🗄️ PostgreSQL

Vaultora uses **PostgreSQL** as its primary relational database.

The project supports environment-based database configuration through `DATABASE_URL`, while also maintaining a PostgreSQL fallback configuration for local development.

### 🎨 Frontend

The frontend is implemented using Django Templates with:

* HTML
* CSS
* Django Template Language
* Reusable base template
* Account pages
* Dashboard pages
* Document management pages

### 🧪 Testing

The project contains dedicated test modules for:

```text
API
Authentication
Documents
```

Example:

```text
backend/tests/
├── test_api.py
├── test_auth.py
└── test_documents.py
```

---

# 🏗️ Project Architecture

```text
Vaultora/
│
├── backend/
│   │
│   ├── api/
│   │   └── v1/
│   │
│   ├── apps/
│   │   ├── accounts/
│   │   ├── categories/
│   │   ├── core_site/
│   │   ├── dashboard/
│   │   └── documents/
│   │
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── core/
│   │   ├── exceptions.py
│   │   ├── pagination.py
│   │   ├── permissions.py
│   │   ├── utils.py
│   │   └── validators.py
│   │
│   ├── services/
│   │   ├── document_service.py
│   │   ├── notification_service.py
│   │   └── storage_service.py
│   │
│   ├── tests/
│   │   ├── test_api.py
│   │   ├── test_auth.py
│   │   └── test_documents.py
│   │
│   ├── manage.py
│   └── requirements.txt
│
├── frontend/
│   ├── static/
│   │   └── css/
│   │
│   └── templates/
│       ├── accounts/
│       ├── dashboard/
│       ├── documents/
│       ├── base.html
│       └── home.html
│
├── database/
│   └── README.md
│
├── docs/
│   ├── api.md
│   ├── architecture.md
│   ├── database.md
│   └── setup.md
│
├── .env.example
├── .gitignore
└── README.md
```

---

# 🛠️ Technology Stack

| Technology            | Purpose                                    |
| --------------------- | ------------------------------------------ |
| Python                | Backend programming language               |
| Django 6.0.7          | Web framework                              |
| Django REST Framework | REST API development                       |
| PostgreSQL            | Relational database                        |
| Psycopg               | PostgreSQL database adapter                |
| Pillow                | Image processing and profile photo support |
| python-dotenv         | Environment variable management            |
| dj-database-url       | Database URL configuration                 |
| Gunicorn              | WSGI application server                    |
| WhiteNoise            | Static file serving                        |
| HTML                  | Frontend structure                         |
| CSS                   | Frontend styling                           |
| Git                   | Version control                            |
| GitHub                | Source code hosting                        |

---

# ⚙️ Requirements

Before running the project, make sure you have:

* Python 3.12+
* PostgreSQL
* Git
* Virtual environment support
* pip

---

#  Installation & Setup

## 1. Clone the repository

```bash
git clone https://github.com/mdsagurali/vaultora.git
```

```bash
cd vaultora
```

---

## 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it:

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r backend/requirements.txt
```

---

## 4. Configure environment variables

Create a `.env` file in the project root:

```text
SECRET_KEY=your-secret-key
DEBUG=True

ALLOWED_HOSTS=127.0.0.1,localhost

CSRF_TRUSTED_ORIGINS=http://127.0.0.1:8000,http://localhost:8000

DATABASE_URL=postgresql://username:password@localhost:5432/vaultora

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

> Never commit your real `.env` file, database credentials, email credentials, or secret keys to GitHub.

A safe example configuration is provided in:

```text
.env.example
```

---

# 🗄️ Database Setup

Create a PostgreSQL database and configure the connection through `DATABASE_URL`.

Example:

```text
DATABASE_URL=postgresql://vaultora_user:password@localhost:5432/vaultora
```

Then run:

```bash
cd backend
```

```bash
python manage.py migrate
```

---

# 👤 Create Superuser

Create an administrator account:

```bash
python manage.py createsuperuser
```

Follow the prompts to set the username, email, and password.

---

# ▶️ Run the Development Server

From the `backend` directory:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

# 🔎 Useful Django Commands

### Check project configuration

```bash
python manage.py check
```

### Create migrations

```bash
python manage.py makemigrations
```

### Apply migrations

```bash
python manage.py migrate
```

### View migration status

```bash
python manage.py showmigrations
```

### Run tests

```bash
python manage.py test
```

### Open Django shell

```bash
python manage.py shell
```

### Collect static files

```bash
python manage.py collectstatic
```

---

# 🔌 API Structure

Vaultora follows a versioned API architecture:

```text
/api/v1/
```

Versioning the API from the beginning makes it easier to introduce future API versions without breaking existing clients.

Detailed API documentation is available in:

```text
docs/api.md
```

---

# 📚 Documentation

Additional project documentation is organized under:

```text
docs/
```

### Architecture

```text
docs/architecture.md
```

Describes the overall application architecture and component organization.

### Database

```text
docs/database.md
```

Contains database-related documentation.

### API

```text
docs/api.md
```

Contains API-related documentation.

### Setup

```text
docs/setup.md
```

Contains project setup and development instructions.

---

# 🔒 Security

Vaultora follows environment-based configuration for sensitive information.

Sensitive values such as:

* Django `SECRET_KEY`
* Database credentials
* Email credentials
* Production configuration

should be stored in environment variables rather than committed to source control.

The repository includes:

```text
.env.example
```

as a template for required environment variables.

---

# 🧪 Project Validation

The project configuration can be verified using:

```bash
python manage.py check
```

Expected result:

```text
System check identified no issues (0 silenced).
```

Migration status can be checked with:

```bash
python manage.py showmigrations
```

---

# 📌 Project Status

**Current Status:** Active Development

The core project structure, authentication system, document management workflow, PostgreSQL integration, REST API architecture, frontend templates, services layer, and automated test structure are implemented.

Future development may include additional API endpoints, advanced document permissions, improved storage integrations, background processing, notifications, and production deployment.

---

# 🗺️ Future Improvements

Potential improvements include:

* [ ] Advanced document permissions
* [ ] Role-based access control
* [ ] Cloud file storage
* [ ] Object storage integration
* [ ] Advanced REST API endpoints
* [ ] API authentication with JWT
* [ ] API documentation with Swagger/OpenAPI
* [ ] Background task processing
* [ ] Redis integration
* [ ] Celery integration
* [ ] Advanced search and filtering
* [ ] Document sharing
* [ ] Activity logging
* [ ] Production deployment
* [ ] CI/CD pipeline

---

# 🤝 Contributing

Contributions are welcome.

To contribute:

```bash
git clone https://github.com/mdsagurali/vaultora.git
```

Create a new branch:

```bash
git checkout -b feature/your-feature
```

Make your changes, test them, and commit:

```bash
git add .
git commit -m "Add: your feature"
```

Push your branch:

```bash
git push origin feature/your-feature
```

Then open a Pull Request.

---

# 📄 License

This project currently does not specify an open-source license.

If this project is intended to be publicly reusable, an appropriate license such as MIT can be added later.

---

# 👨‍💻 Author

**Md Sagur Ali**

Python Backend Developer

### GitHub

https://github.com/mdsagurali

### LinkedIn

https://www.linkedin.com/in/mdsagurali/

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

**Vaultora — Secure, modular, and extensible document management with Django.**
