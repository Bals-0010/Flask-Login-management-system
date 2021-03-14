# Flask-Login-management-system
<br>Simple login management system using Python/Flask


To run: <br>
> python main.py
<br>


### Login Page <br>
![Alt text](/screenshots/login.jpg?raw=true "Login Page")

<br>

### Logged in <br>
![Alt text](/screenshots/loggedin.jpg?raw=true "Logged in")

<br>

### Logged out <br>
![Alt text](/screenshots/loggedout.jpg?raw=true "Logged out")
<br>

To login using sample credentials use:<br>
username : admin<br>
password : admin<br>

<br>
To create a new login credentials (use terminal commands as mentioned below): <br>
>>> python<br>
>>> from main import db, User<br>
>>> user1 = User(username="admin", password= "password")<br>
>>> db.session.add(user1)<br>
>>> db.session.commit()<br>

<br>
To manage database(save.db) using GUI:<br>
https://sqlitebrowser.org/ <br><br>

Sample Screenshot:<br>
![alt text](https://sqlitebrowser.org/images/screenshot.png)
