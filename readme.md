# Fake Recipes Page in Django

This repository contains a fake recipes page developed as part of a course on Django for learning purposes only.

## Purpose

The purpose of this project is to provide a hands-on learning experience with Django, a high-level Python web framework, by building a simple recipe sharing website. This project serves as a practical application of concepts learned throughout the course.

## Features

- User authentication: Users can sign up, log in, and log out.
- Recipe management: Users can create, read, update, and delete recipes.
- Ingredient management: Users can specify ingredients for each recipe.
- Search functionality: Users can search for recipes based on keywords.
- Responsive design: The website is designed to be accessible on various devices.

## Technologies Used

- Python
- Django
- HTML
- CSS

## Setup Instructions

1. Clone the repository:

```bash
git clone <repository_url>
```

2. Navigate to the project directory:

```bash
cd fake-recipes-page-django
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment:

- On Windows:

```bash
venv\Scripts\activate
```

- On macOS and Linux:

```bash
source venv/bin/activate
```

5. Install the required dependencies:

```bash
pip install -r requirements.txt
```

6. Apply migrations:

```bash
python manage.py migrate
```

7. Create a superuser:

```bash
python manage.py createsuperuser
```

8. Run the development server:

```bash
python manage.py runserver
```

9. Access the website in your browser at `http://127.0.0.1:8000`.

## Note

This project is intended for educational purposes only. It is not meant for production use.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.