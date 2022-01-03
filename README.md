# Title 
Data Representation Project 2021

# Description
The purpose of this project is to be able to demonstrate a fundamental understanding of a functional and operational Restful API. This project can be used in whichever manner is seen to demonstrate the folloeing, at a minimum: 
> Flask Server
> REST API
> Database Table
> Web interface

The web application has been developed in Flaskserver with an API that performs calls with a database table. This API has been devloped so that it can perform CRUD operations i.e. Create, Read, Update & Delete files. 
Authorisation has also been added to this project, such that only those with a specific Username & Password have access to this web application. 

# Installation
In order to run this Project, the user will have to clone the publicly available repository to their local machine, via https://github.com/jonkavana/data-representation-project
Once this has been successfully completed, the user will need to be able to create a virtual environment. 
This can be completed with the following commands. 
> "python -m venv venv"
> ".\venv\Scripts\activate.bat
Once the virtual has been stood up, a requirements text file will allow the environment to be re-created. 
The contents of this file can be accessed from any text file editor prior to running it. Once reviewed,  run the following command:  
> "pip freeze -r requirements.txt" 

You have now created the virtual environment if you have followed these steps correctly. If there are any issues with this, a listing of websites has been created in the Research & Support section detailed below.

# Instructions
If you have successfully created a virtual environment as detailed in the 'Installation' section above, then you can proceed with the Project. 
Copy and paste the URL that the virtual environment generates into your preferred browser. This project has been developed in both Chrtome & FIrefox. 
Once you run this URL, you will automatically be shown the 'home.html' page. This page has been created so that it has a closed audience. 
For ease of access however, the credentials have been left in a semi-transparent manner in the field itself. 

> Username: Lecturer 
> Password: DataRep

These have been set to be case sensitive details. Once the user has submitted these details, they will be taken to the main page.

'Index.html': is the main wen application that displays the information that has been generated in the web application, whilst stored to a database. 
It is in this application that we will see the opportunity ot access all of the CRUD functionality that satisfies the requirements of the brief. 
Create: There has been due diligence given to have funcitons in place that will allow for new students to be logged online. 
Read: The information that is currently hosted in the database is in place and is running live, so any adjustments made will be reflected in real time. If the user has accidenly clicked on this button, then a home page has been added to bring the user back to the home screen.
Update: Beside each student, there is the ability to change the details of the individual, apart from their id. The Id has been set as the primary key within the database. If the user has accidenly clicked on this button, then a home page has been added to bring the user back to the home screen.
Delete: Should the user wish to remove an entry from the application completely, they can simply click on the delete button that resides alongsie the student name.

# Research & Support
Pip Command Support - https://pip.pypa.io/en/stable/cli/pip_freeze/

# Additional Material
There is also a numbe of test files that were developed in tandem with any of the fuctionality that was developed. These can be seen in the following files: 
>testDBSelect.py
>testStudentDao.py

The first of these files was created whent there was a need to create a layer of security and to allow for a user not in the local devise to access the database. 
The second of these files was created whilst developing the basic operations of the web application.

# Bibliography - Centralised 
https://stackoverflow.com/questions/16562577/how-can-i-make-a-button-redirect-my-page-to-another-page, retrieved on 29/11/2021 <br>
https://www.w3schools.com/tags/tag_style.asp, retrieved on 29/11/2021 <br>
https://www.kite.com/python/answers/how-to-redirect-to-a-url-using-flask-in-python, retrieved on 29/11/2021 <br>
https://hackersandslackers.com/flask-routes, retrieved on 29/11/2021 <br>
https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_input_test, retrieved on 29/11/2021 <br>
https://stackoverflow.com/questions/29900287/should-head-and-body-tags-be-on-a-different-level-of-indentation-to-html, retrieved on 29/11/2021 <br>
https://www.w3schools.com/tags/tag_input.asp, retrieved on 29/11/2021 <br>
https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/password, retrieved on 29/11/2021 <br>
https://medium.com/swlh/how-to-create-your-first-login-page-with-html-css-and-javascript-602dd71144f1, retrieved on 29/11/2021 <br>
https://htmlcolorcodes.com/, retrieved on 29/11/2021 <br>
https://www.w3.org/Style/Examples/007/fonts.en.html, retrieved on 29/11/2021 <br>
https://medium.com/swlh/how-to-create-your-first-login-page-with-html-css-and-javascript-602dd71144f1, retrieved on 29/11/2021 <br>
https://searchapparchitecture.techtarget.com/definition/RESTful-API#:~:text=A%20RESTful%20API%20is%20an,deleting%20of%20operations%20concerning%20resources, retrieved on 29/11/2021 <br>
https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics, retrieved on 29/11/2021 <br>
https://www.freecodecamp.org/news/get-started-with-css-in-5-minutes-e0804813fc3e/, retrieved on 29/11/2021 <br>
https://www.geeksforgeeks.org/css-introduction/, retrieved on 29/11/2021 <br>
https://www.tutorialspoint.com/flask/index.htm, retrieved on 29/11/2021 <br>
https://flask.palletsprojects.com/en/2.0.x/tutorial/, retrieved on 29/11/2021 <br>