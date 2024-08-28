# Blogino

![License](https://img.shields.io/github/license/MohNamdar/Blogino)
![Django](https://img.shields.io/badge/Django-4.2%2B-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

**Blogino** is a simple weblog website built using Django for the backend and a custom HTML & CSS theme. The project is designed to provide a basic blogging platform with essential features like post creation, editing, and viewing.

![homepage](https://github.com/MohNamdar/Blogino/blob/main/blog/static/images/screenshots/homepage.jpg)

## Features

- Simple and clean UI/UX.
- User authentication (Login, Logout, Registration).
- Create, edit, delete, and view blog posts.
- Comment system for each post.
- Responsive design.

## Preview

![article list](https://github.com/MohNamdar/Blogino/blob/main/blog/static/images/screenshots/article_list.jpg)
![podcast list](https://github.com/MohNamdar/Blogino/blob/main/blog/static/images/screenshots/podcast_list.jpg)
![gallery](https://github.com/MohNamdar/Blogino/blob/main/blog/static/images/screenshots/gallery.jpg)
![article_page1](https://github.com/MohNamdar/Blogino/blob/main/blog/static/images/screenshots/article_page1.jpg)
![article_page2](https://github.com/MohNamdar/Blogino/blob/main/blog/static/images/screenshots/article_page2.jpg)


## Installation

To run this project locally, follow these steps:

### Prerequisites

- Python 3.8+
- Django 4.2+
- Git
- Virtualenv (recommended)
- PostgreSQL with `pg_trgm` extension installed

### Clone the Repository
```bash
git clone https://github.com/MohNamdar/Blogino.git
cd Blogino
```

### Set Up a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Customize Database Settings

Before running the project, make sure to customize the database settings in settings.py to match your PostgreSQL database configuration. You must also ensure that the pg_trgm extension is installed in your PostgreSQL database. You can do this by running the following SQL command:
```bash
CREATE EXTENSION IF NOT EXISTS pg_trgm;
```

### Apply Migrations
After configuring your database, run the following commands to apply the migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the Development Server
```bash
python manage.py runserver
```

### Now you can visit http://127.0.0.1:8000/ in your browser to see the blog in action.
------
## Usage
### Admin Panel
You can access the Django admin panel at /admin/. To create a superuser, run:
``` bash
python manage.py createsuperuser
```
------

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you'd like to see.

### Acknowledgments
- Django framework for making web development easier and faster.
- Using on Personal Webpage [Mohnam.ir](https://Mohnam.ir)
- Thanks to all contributors!
