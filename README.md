# My Django Project

This is a simple Django project set up to demonstrate the use of an SMTP mailing system.

## Project Structure

```
my-django-project
├── my_django_project
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── test.http
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd my-django-project
   ```

2. **Create and activate a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```
   python manage.py migrate
   ```

5. **Run the development server:**
   ```
   python manage.py runserver
   ```

## Usage

- Use the `test.http` file to test the SMTP mailing system by sending emails to users.
- Modify the `settings.py` file to configure your email backend and SMTP settings.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.
