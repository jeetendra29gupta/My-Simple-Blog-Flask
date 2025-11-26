# Flask Blogging Application

A full-featured blogging platform built with Flask, featuring user authentication, blog post management, and a clean,
responsive design. This project uses `uv` as the Python package manager for faster and more reliable dependency
management.

## Features

- User authentication (Sign up, Sign in, Sign out)
- Create, Read, Update, and Delete blog posts
- User-specific blog management
- Responsive web design
- Markdown support for blog content
- Secure password hashing with bcrypt
- CSRF protection
- SQLite database with SQLAlchemy ORM

## Prerequisites

- Python 3.11 or higher
- uv - The ultra-fast Python package installer and resolver
- Git (optional, for version control)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jeetendra29gupta/My-Simple-Blog-Flask.git
   cd My-Simple-Blog-Flask
   ```

2. Initialize the project and install dependencies using `uv`:
   ```bash
   uv init
   uv add flask flask-sqlalchemy flask-login flask-wtf wtforms flask-bcrypt email-validator python-dotenv markdown2
   ```

3. Set up environment variables:
   Create a `.env` file in the project root with the following content:
   ```
   SECRET_KEY=your-secret-key-here
   DATABASE_URI=sqlite:///blog.db
   ```

## Running the Application

1. Sync dependencies (if needed):
   ```bash
   uv sync
   ```

2. Start the development server:
   ```bash
   uv run main.py
   ```

3. Open your browser and navigate to:
   ```
   http://localhost:8181
   ```

## Project Structure

```
Blogging/
├── .venv/               # Virtual environment
├── instance/            # Instance folder for database and config
├── src/                 # Application source code
│   ├── __init__.py
│   ├── config.py        # Configuration settings
│   ├── models.py        # Database models
│   └── routes.py        # Application routes
├── static/              # Static files (CSS, JS, images)
├── templates/           # HTML templates
│   ├── 404.html
│   ├── create-blog.html
│   ├── edit-blog.html
│   ├── index.html
│   ├── layout.html
│   ├── message.html
│   ├── my-blog.html
│   ├── navigation.html
│   ├── signin.html
│   ├── signup.html
│   └── view-blog.html
├── .env                 # Environment variables
├── .gitignore
├── main.py              # Application entry point
└── pyproject.toml       # Project dependencies and metadata
```

## Technologies Used

- **Backend**: Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, JavaScript
- **Authentication**: Flask-Login
- **Password Hashing**: Flask-Bcrypt
- **Form Handling**: Flask-WTF
- **Markdown Support**: Flask-Markdown

## Acknowledgments

- Flask and its ecosystem for providing a robust web framework
- All open-source libraries used in this project

## Screenshot
![{61153CE1-EA96-4576-A0BC-5202A3A7C135}.png](docs/%7B61153CE1-EA96-4576-A0BC-5202A3A7C135%7D.png)
![{D35AEEF5-B465-4FD9-BDE6-86D420B5AB98}.png](docs/%7BD35AEEF5-B465-4FD9-BDE6-86D420B5AB98%7D.png)
![{CBE9E740-590C-4BCB-9EAD-E5D7C451DCDB}.png](docs/%7BCBE9E740-590C-4BCB-9EAD-E5D7C451DCDB%7D.png)
![{7612F514-2789-4C31-A884-85F1EA5CD294}.png](docs/%7B7612F514-2789-4C31-A884-85F1EA5CD294%7D.png)
![{6199C733-066A-4AC1-8E27-8647AE746235}.png](docs/%7B6199C733-066A-4AC1-8E27-8647AE746235%7D.png)
![{0F6477C9-2D47-4404-BA83-75380F8B468C}.png](docs/%7B0F6477C9-2D47-4404-BA83-75380F8B468C%7D.png)