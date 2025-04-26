# Twitter Clone Backend

## Overview

This project is a backend clone of Twitter (X) that implements essential functionalities such as user authentication, tweet management, following users, liking, retweeting, and commenting.  
The backend is built using Django and Django REST Framework (DRF), with PostgreSQL as the database for production environments.

---

## Features

- User authentication with JWT
- User registration and login
- Create, delete, and interact with tweets
- Follow and unfollow users
- Like and unlike tweets
- Retweet tweets
- Comment on tweets

---

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Authentication**: SimpleJWT
- **Database**: PostgreSQL (local and production)
- **API Documentation**: Not yet implemented (Swagger integration recommended)

---

## Architecture

The backend is structured into modular Django apps:

- **accounts**: Handles user management, authentication, and tweets.
- **interactions**: Manages tweet interactions like likes, retweets, and comments.

The backend exposes a RESTful API consumed by the frontend (React).

---

## API Endpoints Overview

### Authentication

- `POST /api/accounts/register/` - Register a new user
- `POST /api/accounts/login/` - Obtain JWT access and refresh tokens
- `POST /api/accounts/login/refresh/` - Refresh expired access token

### User Actions

- `POST /api/accounts/follow/` - Follow a user
- `POST /api/accounts/unfollow/` - Unfollow a user
- `GET /api/accounts/feed/` - Get tweets from followed users

### Tweets

- `POST /api/accounts/tweet/` - Create a new tweet

### Interactions

- `POST /api/interactions/like/<tweet_id>/` - Like or unlike a tweet
- `POST /api/interactions/retweet/<tweet_id>/` - Retweet a tweet
- `POST /api/interactions/comment/<tweet_id>/` - Comment on a tweet

---

## Setup Instructions

### Local Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/twitter-backend.git
   cd twitter-backend
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure PostgreSQL settings in `settings.py` or using a `.env` file.

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser (optional):

   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

---

## Testing Strategy

- Manual testing of all endpoints via Postman during development.
- Automated testing planned for future versions (pytest, Django TestCase).

---

## Project Status

This backend is functional and serves as the foundation for the frontend React application.

- JWT Authentication fully implemented
- Core tweet and interaction functionalities completed
- Ready for deployment with production database configuration

---

## References

- [Django Documentation](https://docs.djangoproject.com/en/5.2/)
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
- [Simple JWT Documentation](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

---

# Observations

- The backend is designed to be secure, modular, and easy to extend.
- Best practices in code organization and RESTful API development were followed.
