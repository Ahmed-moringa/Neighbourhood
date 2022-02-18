# MyNeighbourhood

>[Ahmed Mohamed](https://github.com/Ahmed-moringa)  
>[John Nyamweya](https://github.com/nyamzy)
  
# Description  
If you are like me, You really don’t know what is happening in your neighborhood most of the time. What if an important meeting happens, theft or even death wouldn’t you like to know about it.
Your Job is to create a web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

## Screenshots 
###### Home page
 

 [![neighbourhood.png](https://i.postimg.cc/rFwNnH9S/neighbourhood.png)](https://postimg.cc/QVv7V0wt)

## User Story  
  
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.
  
  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/Ahmed-moringa/Neighbourhood.git
```
##### Navigate into the folder 
 ```bash 
cd Neighbourhood
```
##### Install and activate Virtual Environment
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make Migrations  
 ```bash 
python manage.py makemigrations neighbour
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python](https://www.python.org/)  
* [Django](https://docs.djangoproject.com)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [ahmed.mohamed@student.moringaschool.com]  
  
## License 

* Copyright (c) 2022 **Ahmed Mohamed**
* Copyright (c) 2022 **John Nyamweya**