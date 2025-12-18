# TodoList Django Application

## Project Overview
The objectives of this project are to:

- Implement user authentication (login and registration)
- Protect views using Django authentication decorators
- Manage redirects and authentication flow correctly
- Organize templates and URLs properly
- Use Django’s built-in authentication system

---

## Functionalities

- Users can create an account (register)
- Users can log in using their valid credentials
- Users can log out of the system
- Users can also share tasks among them selfs
 - Users can also delete tasks
- Users can also delete tasks
- Users can also mark tasks as completed or not
- The login page is the default landing page
- Only authenticated users can access the homepage
- Error and success messages are displayed to users

---


---

## Authentication Flow

1. When the application starts, the **login page** is displayed
2. Unauthenticated users are restricted from accessing protected pages
3. Successful login redirects the user to the homepage
4. Logout redirects the user back to the login page
5. The homepage is protected using Django’s `@login_required` decorator

---

## Configuration Settings
python
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'

##Technologies Used
Python
Django Framework
SQLite Database
HTML & CSS

##How to Run the Project
1.pip install django
2.python manage.py makemigrations
3.python manage.py migrate
4.python manage.py runserver

##Application URLs
Page	URL
Login	/
Register	/register/
Homepage	/home/
Logout	/logout/




