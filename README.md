## Marketplace Webapp 🛍️

This assignment will have:
- Marketplace webapp and Dockerfile to build image.
- Docker-compose file to connect to db.
- Kubernetes deployment: still in progress...

## 1. Frontend
- Displays all available products and previously purchased products.
- **Technologies:** HTML,CSS,Bootstrap and JavaScript.

## 2. Backend
- Communicates with database to get available products in stock in the database through an api that is accessible to Frontend.
- Communicates with database to get previously bought items in the database through an api that is accessible to Frontend.
- **Technologies:** Python, Flask.

## 3. Database
- Is contacted only by Backend.
- Dev mode db: Sqlite3
- Prod mode db: PostgreSQL
- **Technologies:** Sqlite3, PostgreSQL (through Flask SQLAlchemy)

To run the webapp in prod mode, change the `debug` value in `docker-compose` to 0 and uncomment the `CMD gunicorn -w 3 --bind 0.0.0.0:5000 run:app` in the Dockerfile. 


Since I have not yet deployed my application on a cloud provider and only tested it locally, it seems that the database ,when importing/exporting to/from gitlab, is always resetting and my products are not being saved, and when I navigate to `127.0.0.1`(localhost), the home page is empty as if I don't have anything saved in my db. 

I have included a `demo` (marketplace-assignment.mp4) to showcase the working webapp.


I have not taken into consideration security measures when connecting to PostgreSQL and accessing the webapp as admin. To create a new admin user switch to the `/register` endpoint and login to the `/login` endpoint. To view admin dashboard navigate to the `/admin` endpoint.



## About the Test Code
Still in progress...

## Additions
- Docker-compose file: connecting the db container, the marketplace container, and reverse proxy container (http service that handles the client requests like nginx): `docker-compose up --build -d`
- Making sure tha if a container crashes it can start up again thanks the `restart: always` in docker-compose
- Deployment on Microsoft Azure using AKS



