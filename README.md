Twitter Clone - Backend
This is the backend of the Twitter Clone project, developed with Django and Django REST Framework.
It provides RESTful APIs for user registration, authentication, tweeting, following users, liking, retweeting, and commenting.

Technologies Used
Python 3.12

Django 5.2

Django REST Framework

PostgreSQL (database)

Project Structure
accounts: User registration, login, tweets, user feed, follow/unfollow.

interactions: Like/unlike tweets, retweet, comment.

Setup Instructions
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/twitter-backend.git
cd twitter-backend
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Apply database migrations:

bash
Copy
Edit
python manage.py migrate
Create a superuser (optional for admin access):

bash
Copy
Edit
python manage.py createsuperuser
Run the development server:

bash
Copy
Edit
python manage.py runserver
Available Endpoints

Endpoint	Method	Description	Authentication
/api/accounts/register/	POST	Register a new user	No
/api/accounts/login/	POST	Obtain JWT access and refresh token	No
/api/accounts/tweet/	POST	Create a new tweet	Yes
/api/accounts/follow/	POST	Follow another user	Yes
/api/accounts/unfollow/	POST	Unfollow a user	Yes
/api/accounts/feed/	GET	Get user feed	Yes
/api/interactions/like/<tweet_id>/	POST	Like or unlike a tweet	Yes
/api/interactions/retweet/<tweet_id>/	POST	Retweet a tweet	Yes
/api/interactions/comment/<tweet_id>/	POST	Comment on a tweet	Yes
Notes
JWT Authentication is required for protected endpoints.

Each tweet is linked to the user who created it.

User actions such as liking, retweeting, and commenting are handled via the interactions app.

References
Django Official Documentation

Django REST Framework Documentation

Simple JWT Documentation


