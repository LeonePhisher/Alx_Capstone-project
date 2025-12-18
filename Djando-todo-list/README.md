# 📝 TodoList Django Application

A Django-based web application featuring user authentication (login & registration) and a protected Todo dashboard.  
The application uses **Django’s default authentication system** and **SQLite** for simplicity.

---

## 🚀 Features

- User Registration
- User Login & Logout
- Login page as the **first landing page**
- Protected homepage (login required)
- Session-based authentication
- Flash messages for user feedback
- Clean project structure with multiple apps


---

## 🔐 Authentication Flow

1. **Landing Page** → Login
2. Unauthenticated users are redirected to the login page
3. Successful login redirects to the homepage
4. Logout redirects back to the login page
5. Protected routes require authentication

---

## ⚙️ Configuration Highlights

`python
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'

How to Run the Project
1.pip install django
2.python manage.py makemigrations
3.python manage.py migrate
4.python manage.py runserver

Application URLs
Page	URL
Login	/
Register	/register/
Homepage	/home/
Logout	/logout/
