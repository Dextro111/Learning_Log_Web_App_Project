# Learning Log Web App

A Django-based web application for tracking and managing learning topics and entries. Users can create accounts, organize their learning topics, and document detailed entries for each topic.

## Overview

**Learning Log** is a personal learning management system built with Django. It allows users to:
- Register and manage user accounts with authentication
- Create and organize learning topics
- Log detailed entries for each topic with timestamps
- View all topics and their associated entries
- Edit existing entries
- Keep track of their learning journey

## Features

- **User Authentication**: Secure user registration and login system
- **Topic Management**: Create and organize learning topics
- **Learning Entries**: Document detailed notes and observations for each topic
- **User-Specific Data**: Each user's topics and entries are private and protected
- **Bootstrap UI**: Clean and responsive user interface using Django Bootstrap 3
- **Database-Backed**: Persistent data storage with SQLite (development) and PostgreSQL (production)

## Project Structure

```
Learning_Log_Web_App_Project/
├── learning_log/           # Main project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # URL routing
│   ├── wsgi.py             # WSGI configuration
│   └── asgi.py             # ASGI configuration
├── learning_logs/          # Main application (topics & entries)
│   ├── models.py           # Database models (Topic, Entry)
│   ├── views.py            # View logic
│   ├── forms.py            # Forms for topics and entries
│   ├── urls.py             # App-specific URLs
│   ├── admin.py            # Django admin configuration
│   ├── templates/          # HTML templates
│   ├── static/             # Static files (CSS, JS)
│   └── migrations/         # Database migrations
├── users/                  # User authentication app
│   ├── models.py           # User models
│   ├── views.py            # Authentication views
│   ├── urls.py             # Auth URLs
│   ├── templates/          # Auth templates
│   └── migrations/         # Database migrations
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
├── runtime.txt             # Python version for deployment
└── procfile                # Procfile for Heroku/Render deployment
```

## Technology Stack

- **Backend**: Django 4.2
- **Database**: SQLite (development), PostgreSQL (production)
- **Frontend**: Django Templates, Bootstrap 3
- **Web Server**: Gunicorn, WhiteNoise (static files)
- **Deployment**: Heroku/Render compatible

## Requirements

- Python 3.x
- Django 4.2
- PostgreSQL (for production)

See `requirements.txt` for complete dependencies.

## Installation

### Prerequisites
- Python 3.8 or higher
- Virtual environment tool (venv, conda, etc.)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Dextro111/Learning_Log_Web_App_Project.git
   cd Learning_Log_Web_App_Project
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv ll_env
   source ll_env/bin/activate  # On Windows: ll_env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Application: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Usage

### Creating an Account
1. Navigate to the login page
2. Click "Register" to create a new account
3. Enter username, email, and password

### Creating Topics
1. Log in to your account
2. Click "Topics" from the navigation
3. Click "New Topic" to add a learning topic
4. Enter the topic name and submit

### Logging Entries
1. Select a topic from your topics list
2. Click "New Entry" 
3. Enter your learning notes or observations
4. Submit to save

### Editing Entries
1. View a topic's entries
2. Click the entry you want to edit
3. Modify your notes
4. Click "Save" to update

## Database Models

### Topic
- `text` (CharField): Topic name/title
- `date_added` (DateTimeField): When the topic was created
- `owner` (ForeignKey): User who owns this topic

### Entry
- `topic` (ForeignKey): Associated topic
- `text` (TextField): Entry content/notes
- `date_added` (DateTimeField): When the entry was created

## API & Views

### Learning Logs Views
- `index/`: Home page
- `topics/`: List all user's topics
- `topic/<id>/`: View specific topic with entries
- `new_topic/`: Create new topic
- `new_entry/<topic_id>/`: Add entry to topic
- `edit_entry/<entry_id>/`: Edit existing entry

### User Views
- `register/`: User registration
- `login/`: User login
- `logout/`: User logout

## Deployment

The application is configured for deployment on Heroku or Render using:
- `Procfile`: Application startup configuration
- `runtime.txt`: Python version specification
- `requirements.txt`: All dependencies
- `gunicorn`: Production-grade web server
- `whitenoise`: Static file serving in production
- `django-heroku`: Heroku-specific Django configuration

## Environment Variables

For production deployment, set:
- `SECRET_KEY`: Django secret key (keep secure!)
- `DEBUG`: Set to `False` in production
- `ALLOWED_HOSTS`: Your production domain
- `DATABASE_URL`: Production database connection string

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## License

This project is open source and available under the MIT License.

## Author

[Dextro111](https://github.com/Dextro111)

## Acknowledgments

Built with Django and inspired by the "Crash Course in Python" learning journey.
