# Title 
Data Representation Project 2021

## Description
The purpose of this project is to be able to demonstrate a fundamental understanding of a functional and operational Restful API that sits in-between a web application and datebase, which when properly running will be running live. This project can be used in whichever manner is seen to demonstrate the following, at a minimum:

> Flask Server <br>
> REST API <br>
> Database Table <br>
> Web interface <br>

The web application has been developed in Flask server with an API that performs calls with a database table. This API has been developed so that it can perform CRUD operations i.e., Create, Read, Update & Delete files. Authorisation has also been added to this project, such that only those with a specific Username & Password have access to this web application and its subsequent functionality.

## Installation for accessing files via a Virtual Environment.
In order to run these files, the user will have to clone the publicly available repository to their local machine, via https://github.com/jonkavana/data-representation-project. Once this has been successfully completed, the user will need to be able to create a virtual environment. This can be completed with the following command from the terminal.
For further advise on the running of the git commands, please see the Support & Research section detailed below.

> "python -m venv venv" <br>
> ".\venv\Scripts\activate.bat" <br>

Once the virtual environment has been stood up, a requirements text file will allow the environment to be re-created. The contents of this file can be accessed from any text file editor prior to running it. Notepad is a free text editor that can be downloaded via https://notepad-plus-plus.org/.

Once reviewed, run the following command:

> "pip freeze -r requirements.txt" <br>

You have now created the virtual environment if you have followed these steps correctly. If there are any issues with this, a listing of websites has been created in the Research & Support section detailed below.

## Instructions for running files once V.Env is live
If you have successfully created a virtual environment as detailed in the 'Installation' section above, then you can proceed with the Project. Copy and paste the URL that the virtual environment generates into your preferred browser. This project has been developed in both Chrome & Firefox. Once you run this URL, you will automatically be shown the 'home.html' page. This page has been created so that it has a closed audience. For ease of access however, the credentials have been left in a semi-transparent manner in the field itself.

> Username: Lecturer <br>
> Password: DataRep <br>

These have been set to be case sensitive details. Once the user has submitted these details, they will be taken to the main page.<br>

'Index.html': is the main wen application that displays the information that has been generated in the web application, whilst stored to a database. It is in this application that we will see the opportunity to access all the CRUD functionality that satisfies the requirements of the brief. Create: There has been due diligence given to have functions in place that will allow for new students to be logged online. Read: The information that is currently hosted in the database is in place and is running live, so any adjustments made will be reflected in real time. If the user has accidentally clicked on this button, then a home page has been added to bring the user back to the home screen. Update: Beside each student, there is the ability to change the details of the individual, apart from their id.<br>

The Id has been set as the primary key within the database. If the user has accidentally clicked on this button, then a home page has been added to bring the user back to the home screen. Delete: Should the user wish to remove an entry from the application completely, they can simply click on the delete button that resides alongside the student name.

## Research & Support
Pip Command Support - https://pip.pypa.io/en/stable/cli/pip_freeze/
Git Commands - https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html
Notepad ++ - https://notepad-plus-plus.org/ 

## Additional Supporting Material
### Test files
There are also several test files that were developed in tandem with any of the functionality that was developed. These can be seen in the following files:

> testDBSelect.py <br>

The above file was created when there was a need to create a layer of security and to allow for a user not in the local devise to access the database.

> testStudentDao.py <br>

This second file was created whilst developing the basic operations of the web application, and has tested all of the CRUD operations as they were developed.

### 'Archive' Folder
This folder has been created to store all of the important information that was of great importance to create the overall studentDao.py file. There are several of these individual files that have been left here for future development if required. <br>
There is also the central file that details the requirements and marking scheme of the project. 

### Static Pages
This folder has been created to store the two central html files that are important to display the information that links all of this project together. In order to get to this point, there is a test file that has been created too, which was utilised throughout the development of this project. 

### Configuration 
There has also been the addition of a configuration file that will allow the user to access all of the information that is on the database, whilst being able to use the login information on their own machine. This has been completed for additional security and functionality purposes. A basic template for this configuration file has also been developed. 

### Requirements
Given that this project has been developed in a virtual environment, a requirements.txt file has been added to allow the end user to operate the application on their machine. There is guidance on how to operate this requirements file that is listed in the installation section of this overview.

### gitignore
A gitignore file has been created to allow for better security on this project. This has been updated throughout the development of the project lifecycle.

## Future Development
I think that the future development of this concept will be expanding out the database and being able to move it into a Python Server. 
From a lessons learned perspective, i think some pen and paper drawings would have been the best place to start, detailing out the schema. The current view of the schema is a very fixed view in order to be able to get the Minimum Viable Product stood up. If this were being started anew, i think it would have been beneficial to create more attributes in the first table, to act as a link to a second, third and fourth table. I think that if there were a column in the students table, such as module, it would be pretty nice to be able to curate a list of all modules available. From this, we can create a view on what is in each module, who teaches it & the hours associated with it. These, in turn, would have acted as the basis for what could have been in the third and fourth tables.

I think the next development from an overall perspective is to be able to host the code in a PythonAnywhere server. The benefit to this is that it is an industry recognised server setting for Python developers. Due to the fact it is a python environment, a lot of the pre-installed packages would be covered off, meaning that the time to create the environment is reduced.

## Bibliography - Centralised 
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
