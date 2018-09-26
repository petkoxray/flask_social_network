# Simple social network built with Flask
***

### Functionalities
- Authentication (regiser, login, reset password)
- Users can create posts
- Users can follow / unfollow other users and can see their posts on home page if followed
- Users can edit their account info and use gravatar for avatar
- Users can write private messages to other users and receive notifications if there is a new message
- Simple search functionality for posts (using elasticsearch)

## Instalation

#### Prerequisites

  - Python >= 3.6
  - Elasticsearch server for the search engine

#### Steps

```sh
git clone https://github.com/petkoxray/flask_social_network
cd flask_social_network
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask db upgrade
set FLASK_APP=run.py
flask run
```
#### How to use
You should configure your environment variables in config.py

#### Demo
Here you can see working demo deployed in Heroku -
https://f-social-network.herokuapp.com/home
###### Example login: test@test.com password: 123
