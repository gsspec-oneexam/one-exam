Technical stack that must be installed in local machine:
	1.Python 3.6.5 install via https://www.python.org/downloads/
	2.NodeJS v12.19.0 install via https://nodejs.org/en/download/

***

Back-end:

1.After cloning the project,install requirements at manage.py file level with command:
>`pip install -r requirements.txt

2.Create database "oneexam" and configure your local mysql in settings.py file

3.Perform migrations at manage.py file level with the following commands:
>`python manage.py makemigrations`
>`python manage.py migrate`

4.Execute all the sql insert queries from insertions.sql file.

5.In config.ini add log directory path in log section.

6.In sendemail.py file add settings.py and In metadata.py file add config.ini local path.

7.Start django server at manage.py file level with command:
>`python manage.py runserver`


---
Front-end:

1.After cloning the project,install react node modules by running the command: 
>`npm install`

2.Delete bootstrap.css file located at /node_modules/bootstrap/dist/css/

3.Install react packages with command:
>`npm install react-hook-form`

>`npm install react-radio-buttons`

4.Run react server at package.json file level by command:
>`npm start`

5.In few minutes application window opens in local default browser.


