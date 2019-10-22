# flask-restAPI
### A demo Rest-API:bee: implementation in Flask

This _"one file"_ Rest-API made with Flask microframework :
- support environment variables an secrets with the **python-dotenv** module: Flask is well integrated with dotenv files out if the box; **.env** file is on gitignore as it's for manage the secrets. An example file is provided.  
**.flaskenv** file is public and has the scope to set app variables.
- store data with a **SQLite** database (easy for demo purpose) with the help of **SQLAlchemy** support.  
The sql data is serialized to be managed as json with **Marshmallow** module
- is security enabled: the access and the CRUD operations aren't session based, but implemented with JWT security (**Flask-JWT-Extended** module)
- has some **CLI commands** to create, delete, seed the database with the Flask CLI
- has simple routes for demo pourpose that implements the CRUD with **GET,POST,PUT and DELETE** methods; the results returns status codes also
- has classes that manage the database tables and its schema.  

#### TO DO
- [ ] Add an email backend to manage things like password reset
